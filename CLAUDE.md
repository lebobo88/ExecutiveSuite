# ExecutiveSuite — AI C-Suite Operating Contract

A comprehensive multi-agent C-suite for enterprise strategic decision support, information triage, and financial architecture integration. Industry-agnostic; structured as a canonical Claude Code plugin (`plugins/executive-suite/`) and referenced as an enterprise roster.

## Provenance

Architecture grounded in: `Corporate Multi-Agent AI Systems for C-Suite Strategic Decision Support, Information Triage, and Financial Architecture Integration.md` (this directory). Agent file format mirrors [RLM-Creative](https://github.com/lebobo88/RLM-Creative) agents. Orchestration patterns informed by [pair-programmer](https://github.com/lebobo88/pair-programmer).

## Roster

### Executives (single-domain agents)
- `ceo` — Chief Executive Officer
- `cso` — Chief Strategy Officer
- `coo` — Chief Operating Officer
- `cfo` — Chief Financial Officer
- `cro` — Chief Revenue Officer
- `chief-risk-officer` — Chief Risk Officer (enterprise risk)
- `cto` — Chief Technology Officer
- `cio` — Chief Information Officer
- `cdo` — Chief Data Officer
- `caio` — Chief AI Officer
- `ciso` — Chief Information Security Officer
- `cpo` — Chief Product Officer
- `cmo` — Chief Marketing Officer
- `cxo` — Chief Customer Experience Officer
- `chief-communications-officer` — Chief Communications Officer
- `chro` — Chief Human Resources Officer
- `clo` — Chief Legal Officer / General Counsel
- `chief-compliance-officer` — Chief Compliance Officer
- `csco` — Chief Supply Chain Officer
- `chief-sustainability-officer` — Chief Sustainability Officer

### Orchestrators (multi-agent topologies)
- `boardroom` — Synthetic boardroom facilitator (hierarchical consensus)
- `mna-cockpit` — M&A opportunity triangulation cockpit
- `crisis-warroom` — Black swan capital preservation war-room
- `capital-allocation` — Capital allocation committee (CFO-led, debate protocol)

## Decision Protocol

Every executive output follows the Executive Memo Format from `plugins/executive-suite/skills/executive-protocol/SKILL.md`. Every multi-agent session follows the Board Meeting Protocol or its variant (debate, war-room, cockpit).

## Financial Hardcoding Directive

Per the research doc Section "Financial Framework Hardcoding Directive", agents MUST treat the following as first-class deterministic tools, not informal guidance:
- WACC computation (capital structure + market inputs)
- NPV, IRR, payback, economic profit
- Real-options valuation (binomial lattice or simulation)
- Monte Carlo scenario engines
- Covenant / leverage / liquidity checkers

Deterministic execution assets are located at `plugins/executive-suite/skills/financial-frameworks/scripts/finance_engine.py`.

Hard guardrails (minimum IRR, max leverage, covenant limits, prohibited counterparties, regulatory caps) MUST be enforced before any agent recommends action. The `financial-frameworks` skill encodes these.

## Governance & HITL

- EU AI Act Article 9 risk-management posture (see `plugins/executive-suite/skills/ai-governance/SKILL.md`)
- Every high-impact recommendation requires HITL approval; agents present options + dissenting opinions, never unilateral go/no-go
- All recommendations traceable to source data, model versions, intermediate reasoning (audit trail)
- Multi-agent failure mitigation: explicit role prompts, verification steps, termination conditions, no free-form swarms

## Multi-Agent Topologies

| Pattern | When to use | Driver agent |
|---------|-------------|--------------|
| Solo | Narrow, high-precision tasks (single-domain memo, NPV computation) | Individual executive |
| Debate (adversarial) | Capital allocation, growth-vs-discipline tensions | `capital-allocation` |
| Hierarchical consensus | Cross-functional strategic decisions | `boardroom` |
| Synthetic boardroom | M&A, major strategy, market entry | `mna-cockpit` or `boardroom` |
| War-room | Black swan, crisis, liquidity event | `crisis-warroom` |

## Output

Executive artifacts saved to `output/<domain>/<topic>-YYYY-MM-DD.md`. Domain directories:

```
output/
  strategy/         # CEO, CSO
  finance/          # CFO, capital-allocation
  revenue/          # CRO
  risk/             # chief-risk-officer
  operations/       # COO
  supply-chain/     # CSCO
  technology/       # CTO
  it/               # CIO
  data/             # CDO
  ai/               # CAIO
  security/         # CISO
  product/          # CPO
  marketing/        # CMO
  customer/         # CXO
  communications/   # chief-communications-officer
  people/           # CHRO
  legal/            # CLO
  compliance/       # chief-compliance-officer
  sustainability/   # chief-sustainability-officer
  board/            # boardroom
  mna/              # mna-cockpit
  crisis/           # crisis-warroom
```

## Conventions

- Every agent declares: model, maxTurns, skills, tools, and color (frontmatter)
- Default models: `opus` for CEO/CSO/CFO/CTO/CAIO/CPO/CLO/chief-risk-officer/boardroom/mna-cockpit/crisis-warroom/capital-allocation; `sonnet` for the rest
- Every agent has explicit `Constraints` (what they don't decide) and a defined output directory
- Every agent cites a decision framework with weighted criteria
- Prompts use structured XML tags (`<trusted_policy>`, `<role_definition>`, `<responsibilities>`, `<decision_framework>`, `<evidence_and_uncertainty>`, `<constraints>`, `<output_contract>`)
