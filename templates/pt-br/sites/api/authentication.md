# {{title}}

Como um cliente prova quem é, e o que ele pode fazer.

## Pegar as credenciais

1. Peça um cliente para o seu serviço (onde e como: formulário, chamado,
   portal).
2. Guarde o segredo do cliente no cofre de segredos, nunca no repositório.

## Chamar a API

Toda requisição leva um token no cabeçalho `Authorization`:

```http
Authorization: Bearer <token>
```

O token expira depois de um tempo. Peça um novo antes de expirar, não depois de
um 401.

## Escopos

| Escopo  | Permite                  |
| ------- | ------------------------ |
| `read`  | Ler os recursos          |
| `write` | Criar e alterar recursos |

## Quando falha

- 401: token ausente, inválido ou expirado
- 403: token válido, mas sem o escopo para esta operação
