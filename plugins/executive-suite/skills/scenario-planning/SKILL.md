---
name: scenario-planning
description: "Scenario planning toolkit — 2x2 matrices, four-case canvas, Monte Carlo setup, sensitivity & tornado, decision-tree EV, war-game, reverse stress test, optionality scoring."
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Scenario Planning

Used by `cso`, `chief-risk-officer`, `cfo`, `crisis-warroom`, `capital-allocation`. Provides the analytic toolkit for thinking under uncertainty beyond single-point forecasts.

## 2x2 Scenario Matrix Construction

1. **Identify drivers** — brainstorm 15–30 forces shaping the future relevant to the decision
2. **Cluster & cull** — reduce to 8–12 driving forces
3. **Score** — each on **impact** (high / low) × **uncertainty** (high / low)
4. **Pick the top 2** — highest impact × highest uncertainty pair
5. **Build the 2x2** — four scenarios at the corners
6. **Name each scenario** — vivid, memorable
7. **Build the narrative** — what would the world look like in this corner?
8. **Identify**: common-denominator bets (robust across all 4); scenario-specific options; canary indicators (which scenario is unfolding?)

## Four-Case Canvas

For any material decision:

| Case | Probability | Description | NPV / outcome | Key drivers |
|---|---|---|---|---|
| **Base** | (typically 50–60%) | Most-likely path | | |
| **Upside** | (typically 15–25%) | Drivers break favorably | | |
| **Downside** | (typically 15–25%) | Drivers break unfavorably | | |
| **Black-swan** | (typically 1–5%) | Tail event; structural break | | |

Recommendation lens: would we take this action even in the downside case (or only if upside)? What's our regret if black-swan hits?

## Monte Carlo Setup

| Step | What to do |
|---|---|
| 1. Identify drivers | 5–15 key uncertain inputs (revenue, margin, cost, tax, working capital) |
| 2. Choose distribution per driver | Normal (symmetric), lognormal (asymmetric, multiplicative), triangular (bounded), beta (constrained), empirical (fit history) |
| 3. Specify correlations | Revenue × margin is rarely independent. Use covariance matrix |
| 4. Run iterations | 10k+ for stable tails; 50k+ for P1 / P99 |
| 5. Report distribution | P5 / P25 / P50 / P75 / P95 — not just mean |
| 6. Tail decomposition | Which driver(s) dominate the bad tail? |

## Sensitivity & Tornado

- **One-at-a-time** swings (±10%, ±25%) around base; rank by NPV delta
- **Tornado chart** — bars sorted by impact magnitude
- Output: **top 5 break-the-case variables** named in every memo
- Limitation: misses interactions (Monte Carlo complements)

## Decision-Tree Expected Value

For sequential decisions with uncertainty:

```
Decision node [□]
 ├── Action A
 │    Chance node (○)
 │     ├── Outcome A1 (prob × value)
 │     └── Outcome A2 (prob × value)
 │     EV(A) = Σ p · v
 └── Action B
      ...
```

Choose the action with highest EV — but report variance / downside too.

## War-Game / Red-Team Alternate Future

For strategy / competitive decisions:

1. Form Red Team (competitor / disruptor) + Blue Team (us) + Control (referee)
2. Each team plays 2–3 moves into the future, reacting to the other
3. Outcomes scored on shared metrics (market share, margin, customer retention)
4. Debrief identifies: blind spots, our most-vulnerable assumptions, counter-moves
5. Output: revised strategy with named counter-moves and trigger indicators

## Reverse Stress Test

Standard approach: scenario → outcome. Reverse: outcome → scenario.

1. Define the **failure outcome** (e.g., cash exhausted in 6 mo; covenant breach; customer-flight reputation event)
2. Work backwards: what scenario would cause this?
3. Identify the **leading indicators** that would precede that scenario
4. Stand up monitoring + a pre-defined response playbook

The research doc highlights reverse stress as critical for black-swan preparedness.

## Strategic Optionality Scoring

For any bet, compute:

```
Total value = Static NPV + Option value − Reversibility cost
```

| Option type | Question | Approximate value |
|---|---|---|
| Defer | Can we wait for more information? | Black-Scholes-style on volatility |
| Expand | Can we scale up if it works? | Lattice on success probability |
| Abandon | Can we exit if it doesn't? | Salvage value relative to commitment |
| Stage | Can we phase commitment? | Multi-period lattice |
| Switch | Can we change use? | Spread option |
| Compound | Does this unlock further options? | Option-on-option |

Bets with high option value justify lower static NPV, especially under high uncertainty.

## Scenario-Planning Cadence

- **Annual** — full scenario refresh (`cso` leads)
- **Quarterly** — driver-status review; scenario-probability update
- **Event-triggered** — material change in any high-uncertainty driver triggers re-base

## Output

Scenario artifacts saved per the requesting role (typically `output/strategy/`, `output/finance/`, `output/risk/`).
