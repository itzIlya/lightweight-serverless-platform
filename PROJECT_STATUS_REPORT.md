# Project Status Report

Date: 2026-06-17

Source basis:
- `ROADMAP.md`
- `proposal.pdf`, "A Lightweight Serverless Execution Platform for Distributed Cloud Environments"
- Current backend, worker, Docker Compose, migrations, and tests

## Executive Summary

The project has a working serverless prototype with the complete basic path:

`upload source -> queue build -> build and push image -> invoke -> run isolated container -> return result`

The platform currently includes:
- Django control plane and REST API
- PostgreSQL metadata storage
- Redis build and invocation queue
- Durable Postgres job records for builds and invocations
- Simple scheduler service for worker placement
- Worker registration and worker-specific queues
- Worker heartbeat detection and stale-worker recovery
- Non-destructive worker queue consumption with processing queues and ACK
- Docker-based asynchronous image builds
- Local Docker registry
- Docker-based function execution
- Build retry policy, cancellation, and per-attempt history
- Invocation-time file uploads with validation and sandbox delivery
- JWT-based account login, refresh, and authenticated management APIs
- Owner-scoped functions, versions, builds, and invocations
- Separate function invocation tokens for non-owner callers
- Build and invocation status, logs, timing, and result capture

The main remaining work is no longer the basic execution path. It is persistent
output artifacts, deeper distributed-worker coordination, security hardening,
observability, evaluation, and final documentation.

## Roadmap Status

### Phase 1: Foundation

Status: Largely complete

Implemented:
- Django backend under `backend/`
- PostgreSQL, Redis, registry, backend, and worker services in Docker Compose
- Models for functions, function versions, invocations, invocation input files,
  build attempts, build policy, jobs, and worker nodes
- Django admin registrations
- Database migrations
- Health endpoint
- REST serializers, views, and routes
- `accounts` app for registration, login, JWT refresh, and current-user lookup
- Account role profile with `user` and `admin` roles
- JWT claims include role and username
- Function creation now uses the authenticated JWT user as owner
- Ownership filtering for functions, versions, build attempts, and invocations
- Admin-only worker-node API
- Shared-token protection for internal worker endpoints

Remaining:
- Password reset / email verification flow
- More complete account-management APIs
- Optional future extraction of accounts into a separate identity service
- API documentation or an OpenAPI schema
- Production secret and JWT signing-key management

### Phase 2: Upload and Build

Status: Complete for the current prototype

Implemented:
- Zip bundle upload and storage in Django media storage
- Required bundle-file and unsafe-path validation
- Function-version runtime, handler, configuration, and input-contract metadata
- Asynchronous build jobs through Redis
- Scheduler-based dispatch to worker-specific queues
- Secure source download by the worker
- Generated runner and Dockerfile
- Docker image build and push to the local registry
- Build status, timestamps, image reference, and logs
- Admin-configurable build retry policy
- Automatic build retries
- Per-attempt build history
- Queued-build cancellation and cooperative running-build cancellation
- API-side build submission limits for user/function hourly rate and queued depth
- Worker-side build leases for distributed execution concurrency
- Per-worker build concurrency capacity

Remaining hardening:
- Build timeout and resource limits
- Source, log, image, and build-history retention policies
- Stronger isolation from the host Docker daemon
- Dependency/image security scanning
- Support for additional runtimes if they remain in project scope

### Phase 3: Invocation Runtime

Status: Core runtime complete; artifact handling and retry policy remain

Implemented:
- Invocation API and Redis queueing
- Scheduler-based dispatch to worker-specific queues
- Selection of a built function version
- Rejection of unbuilt versions
- Isolated Docker execution with networking disabled
- Memory limit and execution timeout
- Event delivery through `event.json` and environment metadata
- Invocation status reporting
- Result, stdout, stderr, exit code, duration, and error capture
- Temporary Docker-managed input/output sandbox
- Invocation access modes:
  - `private`: only owner/admin JWT can invoke
  - `token`: callers can invoke with `X-Function-Token`
  - `public`: callers can invoke without JWT or invocation token
- Opaque hashed function invocation tokens, separate from JWT auth tokens

Invocation-time input files are implemented:
1. A function version declares allowed MIME types, maximum file count, and
   maximum size per file.
2. The invoke request can use `multipart/form-data` with `files` or
   `input_files`.
3. Django validates and stores the files as invocation records.
4. The worker retrieves the file metadata and contents through protected
   internal endpoints.
5. The worker places sanitized, position-prefixed files in
   `/sandbox/input/files`.
6. The container receives file metadata in `FUNCTION_INPUT_FILES_JSON` and the
   directory path in `FUNCTION_INPUT_FILES_DIR`.
7. The Docker sandbox volume is removed after the invocation.

