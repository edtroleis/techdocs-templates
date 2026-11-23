# {{title}}

Todo erro vem com um status HTTP e o mesmo corpo, para o cliente tratar todos
num lugar só.

## Corpo do erro

```json
{
  "code": "invalid_amount",
  "message": "O valor precisa ser maior que zero",
  "request_id": "a1b2c3"
}
```

Mande o `request_id` ao pedir ajuda: ele acha a requisição nos logs.

## Códigos

| Status | Código         | O que fazer                                     |
| ------ | -------------- | ----------------------------------------------- |
| 400    | `invalid_*`    | Corrigir a requisição; repetir não adianta      |
| 404    | `not_found`    | Conferir o identificador                        |
| 409    | `conflict`     | Ler o recurso de novo e repetir                 |
| 429    | `rate_limited` | Esperar o tempo de `Retry-After`                |
| 5xx    | `internal`     | Repetir com espera; se continuar, abrir chamado |

## Repetir

Só repita o que é seguro repetir: leituras, e escritas enviadas com
`Idempotency-Key`.
