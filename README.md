# Lightweight Serverless Platform

This repository is the first implementation pass for the proposal:
`A Lightweight Serverless Execution Platform for Distributed Cloud Environments`.

## Current direction

- Django control plane
- PostgreSQL for persistent metadata
- Redis for queueing and coordination
- Docker-based execution on worker nodes
- Local registry for built function images
- Durable job records plus a simple scheduler service
- Worker-specific Redis queues
- Worker heartbeats and stale-worker recovery

## Build order

1. Control plane skeleton
2. Function upload and version records
3. Image build pipeline
4. Invocation queue and worker execution
5. Warm pools, retries, and metering
6. Observability and evaluation

## Local layout

- `backend/` Django control plane
- `worker/` worker process
- `scheduler/` simple job placement service
- `docker-compose.yml` local stack
- `ROADMAP.md` milestone guide

## Current API surface

- `GET /health/`
- `POST /api/auth/register/`
- `POST /api/auth/token/`
- `POST /api/auth/token/refresh/`
- `GET /api/auth/me/`
- `GET /api/functions/`
- `POST /api/functions/`
- `GET /api/functions/{id}/`
- `GET /api/functions/{id}/versions/`
- `POST /api/functions/{id}/versions/`
- `POST /api/versions/{id}/build/`
- `GET /api/versions/{id}/builds/`
- `POST /api/versions/{id}/cancel-build/`
- `POST /api/functions/{id}/invoke/`
- `GET /api/versions/`
- `GET /api/versions/{id}/`
- `GET /api/build-attempts/`
- `GET /api/build-attempts/{id}/`
- `GET /api/invocations/`
- `GET /api/invocations/{id}/`
- `GET /api/workers/`
- `GET /api/workers/{id}/`

Most platform-management endpoints require:

`Authorization: Bearer <jwt-access-token>`

Worker-node endpoints are admin-only. Worker internal endpoints use
`X-Internal-Token` instead of user JWTs.

Function invocation access is separate from JWT management auth:

- `private`: only the function owner or a platform admin can invoke with JWT.
- `token`: callers can invoke with `X-Function-Token`.
- `public`: callers can invoke without JWT or an invocation token.

Invocation tokens are opaque function-scoped secrets, not JWTs.

## Function bundle format

Uploaded function versions must be zip files containing these top-level files:

- `handler.py`
- `requirements.txt`
- `config.json`

Optional input files may be included too, as long as they do not use unsafe paths.

## Invocation flow

`POST /api/functions/{id}/invoke/` creates an invocation record, creates a
durable `Job` row, and pushes that job ID to the scheduler queue. The scheduler
chooses an online worker, dispatches a specific attempt, and pushes a small
delivery message to that worker's queue. The worker claims that delivery before
fetching the current payload and executing. Only versions with a completed build
can be invoked.

Minimal request:

```json
{
  "event": {
    "name": "Ilya"
  }
}
```

Optional version selection:

```json
{
  "version": "v1",
  "event": {}
}
```

Function creation no longer accepts `owner_id`. The authenticated JWT user is
used as the function owner automatically.

## Worker contract

Each worker registers itself with the backend when it starts and then listens on
two input Redis queues:

- `worker:<worker-name>:invocations`
- `worker:<worker-name>:builds`

The scheduler places invocation and build jobs onto the matching queue. The
worker checks the invocation queue first, then the build queue. Each Redis
message contains only delivery metadata:

```json
{
  "job_id": "<durable job id>",
  "dispatch_attempt": 1
}
```

The worker atomically moves the job ID from one of those input queues to:

`worker:<worker-name>:processing`

Then it asks the backend to claim that exact delivery. If the backend accepts
the claim, it returns the current job payload. That payload includes:

- `request_id`
- `function_slug`
- `version`
- `handler`
- `image_ref`

To run multiple local workers in the prototype:

```powershell
docker compose up -d --scale worker=2
```

Each worker uses its container hostname as its worker name unless `WORKER_NAME`
is explicitly set.
- `config`
- `event`

At runtime the worker:

1. marks the invocation `running`
2. creates temporary input/output sandboxes
3. runs the function image in Docker
4. reads `stdout`, `stderr`, exit code, and `output/result.json`
5. reports the final status back to the backend

The container receives:

- `FUNCTION_EVENT_PATH=/sandbox/input/event.json`
- `FUNCTION_OUTPUT_DIR=/sandbox/output`
- `FUNCTION_HANDLER=<handler from function version>`
- `FUNCTION_REQUEST_ID=<invocation request id>`

The container should write its return value to:

- `/sandbox/output/result.json`

This worker is ready for the image build step, but it will fail cleanly if
`image_ref` is still empty.

