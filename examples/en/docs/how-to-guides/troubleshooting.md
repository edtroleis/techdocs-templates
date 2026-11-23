# Troubleshooting

The problems people hit most often with the Payments Service, and how to solve them.

## The payment stays in `pending`

- **Probable cause:** the provider webhook did not arrive.
- **How to confirm:** `paymentsctl show <id>` has no `provider_event`.
- **How to fix:** `paymentsctl sync <id>` asks the provider for the current state.

## "Idempotency key reused with a different body"

- **Probable cause:** the client sent the same `Idempotency-Key` for a different payment.
- **How to confirm:** the 422 answer lists both bodies.
- **How to fix:** the client must create a new key for each new payment. See
  [ADR 0003](../explanation/adr.md).

## Local environment: `provider-sim` does not start

- **Probable cause:** port 9090 is in use.
- **How to confirm:** `docker compose logs provider-sim` says "address already in use".
- **How to fix:** stop whatever uses the port, or set `PROVIDER_SIM_PORT` in `.env`.
