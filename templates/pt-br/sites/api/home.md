# {{site_name}}

O que esta API faz, em uma ou duas frases, e para quem ela é.

## Antes de começar

- URL base: `https://api.example.com/v1`
- Formato: JSON na entrada e na saída, datas em ISO 8601 (UTC)
- Versão atual: v1. Mudanças que quebram só numa versão nova, avisadas no
  histórico de mudanças

## Primeira chamada

1. Pegue as credenciais, como explica a página Autenticação.

2. Chame um endpoint só de leitura para conferir o acesso:

   ```bash
   curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/health
   ```

3. Procure os endpoints de que precisa na referência da API.

## Limites

- Requisições por minuto por cliente, e o que acontece acima disso (HTTP 429)
- Tamanho máximo de página e de requisição

## Quem cuida

Esta API é mantida por {{owner}}. Dúvidas e pedidos de acesso vão para o canal
do time.
