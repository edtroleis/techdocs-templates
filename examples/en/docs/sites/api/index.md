# Payments API

The API that other services call to charge a customer's card and to refund a payment.

## Before you start

- Base URL: `https://payments.internal.example.com/v1`
- Format: JSON in and out, amounts in cents (`1000` = 10.00), dates in ISO 8601 (UTC)
- Current version: v1. Breaking changes only in v2, announced in the changelog three months before

## First call

1. Get a service token, as described in [Authentication](authentication.md).

2. Check the access with the health endpoint:

   ```bash
   curl -H "Authorization: Bearer $TOKEN" https://payments.internal.example.com/v1/health
   ```

3. Create your first payment in the sandbox, following the [Payments API](../../reference/api-reference.md) reference.

## Limits

- 600 requests per minute per service; above it the API answers 429 with `Retry-After`
- Up to 100 payments per page when listing

## Who looks after it

The Payments team (`#payments-team`). Access requests go through the portal.
