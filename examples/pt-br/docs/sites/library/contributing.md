# Como contribuir

Mudanças de outros times são bem-vindas. A maioria vem de quem precisou de mais uma opção.

## Antes de começar

- Para qualquer coisa maior que uma correção, abra uma issue antes e marque `@payments-team`
- Veja as issues abertas: alguém pode já estar trabalhando nisso

## Rodar na sua máquina

```bash
git clone git@github.example.com:payments/payments-client.git
cd payments-client
make install
make test   # roda contra uma imitação da API de Pagamentos, sem rede
```

## Enviar uma mudança

1. Crie um branch a partir da `main`.
2. Acrescente testes e atualize esta documentação no mesmo pull request.
3. Descreva o problema e a solução; ligue a issue.
4. Um mantenedor revisa em até dois dias úteis.

## Publicar

O time de Pagamentos publica às terças. Uma mudança aceita sai na próxima versão.
