#!/usr/bin/env python3
"""
finance_engine.py — Deterministic Financial Frameworks Engine
ExecutiveSuite / Financial Hardcoding Directive

Implements first-class deterministic tools for:
- WACC (Weighted Average Cost of Capital)
- NPV (Net Present Value)
- IRR (Internal Rate of Return)
- Payback & Discounted Payback
- Profitability Index (PI)
- EVA (Economic Value Added)
- Real-Options Valuation (Binomial Lattice / Cox-Ross-Rubinstein)
- Monte Carlo NPV Scenario Engine
- Covenant & Liquidity Stress Checker
"""

import argparse
import json
import math
import random
import sys
from typing import Any, Dict, List, Optional, Tuple, Union


def compute_wacc(
    equity: float,
    debt: float,
    cost_of_equity: float,
    cost_of_debt: float,
    tax_rate: float,
) -> Dict[str, Any]:
    """
    Computes Weighted Average Cost of Capital (WACC).
    Formula: WACC = (E/V) * Re + (D/V) * Rd * (1 - t)
    """
    if equity < 0 or debt < 0:
        raise ValueError("Equity and Debt values must be non-negative.")
    total_value = equity + debt
    if total_value == 0:
        raise ValueError("Total enterprise capital (Equity + Debt) cannot be zero.")

    weight_equity = equity / total_value
    weight_debt = debt / total_value
    after_tax_cost_of_debt = cost_of_debt * (1.0 - tax_rate)
    wacc = (weight_equity * cost_of_equity) + (weight_debt * after_tax_cost_of_debt)

    return {
        "tool": "WACC",
        "inputs": {
            "equity": equity,
            "debt": debt,
            "total_value": total_value,
            "cost_of_equity": cost_of_equity,
            "cost_of_debt": cost_of_debt,
            "tax_rate": tax_rate,
        },
        "weights": {
            "equity_weight": round(weight_equity, 6),
            "debt_weight": round(weight_debt, 6),
        },
        "after_tax_cost_of_debt": round(after_tax_cost_of_debt, 6),
        "wacc": round(wacc, 6),
        "wacc_percentage": f"{wacc * 100:.2f}%",
    }


def compute_npv(
    rate: float,
    initial_investment: float,
    cash_flows: List[float],
) -> Dict[str, Any]:
    """
    Computes Net Present Value (NPV).
    Formula: NPV = -I0 + sum(CF_t / (1 + r)^t)
    """
    if rate <= -1.0:
        raise ValueError("Discount rate must be greater than -100%.")

    pv_cash_flows = []
    total_pv_inflows = 0.0

    for t, cf in enumerate(cash_flows, start=1):
        discount_factor = 1.0 / ((1.0 + rate) ** t)
        pv = cf * discount_factor
        pv_cash_flows.append({
            "period": t,
            "cash_flow": cf,
            "discount_factor": round(discount_factor, 6),
            "present_value": round(pv, 2),
        })
        total_pv_inflows += pv

    npv = -initial_investment + total_pv_inflows

    return {
        "tool": "NPV",
        "inputs": {
            "discount_rate": rate,
            "initial_investment": initial_investment,
            "cash_flows": cash_flows,
            "periods": len(cash_flows),
        },
        "present_values": pv_cash_flows,
        "total_pv_inflows": round(total_pv_inflows, 2),
        "npv": round(npv, 2),
        "decision_rule": "ACCEPT" if npv > 0 else ("REJECT" if npv < 0 else "INDIFFERENT"),
    }


