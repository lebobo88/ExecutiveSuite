---
name: ai-governance
description: "AI governance — EU AI Act Article 9, NIST AI RMF, ISO/IEC 42001 — risk classification, lifecycle gates, model cards, HITL policy, AI incident response."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# AI Governance

Used by `caio` and `chief-compliance-officer`. Implements the governance posture required by the research doc (Section "Governance, Ethics, and Risk Protection Architecture") and externally by EU AI Act Article 9, NIST AI RMF, and ISO/IEC 42001.

## EU AI Act Risk Categorization

| Class | Treatment | Examples |
|---|---|---|
| **Unacceptable** | Prohibited — do not build/deploy | Social scoring of natural persons, manipulative dark-pattern AI, real-time remote biometric ID in public spaces |
| **High-risk** | Full Article 9 risk-management system; CE marking; HITL; logging; post-market monitoring; conformity assessment | Hiring & HR decisions; education access; credit scoring; safety-critical infra; law enforcement; biometric ID; product safety components |
| **Limited risk** | Transparency obligations: disclose AI use; label deepfakes; chatbot disclosure | Customer-facing chatbots, generative-content tools |
| **Minimal risk** | Voluntary best practices | Spam filters, video-game AI |

**Every AI use case is classified at intake.** High-risk requires CAIO + CLO + CCO joint approval.

## Article 9 Risk Management System Requirements

A continuous risk-management system for high-risk AI must:
1. Identify and analyze known and foreseeable risks
2. Estimate and evaluate risks under intended use and reasonably foreseeable misuse
3. Adopt risk-management measures (design, process, instructions, training)
4. Test the system against measurable metrics & probabilistic thresholds
5. Monitor post-deployment for new failure modes
6. Document everything — auditable trail

## NIST AI RMF — Function Map

| Function | Activities | Owner |
|---|---|---|
| **GOVERN** | Org-wide policies, accountability, culture, tolerance | CAIO + board AI committee |
| **MAP** | Context, stakeholders, intended use, impact | Use-case team + CAIO |
| **MEASURE** | Performance, fairness, robustness, drift, security | ML eng + CAIO |
| **MANAGE** | Risk prioritization, response, monitoring, escalation | Product owner + CAIO |

## Model Lifecycle Gates

| Gate | Required artifacts | Approver |
|---|---|---|
| **Design** | Use-case canvas, risk classification, data plan, HITL design | CAIO |
| **Train** | Data lineage, training-data card, fairness pre-check, intended-use statement | ML lead + CAIO |
| **Validate** | Eval-harness report, red-team report, model card | CAIO + (high-risk: CLO + CCO) |
| **Deploy** | Monitoring plan, rollback plan, HITL operationalized, comms | CAIO + product owner |
| **Monitor** | Drift, performance vs baseline, fairness, incident review (monthly for high-risk) | Product owner + CAIO |
| **Retire** | Migration plan, data retention/deletion, model archive, user comms | CAIO |

## Model Card Template

```
# Model Card — [Model name + version]

## Intended Use
- Primary use case: 
- Out-of-scope uses (explicit):
- Users / stakeholders:

## Risk Classification
- EU AI Act class:
- NIST AI RMF priorities:
- HITL requirement:

## Training Data
- Sources (datasets, dates, licenses):
- Lineage / provenance:
- Known biases / gaps:
- Privacy posture (PII handling):

## Architecture & Training
- Base model + version:
- Fine-tuning / adaptation method:
- Compute footprint:

## Evaluation
- Benchmarks (with scores):
- Fairness metrics (per protected group):
- Robustness tests (adversarial, OOD):
- Red-team findings (with mitigations):

## Deployment
- Serving environment:
- Latency / throughput:
- Cost per inference:
- Monitoring & alerts:
- Rollback procedure:

## Limitations
- Known failure modes:
- Hallucination posture:
- Calibration:

## Maintenance
- Owner:
- Review cadence:
- Retire-by date:
```

## Evaluation Harness Template

A passing harness includes:
- **Capability benchmarks** — task-specific (with baseline + target)
- **Robustness** — adversarial, OOD, prompt-injection, distribution-shift
- **Fairness** — per protected-group performance gap with tolerance
- **Safety** — red-team transcripts; harmful-output rate
- **Calibration** — when high-confidence, how often is it right?
- **Hallucination rate** — sample-and-judge harness
- **Regression suite** — prior failure modes covered
- **Drift detectors** — population stability index, feature drift, label drift

Harness runs at every retrain and on a schedule (weekly for high-risk).

## HITL Gate Criteria

| Class of use | HITL requirement |
|---|---|
| High-risk EU AI Act | Mandatory human review of decision before action |
| Material customer-impacting decisions | Mandatory human review |
| Reversible, low-stakes recommendations | Human-on-the-loop (review on sample / exception) |
| Internal productivity (drafting, summarizing) | Human-in-the-loop on output use |

HITL design must specify: who reviews, what they see, what override authority they have, how dissent is logged, and the latency tolerance.

## Audit-Trail Requirements

Every AI-driven recommendation/decision logs:
- Time, model + version, prompt, retrieval set (for RAG), output
- HITL reviewer + action (accept/modify/reject) + rationale
- Downstream consequence link (where applicable)

Retention: per regulator + per internal policy (typically 7 yr for material decisions).

## AI Incident Response

| Severity | Examples | Response |
|---|---|---|
| SEV-1 | Material harm, regulatory breach, model behavior breaching commitments | Immediate kill-switch; CAIO + CEO + CLO; <1 hr |
| SEV-2 | Performance breach, fairness drift, security finding | Throttle / rollback; CAIO + product owner; <4 hr |
| SEV-3 | Drift / regression detected | Monitoring + plan; ML lead; <24 hr |

Every SEV-1/2 gets a post-incident review with root cause + systemic mitigation.

## AI Red-Team Checklist

- Jailbreak attempts (across known techniques)
- Prompt injection (direct + indirect via retrieval)
- Data extraction (training-data leakage)
- Adversarial inputs (perturbations, OOD)
- Bias probes (per protected group)
- Misuse scenarios (per use-case mapping)
- Hallucination probes (fact-check on closed domain)
- Multi-turn manipulation
- Tool-use abuse (for agent systems)

Red-team report is a release-blocker for high-risk deployments.
