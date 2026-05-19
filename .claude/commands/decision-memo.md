---
description: "Generate a formal Executive Memo on any decision using the appropriate exec(s)."
---

# /decision-memo

Produce a formal Executive Memo on a decision. Single-exec by default; multi-exec on cross-functional decisions.

## Usage

```
/decision-memo <decision question>                    # auto-route to relevant exec
/decision-memo --exec <slug> <decision question>      # explicit
/decision-memo --board <decision question>            # invokes boardroom
```

Examples:
- `/decision-memo Should we delay the launch by 6 weeks to add the SSO feature?`
- `/decision-memo --exec cfo Recommend the FY27 hurdle rate set by risk class`
- `/decision-memo --board Approve the European market entry?`

## Instructions to Claude

1. If `--board`, invoke `boardroom`. If `--exec`, route to that single exec. Otherwise, infer the single exec most directly responsible.
2. Apply the Executive Memo Format from `skills/executive-protocol`.
3. Score all options on the exec's decision framework.
4. List assumptions whose failure would change the recommendation.
5. Surface HITL approvals.
6. Save to `output/<domain>/<decision-kebab>-YYYY-MM-DD.md`.
