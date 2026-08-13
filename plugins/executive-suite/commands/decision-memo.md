---
description: "Generate a formal Executive Memo on any decision using the appropriate exec(s)."
argument-hint: "[--exec <slug> | --board] <decision question>"
---

# /decision-memo

Produce a formal Executive Memo on a decision. Single-exec by default; multi-exec on cross-functional decisions.

## Input
Target Scope & Decision Question: $ARGUMENTS

## Instructions to Claude

1. If `--board`, invoke `boardroom`. If `--exec <slug>`, route to that single exec in `plugins/executive-suite/agents/<slug>.md`. Otherwise, infer the single exec most directly responsible.
2. Apply the Executive Memo Format from `plugins/executive-suite/skills/executive-protocol/SKILL.md`.
3. Score all options on the exec's decision framework.
4. List assumptions whose failure would change the recommendation; label unverified facts as "Information not specified".
5. Surface all required HITL approvals.
6. Save to `output/<domain>/<decision-kebab>-YYYY-MM-DD.md`.
