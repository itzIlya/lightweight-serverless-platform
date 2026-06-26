# Project Status Report

Date: 2026-06-25

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
- Recovery backoff for stale-worker recovered jobs
- Dead-letter state for jobs recovered too many times
- Non-destructive worker queue consumption with processing queues and ACK
- Docker-based asynchronous image builds
- Local Docker registry
- Docker-based function execution
- Build retry policy, cancellation, and per-attempt history
- Invocation-time file uploads with validation and sandbox delivery
- Combined invocation input size limit
- Declared invocation output files with persisted downloads
- Worker-side output validation before artifact upload
- Runtime-enforced `/sandbox/output` tmpfs limit based on the version output
  total-size limit
- Export-copy of tmpfs outputs into the normal sandbox volume before container
  exit, so containers do not need to stay alive for artifact extraction
- Invocation read tokens for token/public callers to read only their own result
  and output artifacts
- JWT-based account login, refresh, and authenticated management APIs
- Owner-scoped functions, versions, builds, and invocations
- Separate function invocation tokens for non-owner callers
- Build and invocation status, logs, timing, and result capture

The main remaining work is no longer the basic execution path. It is deeper
distributed-worker coordination, security hardening, observability, evaluation,
retention/cleanup policies, and final documentation.

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

Status: Core runtime and basic artifact handling complete; retry policy remains

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
- Function-version declarations for expected output filenames
- Combined invocation input size limit
- Output-file count, per-file size, and total-size limits
- Worker-side pre-upload validation of declared output files
- Size-limited tmpfs mount for `/sandbox/output`
- Worker export of `/sandbox/output` into `/sandbox/export/output` before
  container exit
- Worker upload of declared files from the exported output directory
- Public owner/admin APIs to list and download invocation outputs
- Invocation read tokens returned by invoke responses so token/public callers can
  read only their own result and output files
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
- Output MIME allow-listing if needed
- Larger-output storage design beyond memory-backed tmpfs
- Output retention and cleanup policies
- Invocation cancellation
- Invocation retry policy and per-attempt history
- CPU and process-count limits
- Read-only root filesystem and additional container hardening
- Warm-container reuse and cold-start optimization

### Phase 4: Reliability and Distributed Workers

Status: Partially complete

Implemented:
- Separate scheduler pending queues for build and invocation jobs
- Durable `Job` table as the first scheduler/orchestrator migration step
- Redis messages now carry a durable `job_id`
- Dedicated scheduler process for queue-aware job placement
- Worker-specific invocation and build queues
- Shared per-worker processing queues for recovery
- Worker-side invocation priority before build work
- Scheduler round-robin tie-breaking across suitable workers
- Recent-function sticky invocation routing with a 10 second TTL
- Scheduler avoids workers with active builds for invocation placement
- Scheduler sends builds only to idle workers
- Worker registration at startup
- Worker heartbeat endpoint and loop
- Stale-worker expiry
- Worker processing queues for non-destructive job acceptance
- Worker claim validation before execution
- Worker ACK by removing completed job IDs from processing queues
- Scheduler recovery of unfinished jobs from stale workers
- Type-specific recovery backoff for stale-worker recovered jobs:
  - invocations: immediate, then 2 seconds, then 8 seconds
  - builds: 10 seconds, then 30 seconds, then 120 seconds
- Dead-letter handling for jobs recovered too many times
- Scheduler dispatch respects each job's `available_at` timestamp
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
- More complete idempotency protection for duplicate scheduler dispatches
- Worker capability reporting, such as runtimes and available capacity
- Capacity-aware scheduling and routing across multiple workers
- Per-worker concurrency limits and graceful shutdown
- Multi-worker integration and failure tests
- Warm pool or reusable container management

The scheduler now places small delivery messages onto worker-specific invocation
or build queues. Each delivery message contains a durable `job_id` and
`dispatch_attempt`. The worker checks its invocation queue before its build queue,
atomically moves a delivery message to a shared worker-specific processing queue,
then claims that exact delivery through the backend before fetching the payload
and executing. If a worker misses heartbeats, the scheduler marks it offline and
requeues unfinished jobs from its processing queue. Recovered jobs increment a
durable recovery counter, use type-specific backoff, and move to `dead_lettered`
after too many recoveries.

This is a meaningful reliability step, but it is not the final form. Remaining
hardening includes duplicate-safe scheduler dispatch, graceful shutdown, and
multi-worker failure tests.

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
- Live output-file smoke test
- Output validation test plan in `docs/output_file_validation_tests.md`

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
- `GET /api/invocations/{id}/outputs/`
- `GET /api/invocations/{id}/outputs/{file_id}/download/`
- `GET /api/workers/`
- `GET /api/workers/{id}/`

Authentication notes:
- Most management endpoints require `Authorization: Bearer <jwt-access-token>`.
- `GET /api/workers/` and `GET /api/workers/{id}/` are admin-only.
- Function invocation auth is intentionally separate from JWT auth.
- Private functions require owner/admin JWT.
- Token-protected functions accept `X-Function-Token`.
- Public functions accept unauthenticated invocations.
- Invoke responses include an invocation `read_token`; callers can use
  `X-Invocation-Read-Token` to read that one invocation and its output files.

Protected internal worker endpoints:
- `GET /api/internal/builds/{build_request_id}/source/`
- `GET /api/internal/builds/{build_request_id}/state/`
- `PATCH /api/internal/builds/{build_request_id}/report/`
- `GET /api/internal/invocations/{request_id}/inputs/`
- `GET /api/internal/invocations/{request_id}/inputs/{file_id}/download/`
- `POST /api/internal/invocations/{request_id}/outputs/`
- `PATCH /api/internal/invocations/{request_id}/report/`

