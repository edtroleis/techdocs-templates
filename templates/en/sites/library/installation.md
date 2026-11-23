# {{title}}

## Requirements

- Language and minimum version
- Access to the internal package registry, if the library is published there

## Install

```bash
pip install example
```

## Check

```bash
python -c "import example; print(example.__version__)"
```

## Configuration

| Setting           | Default | What it does                 |
| ----------------- | ------- | ---------------------------- |
| `EXAMPLE_TIMEOUT` | `10`    | Seconds before giving up     |
| `EXAMPLE_DEBUG`   | `false` | Logs every request and reply |

## Updating

Read the changelog before a new major version, then update the version in your
dependencies file.
