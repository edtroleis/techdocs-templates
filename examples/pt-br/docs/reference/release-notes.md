# Notas de versão

## 2.4.0 (2026-11-10)

### Novidades

- Estornos parciais: `paymentsctl refund --amount`

### Mudanças

- O `POST /v1/payments` responde 300 ms mais rápido (p99), depois da mudança de índice no banco

### Correções

- Um pagamento podia ficar em `pending` quando o webhook do provedor chegava duas vezes

### Como atualizar

Nada a fazer para quem usa a API.

## 2.3.0 (2026-10-02)

### Novidades

- O modo fila para quando o provedor cai (veja a [RFC 0007](../explanation/rfc.md))
