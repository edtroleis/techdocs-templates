# {{site_name}}

O que fazer quando um alerta dispara. Cada alerta aponta para um runbook; comece
por aqui durante um incidente.

## Índice de alertas

| Alerta             | Severidade | Runbook            |
| ------------------ | ---------- | ------------------ |
| Taxa de erros alta | Crítica    | Runbook de exemplo |
| Fila crescendo     | Aviso      | (a escrever)       |

## Durante um incidente

1. Reconheça o alerta, para ninguém começar o mesmo trabalho.
2. Abra o runbook do alerta e siga os passos.
3. Se o runbook não resolver, escale (veja Escalonamento).
4. Depois do incidente, escreva um pós-mortem.

## Manter os runbooks úteis

- Um runbook que não funcionou é corrigido logo depois do incidente
- Um alerta sem runbook ganha um ou é removido

## Quem cuida

Estes runbooks são mantidos por {{owner}}.
