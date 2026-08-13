---
description: "Run the Capital Allocation Committee debate protocol on a material capital decision."
argument-hint: "<decision frame: project, amount, trade-off>"
disable-model-invocation: true
---

# /capital-decision

Activate `capital-allocation` (CFO-chaired adversarial debate). Implements the 4-step debate protocol: Specification → Opening briefs (growth vs. discipline) → Cross-examination → Adjudication.

## Input
Capital Decision Frame: $ARGUMENTS

## Instructions to Claude

1. Adopt the `capital-allocation` agent persona (see `plugins/executive-suite/agents/capital-allocation.md`).
2. Apply the 4-step debate protocol from `plugins/executive-suite/skills/debate-protocol/SKILL.md`.
3. Apply hard guardrails per `plugins/executive-suite/skills/financial-frameworks/SKILL.md` Hard Guardrails Reference Table using `finance_engine.py`.
4. Compose the standing committee per the decision class (growth advocates + discipline + Referee).
5. Produce the option set (Approve full / Approve staged / Conditional / Restructure / Defer / Decline).
6. Save to `output/finance/<decision-kebab>-YYYY-MM-DD.md`.
7. Surface every guardrail breach with the override path required.
