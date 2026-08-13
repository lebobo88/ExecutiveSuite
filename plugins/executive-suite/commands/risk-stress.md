---
description: "Run a scenario stress test — CFO liquidity + Chief Risk top-register + Chief Sustainability climate."
argument-hint: "[scenario description]"
disable-model-invocation: true
---

# /risk-stress

Run a triple-stress scenario test: financial liquidity (CFO), enterprise top-risk register (Chief Risk), climate transition (Chief Sustainability). Outputs a combined stress posture memo.

## Input
Stress Scenario: $ARGUMENTS

## Instructions to Claude

1. If no scenario is specified in `$ARGUMENTS`, run the default trio: base + moderate (-25% revenue) + severe (-50% revenue) + reverse-stress.
2. Adopt the personas of `cfo`, `chief-risk-officer`, and `chief-sustainability-officer` sequentially (from `plugins/executive-suite/agents/`).
3. Apply liquidity stress template per `plugins/executive-suite/skills/financial-frameworks/SKILL.md` using `finance_engine.py`.
4. Apply scenario-planning template per `plugins/executive-suite/skills/scenario-planning/SKILL.md` (Monte Carlo + tornado).
5. Run reverse stress test per `plugins/executive-suite/skills/enterprise-risk/SKILL.md`.
6. Climate scenario per TCFD / IFRS S2 (1.5°C / 2°C / 3°C+).
7. Synthesize: residual risk vs. risk-appetite statement; named mitigations.
8. Save to `output/risk/stress-<scenario-kebab>-YYYY-MM-DD.md`.
