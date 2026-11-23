# Runbook: muitos pagamentos com erro

Alerta: `PaymentsErrorRateHigh` (mais de 5% dos pagamentos falhando por 5 minutos)

Revisado em 2026-11-01 pelo time de Pagamentos.

## Impacto

Os clientes não conseguem pagar. Os pedidos ficam em "aguardando pagamento" e são cancelados depois de 30
minutos.

## Diagnóstico

1. Abra o dashboard **Payments – overview** e veja os erros por tipo.
2. Se a maioria é `provider_timeout`, confira a página de status do provedor.
3. Se a maioria é `internal`, veja os deploys da última hora.
4. Busque nos logs:

```bash
logs search 'service:payments level:error' --since 15m | head
```

## Ações

1. **Provedor fora do ar:** ligue o modo fila, para os pagamentos esperarem em vez de falhar:

    ```bash
    paymentsctl flags set queue-mode on
    ```

2. **Deploy com problema:** volte para a versão anterior:

    ```bash
    kubectl -n payments rollout undo deployment/payments
    ```

3. Confirme no dashboard que a taxa de erro caiu para menos de 1%.

## Como escalar

- Depois de 15 minutos sem resolver: ligue para o líder do time de Pagamentos.
- Provedor fora do ar por mais de 30 minutos: abra um chamado com o provedor (prioridade 1) e avise em
  `#incidents`.

## Depois de resolver

- Desligue o modo fila, se ligou
- Registre o que aconteceu em `#incidents`
- Abra um postmortem se algum cliente foi afetado
