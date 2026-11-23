# {{title}}

When the runbook does not solve the problem, or the impact is bigger than one
service.

## Severity

| Severity | Example                                  | Escalate after |
| -------- | ---------------------------------------- | -------------- |
| Critical | Customers cannot use a main feature      | 15 minutes     |
| High     | A feature is degraded for some customers | 30 minutes     |
| Warning  | No customer impact yet                   | Next morning   |

## Who to call

1. The on-call of this service (on-call tool, schedule).
2. The on-call of the dependency that is failing.
3. The incident manager, for critical incidents or more than one team involved.

## What to say

- What is failing and since when
- The impact on customers
- What has been tried, and the incident channel
