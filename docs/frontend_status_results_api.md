# Frontend Status And Result API Contract

This document describes the prototype frontend contract for build status,
invocation status, results, output downloads, and invocation ZIP downloads.

## General Rules

- Builds and invocations are asynchronous.
- Frontends poll `poll_after_seconds` when it is not `null`.
- `is_terminal=true` means polling can stop for that resource.
- Prefer `frontend_state`, `can_*`, and `links` fields over deriving UI state
  from internal build/job/orchestrator details.
- Expired invocations are deleted by retention cleanup and return `404`, as if
  they never existed.
- V1 and V2 coordination details are internal. The frontend should use the same
  read APIs for both.

## OpenAPI And Swagger

Backend:

```text
GET /api/schema/
GET /api/docs/
```

Userservice:

```text
GET /api/schema/
GET /api/docs/
```

`/api/schema/` is the source of truth for frontend code generation or Postman
imports. `/api/docs/` loads Swagger UI from a CDN when internet access is
available; the JSON schema still works offline.

## Golden Frontend Path

The main user journey should use this sequence:

```text
1. POST /api/functions/
2. POST /api/functions/{function_id}/source/
3. GET  /api/functions/{function_id}/build-status/
4. POST /api/functions/{function_id}/invoke/
5. GET  /api/invocations/{invocation_id}/
6. GET  /api/invocations/{invocation_id}/download/
```

Each response includes either direct `links` for the next step or a
`poll_after_seconds` hint. The frontend should prefer those response fields over
hardcoded timing or internal job-state assumptions.

### 1. Create Function

```text
POST /api/functions/
Authorization: Bearer <jwt-access-token>
```

Response includes:

```json
{
  "resource": "function",
  "id": 1,
  "build_status": "not_built",
  "links": {
    "source": "/api/functions/1/source/",
    "build_status": "/api/functions/1/build-status/",
    "invoke": "/api/functions/1/invoke/",
    "invocations": "/api/functions/1/invocations/",
    "tokens": "/api/functions/1/tokens/"
  }
}
```

### 2. Upload Source

```text
POST /api/functions/{function_id}/source/
Authorization: Bearer <jwt-access-token>
Content-Type: multipart/form-data
```

Use field `source_bundle` for the ZIP file. The response is `202 Accepted` and
includes:

```json
{
  "resource": "source_replacement",
  "frontend_state": "queued",
  "is_terminal": false,
  "poll_after_seconds": 1,
  "can_cancel": true,
  "can_invoke": false,
  "links": {
    "build_status": "/api/functions/1/build-status/",
    "cancel_build": "/api/versions/2/cancel-build/"
  }
}
```

Then poll `links.build_status`.

## Build Status

```text
GET /api/functions/{function_id}/build-status/
Authorization: Bearer <jwt-access-token>
```

Response shape:

```json
{
  "resource": "build",
  "function_id": 1,
  "state": "queued",
  "frontend_state": "queued",
  "is_terminal": false,
  "poll_after_seconds": 1,
  "can_cancel": true,
  "can_invoke": false,
  "links": {
    "function": "/api/functions/1/",
    "build_status": "/api/functions/1/build-status/",
    "invoke": "/api/functions/1/invoke/",
    "invocations": "/api/functions/1/invocations/"
  },
  "active_version": {},
  "pending_version": {},
  "latest_version": {},
  "latest_attempt": {}
}
```

Build states:

```text
not_built
pending
queued
building
cancelling
built
failed
cancelled
```

Poll while:

```text
queued
building
cancelling
```

Do not poll automatically for `not_built`, `pending`, `built`, `failed`, or
`cancelled`.

## Invocation Status And Result

```text
GET /api/invocations/{invocation_id}/
Authorization: Bearer <jwt-access-token>
```

or, for public/token callers:

```text
GET /api/invocations/{invocation_id}/
X-Invocation-Read-Token: <invocation-read-token>
```

Response shape:

```json
{
  "id": 1,
  "request_id": "uuid",
  "function_version": 1,
  "status": "succeeded",
  "frontend_state": "succeeded",
  "is_terminal": true,
  "poll_after_seconds": null,
  "result_available": true,
  "outputs_available": true,
  "can_read_outputs": true,
  "can_download": true,
  "event": {},
  "result": {},
  "stdout": "text printed by the function",
  "stderr": "text printed to stderr",
  "exit_code": 0,
  "cold_start": false,
  "error_message": "",
  "duration_ms": 123,
  "queued_at": "timestamp",
  "started_at": "timestamp",
  "finished_at": "timestamp",
  "input_files": [],
  "output_files": [],
  "outputs_url": "/api/invocations/1/outputs/",
  "download_url": "/api/invocations/1/download/",
  "links": {
    "self": "/api/invocations/1/",
    "outputs": "/api/invocations/1/outputs/",
    "download": "/api/invocations/1/download/"
  },
  "log_delivery": "zip_only"
}
```

Invocation states:

```text
queued
running
succeeded
failed
timeout
cancelled
```

Poll while:

```text
queued
running
```

Terminal states:

```text
succeeded
failed
timeout
cancelled
```

`stdout` and `stderr` are always present as strings. Long values may be previews.
The full stdout/stderr artifacts are not exposed through standalone log APIs.
They are included only in the invocation ZIP.

## Invocation Outputs

```text
GET /api/invocations/{invocation_id}/outputs/
GET /api/invocations/{invocation_id}/outputs/{output_id}/download/
```

Use either owner/admin JWT auth or:

```text
X-Invocation-Read-Token: <invocation-read-token>
```

Outputs are visible only after the invocation is terminal and the artifact has
been committed. V2 staged outputs are hidden until finalization succeeds.

## Invocation ZIP

```text
GET /api/invocations/{invocation_id}/download/
```

The ZIP contains:

```text
manifest.json
input/
output/
logs/
```

The ZIP is the only user-facing way to download full stdout/stderr logs.

If the ZIP is requested before artifacts are ready, the backend returns:

```json
{
  "detail": "Invocation artifacts are not ready yet.",
  "frontend_state": "running",
  "poll_after_seconds": 1
}
```

with HTTP `409 Conflict`. The frontend should keep polling the invocation detail
endpoint and retry the ZIP only when `can_download=true`.

## Invocation History

```text
GET /api/functions/{function_id}/invocations/
GET /api/functions/{function_id}/invocations/?status=succeeded&limit=25
```

Supported query parameters:

- `status`: filters invocation records by status.
- `limit`: returns at most this many records, clamped between `1` and `100`.

The response is ordered newest first.
