---
name: executive-protocol
description: "Enterprise executive decision frameworks, memo templates, board protocol, RACI, OKR, escalation rules, dissenting-opinion format."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# Executive Protocol

The shared operating protocol for all C-suite agents in `.claude/agents/`. Every output from a single-domain executive or an orchestrator MUST conform to one of the templates below.

## Executive Memo Format

```
# [Topic] — [Role] Analysis — YYYY-MM-DD

## Executive Summary
[2–3 sentence recommendation with confidence level: High / Medium / Low and the reason]

## Situation Assessment
[Current state; what's at stake; what we know / don't know]

## Options Considered
### Option A — [Name]
- Description
- Pros (with evidence)
- Cons (with evidence)
- Score: X/10 on [decision framework]

### Option B — [Name]
[same structure]

### Option C — [Name] (always include "do nothing / status quo" or "kill / return capital")
[same structure]

## Recommendation
[Clear, actionable recommendation with rationale and trade-off statement]

## Decision Framework Scoring
| Criterion | Weight | Option A | Option B | Option C |
|---|---|---|---|---|

## Next Steps
| # | Action | Owner | Deadline | Success Criterion |
|---|---|---|---|---|

## Risk Factors & Mitigations
| Risk | Probability | Impact | Mitigation | Trigger |
|---|---|---|---|---|

## Assumptions That Could Be Wrong
[List the 3–5 assumptions whose failure would change the recommendation]

## HITL / Approvals Required
[Who must approve before execution; what decisions remain with the human]

---
Filed by: [role-slug] | Date: YYYY-MM-DD
Saved to: output/[domain]/[topic]-YYYY-MM-DD.md
```

## Board Meeting Protocol

Used by `boardroom`, `mna-cockpit`, `crisis-warroom`, `capital-allocation`.

```
# Board Meeting — [Topic] — YYYY-MM-DD

## Agenda
[Single-sentence decision frame]

## 1. Situation Brief
[Context, scope, known facts, known unknowns]

## 2. Functional Perspectives
[For each attending executive — 3 to 5 perspectives — analyze through their decision framework]

### [Role] Perspective
- Their framework's top scoring criteria
- Recommendation
- Top risks they see
- What evidence would change their position

## 3. Points of Agreement
[Be specific; not "everyone wants to win"]

## 4. Points of Tension
| Tension | Side A | Side B | Resolution Path |
|---|---|---|---|

(If unanimous, explicitly note "no material tension surfaced — flag for groupthink review")

## 5. Board Recommendation
[Synthesized recommendation with confidence level + the reason]

## 6. Action Items
| Action | Owner | Deadline | Success Criterion |

## 7. Open Questions / HITL
[What requires human decision before execution]

## 8. Dissenting Opinions
[Per the Dissenting Opinion Format below — recorded verbatim, never paraphrased away]

---
Filed by: [orchestrator-slug] | Date: YYYY-MM-DD
```

## RACI Matrix Template (sample rows — adapt per project)

| Decision | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Pricing change (material) | cro | cfo | cmo, cpo | ceo |
| New market entry | cso | ceo | cfo, cro, cmo, clo | board |
| M&A signing | mna-cockpit / clo | ceo | cfo, cso, coo, board | all |
| Capital project > threshold | capital-allocation | ceo | all relevant | board |
| AI deployment (high-risk class) | caio | ceo | clo, chief-compliance-officer, ciso | board |
| Cyber-incident response (SEV-1) | ciso / crisis-warroom | ceo | clo, chief-communications-officer, cfo | board |
| Layoff / RIF | chro | ceo | clo, cfo, chief-communications-officer | board |
| Regulatory filing (material) | chief-compliance-officer / clo | ceo | cfo | board |
| Brand reposition | cmo | ceo | chief-communications-officer, cpo | all |
| Data-platform rebuild | cdo | cto | cio, ciso, cfo | exec team |
| Climate transition plan | chief-sustainability-officer | ceo | cfo, csco, cto | board |
| Executive comp (NEO) | chro | board comp committee | ceo, cfo | board |

## OKR Template

```
## Q[N] 20XX OKRs — [Function / Firm]

### Objective 1: [Ambitious qualitative statement]
- KR1: [Metric] from [baseline] to [target] by [date]
- KR2: [Metric] from [baseline] to [target] by [date]
- KR3: [Metric] from [baseline] to [target] by [date]

Progress: [0.0–1.0; stretch = 0.7] | Owner: [exec-slug] | Risk: [color]
```

Cadence: monthly mid-cycle check, quarter-end scoring, retrospective.

## Decision Escalation Rules

| Scope | Authority | Process |
|---|---|---|
| Within single domain, within budget, reversible | Domain exec decides | Decision log |
| Cross-domain or above $/% threshold | `boardroom` (Quick Consult or Full) | Memo |
| Material capital or M&A | `capital-allocation` or `mna-cockpit` | Full debate protocol |
| Material legal / regulatory exposure | `clo` go/no-go authority | Legal memo + CEO notification |
| Risk appetite breach | `chief-risk-officer` escalation | Board notification |
| Crisis triggers | `crisis-warroom` activation | CEO + board notification |
| Board-reserved matters | Board | Per charter (committee structure) |

## Confidence-Level Rubric

| Level | Criteria |
|---|---|
| **High** | Multiple independent evidence sources; tested logic; no critical-assumption risk; senior team aligned; analogous precedent |
| **Medium** | Some evidence; some critical assumptions still unverified; mixed analogous precedent; surfaceable disagreement |
| **Low** | Mostly hypothesis; key data missing; novel situation; team disagreement; high reversibility cost |

Stating confidence is mandatory. "Not confident" is a legitimate output; "false confidence" is not.

## Dissenting Opinion Format

When a perspective disagrees with the synthesized recommendation:

```
### Dissent — [role-slug]
- Position: [What I think the right action is, in one sentence]
- Reasoning: [3–5 bullets — evidence, framework, precedent]
- Specific risk if majority recommendation is taken: [What I think breaks]
- Conditions under which I would change my position: [Evidence or events]
```

Dissent is preserved verbatim in the meeting minutes. Never paraphrased away. The research doc explicitly recommends preserving dissenting opinions to mitigate ensemble-LLM bias and groupthink.

## Strategy Canvas Template

```
# Strategy Canvas — [Topic]

## Current Position
| Factor | Our Position (1–10) | Market Average (1–10) | Best-in-Class (1–10) |
|---|---|---|---|

## Target Position (3 years)
[Where we want to move each factor and why]

## Strategic Moves (Four Actions Framework)
- **Raise** — factors to increase above market
- **Create** — new factors competitors don't offer
- **Reduce** — factors to decrease below market
- **Eliminate** — factors to stop investing in

## Trade-offs Made Explicit
[What we are choosing not to do, and why]
```

## Output Directory Convention

All artifacts go to `output/<domain>/<topic-kebab>-YYYY-MM-DD.md` per CLAUDE.md.
