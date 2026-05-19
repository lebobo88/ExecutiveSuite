---
description: "Run the M&A Opportunity Triangulation cockpit (7-step workflow per research doc Masterclass 1)."
---

# /mna-review

Activate `mna-cockpit` for an M&A opportunity. Implements the 7-step workflow: signal detection → triage → financial diligence → operational → legal → boardroom synthesis → HITL approval + monitoring.

## Usage

```
/mna-review <target description or deal context>
```

Examples:
- `/mna-review CompetitorX — $80M EV, SaaS, adjacent market, dual-source for our enterprise plan`
- `/mna-review Bolt-on acquisition of regional supplier to vertically integrate inputs`

## Instructions to Claude

1. Adopt the `mna-cockpit` agent persona (see `.claude/agents/mna-cockpit.md`).
2. Execute the 7-step workflow in order. Do not skip steps.
3. Apply hard financial guardrails per `cfo` Financial Viability Gate (see `skills/financial-frameworks/SKILL.md`).
4. Use `skills/mna-playbook` for diligence checklists, valuation methods, real-options on structure, integration playbook.
5. Use `skills/debate-protocol` for the Step 6 boardroom synthesis.
6. Produce the option set (Go / Conditional / Staged / No-go) with explicit conditions.
7. Save to `output/mna/<target-kebab>-YYYY-MM-DD/` (a directory; the dossier has multiple files: target one-pager, financial model summary, operational diligence, legal matrix, decision memo, post-close monitoring plan).
