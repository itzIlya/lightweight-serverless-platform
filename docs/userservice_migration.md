# Userservice Migration

The platform is moving from an in-backend `accounts` app to a separate
userservice.

## Current Target

```text
frontend/client
  |
  +-- userservice
  |     POST /api/auth/register/
  |     POST /api/auth/token/
  |     POST /api/auth/token/refresh/
  |     GET  /api/auth/me/
  |     GET  /api/auth/public-key/
  |     GET  /api/auth/jwks/
  |
  +-- serverless backend
        validates userservice JWT locally from JWKS
        manages functions, builds, invocations, artifacts
```

Userservice owns account data and signs JWTs with RS256. Other services verify
those JWTs with the userservice public key/JWKS, so they do not need to call the
userservice on every request.

## Service Boundaries

Userservice owns:

- users
- passwords
- account roles
- login/register/refresh
- JWT private signing key
- public key and JWKS discovery

Serverless backend owns:

- functions
- function versions
- builds
- invocations
- invocation input/output/log artifacts
- function invocation tokens
- internal worker/orchestrator APIs

Function invocation tokens remain in the serverless backend because they belong
to function invocation access, not account login.

## Current Bridge State

The backend now accepts userservice-issued RS256 JWTs through
`ExternalUserServiceJWTAuthentication`.

For compatibility, the backend still also accepts the old local SimpleJWT tokens.
When the backend receives a valid userservice JWT, it creates or updates a local
shadow user/account row keyed by the userservice `sub` claim. Existing ownership
logic can therefore continue using `Function.owner` while we migrate.

This is intentionally temporary.

## JWT Claims

Userservice access tokens include:

```json
{
  "iss": "serverless-userservice",
  "aud": "serverless-platform",
  "sub": "stable-user-subject",
  "username": "ilya",
  "email": "ilya@example.com",
  "role": "user",
  "token_type": "access",
  "exp": 1785420000
}
```

The backend checks:

- signature
- algorithm
- issuer
- audience
- token type
- expiry
- subject

## Key Discovery And Rotation

Userservice exposes:

```text
GET /api/auth/public-key/
GET /api/auth/jwks/
```

The backend caches JWKS responses for `USERSERVICE_JWKS_CACHE_SECONDS`.

Userservice, or an operator, can force the backend to refetch userservice keys:

```text
POST /api/internal/auth/userservice-jwks-cache/clear/
X-Internal-Token: <shared internal token>
```

## Next Migration Step

Replace local shadow ownership with userservice-subject ownership:

```text
current:
  Function.owner -> local Django User

target:
  Function.owner_subject -> userservice JWT sub
```

The same pattern should later apply to ownership checks for versions, builds,
invocations, outputs, and any user-created settings.

