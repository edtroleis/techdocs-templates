# Erros

Todo erro tem um status HTTP e o mesmo corpo, para o cliente tratar todos num lugar só.

## Corpo do erro

```json
{
  "code": "card_declined",
  "message": "O cartão foi recusado pelo emissor",
  "request_id": "req_8f2a91"
}
```

Mande o `request_id` no `#payments-team` ao pedir ajuda: ele acha a requisição nos logs.

## Códigos

| Status | Código                 | O que fazer                                           |
| ------ | ---------------------- | ----------------------------------------------------- |
| 400    | `invalid_amount`       | O valor precisa ser um inteiro positivo, em centavos  |
| 402    | `card_declined`        | Mostre uma mensagem ao cliente; não repita            |
| 404    | `payment_not_found`    | Confira o id do pagamento e o ambiente                |
| 409    | `idempotency_reused`   | Mesma chave com outro corpo: use uma chave nova       |
| 429    | `rate_limited`         | Espere os segundos de `Retry-After`                   |
| 503    | `provider_unavailable` | Repita com espera crescente, até 5 vezes, mesma chave |

## Repetir

Repita só com a mesma `Idempotency-Key`: o cliente nunca é cobrado duas vezes.
