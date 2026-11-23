# Contributing

Changes from other teams are welcome. Most come from someone who needed one more option.

## Before you start

- For anything bigger than a fix, open an issue first and tag `@payments-team`
- Look at the open issues: someone may already be on it

## Running locally

```bash
git clone git@github.example.com:payments/payments-client.git
cd payments-client
make install
make test   # runs against a fake of the Payments API, no network
```

## Sending a change

1. Create a branch from `main`.
2. Add tests and update these docs in the same pull request.
3. Describe the problem and the solution; link the issue.
4. A maintainer reviews it within two business days.

## Releasing

The Payments team releases on Tuesdays. A merged change goes out in the next release.
