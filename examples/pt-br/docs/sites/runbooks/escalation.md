# Escalonamento

Quando o runbook não resolve o problema, ou há clientes afetados em mais de um produto.

## Severidade

| Severidade | Exemplo                                             | Escalar depois de |
| ---------- | --------------------------------------------------- | ----------------- |
| Crítica    | Mais de 5% dos pagamentos falhando                  | 15 minutos        |
| Alta       | Pagamentos lentos (p99 acima de 3 s), mas passando  | 30 minutos        |
| Aviso      | Estornos atrasados, ainda sem impacto para clientes | Manhã seguinte    |

## Quem acionar

1. O segundo plantão de Pagamentos, pela ferramenta de plantão.
2. O suporte do provedor, para erros `provider_unavailable` (telefone no cofre, `payments/provider`).
3. O gerente de incidentes de plantão, em qualquer incidente crítico.

## O que dizer

- O que está falhando e desde quando (link para o painel)
- Quantos pagamentos foram afetados
- O que já foi tentado, e o canal do incidente (`#inc-<data>-payments`)
