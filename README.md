# ExecutiveSuite

A comprehensive multi-agent C-suite for Claude Code: 20 single-domain executive agents + 4 multi-agent orchestrators (synthetic boardroom, M&A cockpit, crisis war-room, capital allocation committee), 9 shared skills (executive protocol, financial frameworks, AI governance, debate protocol, scenario planning, enterprise risk, M&A playbook, crisis response, stakeholder communications), and 8 slash commands.

Grounded in the research document `Corporate Multi-Agent AI Systems for C-Suite Strategic Decision Support, Information Triage, and Financial Architecture Integration.md`. Implements its **Financial Framework Hardcoding Directive**, its **synthetic boardroom / M&A triangulation / black-swan war-room masterclasses**, and its **EU AI Act / NIST AI RMF governance posture**.

## Quick Start

From any Claude Code session in this directory:

```
/executive-team                                # See the roster
/exec-brief cfo Evaluate the Ohio plant expansion
/board-meeting Should we acquire CompetitorX?
/capital-decision $50M brand campaign vs. R&D investment
/mna-review Bolt-on of regional supplier
/crisis-mode red Ransomware on production ERP
/quarterly-review Q3 2026
/decision-memo Should we delay launch by 6 weeks?
/risk-stress
```

## Roster

### Single-domain executives (20)
ceo · cso · coo · cfo · cro · chief-risk-officer · cto · cio · cdo · caio · ciso · cpo · cmo · cxo · chief-communications-officer · chro · clo · chief-compliance-officer · csco · chief-sustainability-officer

### Multi-agent orchestrators (4)
`boardroom` · `mna-cockpit` · `crisis-warroom` · `capital-allocation`

### Skills (9)
`executive-protocol` · `financial-frameworks` · `ai-governance` · `debate-protocol` · `scenario-planning` · `enterprise-risk` · `mna-playbook` · `crisis-response` · `stakeholder-comms`

### Slash commands (8)
`/exec-brief` · `/board-meeting` · `/mna-review` · `/crisis-mode` · `/capital-decision` · `/quarterly-review` · `/decision-memo` · `/risk-stress` · `/executive-team`

## How it works

Each agent is a standard Claude Code subagent — Markdown with YAML frontmatter (`name`, `description`, `model`, `maxTurns`, `skills`). Subagents are invoked by name (via the Agent tool) or routed automatically when their `description` matches the task. See the [official Claude Code agents documentation](https://code.claude.com/docs/en/sub-agents).

The orchestrators (`boardroom`, `mna-cockpit`, `crisis-warroom`, `capital-allocation`) impersonate multiple executive perspectives **in-process** (not by spawning subagents) — sequential persona adoption per role, with synthesized output. This mitigates the multi-agent failure modes (specification ambiguity, organizational breakdown, weak verification) cataloged in the research doc.

Skills are loaded into context when listed in an agent's `skills:` frontmatter (per the official spec). The `executive-protocol` skill provides the memo + board-meeting + RACI + OKR templates every agent uses.

## Governance Posture

- **Financial Hardcoding Directive** — WACC / NPV / IRR / real-options / Monte Carlo / covenant / liquidity checks as first-class tools (`financial-frameworks` skill)
- **EU AI Act Article 9** — risk classification + lifecycle gates + audit trail (`ai-governance` skill)
- **NIST AI RMF** — GOVERN / MAP / MEASURE / MANAGE function map
- **COSO ERM 2017 + ISO 31000** — enterprise risk framework
- **HITL gates** — every high-impact recommendation surfaces required human approvals
- **Audit trail** — every recommendation traceable to source data, exec persona, framework applied
- **Dissent preservation** — dissenting opinions recorded verbatim, never paraphrased away

## Output structure

```
output/
  strategy/          # ceo, cso
  finance/           # cfo, capital-allocation
  revenue/           # cro
  risk/              # chief-risk-officer
  operations/        # coo
  supply-chain/      # csco
  technology/        # cto
  it/                # cio
  data/              # cdo
  ai/                # caio
  security/          # ciso
  product/           # cpo
  marketing/         # cmo
  customer/          # cxo
  communications/    # chief-communications-officer
  people/            # chro
  legal/             # clo
  compliance/        # chief-compliance-officer
  sustainability/    # chief-sustainability-officer
  board/             # boardroom
  mna/               # mna-cockpit
  crisis/            # crisis-warroom
```

## Provenance & related projects

- Research basis: `Corporate Multi-Agent AI Systems for C‑Suite Strategic Decision Support, Information Triage, and Financial Architecture Integration.md` (this dir)
- Agent format mirrors: `C:\AiAppDeployments\RLM-CLI-Starter\.claude\agents\rlm*.md` (media-vertical C-suite — generalized here to enterprise)
- Orchestration patterns informed by: `C:\AiAppDeployments\pair-programmer` (taxonomy / teams / debate harness)

## To extend

- Add an industry vertical: copy this `.claude/` into a project root and override agent files in that project's `.claude/agents/` (project scope wins per Claude Code subagent precedence).
- Add a new exec: drop a `<slug>.md` into `.claude/agents/` following the template (see any existing agent for the format).
- Add a workflow: drop a `<name>.md` into `.claude/commands/` with a `description:` frontmatter and a body describing the workflow.

## License & sensitivity

Internal-only. Output may contain commercially sensitive analysis; route per `chief-compliance-officer` data-classification policy.
