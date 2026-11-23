# Errors

Every error has an HTTP status and the same body, so a client handles them in one place.

## Error body

```json
{
  "code": "card_declined",
  "message": "The card was declined by the issuer",
  "request_id": "req_8f2a91"
}
```

Send the `request_id` in `#payments-team` when asking for help: it finds the request in the logs.

## Codes

| Status | Code                   | What to do                                      |
| ------ | ---------------------- | ----------------------------------------------- |
| 400    | `invalid_amount`       | The amount must be a positive integer, in cents |
| 402    | `card_declined`        | Show the customer a message; do not retry       |
| 404    | `payment_not_found`    | Check the payment id and the environment        |
| 409    | `idempotency_reused`   | Same key with a different body: use a new key   |
| 429    | `rate_limited`         | Wait for the seconds in `Retry-After`           |
| 503    | `provider_unavailable` | Retry with backoff, up to 5 times, same key     |

## Retries

Retry only with the same `Idempotency-Key`: the customer is never charged twice.
