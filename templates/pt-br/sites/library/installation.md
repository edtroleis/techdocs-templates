# {{title}}

## Requisitos

- Linguagem e versão mínima
- Acesso ao repositório interno de pacotes, se a biblioteca estiver publicada lá

## Instalar

```bash
pip install example
```

## Conferir

```bash
python -c "import example; print(example.__version__)"
```

## Configuração

| Configuração      | Padrão  | O que faz                           |
| ----------------- | ------- | ----------------------------------- |
| `EXAMPLE_TIMEOUT` | `10`    | Segundos antes de desistir          |
| `EXAMPLE_DEBUG`   | `false` | Registra cada requisição e resposta |

## Atualizar

Leia o histórico de mudanças antes de uma versão maior nova e depois troque a
versão no arquivo de dependências.
