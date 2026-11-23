# Your first payment

In this tutorial you charge a test card through the Payments Service running on your machine, and see the
payment go from `pending` to `paid`. It takes about 20 minutes.

## What you will build

A local Payments Service, a test charge of 10.00 USD, and the event that tells the order service the charge
worked.

## Before you start

- Docker and Docker Compose
- `curl` and `jq`
- Access to the `payments-service` repository

## Steps

1. Clone the repository and start the service with its database and the provider simulator:

   ```bash
   git clone https://github.com/example/payments-service.git
   cd payments-service
   docker compose up -d
   ```

   You should see three containers running: `payments`, `postgres` and `provider-sim`.

2. Create a payment:

   ```bash
   curl -s -X POST localhost:8080/v1/payments \
      -H 'Idempotency-Key: tutorial-1' \
      -d '{"orderId": "order-1", "amount": 1000, "currency": "USD", "card": "4242424242424242"}' | jq
   ```

   The answer has `"status": "pending"` and an `id` that starts with `pay_`.

3. Wait two seconds and read it again:

   ```bash
   curl -s localhost:8080/v1/payments/<id> | jq .status
   ```

   It now says `"paid"`: the simulator approved the card.

4. Look at the event the service published:

   ```bash
   docker compose logs payments | grep payment.paid
   ```

   The order service listens to this event to ship the order.

## What you learned

You created a payment, saw it change state asynchronously and found the event other services use.

## Next steps

- [Refund a payment](../how-to-guides/how-to.md)
- [How the service is built](../explanation/architecture.md)