def compute_irr(
    initial_investment: float,
    cash_flows: List[float],
    max_iterations: int = 1000,
    tolerance: float = 1e-7,
) -> Dict[str, Any]:
    """
    Computes Internal Rate of Return (IRR) using Newton-Raphson with bisection fallback.
    """
    cfs = [-initial_investment] + list(cash_flows)
    
    # Check for sign changes
    signs = [cf > 0 for cf in cfs if cf != 0]
    sign_changes = sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i+1])
    if sign_changes == 0:
        return {
            "tool": "IRR",
            "error": "No sign changes in cash flows; IRR does not exist.",
            "irr": None,
        }

    def npv_at(r: float) -> float:
        return sum(cf / ((1.0 + r) ** t) for t, cf in enumerate(cfs))

    def d_npv_at(r: float) -> float:
        return sum(-t * cf / ((1.0 + r) ** (t + 1)) for t, cf in enumerate(cfs))

    # Newton-Raphson
    r = 0.1  # Initial guess
    converged = False
    for _ in range(max_iterations):
        val = npv_at(r)
        if abs(val) < tolerance:
            converged = True
            break
        deriv = d_npv_at(r)
        if abs(deriv) < 1e-12:
            break
        new_r = r - val / deriv
        if new_r <= -0.999:  # Keep rate valid
            new_r = (r - 0.999) / 2.0
        if abs(new_r - r) < tolerance:
            r = new_r
            converged = True
            break
        r = new_r

    # Bisection fallback if Newton didn't converge
    if not converged:
        low, high = -0.99, 10.0
        if npv_at(low) * npv_at(high) <= 0:
            for _ in range(max_iterations):
                mid = (low + high) / 2.0
                val_mid = npv_at(mid)
                if abs(val_mid) < tolerance or (high - low) / 2.0 < tolerance:
                    r = mid
                    converged = True
                    break
                if npv_at(low) * val_mid < 0:
                    high = mid
                else:
                    low = mid

    if not converged or math.isnan(r) or math.isinf(r):
        return {
            "tool": "IRR",
            "error": "IRR calculation did not converge.",
            "multiple_irr_warning": sign_changes > 1,
            "irr": None,
        }

    return {
        "tool": "IRR",
        "inputs": {
            "initial_investment": initial_investment,
            "cash_flows": cash_flows,
        },
        "irr": round(r, 6),
        "irr_percentage": f"{r * 100:.2f}%",
        "multiple_irr_warning": sign_changes > 1,
    }


def compute_payback(
    initial_investment: float,
    cash_flows: List[float],
    discount_rate: float = 0.0,
) -> Dict[str, Any]:
    """
    Computes Payback and Discounted Payback periods.
    """
    cumulative = 0.0
    payback_period = None

    for t, cf in enumerate(cash_flows, start=1):
        prev = cumulative
        cumulative += cf
        if cumulative >= initial_investment and payback_period is None:
            fraction = (initial_investment - prev) / cf if cf != 0 else 0
            payback_period = (t - 1) + fraction

    # Discounted payback
    discounted_cumulative = 0.0
    discounted_payback_period = None

    for t, cf in enumerate(cash_flows, start=1):
        pv = cf / ((1.0 + discount_rate) ** t)
        prev_disc = discounted_cumulative
        discounted_cumulative += pv
        if discounted_cumulative >= initial_investment and discounted_payback_period is None:
            fraction_disc = (initial_investment - prev_disc) / pv if pv != 0 else 0
            discounted_payback_period = (t - 1) + fraction_disc

    return {
        "tool": "Payback",
        "inputs": {
            "initial_investment": initial_investment,
            "cash_flows": cash_flows,
            "discount_rate": discount_rate,
        },
        "simple_payback_years": round(payback_period, 2) if payback_period is not None else None,
        "discounted_payback_years": round(discounted_payback_period, 2) if discounted_payback_period is not None else None,
        "recovered": payback_period is not None,
    }


def compute_profitability_index(
    rate: float,
    initial_investment: float,
    cash_flows: List[float],
) -> Dict[str, Any]:
    """
    Computes Profitability Index (PI).
    Formula: PI = PV(Cash Inflows) / Initial Investment
    """
    if initial_investment <= 0:
        raise ValueError("Initial investment must be positive.")

    npv_res = compute_npv(rate, initial_investment, cash_flows)
    pv_inflows = npv_res["total_pv_inflows"]
    pi = pv_inflows / initial_investment

    return {
        "tool": "ProfitabilityIndex",
        "inputs": {
            "discount_rate": rate,
            "initial_investment": initial_investment,
            "pv_inflows": round(pv_inflows, 2),
        },
        "profitability_index": round(pi, 4),
        "decision_rule": "ACCEPT" if pi > 1.0 else ("REJECT" if pi < 1.0 else "INDIFFERENT"),
    }


def compute_eva(
    nopat: float,
    wacc: float,
    invested_capital: float,
) -> Dict[str, Any]:
    """
    Computes Economic Value Added (EVA).
    Formula: EVA = NOPAT - (WACC * Invested Capital)
    """
    capital_charge = wacc * invested_capital
    eva = nopat - capital_charge

    return {
        "tool": "EVA",
        "inputs": {
            "nopat": nopat,
            "wacc": wacc,
            "invested_capital": invested_capital,
        },
        "capital_charge": round(capital_charge, 2),
        "eva": round(eva, 2),
        "value_creating": eva > 0,
    }


