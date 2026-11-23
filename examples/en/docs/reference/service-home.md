# Payments Service

Charges customers' cards for orders, through an external card provider, and tells the other services when a
payment succeeds or fails.

## Who takes care of it

- **Team:** Payments
- **Channel:** `#payments-team`
- **On call:** PagerDuty schedule "Payments"

## Links

- [Repository](https://github.com/example/payments-service)
- [Dashboards](https://grafana.example.com/d/payments)
- [Catalog entry](https://backstage.example.com/catalog/default/component/payments-service)

## Dependencies

| Depends on    | For                                            |
|---------------|------------------------------------------------|
| Card provider | Charging and refunding cards                   |
| PostgreSQL    | Payments and refunds                           |
| Event bus     | Publishing `payment.paid` and `payment.failed` |

## How to start

- New to the service: [Your first payment](../tutorials/tutorial.md)
- Integrating with it: [Payments API](api-reference.md)
- On call: [Operations and support](operations.md)
