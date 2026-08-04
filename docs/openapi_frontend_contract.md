# OpenAPI And Frontend Contract

Date: 2026-08-02

The prototype now exposes curated OpenAPI 3.0 schemas for the two public-facing
HTTP services.

## Backend

```text
GET http://localhost:8000/api/schema/
GET http://localhost:8000/api/docs/
```

Use this schema for:

- functions
- source replacement and builds
- function invocation-token management
- invocations
- invocation outputs
- invocation ZIP downloads
- admin worker reads

The backend schema documents userservice-issued JWTs as the normal management
authentication mechanism. Backend-local auth endpoints are listed as
compatibility endpoints only.

## Userservice

```text
GET http://localhost:8100/api/schema/
GET http://localhost:8100/api/docs/
```

Use this schema for:

- register
- login
- refresh
- current user
- public key
- JWKS discovery

The userservice issues RS256 JWTs. The backend verifies those JWTs through the
userservice public key/JWKS endpoints.

## Frontend State Rules

Frontend code should prefer the stable response helpers:

```text
frontend_state
is_terminal
poll_after_seconds
can_cancel
can_invoke
result_available
outputs_available
can_read_outputs
can_download
links
```

The UI should not derive product behavior from V1/V2 coordination details,
staged artifact state, Redis state names, worker queues, or build-attempt
internals unless it is an admin/debug screen.

## Swagger UI Note

`/api/docs/` loads Swagger UI from a CDN. If internet access is unavailable,
the docs page may not render the Swagger interface, but `/api/schema/` remains
usable and can be imported into Postman, Insomnia, or a frontend code generator.
