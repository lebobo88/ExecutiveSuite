---
description: "Request a single-domain executive brief — pick the exec and the question; output follows the Executive Memo Format."
argument-hint: "<exec-slug> <question or topic>"
---

# /exec-brief

Use a single C-suite executive agent to produce an Executive Memo on a focused question.

## Input
Target Executive & Question: $ARGUMENTS

## Instructions to Claude

1. Parse the `<exec-slug>` and topic from `$ARGUMENTS`.
2. Adopt the matching agent persona from `plugins/executive-suite/agents/<exec-slug>.md` applying its persona, decision framework, and constraints.
3. Apply that exec's decision framework explicitly.
4. If the question lacks necessary data, explicitly declare "Information not specified" for unverified assumptions.
5. Produce output in Executive Memo Format (see `plugins/executive-suite/skills/executive-protocol/SKILL.md`).
6. Save to `output/<domain>/<topic-kebab>-YYYY-MM-DD.md` per the exec's directive.
7. Surface any HITL approvals required and guardrail breaches (if applicable).

## Available execs

`ceo`, `cso`, `coo`, `cfo`, `cro`, `chief-risk-officer`, `cto`, `cio`, `cdo`, `caio`, `ciso`, `cpo`, `cmo`, `cxo`, `chief-communications-officer`, `chro`, `clo`, `chief-compliance-officer`, `csco`, `chief-sustainability-officer`
