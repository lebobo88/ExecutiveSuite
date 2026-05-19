---
name: financial-frameworks
description: "Deterministic financial tools — WACC, NPV, IRR, payback, EVA, real-options, Monte Carlo, sensitivity, covenant/liquidity checks. The Financial Hardcoding Directive."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# Financial Frameworks — The Hardcoding Directive

Per the research doc (Section "Financial Framework Hardcoding Directive"), corporate finance discipline must be embedded as **first-class deterministic tools and constraints**, not informal guidance. Agents (`cfo`, `mna-cockpit`, `capital-allocation`, `crisis-warroom`) must invoke the relevant tool, log inputs and assumptions, and surface guardrail breaches before recommending action.

Each tool below has: **Purpose · Inputs · Formula · When to use · Example · Pitfalls**.

---

## 1. Weighted Average Cost of Capital (WACC)

- **Purpose**: discount rate for all cash-flow valuations
- **Inputs**: market value of equity (E), market value of debt (D), cost of equity Re, cost of debt Rd (pre-tax), marginal tax rate t
- **Formula**: `WACC = (E/V)·Re + (D/V)·Rd·(1 − t)` where V = E + D
- **Re**: typically CAPM: `Re = Rf + β·(Rm − Rf)` (Rf = risk-free; β = equity beta; Rm − Rf = market risk premium)
- **When to use**: any project / acquisition / asset valuation
- **Example**: E=$800M, D=$200M, Re=10%, Rd=5%, t=25% → WACC = 0.8·10% + 0.2·5%·0.75 = 8.75%
- **Pitfalls**: (1) using book values instead of market; (2) holding D/V constant when transaction changes capital structure (use target structure); (3) cross-border without country-risk adjustment; (4) negative-equity / pre-revenue companies — use comparable firm's WACC or sector cost-of-capital

## 2. Net Present Value (NPV)

- **Purpose**: aggregate value of an investment's discounted cash flows
- **Inputs**: cash flow stream CF_t for t = 0..n; discount rate r (typically WACC + risk premium)
- **Formula**: `NPV = Σ(t=0..n) CF_t / (1+r)^t`
- **Decision rule**: NPV > 0 accept; NPV < 0 reject; for mutually-exclusive, pick highest NPV
- **When to use**: any project with multi-period cash flows
- **Example**: I₀ = −$100, CF₁..₅ = $30 each, r = 10% → NPV = $13.7M
- **Pitfalls**: (1) using nominal cash flows with real discount rate (or vice versa); (2) ignoring terminal value when relevant; (3) double-counting financing costs (cash flows are unlevered FCF when WACC is the discount rate); (4) cash flows not risk-adjusted to discount rate

## 3. Internal Rate of Return (IRR)

- **Purpose**: the rate at which NPV = 0
- **Inputs**: cash flow stream
- **Formula**: solve for r such that `Σ CF_t / (1+r)^t = 0`
- **Decision rule**: IRR ≥ hurdle rate (typically WACC + risk premium)
- **When to use**: sanity-check returns; communicating to non-finance stakeholders
- **Pitfalls**: (1) multiple IRRs when cash flows change sign more than once — use NPV instead; (2) IRR alone misleads for mutually-exclusive projects of different scale — pick by NPV; (3) reinvestment assumption (MIRR fixes); (4) IRR is silent on size

## 4. Payback & Discounted Payback

- **Purpose**: time to recover initial investment
- **Inputs**: cash flow stream
- **Formulas**: payback = years until cumulative CF ≥ I₀; discounted payback uses discounted CF
- **When to use**: liquidity-constrained context, complementary to NPV (never primary)
- **Pitfalls**: (1) ignores cash flows after payback; (2) ignores time value (use discounted variant); (3) inadequate as sole decision criterion

## 5. Profitability Index (PI)

- **Purpose**: NPV per dollar invested — for capital rationing
- **Formula**: `PI = (NPV + I₀) / I₀` (or equivalently `PV(CF) / I₀`)
- **Decision rule**: PI > 1 accept; for rationing, rank by PI
- **When to use**: when capital is constrained and projects are divisible / independent

## 6. Economic Value Added (EVA)

- **Purpose**: operating-period value creation above cost of capital
- **Formula**: `EVA = NOPAT − (WACC × Invested Capital)`
- **NOPAT** = EBIT × (1 − t)
- **When to use**: ongoing-business performance, executive compensation linkage
- **Pitfalls**: (1) invested-capital base must be consistent (book vs adjusted); (2) NOPAT volatility distorts year-over-year reads; (3) ignores future growth options

## 7. Real-Options Valuation

### 7a. Binomial Lattice (walked example)

- **Purpose**: value managerial flexibility (defer, expand, abandon, stage)
- **Inputs**: underlying value S₀; volatility σ; risk-free rate Rf; time T; exercise value X; up factor u; down factor d; risk-neutral probability p
- **Formulas**:
  - `u = e^(σ√Δt)`, `d = 1/u`
  - `p = (e^(Rf·Δt) − d) / (u − d)`
  - At each node, option value = max(intrinsic, e^(−Rf·Δt) · [p·V_up + (1−p)·V_down])
