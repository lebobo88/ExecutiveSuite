---
name: enterprise-risk
description: "Enterprise risk management — COSO ERM 2017 + ISO 31000 — risk taxonomy, appetite statement, top-risk register, KRIs, Bow-Tie, three-lines-of-defense."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# Enterprise Risk Management

Used by `chief-risk-officer`, `chief-compliance-officer`, and any executive scoping risk in their domain. Implements COSO ERM 2017 and ISO 31000.

## Risk Taxonomy

| Category | Sub-categories | Owner |
|---|---|---|
| **Strategic** | Market disruption, competitive position, M&A integration, capital allocation, brand | ceo + cso |
| **Operational** | Process failure, BCM, fraud, key-person, supplier concentration, quality | coo + csco |
| **Financial** | Liquidity, credit, market (FX/rates/commodities), capital structure, tax | cfo |
| **Compliance / Legal** | Regulatory change, examinations, sanctions, AI Act, employment, IP | clo + chief-compliance-officer |
| **Cyber** | Breach, ransomware, IP loss, model attack, third-party software | ciso |
| **Data / Privacy** | GDPR/CCPA exposure, data quality, model drift | cdo + caio |
| **Climate / Sustainability** | Physical risk, transition risk, regulatory (CSRD/SEC), Scope-3 | chief-sustainability-officer |
| **Geopolitical** | Tariff, sanctions, conflict, sovereign action, export control | clo + ceo |
| **Reputational** | Cultural incident, product harm, executive conduct, social media | chief-communications-officer |
| **People** | Talent flight, succession gap, culture decay, DEIB | chro |

## Risk Appetite Statement Template

```
## [Firm] Risk Appetite Statement

We accept these risks deliberately to pursue our strategy:
- Strategic: We pursue [X%] revenue growth, accepting up to [Y%] volatility
- Innovation: We allocate [Z%] of capex to high-uncertainty / high-option-value bets

We tolerate these risks within bounded ranges:
- Financial: net debt/EBITDA ≤ 3.0x; covenant headroom ≥ 20%; cash runway ≥ 12 mo base
- Operational: critical-service interruption ≤ N hours; OEE ≥ 85%; OTIF ≥ 95%
- Cyber: Tier-1 service recovery ≤ 4 hours; zero unencrypted PII at rest

We do not accept:
- Material regulatory violations or sanctions exposure
- Material customer-data exposure
- Executive conduct or product harm meeting major-news-event threshold
- Climate / ESG commitments break (per transition plan)
- Counterparty / supplier concentration > 10% in any single Tier-1 dependency

This statement is reviewed annually by the board and operationalized via KRIs and the top-risk register.
```

## Top-Risk Register Format (5x5 heat-map)

| ID | Risk | Category | Owner | Inherent L | Inherent I | Inherent Score | Controls | Residual L | Residual I | Residual Score | Trend | KRIs | Action plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

- **L** = Likelihood (1 rare → 5 almost certain)
- **I** = Impact (1 trivial → 5 catastrophic)
- **Score** = L × I

Tier the register:
- Tier-1 (≥ 16 residual): board agenda item every meeting; named exec owner; quarterly deep-dive
- Tier-2 (9–15): exec committee monthly; named owner
- Tier-3 (4–8): function-level; reviewed in risk committee
- Tier-4 (≤ 3): monitored; no escalation unless trend reverses

## KRI Dashboard Template

| KRI | Definition | Source | Threshold (Green / Amber / Red) | Cadence | Owner |
|---|---|---|---|---|---|

Triggers:
- **Amber** → escalation memo to risk committee + named action
- **Red** → `crisis-warroom` activation candidate; CEO notified

## Bow-Tie Analysis Template

```
                    [CAUSES]                              [CONSEQUENCES]
   Cause 1 ─┐                                              ┌─ Consequence 1
   Cause 2 ─┼─→  [TOP EVENT / RISK]  →─────────────────────┼─ Consequence 2
   Cause 3 ─┘                                              └─ Consequence 3
        [Preventive controls]              [Mitigative controls]
```

For each cause: preventive control + effectiveness rating + owner.
For each consequence: mitigative control + effectiveness rating + owner.
Identify weakest controls; prioritize improvement.

## Three Lines of Defense

| Line | Role | Owners | Function |
|---|---|---|---|
| **1st** | Operate the controls | Business functions | Day-to-day risk ownership; design + run controls |
| **2nd** | Oversight, framework, testing | Risk + Compliance | Policy, monitoring, advice, escalation |
| **3rd** | Independent assurance | Internal Audit | Test 1st + 2nd; report to board audit committee |

External assurance (external audit, regulator examination) is sometimes called the "4th line."

## Escalation Tiers

| Tier | Trigger | Recipient | Tempo |
|---|---|---|---|
| Function | Threshold breach in single function | Function exec | Within 24 hr |
| Risk Committee | Tier-2 risk material change; multiple amber KRIs | Exec risk committee | Within 48 hr |
| Executive | Tier-1 risk material change; red KRI | CEO + Chief Risk | Within 24 hr |
| Board | Risk appetite breach; material loss event; regulator interest | Board chair + audit/risk committee chair | Same day |
| Crisis | Multiple red KRIs; material loss imminent | `crisis-warroom` activation | Immediate |

## ERM Cadence

- **Daily** — KRI dashboards (automated)
- **Weekly** — risk team review; amber-trend log
- **Monthly** — risk committee (top-risk movement, new emerging risks)
- **Quarterly** — board risk committee + risk register full refresh
- **Annual** — risk appetite statement review; reverse stress test; ERM program self-assessment

## Output

Risk artifacts saved to `output/risk/`. See `chief-risk-officer.md` for the agent that operates this.