## Verified State

Latest verification:
- Migrations applied successfully for `accounts.0001_initial` and
  `functions.0005_invoke_access_and_tokens`
- Migrations applied successfully for `workers.0002_worker_build_concurrency`,
  `functions.0006_build_limits_and_leases`, and `jobs.0001_initial`
- Migrations applied successfully for `jobs.0002_recovery_dead_letter_fields`
- Backend Docker test suite passed: `60` tests
- Worker Docker test suite passed: `42` tests
- Scheduler test suite passed: `17` tests
- Compile check passed for backend, worker, and scheduler
- Migration drift check passed: `No changes detected`
- User journey smoke test passed with tmpfs-backed exported output file
- Single-worker user journey smoke test passed with split queues using function
  `14`, version `21`, and invocation `24`
- Two-worker user journey smoke test passed with split queues using function
  `15`, version `22`, and invocation `25`
- Multi-worker scheduler verification documented in
  `docs/multi_worker_scheduler_test_report.md`

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
- Separate build/invocation pending queues and worker queues
- Queue-aware scheduler placement with round-robin tie-breaking
- Short sticky routing for recently invoked functions
- Build placement only on idle workers
- Worker-side invocation priority before build work
- Recovery backoff and dead-letter handling for recovered jobs
- Dispatch blocking while a recovered job's `available_at` is still in the future
- Worker claim validation before execution
- Stale worker-report rejection using dispatch attempts
- Durable job status updates from worker build/invocation reports
- Invocation output upload validation, owner/download authorization, and
  invocation read-token authorization
- Worker-side output validation for unsafe names, reserved names, file-count
  limit, per-file size limit, total-size limit, and no-upload-on-failure
- Worker tmpfs output mount, export-copy wrapper, Docker archive extraction
  from the stopped container, and no-upload-on-validation-failure behavior

## Important Current Limitations

- The deployment is a local Docker Compose prototype.
- There is one scheduler in local Compose; workers can be scaled with Docker
  Compose, but multi-worker failure testing is still limited.
- A worker crash after accepting a job no longer loses the job immediately;
  stale-worker recovery requeues it from the processing queue with backoff.
- Jobs recovered too many times are moved to `dead_lettered` instead of being
  retried forever.
- The current recovery loop is coarse and heartbeat-based, so recovery is not
  instant.
- Durable jobs exist, but Redis is still the active queue transport.
- Scheduler placement is now queue-aware, but not yet capability-aware by
  runtime, memory, CPU, cached image, or warm-container availability.
- Only Python image builds are currently implemented.
- Invocation input and declared output files are persisted, but retention cleanup
  is not implemented yet.
- `/sandbox/output` is memory-backed tmpfs, so large declared outputs compete
  with function memory and should stay small in this prototype.
- The worker requires access to the Docker socket.
- JWT signing currently uses the project `SECRET_KEY`; production should use a strong dedicated secret/key policy.
- Function invocation tokens can be created at the model level, but there is no public token-management API yet.
- There is no rate limiting for JWT-authenticated, token-based, or public invocations.
- There is no cleanup policy for uploaded sources, input files, images, or logs.
- There is no production UI, dashboard, CI pipeline, or deployment manifest.

## Remaining Work in Recommended Order

### Priority 1: Complete Invocation Artifacts and Reliability

1. Add output MIME allow-listing if output content-type restrictions are needed.
2. Add retention and cleanup policies for sources, inputs, outputs, images, and logs.
3. Add a larger-output artifact strategy, such as direct object-storage upload.
4. Add invocation attempt history and an admin-configurable retry policy.
5. Add invocation cancellation.
6. Make scheduler dispatch more strongly idempotent and duplicate-safe.

### Priority 2: Make Workers Truly Distributed

7. Report worker capabilities and available capacity.
8. Route jobs to suitable workers.
9. Add per-worker concurrency controls and graceful worker shutdown.
10. Test multiple workers and worker-failure scenarios.

### Priority 3: Security and Resource Isolation

11. Add public APIs for creating, listing, rotating, expiring, and revoking function invocation tokens.
12. Add rate limits for JWT-authenticated, token-based, and public invocations.
13. Add password reset and email verification if account UX remains in this backend.
14. Add CPU, process, disk, and output quotas.
15. Use a read-only function root filesystem where possible.
16. Add secret/environment-variable management for functions.
17. Plan an alternative to unrestricted Docker-socket access.
18. Add dependency and image scanning.

### Priority 4: Performance and Observability

19. Add warm-container reuse.
20. Collect resource usage and cold-start metrics.
21. Add structured logs and platform metrics.
22. Add dashboards and operational alerts.
23. Add cleanup and retention jobs.

### Priority 5: Evaluation and Project Completion

24. Add CI for backend, worker, and scheduler tests.
25. Create repeatable benchmark workloads.
26. Run performance, scaling, and failure-recovery experiments.
27. Analyze results against the proposal goals.
28. Write the final report, limitations, and future-work sections.

## Recommended Next Milestone

The next milestone should be:

`stronger multi-worker reliability + invocation retries/cancellation`

Durable job records, scheduler placement, startup worker registration,
worker-specific queues, processing queues, ACK, heartbeat detection,
stale-worker recovery, invocation input files, and invocation output files now
exist. Recovery backoff and dead-letter handling now exist too. The next
reliability steps are duplicate-safe dispatch, invocation retry/cancellation,
and multi-worker failure testing.

Before exposing token-protected or public functions to real users, add
function-invocation-token management APIs and rate limits.
