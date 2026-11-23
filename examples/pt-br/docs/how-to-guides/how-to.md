# Estornar um pagamento

Como estornar um pagamento, inteiro ou em parte, pela linha de comando.

## Passos

1. Ache o pagamento pelo pedido:

    ```bash
    paymentsctl find --order pedido-1
    ```

2. Estorne. Sem `--amount`, estorna tudo:

    ```bash
    paymentsctl refund pay_123 --amount 500 --reason "produto avariado"
    ```

3. Passe para o atendimento o id do estorno (começa com `ref_`).

## Como conferir que deu certo

`paymentsctl show pay_123` mostra o estorno com status `succeeded`. O dinheiro chega ao cliente em 5 a 10 dias
úteis.
