---
description: "Convene a synthetic boardroom session — auto-routes attendees by topic; outputs board minutes."
---

# /board-meeting

Convene the synthetic boardroom (`boardroom` agent) on a topic. Sequential multi-executive perspectives → agreement / tension surfacing → synthesized recommendation + action items.

## Usage

```
/board-meeting <topic>                          # default: Full Board Meeting (3–5 attendees auto-routed)
/board-meeting --format brief <topic>           # Quick Consult (2–3 attendees, short)
/board-meeting --format strategic <topic>       # Strategic Session (5–7 attendees, deep)
/board-meeting --attendees ceo,cfo,cto <topic>  # Explicit attendee list
```

Examples:
- `/board-meeting Should we acquire CompetitorX for $80M?`
- `/board-meeting --format strategic Three-year strategy refresh — enter the European market?`
- `/board-meeting --attendees ceo,cfo,chief-risk-officer,chief-compliance-officer Response to the new EU AI Act high-risk classification of our hiring model`

## Instructions to Claude

1. Adopt the `boardroom` agent persona (see `.claude/agents/boardroom.md`).
2. If attendees not specified, use the Auto-Routing Logic table in `boardroom.md`.
3. Sequentially impersonate each attendee using their decision framework from `.claude/agents/<slug>.md`.
4. Produce output in Board Meeting Protocol format (see `skills/executive-protocol/SKILL.md`).
5. Save to `output/board/<topic-kebab>-YYYY-MM-DD.md`.
6. Preserve dissenting opinions verbatim per the Dissent Format.
