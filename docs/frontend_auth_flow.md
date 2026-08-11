# Frontend Auth And CORS Flow

Date: 2026-08-04

This document describes the frontend authentication contract now that account
management lives in the separate userservice.

## Service URLs

Local development:

```text
userservice: http://localhost:8100
backend:     http://localhost:8000
frontend:    http://localhost:5173
```

The frontend should treat userservice as the identity authority and backend as
the serverless platform API.

## CORS

Both userservice and backend read the same CORS settings:

```text
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000,http://127.0.0.1:3000
CORS_ALLOW_ALL_ORIGINS=false
CORS_ALLOW_CREDENTIALS=false
CORS_PREFLIGHT_MAX_AGE=86400
```

Allowed browser request headers:

```text
authorization
content-type
x-function-token
x-invocation-read-token
x-requested-with
```

Exposed response headers:

```text
content-disposition
content-length
retry-after
```

`content-disposition` matters for invocation ZIP and output-file downloads.

## Login

```text
POST http://localhost:8100/api/auth/token/
Content-Type: application/json
```

```json
{
  "username": "ilya",
  "password": "StrongerPass123!"
}
```

Response:

```json
{
  "user": {
    "id": 1,
    "subject": "uuid",
    "username": "ilya",
    "email": "ilya@example.com",
    "role": "user"
  },
  "access": "userservice-rs256-access-jwt",
  "refresh": "userservice-rs256-refresh-jwt"
}
```

The frontend uses `access` for backend management API calls:

```text
Authorization: Bearer <access>
```

## Register

```text
POST http://localhost:8100/api/auth/register/
```

Register returns the same shape as login: `user`, `access`, and `refresh`.

## Current User

```text
GET http://localhost:8100/api/auth/me/
Authorization: Bearer <access>
```

Use this after page reload to validate the current access token and restore the
current user profile.

## Refresh

When backend or userservice returns `401`, the frontend should try one refresh:

```text
POST http://localhost:8100/api/auth/token/refresh/
Content-Type: application/json
```

```json
{
  "refresh": "<refresh>"
}
```

If refresh succeeds:

1. Replace the stored `access` and `refresh` tokens.
2. Retry the original request once.

If refresh fails:

1. Delete stored tokens.
2. Clear the current user.
3. Redirect to login.

Do not retry refresh in a loop. One refresh attempt per failed request is enough.

## Logout

```text
POST http://localhost:8100/api/auth/logout/
```

The userservice returns an acknowledgement:

```json
{
  "logged_out": true,
  "detail": "Tokens are stateless in this prototype..."
}
```

Current prototype rule:

- JWTs are stateless.
- Logout is completed by deleting `access` and `refresh` on the frontend.
- Server-side refresh-token revocation is future work.

## Token Storage Strategy

Recommended for the first prototype:

- Keep the access token in memory while the app is open.
- Persist the refresh token in `localStorage` only for prototype convenience.
- On page load, use the refresh token to get a new access token, then call
  `/api/auth/me/`.

More secure production direction:

- Store refresh tokens in secure, HttpOnly cookies.
- Add CSRF protection for cookie-auth refresh/logout.
- Add server-side refresh-token revocation or rotation tracking.

We are not doing that yet because the current services use bearer JWTs and
`CORS_ALLOW_CREDENTIALS=false`.

## Backend Calls

Management calls use the userservice access token:

```text
Authorization: Bearer <access>
```

Examples:

```text
GET  http://localhost:8000/api/functions/
POST http://localhost:8000/api/functions/
GET  http://localhost:8000/api/invocations/{id}/
```

Function invocation auth remains separate:

- Private function: owner/admin JWT.
- Token function: `X-Function-Token`.
- Public function: no auth.

Invocation result reads for token/public callers use:

```text
X-Invocation-Read-Token: <read_token_from_invoke_response>
```

This keeps account JWTs, function invocation tokens, and invocation read tokens
separate.

## API Docs

Userservice:

```text
http://localhost:8100/api/schema/
http://localhost:8100/api/docs/
```

Backend:

```text
http://localhost:8000/api/schema/
http://localhost:8000/api/docs/
```
