---
description: "Convene a synthetic boardroom session — auto-routes attendees by topic; outputs board minutes."
argument-hint: "[--format brief|full|strategic] [--attendees slug1,slug2] <topic>"
disable-model-invocation: true
---

# /board-meeting

Convene the synthetic boardroom (`boardroom` agent) on a topic. Sequential multi-executive perspectives → agreement / tension surfacing → synthesized recommendation + action items.

## Input
Meeting Parameters & Topic: $ARGUMENTS

## Instructions to Claude

1. Adopt the `boardroom` orchestrator persona (see `plugins/executive-suite/agents/boardroom.md`).
2. Parse any flags (`--format`, `--attendees`) from `$ARGUMENTS`. If attendees are not specified, use the Auto-Routing Logic table in `boardroom.md`.
3. Sequentially impersonate each attendee in-process using their decision framework. Do NOT spawn subagents.
4. Produce output in Board Meeting Protocol format (see `plugins/executive-suite/skills/executive-protocol/SKILL.md`).
5. Save to `output/board/<topic-kebab>-YYYY-MM-DD.md`.
6. Preserve dissenting opinions verbatim per the Dissent Format. Flag groupthink if perspectives are unanimously identical.
7. Surface all required HITL human approvals.