def compute_binomial_lattice(
    s0: float,
    strike: float,
    rf: float,
    sigma: float,
    t_years: float,
    steps: int = 20,
    option_type: str = "call",
) -> Dict[str, Any]:
    """
    Computes Real-Option Valuation using Cox-Ross-Rubinstein Binomial Lattice.
    """
    if steps < 1:
        raise ValueError("Steps must be at least 1.")
    if sigma <= 0 or t_years <= 0 or s0 <= 0:
        raise ValueError("s0, sigma, and t_years must be positive.")

    dt = t_years / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1.0 / u
    disc = math.exp(-rf * dt)
    p = (math.exp(rf * dt) - d) / (u - d)

    if p < 0 or p > 1:
        raise ValueError(f"Risk-neutral probability p={p:.4f} is outside [0, 1]. Increase steps or check parameters.")

    # Terminal values
    values = []
    for j in range(steps + 1):
        st = s0 * (u ** (steps - j)) * (d ** j)
        if option_type.lower() in ("call", "expand"):
            payoff = max(0.0, st - strike)
        elif option_type.lower() in ("put", "abandon"):
            payoff = max(0.0, strike - st)
        else:
            raise ValueError(f"Unsupported option type: {option_type}")
        values.append(payoff)

    # Backward induction
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            st = s0 * (u ** (i - j)) * (d ** j)
            continuation = disc * (p * values[j] + (1.0 - p) * values[j + 1])
            if option_type.lower() in ("call", "expand"):
                exercise = max(0.0, st - strike)
            else:
                exercise = max(0.0, strike - st)
            values[j] = max(exercise, continuation)

    option_value = values[0]

    return {
        "tool": "RealOptionsBinomialLattice",
        "inputs": {
            "underlying_s0": s0,
            "strike_x": strike,
            "risk_free_rate": rf,
            "volatility_sigma": sigma,
            "time_to_maturity_years": t_years,
            "steps": steps,
            "option_type": option_type,
        },
        "lattice_parameters": {
            "dt": round(dt, 6),
            "up_factor_u": round(u, 6),
            "down_factor_d": round(d, 6),
            "risk_neutral_p": round(p, 6),
        },
        "option_value": round(option_value, 2),
    }


def compute_monte_carlo_npv(
    wacc: float,
    initial_investment: float,
    cash_flow_means: List[float],
    cash_flow_stds: List[float],
    iterations: int = 10000,
    seed: int = 42,
) -> Dict[str, Any]:
    """
    Runs Monte Carlo simulation for NPV across uncertain cash flows.
    """
    if len(cash_flow_means) != len(cash_flow_stds):
        raise ValueError("cash_flow_means and cash_flow_stds must have the same length.")

    random.seed(seed)
    npv_results = []
    periods = len(cash_flow_means)

    for _ in range(iterations):
        pv_sum = 0.0
        for t in range(periods):
            mean = cash_flow_means[t]
            std = cash_flow_stds[t]
            sampled_cf = random.gauss(mean, std)
            pv_sum += sampled_cf / ((1.0 + wacc) ** (t + 1))
        npv_results.append(-initial_investment + pv_sum)

    npv_results.sort()
    n = len(npv_results)

    def percentile(p: float) -> float:
        idx = int(round(p * (n - 1)))
        return npv_results[min(max(0, idx), n - 1)]

    mean_npv = sum(npv_results) / n
    variance = sum((x - mean_npv) ** 2 for x in npv_results) / (n - 1)
    std_npv = math.sqrt(variance)
    prob_loss = sum(1 for x in npv_results if x < 0) / n

    return {
        "tool": "MonteCarloNPV",
        "inputs": {
            "wacc": wacc,
            "initial_investment": initial_investment,
            "periods": periods,
            "cash_flow_means": cash_flow_means,
            "cash_flow_stds": cash_flow_stds,
            "iterations": iterations,
        },
        "distribution": {
            "mean_npv": round(mean_npv, 2),
            "std_npv": round(std_npv, 2),
            "p5_downside_tail": round(percentile(0.05), 2),
            "p10": round(percentile(0.10), 2),
            "p25": round(percentile(0.25), 2),
            "p50_median": round(percentile(0.50), 2),
            "p75": round(percentile(0.75), 2),
            "p90": round(percentile(0.90), 2),
            "p95_upside": round(percentile(0.95), 2),
            "probability_of_loss_npv_negative": f"{prob_loss * 100:.2f}%",
        },
        "guardrail_status": "PASS" if percentile(0.05) >= 0 else "WARNING_DOWNSIDE_RISK",
    }


