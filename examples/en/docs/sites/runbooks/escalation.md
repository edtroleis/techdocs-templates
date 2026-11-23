# Escalation

When the runbook does not solve the problem, or customers in more than one product are affected.

## Severity

| Severity | Example                                        | Escalate after |
| -------- | ---------------------------------------------- | -------------- |
| Critical | More than 5% of payments failing               | 15 minutes     |
| High     | Payments slow (p99 over 3 s) but going through | 30 minutes     |
| Warning  | Refunds delayed, no customer impact yet        | Next morning   |

## Who to call

1. The second Payments on-call, through the on-call tool.
2. The provider's support line, for `provider_unavailable` errors (number in the vault, `payments/provider`).
3. The incident manager on duty, for any critical incident.

## What to say

- What is failing and since when (link to the dashboard)
- How many payments are affected
- What has been tried, and the incident channel (`#inc-<date>-payments`)
