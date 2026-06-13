# AGENTS.md — ExecutiveSuite Cross-Tool Behavioral Contract

This file is the cross-tool entry point for any AI agent (Claude Code, Codex, Gemini, Copilot, etc.) working inside the ExecutiveSuite repo. The authoritative operating contract is **[`CLAUDE.md`](CLAUDE.md)** — read it first; this file summarizes identity, governance precedence, and pointers.

## Identity

ExecutiveSuite is a multi-agent **C-suite** for enterprise strategic decision support, information triage, and financial architecture integration: 20 single-domain executive agents, 4 multi-agent orchestrators (boardroom, mna-cockpit, crisis-warroom, capital-allocation), 9 shared skills, and 9 slash commands (24 agents total). Industry-agnostic; runs standalone or as the **"executive" squad** under [Hydra](https://github.com/lebobo88/Hydra).

## Ecosystem & Governance Precedence

ExecutiveSuite is one of nine sibling AI systems bound by **[AgentMesh](https://github.com/lebobo88/AgentMesh)** (the tenth, binding control plane). It enrolls into the mesh via the root `mesh-manifest.yaml`. AgentMesh routes and observes but enforces **no governance of its own**. Authority follows the precedence order:

> **TheEights → AgentSmith → Hydra**

- **[TheEights](https://github.com/lebobo88/TheEights)** — root of trust: memory, audit, identity, governance, self-evolution. Owns the propose/evaluate/commit cycle for evolving ExecutiveSuite's skills, rubrics, and agents; owns constitution attestation.
- **[AgentSmith](https://github.com/lebobo88/AgentSmith)** — artifact inspection and the N1..N10 fail-closed invariants; quarantine + sentinel.
- **[Hydra](https://github.com/lebobo88/Hydra)** — LangGraph supervisor that dispatches goals to ExecutiveSuite as the executive squad.

See `README.md` (Ecosystem section) for the full mesh map.

## Hard Rules

1. **Never edit `CONSTITUTION.md`.** It is the hash-pinned immortal head. Proposed amendments route as HITL through TheEights, never inline.
2. **Never bypass HITL.** Every high-impact recommendation surfaces required human approvals; agents present options + dissenting opinions, never a unilateral go/no-go.
3. **Honor the Financial Hardcoding Directive.** WACC / NPV / IRR / real-options / Monte Carlo / covenant / liquidity checks are first-class deterministic tools, not informal guidance. Hard guardrails are enforced *before* any recommendation (see `CLAUDE.md` and the `financial-frameworks` skill).
4. **Preserve dissent.** Dissenting opinions are recorded verbatim, never paraphrased away.
5. **Maintain the audit trail.** Every recommendation is traceable to source data, exec persona, and framework applied.

## Engineering Standards

- Agents are standard Claude Code subagents: Markdown + YAML frontmatter (`name`, `description`, `model`, `maxTurns`, `skills`).
- Default models: `opus` for CEO/CSO/CFO/CTO/CAIO/CPO/CLO/chief-risk-officer + all orchestrators; `sonnet` for the rest.
- Skills live under `.claude/skills/<name>/SKILL.md`; commands under `.claude/commands/`.
- Every executive declares explicit `Constraints` (what they do not decide) and a defined output directory.

## Where To Read More

- `CLAUDE.md` — the authoritative operating contract (roster, decision protocol, output structure, conventions).
- `CONSTITUTION.md` — the immortal head (read-only).
- `README.md` — architecture, ecosystem map, roster, installation.
- `Corporate Multi-Agent AI Systems...md` — the research basis grounding the design.