Remaining:
- Persist arbitrary files written to `/sandbox/output`
- Public APIs to list and download invocation output files
- Output size, count, MIME, and retention limits
- Invocation cancellation
- Invocation retry policy and per-attempt history
- Dead-letter handling for permanently failed invocations
- CPU and process-count limits
- Read-only root filesystem and additional container hardening
- Warm-container reuse and cold-start optimization

### Phase 4: Reliability and Distributed Workers

Status: Partially complete

Implemented:
- Shared typed queue for build and invocation jobs
- Durable `Job` table as the first scheduler/orchestrator migration step
- Redis messages now carry a durable `job_id`
- Dedicated scheduler process for simple job placement
- Worker-specific Redis queues
- Worker registration at startup
- Worker heartbeat endpoint and loop
- Stale-worker expiry
- Worker processing queues for non-destructive job acceptance
- Worker claim validation before execution
- Worker ACK by removing completed job IDs from processing queues
- Scheduler recovery of unfinished jobs from stale workers
- Dispatch-attempt metadata to ignore stale worker reports
- Worker reports update durable job status
- Invocation timeouts
- Build retries, history, and cancellation
- Build submission rate limits
- Build execution leases with expiry and release
- Protected worker-to-backend reporting
- Persistent API-visible job state
- User-facing management APIs require JWT auth
- Worker-node API requires admin role
- Internal worker endpoints continue to use `X-Internal-Token`

Remaining:
- Invocation retries with configurable backoff
- Dead-letter queue
- More complete idempotency protection for duplicate scheduler dispatches
- Worker capability reporting, such as runtimes and available capacity
- Capacity-aware scheduling and routing across multiple workers
- Per-worker concurrency limits and graceful shutdown
- Multi-worker integration and failure tests
- Warm pool or reusable container management

The scheduler now places small delivery messages onto worker-specific queues.
Each delivery message contains a durable `job_id` and `dispatch_attempt`. The
worker atomically moves a delivery message to a worker-specific processing queue,
then claims that exact delivery through the backend before fetching the payload
and executing. If a worker misses heartbeats, the scheduler marks it offline and
requeues unfinished jobs from its processing queue.

This is a meaningful reliability step, but it is not the final form. Remaining
hardening includes duplicate-safe scheduler dispatch, dead-letter handling,
backoff, graceful shutdown, and multi-worker failure tests.

### Phase 5: Metrics and Evaluation

Status: Early

Implemented:
- Invocation and build duration
- Queue, start, and finish timestamps
- Invocation stdout, stderr, status, and exit code
- Build logs and attempt history
- Django admin filtering
- Backend and worker tests
- JWT/auth/ownership tests
- Invocation token tests
- Live upload/build/invoke smoke tests

Remaining:
- Structured, searchable logs
- Queue-depth, throughput, error-rate, and latency metrics
- CPU and memory usage metering
- Cold-start measurements
- Worker health and capacity metrics
- Metrics endpoint and dashboard
- Repeatable benchmark scripts and workloads
- Cold versus warm execution comparison
- Single-worker versus multi-worker evaluation
- Failure-recovery experiments
- Evaluation tables, charts, and analysis
- Final report with results, limitations, and comparison to the proposal

## Current API Surface

Available endpoints:
- `GET /health/`
- `POST /api/auth/register/`
- `POST /api/auth/token/`
- `POST /api/auth/token/refresh/`
- `GET /api/auth/me/`
- `GET|POST /api/functions/`
- `GET /api/functions/{id}/`
- `GET|POST /api/functions/{id}/versions/`
- `POST /api/functions/{id}/invoke/`
- `GET /api/versions/`
- `GET /api/versions/{id}/`
- `POST /api/versions/{id}/build/`
- `GET /api/versions/{id}/builds/`
- `POST /api/versions/{id}/cancel-build/`
- `GET /api/build-attempts/`
- `GET /api/build-attempts/{id}/`
- `POST /api/build-attempts/{id}/cancel/`
- `GET /api/invocations/`
- `GET /api/invocations/{id}/`
- `GET /api/workers/`
- `GET /api/workers/{id}/`

Authentication notes:
- Most management endpoints require `Authorization: Bearer <jwt-access-token>`.
- `GET /api/workers/` and `GET /api/workers/{id}/` are admin-only.
- Function invocation auth is intentionally separate from JWT auth.
- Private functions require owner/admin JWT.
- Token-protected functions accept `X-Function-Token`.
- Public functions accept unauthenticated invocations.

Protected internal worker endpoints:
- `GET /api/internal/builds/{build_request_id}/source/`
- `GET /api/internal/builds/{build_request_id}/state/`
- `PATCH /api/internal/builds/{build_request_id}/report/`
- `GET /api/internal/invocations/{request_id}/inputs/`
- `GET /api/internal/invocations/{request_id}/inputs/{file_id}/download/`
- `PATCH /api/internal/invocations/{request_id}/report/`

