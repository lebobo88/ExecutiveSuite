---
description: "Run a scenario stress test — CFO liquidity + Chief Risk top-register + Chief Sustainability climate."
---

# /risk-stress

Run a triple-stress scenario test: financial liquidity (CFO), enterprise top-risk register (Chief Risk), climate transition (Chief Sustainability). Outputs a combined stress posture memo.

## Usage

```
/risk-stress [scenario]
```

If no scenario is specified, run the default trio: base + moderate (-25% revenue) + severe (-50% revenue) + reverse-stress.

Examples:
- `/risk-stress`
- `/risk-stress Sustained -30% volume from new tariff regime for 18 months`
- `/risk-stress Carbon-price step to $150/tCO2e by 2030`

## Instructions to Claude

1. Adopt the personas of `cfo`, `chief-risk-officer`, and `chief-sustainability-officer` sequentially.
2. Apply liquidity stress template per `skills/financial-frameworks`.
3. Apply scenario-planning template per `skills/scenario-planning` (Monte Carlo + tornado).
4. Run reverse stress test per `skills/enterprise-risk`.
5. Climate scenario per TCFD / IFRS S2 (1.5°C / 2°C / 3°C+).
6. Synthesize: residual risk vs. risk-appetite statement; named mitigations.
7. Save to `output/risk/stress-<scenario-kebab>-YYYY-MM-DD.md`.
