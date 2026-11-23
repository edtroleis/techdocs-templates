# Rotate the provider API key

This guide shows how to replace the API key the Payments Service uses to talk to the card provider, without
downtime. Do it every 90 days, or right away if the key leaks.

## Goal

The service uses a new key, and the old key is revoked.

## Before you start

- Admin access to the provider dashboard
- Write access to the `payments/provider` secret in the vault
- A quiet moment: avoid the first and last day of the month

## Steps

1. In the provider dashboard, open **API keys** and create a new key named `payments-<date>`.

2. Save it in the vault as the **secondary** key:

   ```bash
   vault kv patch secret/payments/provider secondary_key=<new key>
   ```

3. Restart the service. It tries the primary key and falls back to the secondary one:

   ```bash
   kubectl -n payments rollout restart deployment/payments
   ```

4. Swap the keys in the vault: the new key becomes `primary_key`, and the old one is removed.

5. Restart the service again and revoke the old key in the provider dashboard.

## Check that it worked

In the **Payments – provider** dashboard, authentication errors stay at zero and the approval rate does not
drop.

## Common problems

- **401 from the provider after step 5:** the old key was revoked before the restart finished. Put it back as
  `secondary_key` and restart.
