# Trocar a chave da API do provedor

Este guia mostra como trocar a chave que o Serviço de Pagamentos usa para falar com o provedor de cartões, sem
deixar o serviço fora do ar. Faça a cada 90 dias, ou na hora se a chave vazar.

## Objetivo

O serviço usa uma chave nova, e a antiga é revogada.

## Antes de começar

- Acesso de administrador ao painel do provedor
- Permissão de escrita no segredo `payments/provider` do cofre
- Um momento tranquilo: evite o primeiro e o último dia do mês

## Passos

1. No painel do provedor, abra **API keys** e crie uma chave nova chamada `payments-<data>`.

2. Guarde a chave no cofre como a **secundária**:

   ```bash
   vault kv patch secret/payments/provider secondary_key=<chave nova>
   ```

3. Reinicie o serviço. Ele tenta a chave primária e, se falhar, a secundária:

   ```bash
   kubectl -n payments rollout restart deployment/payments
   ```

4. Troque as chaves no cofre: a nova vira `primary_key`, e a antiga sai.

5. Reinicie o serviço de novo e revogue a chave antiga no painel do provedor.

## Como conferir que deu certo

No dashboard **Payments – provider**, os erros de autenticação continuam em zero e a taxa de aprovação não cai.

## Problemas comuns

- **401 do provedor depois do passo 5:** a chave antiga foi revogada antes de o reinício terminar. Volte com ela
  como `secondary_key` e reinicie.
