# Seu primeiro pagamento

Neste tutorial você cobra um cartão de teste pelo Serviço de Pagamentos rodando na sua máquina e vê o
pagamento passar de `pending` para `paid`. Leva uns 20 minutos.

## O que você vai construir

Um Serviço de Pagamentos local, uma cobrança de teste de 10,00 BRL e o evento que avisa o serviço de pedidos
que a cobrança deu certo.

## Antes de começar

- Docker e Docker Compose
- `curl` e `jq`
- Acesso ao repositório `payments-service`

## Passos

1. Clone o repositório e suba o serviço com o banco de dados e o simulador do provedor:

   ```bash
   git clone https://github.com/example/payments-service.git
   cd payments-service
   docker compose up -d
   ```

   Você deve ver três containers rodando: `payments`, `postgres` e `provider-sim`.

2. Crie um pagamento:

   ```bash
   curl -s -X POST localhost:8080/v1/payments \
      -H 'Idempotency-Key: tutorial-1' \
      -d '{"orderId": "pedido-1", "amount": 1000, "currency": "BRL", "card": "4242424242424242"}' | jq
   ```

   A resposta tem `"status": "pending"` e um `id` que começa com `pay_`.

3. Espere dois segundos e leia de novo:

   ```bash
   curl -s localhost:8080/v1/payments/<id> | jq .status
   ```

   Agora diz `"paid"`: o simulador aprovou o cartão.

4. Veja o evento que o serviço publicou:

   ```bash
   docker compose logs payments | grep payment.paid
   ```

   O serviço de pedidos escuta esse evento para enviar o pedido.

## O que você aprendeu

Você criou um pagamento, viu o estado mudar sem esperar a resposta e achou o evento que os outros serviços usam.

## Próximos passos

- [Estornar um pagamento](../how-to-guides/how-to.md)
- [Como o serviço é construído](../explanation/architecture.md)