## Verified State

Latest verification:
- Migrations applied successfully for `accounts.0001_initial` and
  `functions.0005_invoke_access_and_tokens`
- Migrations applied successfully for `workers.0002_worker_build_concurrency`,
  `functions.0006_build_limits_and_leases`, and `jobs.0001_initial`
- Backend Docker test suite passed: `46` tests
- Worker Docker test suite passed: `21` tests
- Scheduler test suite passed: `7` tests
- Compile check passed for backend, worker, and scheduler
- Migration drift check passed: `No changes detected`

The backend test suite now covers:
- JWT registration, login, refresh support, and `/api/auth/me/`
- JWT-authenticated function, build, and invocation API access
- Owner isolation across functions, versions, build attempts, and invocations
- Admin-only worker-node access
- Worker internal endpoints protected by `X-Internal-Token`
- Function invocation tokens using `X-Function-Token` separately from JWT
- Public, private, and token-protected invocation modes
- Durable job records for build and invocation enqueue paths
- Scheduler internal APIs for reading and dispatching queued jobs
- Worker self-registration for scheduler placement
- Worker heartbeats and stale-worker expiry
- Worker processing queue recovery
- Worker claim validation before execution
- Stale worker-report rejection using dispatch attempts
- Durable job status updates from worker build/invocation reports

## Important Current Limitations

- The deployment is a local Docker Compose prototype.
- There is one scheduler and normally one worker process in local Compose.
- A worker crash after accepting a job no longer loses the job immediately;
  stale-worker recovery requeues it from the processing queue.
- The current recovery loop is coarse and heartbeat-based, so recovery is not
  instant.
- Durable jobs exist, but Redis is still the active queue transport.
- Scheduler placement is simple first-online-worker selection, not capacity-aware
  routing.
- Only Python image builds are currently implemented.
- Invocation input files are persisted, but output files are not.
- The worker requires access to the Docker socket.
- JWT signing currently uses the project `SECRET_KEY`; production should use a strong dedicated secret/key policy.
- Function invocation tokens can be created at the model level, but there is no public token-management API yet.
- There is no rate limiting for JWT-authenticated, token-based, or public invocations.
- There is no cleanup policy for uploaded sources, input files, images, or logs.
- There is no production UI, dashboard, CI pipeline, or deployment manifest.

## Remaining Work in Recommended Order

### Priority 1: Complete Invocation Artifacts and Reliability

1. Add an `InvocationOutputFile` model and media storage.
2. Upload files from `/sandbox/output` to the backend after execution.
3. Add output-file list and download APIs.
4. Add output count, size, MIME, and retention policies.
5. Add invocation attempt history and an admin-configurable retry policy.
6. Add invocation cancellation.
7. Add dead-letter handling for permanently failed/recovered-too-many-times jobs.
8. Add retry backoff for recovered jobs.
9. Make scheduler dispatch more strongly idempotent and duplicate-safe.

### Priority 2: Make Workers Truly Distributed

10. Report worker capabilities and available capacity.
11. Route jobs to suitable workers.
12. Add per-worker concurrency controls and graceful worker shutdown.
13. Test multiple workers and worker-failure scenarios.

### Priority 3: Security and Resource Isolation

14. Add public APIs for creating, listing, rotating, expiring, and revoking function invocation tokens.
15. Add rate limits for JWT-authenticated, token-based, and public invocations.
16. Add password reset and email verification if account UX remains in this backend.
17. Add CPU, process, disk, and output quotas.
18. Use a read-only function root filesystem where possible.
19. Add secret/environment-variable management for functions.
20. Plan an alternative to unrestricted Docker-socket access.
21. Add dependency and image scanning.

### Priority 4: Performance and Observability

22. Add warm-container reuse.
23. Collect resource usage and cold-start metrics.
24. Add structured logs and platform metrics.
25. Add dashboards and operational alerts.
26. Add cleanup and retention jobs.

### Priority 5: Evaluation and Project Completion

27. Automate the full upload/build/invoke/file integration test.
28. Add CI for backend, worker, and scheduler tests.
29. Create repeatable benchmark workloads.
30. Run performance, scaling, and failure-recovery experiments.
31. Analyze results against the proposal goals.
32. Write the final report, limitations, and future-work sections.

## Recommended Next Milestone

The next milestone should be:

`persistent invocation output artifacts + stronger multi-worker reliability`

Durable job records, scheduler placement, startup worker registration,
worker-specific queues, processing queues, ACK, heartbeat detection, and
stale-worker recovery now exist. The next reliability steps are duplicate-safe
dispatch, backoff, dead-letter handling, and multi-worker failure testing.

After that, persistent invocation output files should close the current
input/output artifact asymmetry.

Before exposing token-protected or public functions to real users, add
function-invocation-token management APIs and rate limits.
