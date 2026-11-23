# payments-client

O cliente Python da API de Pagamentos: autenticação, novas tentativas e chaves de idempotência, para nenhum time
escrever isso de novo.

## Exemplo mínimo

```python
from payments_client import Payments

payments = Payments()  # lê as credenciais do serviço no cofre
payment = payments.create(order_id="ord_42", amount=1000, currency="BRL", card="tok_visa")
print(payment.status)
```

## Quando usar

- Qualquer serviço em Python que cobra ou estorna um cliente
- Não para a página de checkout: o navegador fala com o componente do próprio provedor

## Versões

O cliente segue o versionamento semântico. A versão 3 é a atual; a versão 2 recebe correções de segurança até
junho.

## Quem cuida

O time de Pagamentos (`#payments-team`).
