---
description: "Activate the Black Swan Capital Preservation war-room (6-step workflow per research doc Masterclass 2)."
argument-hint: "<tier: yellow|orange|red> <event description>"
disable-model-invocation: true
---

# /crisis-mode

Activate `crisis-warroom` for a black-swan event or sustained shock. Implements the 6-step workflow: early-warning telemetry → liquidity & covenant stress → operational reconfiguration → regulatory & contractual guardrails → synthetic crisis war-room → HITL execution.

## Input
Crisis Parameters & Event: $ARGUMENTS

## Instructions to Claude

1. Adopt the `crisis-warroom` agent persona (see `plugins/executive-suite/agents/crisis-warroom.md`).
2. Declare the tier (`yellow` | `orange` | `red`); log the trigger.
3. Execute the 6-step workflow.
4. Apply the Rapid Liquidity Stress template via `finance_engine.py`.
5. Draft a Holding Statement (≤ 60 min for SEV-1) per `plugins/executive-suite/skills/crisis-response/SKILL.md`.
6. Produce a decision log: every decision time-stamped + attributed.
7. Identify HITL decisions required and the named human executive.
8. Save artifacts to `output/crisis/<event-kebab>-YYYY-MM-DD/`.
9. After de-escalation, schedule the AAR (within 30 days).
