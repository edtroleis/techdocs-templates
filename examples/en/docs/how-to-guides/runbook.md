# Runbook: high payment error rate

Alert: `PaymentsErrorRateHigh` (more than 5% of payments failing for 5 minutes)

Last reviewed on 2026-11-01 by the Payments team.

## Impact

Customers cannot pay. Orders stay in "waiting for payment" and are cancelled after 30 minutes.

## Diagnosis

1. Open the **Payments – overview** dashboard and look at errors by type.
2. If most errors are `provider_timeout`, check the provider status page.
3. If most errors are `internal`, look at the deploys of the last hour.
4. Search the logs:

```bash
logs search 'service:payments level:error' --since 15m | head
```

## Actions

1. **Provider down:** turn on the queue mode, so payments wait instead of failing:

    ```bash
    paymentsctl flags set queue-mode on
    ```

2. **Bad deploy:** roll back to the previous version:

    ```bash
    kubectl -n payments rollout undo deployment/payments
    ```

3. Confirm the error rate drops below 1% in the dashboard.

## How to escalate

- After 15 minutes without a fix: call the Payments team lead.
- Provider down for more than 30 minutes: open a ticket with the provider (priority 1) and tell `#incidents`.

## After it is solved

- Turn off the queue mode, if you turned it on
- Write down what happened in `#incidents`
- Open a postmortem if customers were affected
