# Release notes

## 2.4.0 (2026-11-10)

### Added

- Partial refunds: `paymentsctl refund --amount`

### Changed

- `POST /v1/payments` answers in 300 ms less (p99), after the database index change

### Fixed

- A payment could stay `pending` when the provider webhook arrived twice

### Upgrade notes

Nothing to do for clients of the API.

## 2.3.0 (2026-10-02)

### Added

- The queue mode for provider outages (see [RFC 0007](../explanation/rfc.md))
