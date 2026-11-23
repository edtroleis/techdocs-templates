# Payments API

The HTTP API of the Payments Service, for services that need to charge a customer.

## Overview

- Base URL: `https://payments.internal.example.com`
- JSON in and out; amounts in cents (`1000` = 10.00)

## Authentication

A service token in the `Authorization: Bearer <token>` header. Ask for one in `#payments-team`.

## Endpoints

### Create a payment

`POST /v1/payments`

| Field      | Type    | Required | Description                  |
| ---------- | ------- | -------- | ---------------------------- |
| `orderId`  | string  | yes      | The order being paid         |
| `amount`   | integer | yes      | Amount in cents              |
| `currency` | string  | yes      | ISO 4217 code, such as `USD` |
| `card`     | string  | yes      | Card token from the checkout |

The `Idempotency-Key` header is required: the same key with the same body returns the same payment.

```json
{ "id": "pay_123", "status": "pending", "amount": 1000, "currency": "USD" }
```

Errors: `400` invalid field, `402` card declined, `422` idempotency key reused with another body.

### Read a payment

`GET /v1/payments/{id}`. Returns the payment, with `status` one of `pending`, `paid`, `failed`, `refunded`.

## Limits

100 requests per second per service. Above that: `429`, with `Retry-After`.

## Versions

`v1` is the current version. Breaking changes get a new version and six months of overlap.
