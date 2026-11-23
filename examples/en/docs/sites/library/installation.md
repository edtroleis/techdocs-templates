# Installation

## Requirements

- Python 3.10 or newer
- The internal package index configured (it comes ready in the service template)

## Install

```bash
pip install "payments-client>=3,<4"
```

## Check

```bash
python -c "import payments_client; print(payments_client.__version__)"
```

## Configuration

| Setting                | Default   | What it does                            |
| ---------------------- | --------- | --------------------------------------- |
| `PAYMENTS_ENV`         | `sandbox` | `sandbox` or `production`               |
| `PAYMENTS_TIMEOUT`     | `10`      | Seconds before giving up on one request |
| `PAYMENTS_MAX_RETRIES` | `5`       | Retries for 429 and 503, same key       |

## Updating from version 2

Version 3 renamed `charge()` to `create()` and returns amounts in cents. Change the calls, run your tests,
then update the version.
