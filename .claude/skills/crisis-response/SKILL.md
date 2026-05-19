---
name: crisis-response
description: "Crisis response toolkit — classification, trigger thresholds, escalation tiers, war-room activation, rapid liquidity stress, supply-chain alternate-source, holding-statement, AAR."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# Crisis Response

Used by `crisis-warroom`, `chief-risk-officer`, `chief-communications-officer`, `cfo`, `ciso`, `coo`, `csco`. Built on the research doc's Masterclass 2 ("Black Swan Capital Preservation").

## Crisis Classification

| Class | Examples | Lead role |
|---|---|---|
| **Financial / liquidity** | Covenant trip imminent; counterparty default; market dislocation | `cfo` + `chief-risk-officer` |
| **Operational** | Major plant down; supply collapse; logistics shutdown | `coo` + `csco` |
| **Cyber** | Ransomware, breach, IP exfiltration, model attack | `ciso` |
| **Legal / regulatory** | Material litigation, sanctions exposure, investigation, license action | `clo` |
| **Reputational** | Executive conduct, product harm, social/cultural event | `chief-communications-officer` + `ceo` |
| **Geopolitical** | Tariff, conflict, expropriation, sovereign action | `clo` + `cfo` + `csco` |
| **Health / safety** | On-site injury / fatality; public-safety product event | `coo` + `clo` + `chief-communications-officer` |

Multi-class events are common (cyber → reputational → regulatory). The `crisis-warroom` coordinates.

## Trigger Thresholds & Escalation Tiers

| Tier | Trigger | Tempo | Notified |
|---|---|---|---|
| **Yellow** | Single KRI at amber; composite risk index trending | Daily standup; 4-hr decision tempo | Function exec + Chief Risk |
| **Orange** | Multiple amber KRIs OR single red KRI | War-room activated; 2-hr decision tempo | + CEO |
| **Red** | Material loss event realized or imminent | Continuous war-room; 30-60 min HITL | + Board chair + audit/risk committee chair |

## War-Room Activation Checklist

Within first hour:
- [ ] Tier declared (yellow / orange / red) + reason logged
- [ ] War-room participants identified per crisis class
- [ ] Communication channel established (secure; logged)
- [ ] First situational brief produced
- [ ] CEO + (if red) Board chair notified per the matrix
- [ ] Decision log started (every decision time-stamped + attributed)
- [ ] Holding statement drafted (60-min target for SEV-1)
- [ ] Legal hold considered (with `clo`)
- [ ] Stakeholder cascade plan reviewed
- [ ] Treasury notified to stand by

## Rapid Liquidity Stress Template (within 1 hour of activation)

| Scenario | Revenue Δ | Days to cash exhaustion (base) | Covenant breach? | Recommended action |
|---|---|---|---|---|
| Base | 0% | | | Monitor |
| Mild | −10% | | | Operating actions only |
| Moderate | −25% | | | Capex freeze + cost-out |
| Severe | −50% | | | Working-capital tightening + hedge |
| Catastrophic | −75% or event-driven | | | Capital action (revolver draw, equity, deal-pivot) |

Monte Carlo applied to historical analog crises (2008, 2020, sector-specific). Report P5 outcome.

## Supply-Chain Alternate-Source Playbook

| Step | Action | Owner |
|---|---|---|
| 1 | Identify impacted SKUs / categories (with revenue / EBITDA exposure) | csco |
| 2 | Activate pre-tested alternate suppliers per critical-tier list | csco |
| 3 | Reallocate inventory across regions | csco + coo |
| 4 | Mode-shift logistics (air vs. ocean; alternate ports) | csco |
| 5 | Customer commitments triage (defend SLAs vs. renegotiate) | cxo + cro |
| 6 | Working-capital impact computed | csco + cfo |
| 7 | Force-majeure declarations evaluated | clo |
| 8 | Daily status against pre-defined recovery curve | csco |

## Holding-Statement Template (60-min publish target for SEV-1)

```
[Timestamp]

We are aware of [factual description of event in 1 sentence].

Our priority is [primary affected stakeholder — e.g., customer safety, employee wellbeing, data security].

We have:
- [Action 1 we are taking right now]
- [Action 2]
- [Action 3]

We will provide our next update by [specific time].

For verified information, please reference [single channel].

[Named accountable executive] is leading our response.
```

Avoid: speculation on cause, blame attribution, commitments before facts confirm, jargon, defensive tone.

Cadence: every 2–4 hours during active SEV-1; every 24 hours during sustained event; final after-action public statement on closure.

## Stakeholder Comms Cascade

| Sequence | Audience | Channel | Owner |
|---|---|---|---|
| T+0 | War-room + CEO | Secure channel | Crisis lead |
| T+15min | Board chair (red only) | Secure call | CEO |
| T+30min | Affected internal teams | Secure broadcast | Function leads |
| T+60min | Customers (if affected) | Email + status page | cxo / chief-communications-officer |
| T+60min | Public (if material) | Holding statement | chief-communications-officer |
| T+2hr | Regulators (if required) | Per regulatory channel | clo + chief-compliance-officer |
| T+24hr | Update cycle begins | Per audience | Per owner |

## Post-Crisis After-Action Review (AAR) Template

Within 30 days of de-escalation:

```
# Crisis AAR — [Event name] — [Dates]

## Timeline
[Reconstruction from decision log]

## What happened (root cause)
[Causal chain; no blame; systemic + proximate causes]

## What went well
[Decisions / actions that worked; preserve as patterns]

## What went poorly
[Decisions / actions that didn't; lessons]

## Counter-factuals
[What would we have done differently with hindsight? Was that information available in real time?]

## Systemic mitigations
[New KRIs to add; controls to strengthen; playbook updates; training needs]

## Action items
| Action | Owner | Deadline |

## Reporting
[To board audit/risk committee; to regulator if required]
```

## Output

Crisis artifacts saved to `output/crisis/`. See `crisis-warroom.md` for the agent that operates this.
