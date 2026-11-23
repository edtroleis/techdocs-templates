# {{title}}

How a client proves who it is, and what it is allowed to do.

## Getting credentials

1. Request a client for your service (where and how: form, ticket, portal).
2. Store the client secret in your secrets manager, never in the repository.

## Calling the API

Every request carries a token in the `Authorization` header:

```http
Authorization: Bearer <token>
```

The token expires after a set time. Ask for a new one before it expires, not
after a 401.

## Scopes

| Scope   | Allows                     |
| ------- | -------------------------- |
| `read`  | Reading the resources      |
| `write` | Creating and changing them |

## When it fails

- 401: missing, invalid or expired token
- 403: valid token without the scope for this operation
