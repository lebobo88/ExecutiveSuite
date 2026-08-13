# Boardroom Session

## Prompt

```
[Hydra→Executive Squad] You are the boardroom facilitator. Convene relevant executives (boardroom, caio, capital-allocation, cdo, ceo, cfo, chief-communications-officer, chief-compliance-officer). Topic: Decompose goal + budget split

[bon-candidate 3/3]

Constraints: {'budget_usd': None, 'token_limit': None, 'deadline_ts': None, 'risk_tolerance': 'medium', 'priority': 'P2', 'industries': []}
Envelope type: C_SUITE_DECISION_PACKET
Follow ExecutiveSuite Board Meeting Protocol. Output a C_SUITE_DECISION_PACKET with proposed_tasks decomposed for downstream squads, and a DECISION_RECORD with dissenting opinions preserved verbatim.
```

## Host-pickup result

- status: host_pickup_required
- summary: impersonation-prompt for agent='boardroom', 634b

## Raw

```json
{'status': 'host_pickup_required', 'summary': "impersonation-prompt for agent='boardroom', 634b", 'agent': 'boardroom', 'prompt_preview': "[Hydra→Executive Squad] You are the boardroom facilitator. Convene relevant executives (boardroom, caio, capital-allocation, cdo, ceo, cfo, chief-communications-officer, chief-compliance-officer). Topic: Decompose goal + budget split\n\n[bon-candidate 3/3]\n\nConstraints: {'budget_us"}
```
