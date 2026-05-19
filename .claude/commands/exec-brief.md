---
description: "Request a single-domain executive brief — pick the exec and the question; output follows the Executive Memo Format."
---

# /exec-brief

Use a single C-suite executive agent to produce an Executive Memo on a focused question.

## Usage

```
/exec-brief <exec-slug> <question or topic>
```

Examples:
- `/exec-brief cfo Evaluate the $25M production capacity expansion at the Ohio plant`
- `/exec-brief cmo Should we shift 20% of paid spend from search to YouTube?`
- `/exec-brief chief-risk-officer Refresh the top-risk register for Q3`
- `/exec-brief caio Classify our new résumé-screening model under the EU AI Act`

## Instructions to Claude

1. Parse the slug; route to the matching agent in `.claude/agents/<slug>.md` by adopting its persona, decision framework, and constraints.
2. Apply that exec's decision framework explicitly.
3. Produce output in Executive Memo Format (see `skills/executive-protocol/SKILL.md`).
4. Save to `output/<domain>/<topic-kebab>-YYYY-MM-DD.md` per the exec's directive.
5. Surface any HITL approvals required and guardrail breaches (if applicable).

## Available execs

`ceo`, `cso`, `coo`, `cfo`, `cro`, `chief-risk-officer`, `cto`, `cio`, `cdo`, `caio`, `ciso`, `cpo`, `cmo`, `cxo`, `chief-communications-officer`, `chro`, `clo`, `chief-compliance-officer`, `csco`, `chief-sustainability-officer`
