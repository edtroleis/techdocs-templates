# Autenticação

Cada serviço que chama a API de Pagamentos tem o seu cliente, para sabermos quem cobrou o quê.

## Pegar as credenciais

1. No portal, abra **Acessos → API de Pagamentos** e escolha o seu serviço no catálogo.
2. O segredo do cliente vai direto para o cofre, em `payments/<seu-serviço>`. Ninguém vê o segredo num chat.

## Chamar a API

Troque o segredo por um token, válido por uma hora:

```bash
curl -X POST https://auth.internal.example.com/token \
  -d grant_type=client_credentials -d scope="payments:write"
```

Mande o token em toda requisição:

```http
Authorization: Bearer eyJhbGciOi...
```

Renove o token cinco minutos antes de expirar; as bibliotecas de cliente fazem isso por você.

## Escopos

| Escopo           | Permite                                         |
| ---------------- | ----------------------------------------------- |
| `payments:read`  | Ler pagamentos e estornos                       |
| `payments:write` | Criar pagamentos                                |
| `refunds:write`  | Estornar, só para as ferramentas de atendimento |

## Quando falha

- 401 `invalid_token`: o token expirou ou veio do sandbox
- 403 `missing_scope`: peça o escopo no portal; leva um dia útil