- **When to use**: staged investments, abandonment options, expansion options on existing capacity
- **Example**: S₀ = $100M, σ = 30%, T = 2 yr, X = $80M (abandon for salvage), Rf = 4%; 2-step lattice yields option value substantially higher than naive NPV if downside is severe

### 7b. Black-Scholes Sketch (call-option analogy)

- `C = S·N(d₁) − X·e^(−Rf·T)·N(d₂)`
- `d₁ = [ln(S/X) + (Rf + σ²/2)·T] / (σ√T)`, `d₂ = d₁ − σ√T`
- Useful for fast first-cut on growth-option value (e.g., R&D pipeline)

### 7c. Monte Carlo for Path-Dependent

When optimal-exercise depends on path (Least-Squares Monte Carlo, Longstaff-Schwartz), simulate underlying and regress to estimate continuation value.

- **Pitfalls** (all real-options methods): (1) volatility estimate is the dominant assumption — sensitivity-test it; (2) modeling managerial flexibility you won't actually exercise (over-optimism); (3) double-counting (don't add option value to a DCF that already implicitly captures flexibility)

## 8. Monte Carlo Scenario Engine

- **Purpose**: distribution of outcomes when key drivers are uncertain
- **Inputs**: distribution per driver (normal, lognormal, triangular, beta); correlations; 10k+ iterations
- **When to use**: any decision where downside tail matters or where multiple uncertain drivers interact
- **Output**: P5 / P25 / P50 / P75 / P95 of NPV (or any metric); plus probability of value-destroying outcome
- **Pitfalls**: (1) ignoring correlations (revenue and margin are not independent); (2) garbage-in / garbage-out on distributions — fit to history; (3) reporting only the mean (reading P5 matters more for guardrails)

## 9. Sensitivity Analysis & Tornado

- **Purpose**: rank assumptions by impact on outcome
- **Method**: one-variable-at-a-time swings (±10%, ±25%) around base; rank by NPV delta
- **When to use**: every material analysis — name the top 5 break-the-case variables
- **Pitfalls**: one-at-a-time misses interactions (Monte Carlo complements)

## 10. Capital-Budgeting Decision Tree

```
Strategic fit?
└── No → reject (archive with rationale)
└── Yes → Run NPV at WACC + risk premium
          ├── NPV < 0 → reject (unless real-option value justifies)
          └── NPV ≥ 0 → Check guardrails
                        ├── Any guardrail fail → restructure or board override
                        └── All guardrails pass → Run Monte Carlo
                                                  ├── P5 catastrophic → restructure / decline / hedge
                                                  └── P5 acceptable → Recommend (full / staged / conditional)
```

## 11. Capital-Rationing Prioritization

When capital is constrained: rank by **Profitability Index** (NPV per $ invested), subject to:
- Mandatory projects (compliance, safety) funded first
- Strategic enabler / option-value projects funded next (even at lower PI) when they unlock larger downstream optionality
- Discretionary funded by PI rank until capital exhausted

## 12. Covenant & Leverage Checker

Run before any material capital action:

| Ratio | Formula | Typical covenant | Action if within 20% of limit |
|---|---|---|---|
| Net debt / LTM EBITDA | (Total Debt − Cash) / EBITDA | ≤ 3.0–4.5x sector-dependent | Flag; alternative-action review |
| Interest coverage | EBITDA / Interest expense | ≥ 3.0x | Flag |
| Fixed-charge coverage | (EBITDA − Capex) / (Interest + Lease) | ≥ 1.5x | Flag |
| DSCR (debt service coverage) | NOI / Total debt service | ≥ 1.25x | Flag |

## 13. Liquidity Stress

| Scenario | Revenue Δ | Action | Cash runway target |
|---|---|---|---|
| Base | 0 | Plan | ≥ 12 mo |
| Mild | −10% | Operating actions only | ≥ 9 mo |
| Moderate | −25% | Capex freeze + cost-out | ≥ 6 mo |
| Severe | −50% | Working-capital tightening + hedge | ≥ 3 mo |
| Catastrophic | −75% / event | Activate `crisis-warroom` | survive |

## 14. Hard Guardrails Reference Table

| Guardrail | Default | Override path |
|---|---|---|
| Hurdle rate | WACC + risk-class premium | CEO + Board with documented thesis |
| Net leverage | ≤ 3.0x net debt/EBITDA | Board only |
| Covenant headroom | ≥ 20% post-action | Board only |
| Cash runway | ≥ 12 mo base / ≥ 6 mo stress | Board only |
| Counterparty concentration | < 10% recv/treasury | CFO sign-off |
| Sanctions / prohibited | Zero exposure | NEVER — non-overrideable |
| ESG / climate plan | No material breach | Board + Chief Sustainability sign-off |

## Required Logging Discipline

Every tool invocation logs: tool, inputs (named), assumptions, output, decision, time, author. This is non-negotiable for audit and AI-governance traceability (Research Doc Governance section + EU AI Act Article 9).
