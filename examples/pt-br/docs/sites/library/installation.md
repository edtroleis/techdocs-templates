# Instalação

## Requisitos

- Python 3.10 ou mais novo
- O índice interno de pacotes configurado (ele vem pronto no template de serviço)

## Instalar

```bash
pip install "payments-client>=3,<4"
```

## Conferir

```bash
python -c "import payments_client; print(payments_client.__version__)"
```

## Configuração

| Configuração           | Padrão    | O que faz                                    |
| ---------------------- | --------- | -------------------------------------------- |
| `PAYMENTS_ENV`         | `sandbox` | `sandbox` ou `production`                    |
| `PAYMENTS_TIMEOUT`     | `10`      | Segundos antes de desistir de uma requisição |
| `PAYMENTS_MAX_RETRIES` | `5`       | Novas tentativas para 429 e 503, mesma chave |

## Atualizar da versão 2

A versão 3 trocou `charge()` por `create()` e devolve os valores em centavos. Troque as chamadas, rode os seus
testes e depois atualize a versão.
