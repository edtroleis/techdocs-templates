# API de Pagamentos

A API que os outros serviços chamam para cobrar o cartão de um cliente e para estornar um pagamento.

## Antes de começar

- URL base: `https://payments.internal.example.com/v1`
- Formato: JSON na entrada e na saída, valores em centavos (`1000` = 10,00), datas em ISO 8601 (UTC)
- Versão atual: v1. Mudanças que quebram só na v2, avisadas no histórico três meses antes

## Primeira chamada

1. Pegue um token de serviço, como explica [Autenticação](authentication.md).

2. Confira o acesso com o endpoint de saúde:

   ```bash
   curl -H "Authorization: Bearer $TOKEN" https://payments.internal.example.com/v1/health
   ```

3. Crie o seu primeiro pagamento no sandbox, seguindo a referência da [API de Pagamentos](../../reference/api-reference.md).

## Limites

- 600 requisições por minuto por serviço; acima disso a API responde 429 com `Retry-After`
- Até 100 pagamentos por página na listagem

## Quem cuida

O time de Pagamentos (`#payments-team`). Pedidos de acesso vão pelo portal.