## Asynchronous build flow

`POST /api/versions/{id}/build/`:

1. marks the version `queued` and returns HTTP `202` immediately
2. creates a new build-attempt record with its own request ID
3. creates a durable `Job` row and pushes the job ID to the scheduler queue
4. the scheduler chooses an online worker and pushes a delivery message to that
   worker's queue
5. the worker marks the build `building`
6. the worker securely downloads the uploaded source bundle from the backend
7. it extracts the bundle and writes `.serverless/runner.py` and a Dockerfile
8. it builds the image and pushes it to the local registry
9. it reports `built`, `failed`, or `cancelled`, logs, timestamps, and `image_ref` to Django

Build state is available from `GET /api/versions/{id}/`. The normal lifecycle
is `pending -> queued -> building -> built`, or `failed` when the worker cannot
complete the build. If the user cancels a queued or running build, the state
becomes `cancelled`.

Builds and invocations use separate scheduler Redis lists:

- `scheduler-pending-invocations`
- `scheduler-pending-builds`

Those lists contain durable job IDs only. The scheduler loads the matching
Postgres `Job`, picks a worker, and pushes a delivery message to the matching
worker-specific queue. The worker claims that delivery with the backend and then
receives the stored payload. The payload `type` field lets the worker dispatch
each job to the correct executor.

Every queued build or invocation also creates a durable `Job` row in Postgres.
The scheduler queue message is the `job_id`. Redis is still the active transport,
but the `Job` table is now the source of truth for scheduler placement and
worker status reports. Worker reports update the matching durable job status to
`running`, `succeeded`, `failed`, or `cancelled`.

### Scheduler flow

1. The API writes a `Job` row with status `queued`.
2. The API pushes the job ID to `scheduler-pending-invocations` or
   `scheduler-pending-builds`.
3. The scheduler reads the job ID and asks the backend for the job payload.
4. The scheduler asks the backend for online workers.
5. The scheduler tries invocation jobs first, uses short recent-function
   affinity when safe, and otherwise uses queue-aware round-robin placement.
6. The scheduler asks the backend to mark the job `dispatched` to that worker
   and assign a `dispatch_attempt`.
7. The scheduler pushes `{job_id, dispatch_attempt}` to
   `worker:<worker-name>:invocations` or `worker:<worker-name>:builds`.
8. The worker checks its invocation queue before its build queue and atomically
   moves the delivery message to
   `worker:<worker-name>:processing`.
9. The worker claims the delivery through the backend.
10. The backend verifies the worker and dispatch attempt, then marks the job
    `running` and returns the payload.
11. The worker executes only after claim acceptance.
12. The worker reports lifecycle changes to the backend.
13. After a terminal report, the worker ACKs by removing the delivery message from the
    processing queue.

### Worker heartbeat and recovery

Workers send heartbeats to the backend every `WORKER_HEARTBEAT_SECONDS`
seconds. The scheduler periodically asks the backend to mark stale workers
offline after `WORKER_STALE_AFTER_SECONDS`.

When a worker is stale, the scheduler scans that worker's processing queue:

`worker:<worker-name>:processing`

For each unfinished job ID, the scheduler:

1. marks the durable job back to `queued`
2. removes the job ID from the stale worker's processing queue
3. pushes the job ID back to the matching scheduler pending queue

Each dispatch receives a `dispatch_attempt` number. Worker reports include the
job ID, worker name, and dispatch attempt, so old reports from recovered jobs do
not overwrite the current job state.

### Build history and cancellation

- `GET /api/versions/{id}/builds/` lists every build attempt for that version.
- `GET /api/build-attempts/{id}/` retrieves one attempt.
- `POST /api/versions/{id}/cancel-build/` cancels the active build attempt.
- `POST /api/build-attempts/{id}/cancel/` cancels a specific attempt.

Retry policy is stored in the singleton `BuildPolicy` row and defaults to `2`
retries. That means one initial build plus up to two automatic retries.

### Build rate limits and leases

Build submission limits are also stored in `BuildPolicy`:

- builds per user per hour
- builds per function per hour
- queued builds per user
- queued builds per function
- global concurrent build leases
- build lease duration

The API enforces submission/rate limits before queueing a build. Actual build
execution concurrency is controlled by worker leases:

1. the worker receives a `function.build` job
2. the worker asks the backend for a build lease
3. the backend grants the lease only if global and worker capacity are available
4. the worker runs Docker only after a lease is granted
5. the worker releases the lease when build processing finishes
6. if no lease is available, the worker requeues the job

This keeps API admission control separate from distributed execution scheduling.

The image tag format is:

`<local-registry>/functions/<function-slug>:v<version-id>-<version>`
