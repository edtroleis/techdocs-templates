# Serviço de Pagamentos

Cobra os cartões dos clientes pelos pedidos, por meio de um provedor de cartões externo, e avisa os outros
serviços quando um pagamento dá certo ou falha.

## Quem cuida

- **Time:** Pagamentos
- **Canal:** `#payments-team`
- **Plantão:** escala "Payments" no PagerDuty

## Links

- [Repositório](https://github.com/example/payments-service)
- [Dashboards](https://grafana.example.com/d/payments)
- [Entrada no catálogo](https://backstage.example.com/catalog/default/component/payments-service)

## Dependências

| Depende de            | Para                                       |
|-----------------------|--------------------------------------------|
| Provedor de cartões   | Cobrar e estornar cartões                  |
| PostgreSQL            | Pagamentos e estornos                      |
| Barramento de eventos | Publicar `payment.paid` e `payment.failed` |

## Como começar

- Novo no serviço: [Seu primeiro pagamento](../tutorials/tutorial.md)
- Integrando com ele: [API de Pagamentos](api-reference.md)
- De plantão: [Operação e suporte](operations.md)
