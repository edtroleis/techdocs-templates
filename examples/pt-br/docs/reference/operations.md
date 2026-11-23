# Operação e suporte

Como o Serviço de Pagamentos é operado no dia a dia.

## Plantão e escalonamento

- Escala "Payments" no PagerDuty, uma semana para cada pessoa, troca às segundas às 10:00
- Escalonamento: pessoa de plantão → líder do time → head de engenharia

## SLOs

| SLO                                            | Meta   | Janela  |
| ---------------------------------------------- | ------ | ------- |
| Pagamentos criados sem erro                    | 99,9%  | 30 dias |
| Tempo de resposta do `POST /v1/payments` (p99) | 800 ms | 30 dias |

## Alertas

| Alerta                   | Runbook                                                     |
| ------------------------ | ----------------------------------------------------------- |
| `PaymentsErrorRateHigh`  | [Muitos pagamentos com erro](../how-to-guides/runbook.md)   |
| `PaymentsPendingTooLong` | [Solução de problemas](../how-to-guides/troubleshooting.md) |

## Dashboards e logs

- **Payments – overview:** tráfego, erros e latência
- **Payments – provider:** respostas e timeouts do provedor
- Logs: `service:payments`

## Deploy e rollback

Todo merge na `main` vai para staging. Produção precisa de uma aprovação na pipeline. Rollback:
`kubectl -n payments rollout undo deployment/payments`.

## Manutenção

- Trocar a chave da API do provedor a cada 90 dias ([guia](../how-to-guides/guide.md))
- Banco de dados: versões menores aplicadas pelo time de plataforma aos domingos
