---
description: "Show the executive roster, orchestrators, skills, and commands available in ExecutiveSuite."
argument-hint: ""
---

# /executive-team

Display the C-suite roster with one-line descriptions, plus orchestrators, skills, and slash commands.

## Instructions to Claude

Produce a structured listing:

### Single-Domain Executives (20)
Read each `plugins/executive-suite/agents/*.md` (excluding orchestrators) and list:
- `<slug>` — Full title — one-line description from frontmatter

Ordered: `ceo`, `cso`, `coo`, `cfo`, `cro`, `chief-risk-officer`, `cto`, `cio`, `cdo`, `caio`, `ciso`, `cpo`, `cmo`, `cxo`, `chief-communications-officer`, `chro`, `clo`, `chief-compliance-officer`, `csco`, `chief-sustainability-officer`

### Orchestrators (4)
- `boardroom` — Synthetic boardroom facilitator (hierarchical consensus)
- `mna-cockpit` — M&A Opportunity Triangulation (research doc Masterclass 1)
- `crisis-warroom` — Black Swan Capital Preservation (research doc Masterclass 2)
- `capital-allocation` — Capital Allocation Committee (debate protocol)

### Skills (9)
List from `plugins/executive-suite/skills/*/SKILL.md`: name + description from frontmatter.

### Slash commands (9)
List from `plugins/executive-suite/commands/*.md`: name + description.

### Output directories
Reference `CLAUDE.md` for the `output/*` layout.

End with a 2-sentence summary of when to use which orchestrator and which command.
