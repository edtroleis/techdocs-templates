# Solução de problemas

Os problemas mais comuns com o Serviço de Pagamentos, e como resolver.

## O pagamento fica em `pending`

- **Causa provável:** o webhook do provedor não chegou.
- **Como confirmar:** `paymentsctl show <id>` não tem `provider_event`.
- **Como resolver:** `paymentsctl sync <id>` pergunta ao provedor o estado atual.

## "Idempotency key reused with a different body"

- **Causa provável:** o cliente mandou a mesma `Idempotency-Key` para outro pagamento.
- **Como confirmar:** a resposta 422 mostra os dois corpos.
- **Como resolver:** o cliente precisa criar uma chave nova para cada pagamento novo. Veja o
  [ADR 0003](../explanation/adr.md).

## Ambiente local: o `provider-sim` não sobe

- **Causa provável:** a porta 9090 está em uso.
- **Como confirmar:** `docker compose logs provider-sim` diz "address already in use".
- **Como resolver:** pare o que está usando a porta, ou defina `PROVIDER_SIM_PORT` no `.env`.
