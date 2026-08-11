# Frontend Prototype

Date: 2026-08-04

The frontend prototype lives in `frontend/` and is dependency-free. It is served
as static files from `http://localhost:5173`.

## Pages

- Landing page with Home, About Us and Contact Us navigation.
- Login and signup page.
- Signed-in workspace with:
  - My Functions list
  - Add New Function button
  - Function editor
  - In-page build queued/status notifications
  - Invocation token management for the selected function
  - Invocation history for the selected function

## API Flow

The frontend uses:

```text
userservice /api/auth/register/
userservice /api/auth/token/
userservice /api/auth/token/refresh/
userservice /api/auth/logout/
userservice /api/auth/me/

backend GET/PATCH/POST /api/functions/
backend POST /api/functions/{id}/source/
backend GET /api/functions/{id}/build-status/
backend POST /api/functions/{id}/invoke/
backend GET /api/functions/{id}/invocations/
backend GET /api/invocations/{id}/
backend GET /api/invocations/{id}/download/
backend GET/POST/PATCH /api/functions/{id}/tokens/
backend POST /api/functions/{id}/tokens/{token_id}/rotate/
backend POST /api/functions/{id}/tokens/{token_id}/revoke/
```

## Source Editor Behavior

Users paste function code and requirements text. The browser creates a ZIP with:

```text
handler.py
requirements.txt
config.json
```

That ZIP is uploaded as `source_bundle` to the existing backend build API.

For new functions, the editor creates the function shell first and then uploads
the generated ZIP. For existing functions, the editor updates metadata first
and then uploads the replacement source.

## Invocation History

Invocation records now include:

```text
invocation_auth_type
invocation_token
invocation_token_name
invocation_token_prefix
```

These fields let the frontend show whether an invocation came from owner JWT,
public access, or a function invocation token.
