---
description: "Run the Capital Allocation Committee debate protocol on a material capital decision."
---

# /capital-decision

Activate `capital-allocation` (CFO-chaired adversarial debate). Implements the 4-step debate protocol: Specification → Opening briefs (growth vs. discipline) → Cross-examination → Adjudication.

## Usage

```
/capital-decision <decision frame>
```

Examples:
- `/capital-decision $50M expansion of California manufacturing capacity — vs. return of capital`
- `/capital-decision $15M into new AI agent platform — competing with bolt-on M&A target`
- `/capital-decision $30M brand campaign vs. $30M product investment vs. dividend increase`

## Instructions to Claude

1. Adopt the `capital-allocation` agent persona (see `.claude/agents/capital-allocation.md`).
2. Apply the 4-step debate protocol from `skills/debate-protocol`.
3. Apply hard guardrails per `skills/financial-frameworks` Hard Guardrails Reference Table.
4. Compose the standing committee per the decision class (growth advocates + discipline + Referee).
5. Produce the option set (Approve full / Approve staged / Conditional / Restructure / Defer / Decline).
6. Save to `output/finance/<decision-kebab>-YYYY-MM-DD.md`.
7. Surface every guardrail breach with the override path required.
