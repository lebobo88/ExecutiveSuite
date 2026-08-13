---
name: debate-protocol
description: "Adversarial red-team debate protocol — when to use it, the 4-step structure, role-pair recipes, Referee scoring, termination conditions, MAS failure mitigations."
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Debate Protocol

Per the research doc (Section "Adversarial Red-Teaming (Debate Protocol)"), debate-style multi-agent topologies mitigate individual-LLM bias and surface hidden assumptions. Used by `capital-allocation`, `mna-cockpit`, `boardroom` (when explicitly invoked), and `crisis-warroom` (option-ranking step).

## When to Use Debate vs. Consensus

| Pattern | Use when |
|---|---|
| **Debate** | Decision is high-stakes, irreversible, contains strong narrative pull, has structural tension between functions, has well-known cognitive biases (sunk cost, anchoring, optimism) |
| **Hierarchical consensus** (boardroom) | Decision is cross-functional but not adversarial; perspectives need to compose, not contend |
| **Solo** | Narrow, high-precision, single-domain; debate adds overhead without insight gain |

Default: capital allocation, M&A, growth-vs-discipline tradeoffs → DEBATE. Strategy refresh, talent calibration, ESG plan → CONSENSUS.

## 4-Step Protocol

### Step 1 — Specification (Orchestrator)

Define decision frame and shared data bundle:

```
Decision: [What is being decided]
Shared data: [What both sides have access to]
Time horizon: [N years / quarters]
Reversibility: [How much we can unwind]
Decision authority: [Who has final say after debate]
```

Both sides agree on the frame before opening. Disagreement on frame is itself a finding — escalate to the orchestrator to resolve.

### Step 2 — Opening Briefs

Structured templates — both sides answer the same questions, from opposing positions:

**Pro-Action template:**
```
Position: [What we should do]
Strategic thesis: [Why it matters; what changes for the firm]
Base case: [Quantified expected outcome]
Upside drivers: [Specific, evidenced]
Downside acknowledgment: [Honest worst case]
Optionality preserved: [What future moves does this enable?]
Execution plan: [Phased, owners, milestones]
Kill criteria: [What stops us mid-flight]
```

**Discipline-Challenge template:**
```
Where the base case is too optimistic: [3–5 specific assumptions]
What discipline lens shows: [Stressed financials / risk]
Hidden costs: [TCO, integration, working capital, talent]
Guardrail check: [Pass / fail / margin on each]
Opportunity cost: [What else could we do?]
Reversibility cost: [How much to unwind]
Catastrophic-failure conditions: [Reverse stress]
```

Briefs are written; both sides read the other's before cross-examination (no surprise rhetoric).

### Step 3 — Cross-Examination

Each side queries the other:
- Assumption: "Your case assumes X — what's the evidence?"
- Data gap: "Do we have commitments or just TAM?"
- Model risk: "Your WACC assumes current capital structure — does this transaction change it?"
- Execution dependency: "Synergy curve assumes 2 integrations in 12 months — can we?"

**Single round of clarification per question.** No infinite back-and-forth (this is the step-repetition MAS failure mode the research doc cites).

### Step 4 — Adjudication

A Referee (CEO-aligned synthesizer; not a debater) writes:

```
## Points of Agreement
[Where evidence converges; one side conceded]

## Resolved Tensions
[Tension + the evidence that resolved it + the new shared position]

## Unresolved Tensions
[Tension + what data would resolve it + cost/time to obtain]

## Guardrail Status
[Each guardrail: pass / fail / margin]

## Confidence
High / Medium / Low — with the reason

## Option Set
[Concrete options with explicit conditions — never a binary]
```

## Role-Pair Recipes (common pairings)

| Topic | Advocate | Challenger | Referee |
|---|---|---|---|
| Capital allocation (growth) | cmo + cpo | cfo + chief-risk-officer | ceo |
| Build-vs-buy (technology) | cto | cfo | cpo (user-value lens) |
| Speed-vs-security | cpo + cto | ciso | ceo |
| Marketing spend (brand vs perf) | cmo (brand) | cmo (perf) + cfo | ceo |
| Talent investment vs cost | chro | cfo | ceo |
| Sustainable sourcing vs cost | chief-sustainability-officer | csco + cfo | ceo |
| M&A: strategic premium | cso + cmo | cfo + chief-risk-officer | ceo |
| Pricing power test | cro | cfo + cmo | ceo |

## Referee Scoring Rubric

Each side scored on:

| Criterion | Weight |
|---|---|
| Evidence quality (data + analogous precedent) | 30% |
| Logical coherence (no contradictions; framework consistent) | 20% |
| Engagement with counter-evidence (acknowledged + addressed) | 20% |
| Quantification (financial + operational) | 20% |
| Reversibility-cost honesty | 10% |

The Referee scores; the better-supported case is preferred. Ties default to discipline (reversibility).

## Termination Conditions (MAS Failure Mitigations)

The research doc names these failure modes; the protocol mitigates each:

| Failure mode | Mitigation |
|---|---|
| Step repetition | Single clarification round; Referee enforces |
| Derailment | Frame agreed in Step 1; off-frame questions deferred |
| Missing verification | Both sides answer same questions; Referee gates on completeness |
| Premature termination | Adjudication explicitly checks each section above |
| Late termination | Cross-examination time-boxed (default: 30 min / 5 exchanges) |
| Specification ambiguity | Step 1 is explicit; "Decision: …" sentence required |
| Organizational breakdown | Role-pair recipe pre-defined; no ad-hoc participation |
| Inter-agent conflict (irreconcilable) | Explicit "irreconcilable" flag → escalate to CEO with both positions preserved |

## Output

Saved per the orchestrator invoking the protocol (typically `output/finance/`, `output/mna/`, `output/crisis/`, `output/board/`).
