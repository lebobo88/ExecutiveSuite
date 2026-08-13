---
description: "Run a full-C-suite quarterly business review — every exec contributes a section."
argument-hint: "Q[N] [YYYY]"
disable-model-invocation: true
---

# /quarterly-review

Run a comprehensive Quarterly Business Review (QBR) with contributions from every relevant C-suite agent. Each exec produces a one-page section in their domain.

## Input
Target Quarter: $ARGUMENTS

## Instructions to Claude

For the named quarter from `$ARGUMENTS`, generate sections in this order, adopting each exec's persona from `plugins/executive-suite/agents/`:

1. **CEO** — Strategic context, top 3 quarterly highlights / lowlights, capital allocation summary
2. **CSO** — Strategic-bet portfolio status, M&A pipeline, competitive intel update
3. **CFO** — Financial performance (vs. plan + vs. guidance), liquidity & covenant headroom, capital deployed
4. **CRO** — Revenue, pipeline coverage, NRR/GRR, top 5 wins/losses with lessons
5. **CMO** — Pipeline contribution, brand health, CAC/LTV trajectory, top campaign learning
6. **CPO** — Roadmap status, North Star Metric, top 3 launched / killed features
7. **CXO** — NPS / CSAT / CES, churn / expansion drivers, top customer themes
8. **COO** — Operational KPIs (OEE, OTIF, productivity, safety), top 3 process improvements
9. **CSCO** — Supply-chain resilience, supplier risk events, working-capital (CCC)
10. **CTO** — Platform health (DORA), top tech investments, build/buy/partner decisions
11. **CIO** — Application portfolio status (TIME), integration & ITSM KPIs
12. **CDO** — Data quality / lineage / privacy posture, top data products
13. **CAIO** — AI use-case portfolio, model lifecycle status, AI incidents (if any)
14. **CISO** — Cyber posture (NIST CSF), incidents, top control gaps closing
15. **CHRO** — Workforce, engagement, top talent moves, succession depth
16. **CLO** — Material legal matters, regulatory developments, contract risk
17. **Chief Compliance** — Compliance program status, exam readiness, hotline themes
18. **Chief Risk** — Top-risk register movement, risk-appetite breaches, KRI trends
19. **Chief Sustainability** — ESG/climate progress, Scope 1/2/3, disclosure readiness
20. **Chief Communications** — Stakeholder narrative, IR / employee / customer pulse

**Synthesize**: top 5 themes across the QBR, top 3 risks emerging, top 3 priorities for next quarter.

Save to `output/board/qbr-Q[N]-YYYY-MM-DD.md`.
