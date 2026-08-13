#!/usr/bin/env python3
"""
test_finance_engine.py — Unit Tests for Deterministic Financial Frameworks Engine
"""

import math
import sys
import unittest
from pathlib import Path

# Add script directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "plugins" / "executive-suite" / "skills" / "financial-frameworks" / "scripts"))

from finance_engine import (
    compute_wacc,
    compute_npv,
    compute_irr,
    compute_payback,
    compute_profitability_index,
    compute_eva,
    compute_binomial_lattice,
    compute_monte_carlo_npv,
    compute_covenant_check,
)


class TestFinanceEngine(unittest.TestCase):

    def test_wacc_standard(self):
        # Example from research doc & skill: E=800, D=200, Re=10%, Rd=5%, t=25% -> 8.75%
        res = compute_wacc(equity=800.0, debt=200.0, cost_of_equity=0.10, cost_of_debt=0.05, tax_rate=0.25)
        self.assertAlmostEqual(res["wacc"], 0.0875, places=4)
        self.assertEqual(res["wacc_percentage"], "8.75%")
        self.assertAlmostEqual(res["weights"]["equity_weight"], 0.8, places=2)
        self.assertAlmostEqual(res["weights"]["debt_weight"], 0.2, places=2)

    def test_npv_positive_and_negative(self):
        # I0 = 100, CF = [30, 30, 30, 30, 30], r = 10% -> NPV = 13.72
        res = compute_npv(rate=0.10, initial_investment=100.0, cash_flows=[30.0, 30.0, 30.0, 30.0, 30.0])
        self.assertAlmostEqual(res["npv"], 13.72, places=1)
        self.assertEqual(res["decision_rule"], "ACCEPT")

        # Reject case
        res_reject = compute_npv(rate=0.25, initial_investment=100.0, cash_flows=[20.0, 20.0, 20.0])
        self.assertLess(res_reject["npv"], 0)
        self.assertEqual(res_reject["decision_rule"], "REJECT")

    def test_irr_calculation(self):
        # I0 = 100, CF = [30, 30, 30, 30, 30] -> IRR ~ 15.24%
        res = compute_irr(initial_investment=100.0, cash_flows=[30.0, 30.0, 30.0, 30.0, 30.0])
        self.assertIsNotNone(res["irr"])
        self.assertAlmostEqual(res["irr"], 0.1524, places=2)

    def test_payback_periods(self):
        # I0 = 100, CF = [40, 40, 40, 40] -> Payback = 2.5 years, Discounted payback ~ 3.02 years
        res = compute_payback(initial_investment=100.0, cash_flows=[40.0, 40.0, 40.0, 40.0], discount_rate=0.10)
        self.assertEqual(res["simple_payback_years"], 2.5)
        self.assertIsNotNone(res["discounted_payback_years"])
        self.assertGreater(res["discounted_payback_years"], 2.5)
        self.assertLess(res["discounted_payback_years"], 4.0)

    def test_profitability_index(self):
        res = compute_profitability_index(rate=0.10, initial_investment=100.0, cash_flows=[30.0, 30.0, 30.0, 30.0, 30.0])
        self.assertGreater(res["profitability_index"], 1.0)
        self.assertEqual(res["decision_rule"], "ACCEPT")

    def test_eva_calculation(self):
        # NOPAT = 15, WACC = 8.75%, Capital = 100 -> Capital Charge = 8.75, EVA = 6.25
        res = compute_eva(nopat=15.0, wacc=0.0875, invested_capital=100.0)
        self.assertAlmostEqual(res["eva"], 6.25, places=2)
        self.assertTrue(res["value_creating"])

    def test_binomial_lattice_option(self):
        # S0 = 100, X = 80, Rf = 4%, Sigma = 30%, T = 2yr
        res = compute_binomial_lattice(s0=100.0, strike=80.0, rf=0.04, sigma=0.30, t_years=2.0, steps=20, option_type="call")
        self.assertGreater(res["option_value"], 25.0)
        self.assertLess(res["option_value"], 45.0)

    def test_monte_carlo_npv(self):
        res = compute_monte_carlo_npv(
            wacc=0.10,
            initial_investment=100.0,
            cash_flow_means=[30.0, 30.0, 30.0, 30.0, 30.0],
            cash_flow_stds=[5.0, 5.0, 5.0, 5.0, 5.0],
            iterations=5000,
            seed=123,
        )
        self.assertAlmostEqual(res["distribution"]["mean_npv"], 13.72, delta=2.0)
        self.assertIn("p5_downside_tail", res["distribution"])
        self.assertIn("p95_upside", res["distribution"])

    def test_covenant_checker(self):
        # Safe case: Net debt = 200 - 50 = 150, EBITDA = 100 -> Leverage = 1.5x (Limit 3.0x, headroom 50%)
        # Interest = 20 -> Coverage = 5.0x (Min 3.0x, headroom 66.7%)
        safe = compute_covenant_check(total_debt=200.0, cash=50.0, ltm_ebitda=100.0, interest_expense=20.0, max_leverage=3.0, min_interest_coverage=3.0)
        self.assertEqual(safe["guardrail_status"], "PASS")

        # Breach case: Net debt = 350 - 10 = 340, EBITDA = 100 -> Leverage = 3.4x (>3.0x)
        breach = compute_covenant_check(total_debt=350.0, cash=10.0, ltm_ebitda=100.0, interest_expense=40.0, max_leverage=3.0, min_interest_coverage=3.0)
        self.assertEqual(breach["guardrail_status"], "BREACH")
        self.assertTrue(any("Leverage ratio" in f for f in breach["flags"]))


if __name__ == "__main__":
    unittest.main()
