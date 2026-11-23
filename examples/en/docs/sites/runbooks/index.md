# Payments runbooks

What to do when a Payments alert fires. Each alert points to one runbook; start here during an incident.

## Alert index

| Alert                   | Severity | Runbook                                                   |
| ----------------------- | -------- | --------------------------------------------------------- |
| `PaymentsErrorRateHigh` | Critical | [High payment error rate](../../how-to-guides/runbook.md) |
| `ProviderLatencyHigh`   | High     | [Troubleshooting](../../how-to-guides/troubleshooting.md) |
| `RefundQueueGrowing`    | Warning  | (to write)                                                |

## During an incident

1. Acknowledge the page, so the second on-call does not start the same work.
2. Open the runbook for the alert and follow it.
3. If the runbook does not solve it in 15 minutes, [escalate](escalation.md).
4. Within five business days, write a [postmortem](../../explanation/postmortem.md).

## Keeping the runbooks useful

- A runbook that did not work is fixed in the postmortem actions
- An alert without a runbook for two weeks is removed

## Who looks after it

The Payments on-call rotation.
