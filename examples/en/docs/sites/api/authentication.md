# Authentication

Every service that calls the Payments API has its own client, so we know who charged what.

## Getting credentials

1. In the portal, open **Access → Payments API** and choose your service from the catalog.
2. The client secret goes straight to the vault, under `payments/<your-service>`. Nobody sees it in a chat.

## Calling the API

Exchange the secret for a token, valid for one hour:

```bash
curl -X POST https://auth.internal.example.com/token \
  -d grant_type=client_credentials -d scope="payments:write"
```

Send it in every request:

```http
Authorization: Bearer eyJhbGciOi...
```

Renew the token five minutes before it expires; the client libraries do this for you.

## Scopes

| Scope            | Allows                                |
| ---------------- | ------------------------------------- |
| `payments:read`  | Reading payments and refunds          |
| `payments:write` | Creating payments                     |
| `refunds:write`  | Refunding, only for the support tools |

## When it fails

- 401 `invalid_token`: the token expired or came from the sandbox
- 403 `missing_scope`: ask for the scope in the portal; it takes one business day
