---
name: mna-playbook
description: "M&A playbook — deal thesis, screening, financial/commercial/legal diligence, valuation methods, real-options on deal structure, integration playbook, post-deal KPIs."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# M&A Playbook

Used by `mna-cockpit`, `cso`, `cfo`, `clo`. Embodies the discipline that prevents value-destroying acquisitions: optimistic synergies, inadequate integration planning, insufficient risk pricing.

## Deal-Thesis Canvas

```
## Deal Thesis — [Target]

### Why this target?
- Strategic adjacency (market / capability / tech / customer):
- Why now (timing thesis):
- Why us (capability fit; we can extract value others can't):

### Value-creation hypothesis
- Revenue synergies (specific, quantified):
- Cost synergies (specific, quantified):
- Capability acquisition (talent, IP, technology):
- Strategic optionality unlocked:

### Risks acknowledged up front
- Integration:
- Cultural:
- Customer overlap / cannibalization:
- Regulatory:
- Key-person:

### Walk-away criteria
- Maximum price (per share / EV):
- Maximum leverage post-close:
- Conditions that would cause us to walk:
```

## Target-Screening Checklist

| Gate | Threshold | Pass / Fail |
|---|---|---|
| Strategic fit (adjacency hypothesis) | Credible | |
| Size fit (EV range) | Board-approved band | |
| Financial health (revenue growth, margin, FCF) | Acceptable | |
| Antitrust / regulatory red flags | None disqualifying | |
| Reputational red flags | None disqualifying | |
| ESG / climate posture | Consistent with transition plan | |
| Strategic capacity to integrate | We are not already over-extended | |

## Financial Diligence Checklist

| Area | Required artifacts |
|---|---|
| Historicals | 3 yr audited; LTM trailing; QoE adjustments |
| Quality of earnings | Non-recurring items, accounting changes, customer concentration, related-party |
| LTM normalization | Adjust for one-time, working-capital seasonality, stock-comp |
| Working-capital target | Methodology; PEG / non-PEG; what's "normal" |
| Debt-like items | Identified; impact on EV-to-equity bridge |
| Off-balance-sheet | Leases, contingent liabilities, warranties, guarantees |
| Tax | Audits, NOLs, attributes survivable, transfer-pricing exposure |
| Forecast | Re-built bottom-up; key driver assumptions tested |

## Commercial Diligence Checklist

| Area | Required artifacts |
|---|---|
| Market sizing | TAM/SAM/SOM; growth drivers; cyclical vs structural |
| Customer interviews | NPS, churn, share-of-wallet, willingness-to-pay |
| Competitive position | Share, win/loss, moat assessment |
| Pricing | Realized, list, discount governance, elasticity |
| Sales productivity | Per-rep, ramp time, cycle length |
| Product position | Roadmap credibility, technical debt, AI exposure |

## Synergy Estimation (cost + revenue)

| Type | Estimation method | Realization curve |
|---|---|---|
| Cost — back-office consolidation | Per-FTE × headcount × dis-synergy haircut | yr1: 30% / yr2: 60% / yr3: 90% |
| Cost — facility consolidation | Lease + occupancy savings | yr1: 0% / yr2: 50% / yr3: 100% |
| Cost — procurement | Pooled volume × pricing concession × supplier concentration risk | yr1: 25% / yr2: 75% / yr3: 100% |
| Revenue — cross-sell | (Customers × penetration × ARPU) × probability | yr1: 10% / yr2: 30% / yr3: 60% (cautious) |
| Revenue — bundling / pricing | Customer surplus realizable × conversion rate | yr1: 20% / yr2: 50% / yr3: 80% |

**Discount synergies at a higher hurdle** than base-business cash flows (e.g., WACC + 3–5%). Revenue synergies require harsher discount than cost.

## Legal & Regulatory Diligence (abbrev.)

- Corporate / cap table / equity instruments
- Material contracts (assignability / CoC clauses)
- Antitrust threshold (HSR US; EU; sector-specific approvals)
- IP (chain of title, OSS compliance, freedom-to-operate)
- Employment (top talent, equity, IP assignment, immigration)
- Privacy & data (DPIAs, breach history, cross-border)
- Litigation / regulatory inquiries
- Tax
- ESG / climate disclosures

Coordinate with `clo` for legal-risk matrix (fatal / remediable / acceptable).

## Valuation Methods (triangulation)

| Method | When | Caveat |
|---|---|---|
| DCF | Almost always | Sensitive to terminal value & WACC |
| Trading comps (EV/EBITDA, EV/Rev) | Public peer set available | Multiples expand/contract; pick cycle-adjusted |
| Precedent transactions | Recent comparable deals | Control premium varies; size matters |
| LBO | Sponsor-comparable; check max LBO price | Reveals leverage capacity, not strategic value |
| Sum-of-the-parts | Multi-segment targets | Allocation assumptions |
| Real-options | Staged structures, contingent consideration | Volatility assumption dominates |

**Triangulate 3+ methods.** Report the range, not the point.

## Real-Options on Deal Structure

| Structure | When | Option value |
|---|---|---|
| **Earn-out** | Synergy realization uncertain; seller confident | Defers risk to seller; reduces upfront price |
| **Contingent consideration** | Specific milestones (regulatory, customer retention) | Aligns incentives |
| **Staged / phased** | Big-bet integration; capability acquisition | Real-options value of cancel-at-step |
| **Minority + option to acquire** | Capability we want to validate first | Pay for the option, exercise on evidence |
| **Joint venture** | Capability with shared risk; market entry | Reversibility |

## Integration Playbook (Day-1 / Day-100 / Year-1)

### Day-1
- Combined ELT communication
- Customer communication (with `chief-communications-officer`)
- Employee communication (with `chro`)
- Legal entity / payroll / benefits continuity
- Critical-system access / security (with `ciso`)

### Day-100
- Org-design decisions for top 3 layers
- Customer-overlap rationalization plan
- Quick-win cost synergies actioned
- Cultural integration program launched
- KPI dashboard live

### Year-1
- Synergy capture vs plan (with explanation for any miss)
- Customer retention vs pre-close NPS
- Talent retention vs pre-close benchmark
- Working-capital integrated
- Systems integration milestones hit
- Post-close review to board

## Post-Deal KPI Tracker

| KPI | Baseline | Target | Actual M3 | M6 | M12 |
|---|---|---|---|---|---|
| Synergy capture ($M) | | | | | |
| Customer retention (% of pre-close ARR) | | | | | |
| Top-100 talent retention | | | | | |
| Cultural-integration index | | | | | |
| Systems-integration milestones (% hit) | | | | | |
| Operating margin (combined) | | | | | |

## Output

M&A artifacts saved to `output/mna/`. Each deal gets a full dossier; see `mna-cockpit.md`.
