# {{site_name}}

What this API does, in one or two sentences, and who it is for.

## Before you start

- Base URL: `https://api.example.com/v1`
- Format: JSON in and out, dates in ISO 8601 (UTC)
- Current version: v1. Breaking changes only in a new version, announced in the
  changelog

## First call

1. Get credentials, as described in Authentication.

2. Call a read-only endpoint to check the access:

   ```bash
   curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/health
   ```

3. Look up the endpoints you need in the API reference.

## Limits

- Requests per minute per client, and what happens above it (HTTP 429)
- Maximum page size and request size

## Who looks after it

This API is maintained by {{owner}}. Questions and access requests go to the
team channel.
