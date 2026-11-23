# payments-client

The Python client for the Payments API: authentication, retries and idempotency keys, so no team writes them
again.

## Minimal example

```python
from payments_client import Payments

payments = Payments()  # reads the service credentials from the vault
payment = payments.create(order_id="ord_42", amount=1000, currency="USD", card="tok_visa")
print(payment.status)
```

## When to use it

- Any Python service that charges or refunds a customer
- Not for the checkout page: the browser talks to the provider's own widget

## Versions

The client follows semantic versioning. Version 3 is the current one; version 2 gets security fixes until
June.

## Who looks after it

The Payments team (`#payments-team`).
