# {{title}}

Quando o runbook não resolve o problema, ou o impacto é maior que um serviço.

## Severidade

| Severidade | Exemplo                                  | Escalar depois de |
| ---------- | ---------------------------------------- | ----------------- |
| Crítica    | Clientes sem uma função principal        | 15 minutos        |
| Alta       | Função degradada para parte dos clientes | 30 minutos        |
| Aviso      | Ainda sem impacto para clientes          | Manhã seguinte    |

## Quem acionar

1. O plantão deste serviço (ferramenta de plantão, escala).
2. O plantão da dependência que está falhando.
3. O gerente de incidentes, em incidentes críticos ou com mais de um time
   envolvido.

## O que dizer

- O que está falhando e desde quando
- O impacto para os clientes
- O que já foi tentado, e o canal do incidente
