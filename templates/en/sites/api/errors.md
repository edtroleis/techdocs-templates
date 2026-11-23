# {{title}}

Every error comes with an HTTP status and the same body, so a client can handle
them in one place.

## Error body

```json
{
  "code": "invalid_amount",
  "message": "The amount must be greater than zero",
  "request_id": "a1b2c3"
}
```

Send the `request_id` when asking for help: it finds the request in the logs.

## Codes

| Status | Code           | What to do                                    |
| ------ | -------------- | --------------------------------------------- |
| 400    | `invalid_*`    | Fix the request; retrying will not help       |
| 404    | `not_found`    | Check the identifier                          |
| 409    | `conflict`     | Read the resource again and retry             |
| 429    | `rate_limited` | Wait for the time in `Retry-After`            |
| 5xx    | `internal`     | Retry with backoff; open a ticket if it lasts |

## Retries

Only retry what is safe to repeat: reads, and writes sent with an
`Idempotency-Key`.
