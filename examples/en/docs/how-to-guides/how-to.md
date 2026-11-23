# Refund a payment

How to refund a payment, fully or in part, from the command line.

## Steps

1. Find the payment by the order:

    ```bash
    paymentsctl find --order order-1
    ```

2. Refund it. Leave out `--amount` to refund everything:

    ```bash
    paymentsctl refund pay_123 --amount 500 --reason "damaged item"
    ```

3. Tell the customer support agent the refund id (it starts with `ref_`).

## Check that it worked

`paymentsctl show pay_123` lists the refund with status `succeeded`. The money reaches the customer in 5 to
10 business days.
