# Serverless Platform Frontend

This is the React/Vite frontend for the platform. It is a guided product UI, not
an API demo: creating/building a function and invoking it are each broken into
short, focused steps.

Run it with the local platform stack from the project root:

```powershell
docker compose up -d --build frontend
```

The Dockerfile uses Runflare for its Node image by default. To use Arvan instead:

```powershell
docker compose build --build-arg NODE_IMAGE=docker.arvancloud.ir/node:22-alpine frontend
docker compose up -d frontend
```

Then open:

```text
http://localhost:5173
```

Default service URLs:

```text
userservice: http://localhost:8100
backend:     http://localhost:8000
```

Implemented user flow:

```text
landing page
login/sign up
my functions list
add new function
guided function builder: identity -> code -> contract -> build
function hub: overview, build status, guided run, history, access tokens, API guide
guided invocation: choose sync/async -> JSON/files -> result
auto-poll build and invocation status
view returned JSON and exit status
download invocation ZIP
create/update/rotate/revoke invocation tokens
view invocation history, including token metadata when a function token was used
```

The editor creates an uncompressed ZIP in the browser containing:

```text
handler.py
requirements.txt
config.json
```

The backend still validates and builds the uploaded ZIP. The frontend does not
replace backend validation.

Prototype auth storage:

```text
access JWT:  localStorage
refresh JWT: localStorage
```

This is intentionally simple for the local prototype. Production should move to
a safer refresh-token strategy.
