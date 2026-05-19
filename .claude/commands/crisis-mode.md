---
description: "Activate the Black Swan Capital Preservation war-room (6-step workflow per research doc Masterclass 2)."
---

# /crisis-mode

Activate `crisis-warroom` for a black-swan event or sustained shock. Implements the 6-step workflow: early-warning telemetry → liquidity & covenant stress → operational reconfiguration → regulatory & contractual guardrails → synthetic crisis war-room → HITL execution.

## Usage

```
/crisis-mode <tier> <event description>
```

Tier: `yellow` | `orange` | `red`

Examples:
- `/crisis-mode orange Major Tier-1 supplier has filed for bankruptcy; 35% of input volume at risk`
- `/crisis-mode red Ransomware detected on production ERP; ~24 hr to operational paralysis`
- `/crisis-mode yellow Geopolitical escalation in Region X threatens 15% of revenue`

## Instructions to Claude

1. Adopt the `crisis-warroom` agent persona (see `.claude/agents/crisis-warroom.md`).
2. Declare the tier; log the trigger.
3. Execute the 6-step workflow.
4. Apply the Rapid Liquidity Stress template (≤ 1 hr).
5. Draft a Holding Statement (≤ 60 min for SEV-1) per `skills/crisis-response`.
6. Produce a decision log: every decision time-stamped + attributed.
7. Identify HITL decisions required and the named human.
8. Save artifacts to `output/crisis/<event-kebab>-YYYY-MM-DD/`.
9. After de-escalation, schedule the AAR (within 30 days).
