# ADR 0003: chaves de idempotência na criação de pagamentos

Status: Aceito

Data: 2026-03-14

## Contexto

Os clientes repetem o `POST /v1/payments` quando a rede falha. Sem proteção, uma repetição depois de uma resposta
lenta criava um segundo pagamento e cobrava o cliente duas vezes (veja o [postmortem](postmortem.md)).

## Decisão

O `POST /v1/payments` exige o cabeçalho `Idempotency-Key`. O serviço guarda a chave com o corpo da requisição por
24 horas. A mesma chave com o mesmo corpo devolve o primeiro pagamento; com outro corpo, responde `422`.

## Consequências

- Repetir é seguro para os clientes.
- Todos os clientes precisaram mudar para mandar o cabeçalho (feito no 2º trimestre).
- A tabela de chaves cresce; um job apaga as chaves com mais de 24 horas.

## Alternativas consideradas

- **Evitar repetição pelo id do pedido:** não permite dois pagamentos para um pedido (pagamento dividido).
- **Pedir ao provedor para evitar repetições:** o provedor só oferece isso por 1 hora.
