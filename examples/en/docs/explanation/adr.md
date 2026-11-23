# ADR 0003: idempotency keys on payment creation

Status: Accepted

Date: 2026-03-14

## Context

Clients retry `POST /v1/payments` when the network fails. Without protection, a retry after a slow answer
created a second payment and charged the customer twice (see the [postmortem](postmortem.md)).

## Decision

`POST /v1/payments` requires an `Idempotency-Key` header. The service stores the key with the request body for
24 hours. The same key with the same body returns the first payment; with another body, it answers `422`.

## Consequences

- Retries are safe for clients.
- Every client had to change to send the header (done in Q2).
- The table of keys grows; a job deletes keys older than 24 hours.

## Alternatives considered

- **Deduplicate by order id:** does not allow two payments for one order (split payments).
- **Ask the provider to deduplicate:** the provider only offers it for 1 hour.