def compute_covenant_check(
    total_debt: float,
    cash: float,
    ltm_ebitda: float,
    interest_expense: float,
    capex: float = 0.0,
    max_leverage: float = 3.0,
    min_interest_coverage: float = 3.0,
    min_runway_months: float = 12.0,
    monthly_burn: float = 0.0,
) -> Dict[str, Any]:
    """
    Evaluates debt covenants, leverage ceiling, and liquidity runway.
    """
    net_debt = total_debt - cash
    leverage_ratio = (net_debt / ltm_ebitda) if ltm_ebitda > 0 else float("inf")
    interest_coverage = (ltm_ebitda / interest_expense) if interest_expense > 0 else float("inf")
    runway_months = (cash / monthly_burn) if monthly_burn > 0 else (float("inf") if cash > 0 else 0.0)

    # 20% Headroom calculations
    leverage_headroom_pct = ((max_leverage - leverage_ratio) / max_leverage) * 100 if max_leverage > 0 else 0
    coverage_headroom_pct = ((interest_coverage - min_interest_coverage) / min_interest_coverage) * 100 if min_interest_coverage > 0 else 0

    flags = []
    if leverage_ratio > max_leverage:
        flags.append(f"BREACH: Leverage ratio {leverage_ratio:.2f}x exceeds ceiling {max_leverage:.2f}x")
    elif leverage_headroom_pct < 20.0:
        flags.append(f"WARNING: Leverage headroom is {leverage_headroom_pct:.1f}% (target >= 20%)")

    if interest_coverage < min_interest_coverage:
        flags.append(f"BREACH: Interest coverage {interest_coverage:.2f}x below minimum {min_interest_coverage:.2f}x")
    elif coverage_headroom_pct < 20.0:
        flags.append(f"WARNING: Coverage headroom is {coverage_headroom_pct:.1f}% (target >= 20%)")

    if runway_months < min_runway_months and monthly_burn > 0:
        flags.append(f"BREACH: Cash runway {runway_months:.1f} months is below required {min_runway_months:.1f} months")

    status = "BREACH" if any("BREACH" in f for f in flags) else ("WARNING" if flags else "PASS")

    return {
        "tool": "CovenantAndLiquidityChecker",
        "inputs": {
            "total_debt": total_debt,
            "cash": cash,
            "net_debt": round(net_debt, 2),
            "ltm_ebitda": ltm_ebitda,
            "interest_expense": interest_expense,
            "capex": capex,
            "monthly_burn": monthly_burn,
        },
        "metrics": {
            "net_debt_to_ebitda": round(leverage_ratio, 2) if not math.isinf(leverage_ratio) else "Infinity",
            "leverage_ceiling": max_leverage,
            "leverage_headroom_percentage": f"{leverage_headroom_pct:.1f}%",
            "interest_coverage_ratio": round(interest_coverage, 2) if not math.isinf(interest_coverage) else "Infinity",
            "min_interest_coverage": min_interest_coverage,
            "coverage_headroom_percentage": f"{coverage_headroom_pct:.1f}%",
            "cash_runway_months": round(runway_months, 1) if not math.isinf(runway_months) else "Self-funding",
        },
        "guardrail_status": status,
        "flags": flags,
    }


def main():
    parser = argparse.ArgumentParser(description="Deterministic Financial Frameworks CLI")
    parser.add_argument("--tool", required=True, choices=["wacc", "npv", "irr", "payback", "pi", "eva", "real-options", "monte-carlo", "covenants"])
    parser.add_argument("--params", required=True, help="JSON string of parameter inputs")

    args = parser.parse_args()
    try:
        params = json.loads(args.params)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"Invalid JSON parameters: {e}"}))
        sys.exit(1)

    try:
        if args.tool == "wacc":
            res = compute_wacc(**params)
        elif args.tool == "npv":
            res = compute_npv(**params)
        elif args.tool == "irr":
            res = compute_irr(**params)
        elif args.tool == "payback":
            res = compute_payback(**params)
        elif args.tool == "pi":
            res = compute_profitability_index(**params)
        elif args.tool == "eva":
            res = compute_eva(**params)
        elif args.tool == "real-options":
            res = compute_binomial_lattice(**params)
        elif args.tool == "monte-carlo":
            res = compute_monte_carlo_npv(**params)
        elif args.tool == "covenants":
            res = compute_covenant_check(**params)
        else:
            res = {"error": f"Unknown tool: {args.tool}"}

        print(json.dumps(res, indent=2))
    except Exception as ex:
        print(json.dumps({"error": str(ex)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
