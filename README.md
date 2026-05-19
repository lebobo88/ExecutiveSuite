# ExecutiveSuite

A comprehensive multi-agent C-suite for Claude Code: 20 single-domain executive agents + 4 multi-agent orchestrators (synthetic boardroom, M&A cockpit, crisis war-room, capital allocation committee), 9 shared skills (executive protocol, financial frameworks, AI governance, debate protocol, scenario planning, enterprise risk, M&A playbook, crisis response, stakeholder communications), and 8 slash commands.

Grounded in the research document `Corporate Multi-Agent AI Systems for C-Suite Strategic Decision Support, Information Triage, and Financial Architecture Integration.md`. Implements its **Financial Framework Hardcoding Directive**, its **synthetic boardroom / M&A triangulation / black-swan war-room masterclasses**, and its **EU AI Act / NIST AI RMF governance posture**.

## Installation

ExecutiveSuite can be installed at **project scope** (only available inside this directory — the default) or **user scope** (available in every project on the machine).

### Project scope (default)

Already done — the `.claude/` directory in this repo is auto-discovered by Claude Code when you run a session here.

### User scope (Windows, symlink — recommended for live updates)

Symlink the agents/skills/commands into `~/.claude/` so edits in this repo propagate to every project instantly. Requires either an **elevated PowerShell** or Windows **Developer Mode** enabled (`Settings → System → For developers → Developer Mode`).

```powershell
$src = "C:\AiAppDeployments\ExecutiveSuite\.claude"
$dst = "$env:USERPROFILE\.claude"

foreach ($d in 'agents','skills','commands') {
  Get-ChildItem "$src\$d" | ForEach-Object {
    $linkPath = Join-Path "$dst\$d" $_.Name
    if (Test-Path $linkPath) { Remove-Item $linkPath -Recurse -Force }
    New-Item -ItemType SymbolicLink -Path $linkPath -Target $_.FullName | Out-Null
  }
}
```

Verify:

```powershell
$dst = "$env:USERPROFILE\.claude"
foreach ($d in 'agents','skills','commands') {
  $n = (Get-ChildItem "$dst\$d" |
        Where-Object { $_.LinkType -eq 'SymbolicLink' -and $_.Target -like '*ExecutiveSuite*' }).Count
  "$d : $n symlinks"
}
# Expected: agents : 24, skills : 9, commands : 9
```

**What's intentionally NOT linked:**
- `settings.json` — project-scoped (output root + statusline); do not promote to user scope.
- `CLAUDE.md` — project contract; promoting it would inject ExecutiveSuite framing into every unrelated project.

**Output location after user-scope install:** the agents write to `output/<domain>/…` relative to **the project Claude Code was launched from**, so each project accumulates its own `output/` tree. No `output/` is written into `~/.claude/`.

**Caveats:**
- Moving or deleting this repo breaks every symlink.
- Renaming an asset in the repo leaves a dangling link in `~/.claude/` until the script is re-run.

### User scope — copy instead (no Developer Mode / Admin needed)

If you can't enable Developer Mode and don't want to run as Admin, copy instead of symlinking. Edits in the repo will then require re-running this to propagate.

```powershell
$src = "C:\AiAppDeployments\ExecutiveSuite\.claude"
$dst = "$env:USERPROFILE\.claude"

Copy-Item "$src\agents\*"   "$dst\agents\"   -Recurse -Force
Copy-Item "$src\skills\*"   "$dst\skills\"   -Recurse -Force
Copy-Item "$src\commands\*" "$dst\commands\" -Recurse -Force
```

### Rollback (user scope)

Removes only the ExecutiveSuite assets from `~/.claude/` (links or copies); leaves the source repo untouched.

```powershell
$dst = "$env:USERPROFILE\.claude"

# Symlinks: safe filter by target
foreach ($d in 'agents','skills','commands') {
  Get-ChildItem "$dst\$d" |
    Where-Object { $_.LinkType -eq 'SymbolicLink' -and $_.Target -like '*ExecutiveSuite*' } |
    ForEach-Object { Remove-Item $_.FullName -Force }
}

# Copies: remove by name
$execAgents = 'ceo','cso','coo','cfo','cro','chief-risk-officer','cto','cio','cdo','caio','ciso','cpo','cmo','cxo','chief-communications-officer','chro','clo','chief-compliance-officer','csco','chief-sustainability-officer','boardroom','mna-cockpit','crisis-warroom','capital-allocation'
$execAgents | ForEach-Object { Remove-Item "$dst\agents\$_.md" -ErrorAction SilentlyContinue }

$execSkills = 'executive-protocol','financial-frameworks','ai-governance','debate-protocol','scenario-planning','enterprise-risk','mna-playbook','crisis-response','stakeholder-comms'
$execSkills | ForEach-Object { Remove-Item "$dst\skills\$_" -Recurse -Force -ErrorAction SilentlyContinue }

$execCmds = 'exec-brief','board-meeting','mna-review','crisis-mode','capital-decision','quarterly-review','decision-memo','risk-stress','executive-team'
$execCmds | ForEach-Object { Remove-Item "$dst\commands\$_.md" -ErrorAction SilentlyContinue }
```

### macOS / Linux

`~/.claude/` works the same on POSIX systems. Use `ln -s` instead of `New-Item -ItemType SymbolicLink`:

```bash
src="$HOME/AiAppDeployments/ExecutiveSuite/.claude"   # adjust path
dst="$HOME/.claude"
for d in agents skills commands; do
  for f in "$src/$d"/*; do
    ln -snf "$f" "$dst/$d/$(basename "$f")"
  done
done
```

## Quick Start

Once installed (either scope), from any Claude Code session:

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
