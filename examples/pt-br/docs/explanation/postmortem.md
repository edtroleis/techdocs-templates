# Postmortem: cobranças em dobro em 2026-03-02

Uma revisão sem culpados. O objetivo é aprender, não achar culpados.

## Resumo

Por 40 minutos, 312 clientes foram cobrados duas vezes. Todos foram reembolsados no mesmo dia.

## Impacto

- 312 cobranças em dobro, 18.400 BRL no total, estornadas até as 18:00
- 47 chamados no atendimento

## Linha do tempo

| Hora  | O que aconteceu                                                |
|-------|----------------------------------------------------------------|
| 14:05 | O provedor passa a responder em 20 s em vez de 1 s             |
| 14:06 | O checkout desiste em 10 s e repete o pagamento                |
| 14:20 | O atendimento avisa de clientes cobrados duas vezes            |
| 14:45 | Repetições do checkout desligadas; as cobranças em dobro param |
| 18:00 | Último estorno feito                                           |

## Causa raiz

O checkout repetia os pagamentos depois de um timeout, e o Serviço de Pagamentos não tinha como diferenciar uma
repetição de um pagamento novo.

## O que funcionou e o que não

- Funcionou: os estornos tinham script e terminaram no mesmo dia.
- Não funcionou: não havia alerta de cobrança em dobro; o atendimento soube primeiro.

## Ações

| Ação                                                     | Dono       | Prazo      |
|----------------------------------------------------------|------------|------------|
| Chaves de idempotência ([ADR 0003](adr.md))              | Pagamentos | 2026-04-15 |
| Alerta para dois pagamentos do mesmo pedido em 5 minutos | Pagamentos | 2026-03-20 |
