# {{title}}

Changes from other teams are welcome. This page says how to get one merged
quickly.

## Before you start

- Open an issue to discuss anything bigger than a fix, before writing the code
- Check that nobody is already working on it

## Running locally

```bash
git clone <repository>
make install
make test
```

## Sending a change

1. Create a branch from `main`.
2. Add tests for what you changed, and update this documentation.
3. Open a pull request describing the problem and the solution.
4. A maintainer reviews it within the agreed time.

## Releasing

Only maintainers release versions. A merged change goes out in the next release.
