# API de Pagamentos

A API HTTP do Serviço de Pagamentos, para os serviços que precisam cobrar um cliente.

## Visão geral

- URL base: `https://payments.internal.example.com`
- JSON na entrada e na saída; valores em centavos (`1000` = 10,00)

## Autenticação

Um token de serviço no cabeçalho `Authorization: Bearer <token>`. Peça um em `#payments-team`.

## Endpoints

### Criar um pagamento

`POST /v1/payments`

| Campo      | Tipo    | Obrigatório | Descrição                         |
|------------|---------|-------------|-----------------------------------|
| `orderId`  | string  | sim         | O pedido que está sendo pago      |
| `amount`   | integer | sim         | Valor em centavos                 |
| `currency` | string  | sim         | Código ISO 4217, como `BRL`       |
| `card`     | string  | sim         | Token do cartão vindo do checkout |

O cabeçalho `Idempotency-Key` é obrigatório: a mesma chave com o mesmo corpo devolve o mesmo pagamento.

```json
{ "id": "pay_123", "status": "pending", "amount": 1000, "currency": "BRL" }
```

Erros: `400` campo inválido, `402` cartão recusado, `422` chave de idempotência reaproveitada com outro corpo.

### Ler um pagamento

`GET /v1/payments/{id}`. Devolve o pagamento, com `status` igual a `pending`, `paid`, `failed` ou `refunded`.

## Limites

100 requisições por segundo por serviço. Acima disso: `429`, com `Retry-After`.

## Versões

`v1` é a versão atual. Mudanças incompatíveis ganham uma versão nova e seis meses de convivência.
