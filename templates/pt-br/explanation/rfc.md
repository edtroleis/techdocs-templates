---
template:
  version: 1
  name: RFC / design doc
  description: Uma proposta antes da decisão (o ADR registra o resultado)
  category: explanation
  example: explanation/rfc.md
  folder: rfcs
  numbered: true
  fields:
    status:
      prompt: Status
      default: "Rascunho"
---

# {{title}}

Status: {{status}}

Autor: {{owner}} · Data: {{date}}

## Resumo

A proposta em duas ou três frases.

## Problema

O que está errado hoje e quem isso afeta. Números ajudam: erros, tempo, custo.

## Proposta

Como funcionaria. Um diagrama, os fluxos principais e o que muda para cada time.

## Alternativas

| Opção          | Prós | Contras |
| -------------- | ---- | ------- |
| A proposta     |      |         |
| Não fazer nada |      |         |

## Riscos e perguntas em aberto

- O que pode dar errado, e como perceberíamos
- O que ainda precisa de resposta, e quem pode responder

## Implantação

Os passos para chegar lá, e como voltar atrás.
