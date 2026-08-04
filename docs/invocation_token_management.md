# Invocation Token Management

Function invocation tokens are separate from JWT login tokens.

JWTs authenticate platform users who manage functions, versions, builds, and
token settings. Invocation tokens authenticate callers who are allowed to invoke
a specific token-protected function.

## API Endpoints

All token-management endpoints require an owner/admin JWT:

```text
Authorization: Bearer <jwt-access-token>
```

Available endpoints:

```text
GET    /api/functions/{function_id}/tokens/
POST   /api/functions/{function_id}/tokens/
GET    /api/functions/{function_id}/tokens/{token_id}/
PATCH  /api/functions/{function_id}/tokens/{token_id}/
DELETE /api/functions/{function_id}/tokens/{token_id}/
POST   /api/functions/{function_id}/tokens/{token_id}/revoke/
POST   /api/functions/{function_id}/tokens/{token_id}/rotate/
```

`DELETE` is a soft revoke. The token row remains for audit/history, but the
secret can no longer invoke the function.

## Create Token

Request:

```json
{
  "name": "mobile-app",
  "expires_at": "2026-08-30T12:00:00Z"
}
```

Response:

```json
{
  "token": {
    "id": 1,
    "name": "mobile-app",
    "prefix": "fn_abcd1234",
    "is_active": true,
    "expires_at": "2026-08-30T12:00:00Z",
    "revoked_at": null,
    "last_used_at": null,
    "created_at": "2026-07-30T10:00:00Z",
    "updated_at": "2026-07-30T10:00:00Z"
  },
  "raw_token": "fn_..."
}
```

The raw token is returned only once. List/detail responses never return the raw
token or token hash.

## Invoke With Token

For a function whose `invoke_access` is `token`, the caller invokes with:

```text
X-Function-Token: fn_...
```

Example:

```text
POST /api/functions/{function_id}/invoke/
X-Function-Token: fn_...
Content-Type: application/json
```

## Rotate Token

Rotation replaces the old secret with a new one:

```text
POST /api/functions/{function_id}/tokens/{token_id}/rotate/
```

Optional body:

```json
{
  "expires_at": "2026-09-30T12:00:00Z"
}
```

The old raw token stops working immediately. The response returns the new
`raw_token` once.

## Access Rules

- Function owners can manage tokens for their own functions.
- Platform admins can manage tokens for any function.
- Other users cannot see, create, rotate, revoke, or update tokens for functions
  they do not own.
- Expired, inactive, or revoked tokens cannot invoke.
- Active token names must be unique per function, case-insensitively.
- The default maximum is 20 active invocation tokens per function, controlled by
  `MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION`.

