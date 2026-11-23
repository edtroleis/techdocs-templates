# Runbooks de Pagamentos

O que fazer quando um alerta de Pagamentos dispara. Cada alerta aponta para um runbook; comece por aqui durante
um incidente.

## Índice de alertas

| Alerta                  | Severidade | Runbook                                                        |
| ----------------------- | ---------- | -------------------------------------------------------------- |
| `PaymentsErrorRateHigh` | Crítica    | [Muitos pagamentos com erro](../../how-to-guides/runbook.md)   |
| `ProviderLatencyHigh`   | Alta       | [Solução de problemas](../../how-to-guides/troubleshooting.md) |
| `RefundQueueGrowing`    | Aviso      | (a escrever)                                                   |

## Durante um incidente

1. Reconheça o chamado, para o segundo plantão não começar o mesmo trabalho.
2. Abra o runbook do alerta e siga os passos.
3. Se o runbook não resolver em 15 minutos, [escale](escalation.md).
4. Em até cinco dias úteis, escreva um [pós-mortem](../../explanation/postmortem.md).

## Manter os runbooks úteis

- Um runbook que não funcionou é corrigido nas ações do pós-mortem
- Um alerta sem runbook por duas semanas é removido

## Quem cuida

A escala de plantão de Pagamentos.
