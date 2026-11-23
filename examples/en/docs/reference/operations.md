# Operations and support

How the Payments Service is run day to day.

## On call and escalation

- PagerDuty schedule "Payments", one week each, handover on Mondays at 10:00
- Escalation: on-call engineer → team lead → head of engineering

## SLOs

| SLO                                      | Target | Window  |
| ---------------------------------------- | ------ | ------- |
| Payments created without error           | 99.9%  | 30 days |
| Time to answer `POST /v1/payments` (p99) | 800 ms | 30 days |

## Alerts

| Alert                    | Runbook                                                |
| ------------------------ | ------------------------------------------------------ |
| `PaymentsErrorRateHigh`  | [High payment error rate](../how-to-guides/runbook.md) |
| `PaymentsPendingTooLong` | [Troubleshooting](../how-to-guides/troubleshooting.md) |

## Dashboards and logs

- **Payments – overview:** traffic, errors and latency
- **Payments – provider:** answers and timeouts from the provider
- Logs: `service:payments`

## Deploy and rollback

Every merge to `main` goes to staging. Production needs one approval in the pipeline. Rollback:
`kubectl -n payments rollout undo deployment/payments`.

## Maintenance

- Rotate the provider API key every 90 days ([guide](../how-to-guides/guide.md))
- Database: minor versions are applied by the platform team on Sundays
