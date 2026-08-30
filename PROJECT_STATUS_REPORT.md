# Project Status Report

Date: 2026-07-30

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
- Transactional job outbox with idempotent Redis Stream publication
- Read-only V2 shadow orchestrator and V1/V2 placement comparison gate
- Redis-owned worker heartbeat and capacity leases with a Django compatibility
  projection
- Pilot V2 build and invocation authority using Redis Streams and orchestrator
  leases
- Staged V2 invocation completions with checksummed, attempt-fenced output
  artifacts and terminal visibility rules
- Retryable invocation finalizer and expired-stage cleanup services
- Asynchronous PostgreSQL projection of V2 dispatch, running, recovery, and
  terminal state
- Simple scheduler service for worker placement
- Worker registration and worker-specific queues
- Worker heartbeat detection and stale-worker recovery
- Multithreaded workers with bounded invocation/build concurrency
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
- Scheduler-aware warm-container routing for exact idle warm matches
- Guarded predictive sticky routing as a fallback when exact warm metadata is
  not yet visible
- Usage- and pressure-aware warm-container eviction
- Repeatable warm-routing benchmark with cold baseline, initial warm run, and
  tuned warm run
- Invocation read tokens for token/public callers to read only their own result
  and output artifacts
- S3-compatible object storage configuration for media artifacts, live
  smoke-tested against Parspack
- Invocation logs stored as object-storage-backed artifacts with database
  previews
- Function active-version pointer and safe source-replacement/rebuild flow
- Function image ledger for active, superseded, failed, deleted, and
  delete-failed registry images
- Safe registry-image cleanup scheduling for replaced builds, failed candidate
  builds, and deleted functions
- User-facing function summaries that expose the active image, current build
  status, pending build, and per-function invocation history without requiring
  the frontend to understand every internal version row
- Frontend-facing response helpers across the main user path, including
  `resource`, `frontend_state`, `can_*` flags, polling hints, stable `links`,
  and ZIP-not-ready semantics
- Curated OpenAPI 3.0 schema and Swagger docs endpoints for both backend and
  userservice
- Separate userservice for account login, refresh, JWT issuing, and public-key
  discovery, with backend-side userservice JWT verification
- Browser-facing CORS configuration for backend and userservice, including
  frontend auth headers and download response headers
- Frontend auth-flow documentation for login, refresh, logout, token storage,
  backend calls, and expired-token handling
- Owner-scoped functions, versions, builds, and invocations
- Function invocation-token management APIs for non-owner callers
- Build and invocation status, logs, timing, and result capture
- Retention policy docs and cleanup commands for expired invocations and
  dead-letter jobs

The main remaining work is no longer the basic execution path. It is deeper
distributed-worker coordination, security hardening, operational alerting,
evaluation, resource controls, and final documentation.

## Roadmap Status

### Phase 1: Foundation

Status: Largely complete

Implemented:
- Django backend under `backend/`
- Django userservice under `userservice/`
- PostgreSQL, Redis, registry, backend, and worker services in Docker Compose
- Separate userservice PostgreSQL database in Docker Compose
- Models for functions, function versions, invocations, invocation input files,
  build attempts, build policy, jobs, and worker nodes
- Django admin registrations
- Database migrations
- Health endpoint
- REST serializers, views, and routes
- `userservice` for registration, login, JWT refresh, current-user lookup,
  public-key discovery, and JWKS discovery
- Userservice logout acknowledgement endpoint for the current stateless JWT
  prototype flow
- Userservice OpenAPI schema and Swagger docs at `/api/schema/` and `/api/docs/`
- Backend compatibility bridge for userservice-issued RS256 JWTs
- Backend OpenAPI schema and Swagger docs at `/api/schema/` and `/api/docs/`
- Account role profile with `user` and `admin` roles
- Userservice JWT claims include stable subject, role, username, email,
  issuer, audience, token type, and expiry
- Backend still accepts previous local SimpleJWT tokens during migration
- Function creation now uses the authenticated JWT user as owner
- Ownership filtering for functions, versions, build attempts, and invocations
- Admin-only worker-node API
- Shared-token protection for internal worker endpoints

Remaining:
- Password reset / email verification flow
- More complete account-management APIs
- Replace local backend shadow users and `Function.owner` foreign keys with
  external userservice subject ownership fields
- Production secret and JWT signing-key management

### Phase 2: Upload and Build

Status: Complete for the current prototype

Implemented:
- Zip bundle upload and storage in Django media storage
- Required bundle-file and unsafe-path validation
- Function-version runtime, handler, configuration, and input-contract metadata
- Source replacement API that creates a candidate build while keeping the
  existing active image live
- Successful builds promote `Function.active_version`; failed builds do not
  break current invocations
- Successful rebuilds mark the old image as `pending_delete` for later registry
  cleanup
- Failed candidate builds with produced image references are also marked
  `pending_delete`
- Function deletion removes source bundles and invocation artifacts, then leaves
  image records queued for registry cleanup
- Registry cleanup command skips images that are still the active image for a
  function
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
- Build-history retention policy, if we eventually decide not to keep it
  indefinitely
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
- Optional runner direct-upload fast path that sends declared outputs straight
  to the backend with a scoped upload token and skips Docker output export/copy
- Public owner/admin APIs to list and download invocation outputs
- Frontend-facing create-function, source-upload, build-status, invocation
  polling, result, output-link, and invocation ZIP download semantics
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
- Invocation cancellation
- Invocation retry policy and per-attempt history
- CPU and process-count limits
- Read-only root filesystem and additional container hardening
- Prewarming and deeper cold-start optimization
- Compose-backed backend tests for the direct-upload fast path once Docker is
  reachable again

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
- Scheduler-aware invocation routing to exact matching idle warm containers
- Guarded predictive sticky routing for recent exact function-version routes
  when no exact warm match is visible
- Local warm-container reservations to avoid overbooking one idle warm container
  during burst dispatch between worker heartbeats
- Warm-container reuse counters, memory-pressure eviction, and eviction reasons
- Scheduler avoids workers with active builds for invocation placement
- Scheduler sends builds only to idle workers
- Worker registration at startup
- Worker heartbeat endpoint and loop
- Worker heartbeat metadata for active jobs, active builds, active invocations,
  and warm-container inventory
- V2 worker heartbeat status propagation for `online`, `draining`, and
  `offline`
- Graceful worker drain on SIGTERM/SIGINT: workers stop accepting new jobs,
  continue heartbeating as `draining`, wait for active jobs, then mark
  themselves `offline`
- Stale-worker expiry
- Worker processing queues for non-destructive job acceptance
- Worker claim validation before execution
- Worker ACK by removing completed job IDs from processing queues
- Per-worker thread-pool execution with separate total, invocation, and build
  concurrency limits
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
- V2 invocation retry policy fields on function versions
- V2 invocation attempt history projected into PostgreSQL
- V2 invocation retry scheduling for retryable platform failures with
  idempotent lost-response handling
- Build submission rate limits
- Build execution leases with expiry and release
- Protected worker-to-backend reporting
- Persistent API-visible job state
- User-facing management APIs require JWT auth
- Worker-node API requires admin role
- Internal worker endpoints continue to use `X-Internal-Token`

Remaining:
- More complete idempotency protection for duplicate scheduler dispatches
- Worker capability reporting, such as runtimes, memory classes, cached images,
  and supported runtimes
- More advanced capacity-aware scheduling beyond queue depth and active builds
- Broader multi-worker crash and network-partition tests
- Proactive warm-container prewarming

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
hardening includes duplicate-safe scheduler dispatch, richer capability-aware
routing, and multi-worker failure tests.

Warm-container Stage 1 is implemented behind
`WORKER_WARM_CONTAINERS_ENABLED`. Each worker can keep a small local pool of
reactively warmed containers keyed by function version, image, handler, memory,
and output tmpfs size. A reused warm container receives a fresh event file,
fresh input directory, fresh output directory, and a fresh `/runner.py` process
per invocation. Containers are evicted by idle TTL, max age, max uses, failed
execution, cleanup failure, or least-recently-used pressure. This stage is
worker-local when first introduced. The worker keeps one shared invocation
executor per process so the warm pool survives across jobs.

A newer resident-runner variant is now implemented behind
`WORKER_WARM_RESIDENT_RUNNER_ENABLED`. In that mode, the warm container starts a
long-lived in-container HTTP runner, and the worker talks to that resident
runner instead of launching a fresh `python /runner.py` process for every warm
invocation. The first real smoke run showed the second warm invocation dropping
to 32 ms worker-side with Docker output export skipped for JSON-only results.

Warm-container Stage 1 benchmarking is documented in
`docs/warm_container_stage1_benchmark_report.md`. In the focused executor
benchmark, steady-state warm median duration improved from 3819 ms to 2572 ms
for no-op invocations and from 4798 ms to 2695 ms for one-second invocations.
In the valid API-level sequential no-op benchmark, median invocation duration
improved from 1620 ms to 925 ms.

Warm-container Stage 2 is implemented. Workers publish compact warm-pool
inventory in heartbeat metadata, grouped by function version, image, handler,
memory, and output tmpfs size. The scheduler and V2 production orchestrator now
prefer workers with an exact idle warm match before falling back to the existing
build-aware, least-loaded placement policy. The old recent-function route is no
longer used as a primary placement rule. A guarded predictive sticky fallback
has been added for testing: if no exact warm match is visible, the scheduler can
prefer the most recent exact function-version route only when that worker has no
build pressure, has invocation capacity, and is not materially more loaded than
the best candidate.

Warm-container Stage 4 is implemented without minimum warm instances. The worker
pool now tracks reuse hits, total uses, memory cost, and eviction reasons.
Eviction is usage- and pressure-aware: hot containers are preferred over cold
containers, per-function over-limit eviction removes the lowest-value idle
container for that function version, global pool pressure removes the lowest
value idle container, and optional memory pressure can evict large cold
containers first. `WORKER_WARM_MAX_MEMORY_MB=0` keeps memory-pressure eviction
disabled by default.

Warm-container Stage 4 benchmarking is documented in
`docs/warm_routing_stage4_benchmark_report.md`, with raw data in
`docs/warm_routing_benchmark_cold_baseline_2026-07-19.json`,
`docs/warm_routing_benchmark_2026-07-19.json`, and
`docs/warm_routing_benchmark_tuned_2026-07-19.json`. Predictive-sticky raw data
is stored in `docs/warm_routing_benchmark_sticky_tuned_2026-07-19.json` and
`docs/warm_routing_benchmark_sticky_guarded_2026-07-19.json`. In the tuned
two-worker run, hot sequential no-op invocations improved from 2199 ms
cold-baseline median executor time to 928 ms, and hot-after-pressure improved
from 2609 ms to 842 ms. The benchmark also showed that warm-aware routing
depends on fresh worker warm-pool metadata; the benchmark profile now uses a
2-second worker heartbeat instead of the default 10-second heartbeat. Guarded
predictive sticky is safe but not a clear performance win over the 2-second
heartbeat run, so it should remain a fallback hint.

### Orchestrator V2 Migration Foundation

Status: Steps 1-10 and 12-13 implemented; Step 14 controls ready but retirement
not activated; Step 11 status-read cutover remains

Implemented:
- Frozen and documented V1 coordination contract
- Per-job `coordination_version`, with all existing and new jobs defaulting to V1
- V1 scheduler guard that refuses accidentally queued V2 jobs
- Redis AOF persistence with a Docker-managed data volume
- Redis and backend health-gated service startup
- Scheduler and worker restart policies for Redis restart recovery
- Shadow-only V2 Redis job state machine with atomic Lua transitions for create,
  dispatch, claim, lease renewal, requeue, cancellation, dead-lettering,
  finalization, and terminal completion
- Dispatch-attempt fencing and idempotent claim/completion behavior
- Artifact-commit requirement before a V2 job can become `succeeded`
- Real-Redis integration tests for legal, illegal, duplicate, and stale
  transitions
- Transactional `job.created` outbox rows committed with their `Job`
- Idempotent outbox relay to the `orchestrator:events` Redis Stream
- Real crash-window test proving retry does not duplicate a Stream event
- Read-only shadow orchestrator with no backend dispatch or worker-queue push
- V1/V2 placement comparison suite for invocation and build decisions
- Redis worker operational records with atomic heartbeat/lease updates and
  stale-worker expiry
- V2 shadow placement reads Redis worker state
- Django worker heartbeat remains as the V1 compatibility projection
- Live three-worker verification of matching Redis and Django capacity state
- Production V2 orchestrator service with protected claim, lease-renewal, and
  completion APIs
- Atomic V2 dispatch state plus worker-Stream publication
- Dispatch and running leases with recovery and stale-attempt fencing
- Consumer-group pending-entry reclamation for creation events
- Attempt- and dispatch-specific immutable build image tags
- Artifact-commit requirement before a V2 image becomes API-visible
- Idempotent duplicate completion and projection publication
- Asynchronous PostgreSQL projector with stale-event rejection
- Worker-specific V2 build and invocation Streams
- Orphan-image detection and registry manifest cleanup
- V2 recovery ceiling and dead-letter projection
- Creation-time build and invocation pilot flags, both defaulting to off
- Two successful live V2 builds and one successful live V2 invocation
- Attempt-fenced staged invocation output upload with SHA-256 manifests
- Staged result, stdout, stderr, timing, and output metadata hidden from all
  user APIs until terminal projection
- Idempotent backend artifact commit with stable `artifact_commit_id`
- Invocation completion transfer from worker delivery to a retryable Redis
  finalization Stream
- Finalizer service that commits backend artifacts before asking the
  orchestrator for a terminal transition
- Terminal projector verification of completion ID and artifact commit ID
- 24-hour cleanup for abandoned staged artifacts
- A successful live Step 10 V2 invocation through worker, finalizer,
  orchestrator, and PostgreSQL projection
- Atomic Redis repair indexes for pre-publication finalization and terminal
  projection crash windows
- Bounded startup reconciliation for expired leases, abandoned creation
  events, finalizing jobs, and terminal projections
- Pending-entry recovery for restarted finalizer and projector consumers
- Five-minute, 100-row cross-store audit with one pipelined Redis read and
  network repair only on detected mismatches
- Indexed PostgreSQL V2 reconciliation queries
- Deterministic percentage rollout and explicit function canaries for builds
  and invocations
- Pilot booleans retained as immediate kill switches for new traffic
- Live Redis AOF restart and mixed V1/V2 canary verification
- Ordered V2 eligibility stages for internal, build, private, token, public,
  and all-new-job traffic
- Protected Redis-native monitoring for error rate, finalizing age, duplicates,
  recoveries, projection lag, and finalization lag
- V1 creation and coordination endpoint retirement switches, enabled for
  compatibility by default
- Non-destructive V1 drain readiness command using grouped SQL and one Redis
  pipeline over known queues
- Guarded V1 Redis List retirement command requiring a drained state and
  explicit confirmation
- Live internal-stage V2 canary with clean terminal and lag metrics

Not implemented yet:
- Step 11 Redis-first API status reads and terminal fallback semantics
- A sustained full-V2 soak period before actually disabling V1
- One compatibility release before deleting V1 implementation code
- Broad canary load, network-partition, and process-kill experiments

All production execution remains on coordination V1.

### Phase 5: Metrics, Logs, and Evaluation

Status: Functional local observability stack implemented

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
- Real concurrent workload test in `docs/real_workload_test_report.md`
- Invocation latency profile in `docs/invocation_latency_profile_report.md`
- Prometheus-compatible metrics endpoints for backend and userservice
- Prometheus-compatible internal metrics for orchestrator and worker
- Prometheus, Grafana, Loki, Alloy, cAdvisor, Redis exporter, and Postgres
  exporters in the Docker Compose `observability` profile
- Grafana dashboard provisioning for platform state, job state, worker load,
  warm-pool state, orchestrator lag, and recent platform errors
- Docker log collection through Alloy into Loki for platform application
  services
- Runflare mirror override for environments where Docker Hub is unavailable
- Observability usage notes in `docs/observability_stack.md`

Remaining:
- More structured application log fields and consistent request/job IDs in log
  messages
- More precise throughput, error-rate, and percentile latency metrics
- Per-function and per-owner resource metering with careful cardinality limits
- Cold-start measurements
- Alert rules for stuck finalization, unhealthy workers, queue growth, and high
  error rates
- OpenTelemetry tracing for cross-service request/job timelines
- Repeatable benchmark scripts and workloads
- Cold versus warm execution comparison
- Broader single-worker versus multi-worker evaluation
- More detailed Docker lifecycle and warm-start benchmarking
- Failure-recovery experiments
- Evaluation tables, charts, and analysis
- Final report with results, limitations, and comparison to the proposal

## Current API Surface

Available endpoints:
- `GET /health/`
- Userservice: `GET /health/`
- Userservice: `POST /api/auth/register/`
- Userservice: `POST /api/auth/token/`
- Userservice: `POST /api/auth/token/refresh/`
- Userservice: `POST /api/auth/logout/`
- Userservice: `GET /api/auth/me/`
- Userservice: `GET /api/auth/public-key/`
- Userservice: `GET /api/auth/jwks/`
- `GET|POST /api/functions/`
- `GET /api/functions/{id}/`
- `DELETE /api/functions/{id}/`
- `GET /api/functions/{id}/build-status/`
- `POST /api/functions/{id}/source/`
- `GET /api/functions/{id}/invocations/`
- `GET|POST /api/functions/{id}/tokens/`
- `GET|PATCH|DELETE /api/functions/{id}/tokens/{token_id}/`
- `POST /api/functions/{id}/tokens/{token_id}/revoke/`
- `POST /api/functions/{id}/tokens/{token_id}/rotate/`
- `GET|POST /api/functions/{id}/versions/`
- `POST /api/functions/{id}/invoke/`
- `POST /api/functions/{id}/invoke-sync/`
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
- `GET /api/invocations/{id}/download/`
- `GET /api/workers/`
- `GET /api/workers/{id}/`

Authentication notes:
- Most management endpoints require `Authorization: Bearer <jwt-access-token>`.
- `GET /api/workers/` and `GET /api/workers/{id}/` are admin-only.
- Function invocation auth is intentionally separate from JWT auth.
- Private functions require owner/admin JWT.
- Token-protected functions accept `X-Function-Token`.
- Public functions accept unauthenticated invocations.
- Function owners/admins can create, list, update, revoke, expire, and rotate
  function-scoped invocation tokens. Raw token values are returned only once on
  create or rotate; token hashes are never exposed through the API.
- Invoke responses include an invocation `read_token`; callers can use
  `X-Invocation-Read-Token` to read that one invocation and its output files.
- Invocation responses support `response_mode=simple|advanced`.
  `simple` is the default and returns only pending poll handles or terminal
  function result plus committed output download paths. `advanced` returns the
  full dashboard/operator payload, including status metadata, stdout/stderr
  previews, exit status, links, and platform fields.

Protected internal worker endpoints:
- `POST /api/internal/auth/userservice-jwks-cache/clear/`
- `GET /api/internal/builds/{build_request_id}/source/`
- `GET /api/internal/builds/{build_request_id}/state/`
- `PATCH /api/internal/builds/{build_request_id}/report/`
- `GET /api/internal/invocations/{request_id}/inputs/`
- `GET /api/internal/invocations/{request_id}/inputs/{file_id}/download/`
- `POST /api/internal/invocations/{request_id}/outputs/`
- `POST /api/internal/invocations/{request_id}/staged-outputs/`
- `POST /api/internal/invocations/{request_id}/staged-completions/{completion_id}/commit/`
- `PATCH /api/internal/invocations/{request_id}/report/`

## Verified State

Latest verification:
- Migrations applied successfully for `accounts.0001_initial` and
  `functions.0005_invoke_access_and_tokens`
- Migrations applied successfully for `workers.0002_worker_build_concurrency`,
  `functions.0006_build_limits_and_leases`, and `jobs.0001_initial`
- Migrations applied successfully for `jobs.0002_recovery_dead_letter_fields`
- Migrations applied successfully for `jobs.0003_job_coordination_version` and
  `jobs.0004_outboxevent`
- Migration applied successfully for `invocations.0004_staged_completions`
- Migrations applied successfully for `functions.0010_functionimage` and
  `functions.0011_backfill_function_images`
- Userservice migrations applied successfully through `accounts.0001_initial`
- Focused functions test suite passed: `51` tests
- Userservice account/JWT suite passed: `3` tests
- Backend account suite passed: `4` tests, including userservice RS256 JWT
  verification and shadow-owner creation
- Adjacent accounts/invocations/jobs/workers test suite passed: `81` tests
- Backend Docker app test suite passed: `133` tests
- Worker Docker test suite passed: `78` tests
- Scheduler/orchestrator test suite passed: `75` tests
- Compile check passed for backend, worker, and scheduler
- Compile check passed for userservice
- Backend and userservice migration drift checks passed: `No changes detected`
- OpenAPI/frontend-contract focused backend test run passed: `31` tests across
  backend schema docs, function create/build/source responses, invocation
  queued/result/download contract, and V2 invocation reads
- Userservice OpenAPI focused test run passed: `2` tests
- Compile checks passed for the touched backend and userservice API/docs modules
- Live schema smoke passed for `http://localhost:8000/api/schema/` and
  `http://localhost:8100/api/schema/`
- Live Swagger docs smoke passed for `http://localhost:8000/api/docs/` and
  `http://localhost:8100/api/docs/`
- Live backend schema smoke confirmed function/invocation `resource` fields and
  invocation ZIP `409` not-ready response documentation
- Parspack object-storage smoke retest passed on 2026-08-04 from inside the
  backend container: direct storage save/read/delete worked, repeated tiny
  writes worked, no recent Loki Parspack/DNS errors were found, and invocation
  log-artifact storage wrote and verified committed stdout/stderr files
- Backend CORS/auth focused test run passed: `6` tests across CORS preflight,
  OpenAPI docs, and userservice JWT compatibility
- Userservice CORS/auth focused test run passed: `8` tests across CORS
  preflight, OpenAPI docs, register/login/refresh/logout, `/me`, and JWKS
- Live browser-style CORS preflight smoke passed for backend and userservice
- Live userservice logout smoke passed at `http://localhost:8100/api/auth/logout/`
- Live userservice-to-backend auth smoke passed: userservice registered a user,
  issued an RS256 JWT, backend verified it through JWKS, created a local shadow
  account, and created function `70`
- Userservice public-key and JWKS endpoints returned an RSA `RS256` key
- User journey smoke test passed with tmpfs-backed exported output file
- Single-worker user journey smoke test passed with split queues using function
  `14`, version `21`, and invocation `24`
- Two-worker user journey smoke test passed with split queues using function
  `15`, version `22`, and invocation `25`
- Multi-worker scheduler verification documented in
  `docs/multi_worker_scheduler_test_report.md`
- Real concurrent invocation workload documented in
  `docs/real_workload_test_report.md`
- Invocation latency profiling documented in
  `docs/invocation_latency_profile_report.md`
- Real V1/V2 invocation comparison documented in
  `docs/invocation_v1_v2_comparison_report.md` with raw measurements in
  `docs/invocation_v1_v2_comparison_2026-07-02.json`: all 44 measured
  invocations succeeded and returned matching results; V2 reduced the
  12-request burst wall time by 28.9% and left finalization/projection lag at
  zero
- Orchestrator steps 5-7 verification documented in
  `docs/orchestrator_migration_steps_5_7_test_report.md`
- V2 build and invocation pilot verification documented in
  `docs/orchestrator_migration_steps_8_9_test_report.md`
- V2 staged completion verification documented in
  `docs/orchestrator_migration_step_10_test_report.md`
- V2 reconciliation and gradual-cutover verification documented in
  `docs/orchestrator_migration_steps_12_13_test_report.md`
- Ordered cutover and V1 retirement verification documented in
  `docs/orchestrator_migration_steps_13_14_test_report.md`
- Warm-container Stage 2 scheduler/orchestrator tests passed, covering exact
  warm-match routing, old recent-route removal, local warm reservations, live
  heartbeat inventory, Redis worker-state preservation, and V2 production
  dispatch to a warm worker
- Warm-container Stage 4 worker tests passed, covering hot-container survival
  under pool pressure, memory-pressure eviction, per-function over-limit
  eviction, and eviction-reason recording
- Warm-container Stage 4 real workload benchmark documented in
  `docs/warm_routing_stage4_benchmark_report.md`; all benchmark invocations
  succeeded across cold baseline, initial warm, and tuned warm runs
- Real-world milestone 6/7 integrity suite documented in
  `docs/real_world_integrity_suite_report.md`; the final accepted run used
  Parspack S3-compatible object storage and passed source replacement under
  concurrent traffic, declared output visibility, invocation read-token
  isolation, image cleanup after replacement, image cleanup after function
  deletion, and an 8-invocation concurrent burst

The backend test suite now covers:
- JWT registration, login, refresh support, and `/api/auth/me/`
- Userservice RS256 JWT issuing, refresh, logout acknowledgement, `/me`, public
  key and JWKS discovery
- Backend verification of userservice RS256 JWTs using JWKS, including shadow
  user/account creation for the current compatibility phase
- JWT-authenticated function, build, and invocation API access
- Owner isolation across functions, versions, build attempts, and invocations
- Admin-only worker-node access
- Worker internal endpoints protected by `X-Internal-Token`
- Function invocation tokens using `X-Function-Token` separately from JWT
- Function invocation-token management APIs for create, list, detail, update,
  soft revoke, expiry, rotation, last-used tracking, ownership/admin access,
  max active token limits, and no token/hash leakage
- Public, private, and token-protected invocation modes
- Durable job records for build and invocation enqueue paths
- Scheduler internal APIs for reading and dispatching queued jobs
- Worker self-registration for scheduler placement
- Worker heartbeats and stale-worker expiry
- Worker processing queue recovery
- Separate build/invocation pending queues and worker queues
- Queue-aware scheduler placement with round-robin tie-breaking
- Warm-aware invocation routing to workers with exact idle warm-container
  matches
- Build placement only on idle workers
- Worker-side invocation priority before build work
- Worker-side thread pool with bounded total/invocation/build concurrency
- Worker heartbeats report active invocation and build counts
- Worker heartbeats report live warm-container inventory
- Worker heartbeats report drain/offline status so V2 placement excludes
  draining workers
- Recovery backoff and dead-letter handling for recovered jobs
- V2 invocation retry policy, retry backoff, retry-safe completion
  idempotency, and invocation attempt history
- Dispatch blocking while a recovered job's `available_at` is still in the future
- Worker claim validation before execution
- Stale worker-report rejection using dispatch attempts
- Durable job status updates from worker build/invocation reports
- Invocation output upload validation, owner/download authorization, and
  invocation read-token authorization
- Frontend-facing invocation detail contract with `frontend_state`,
  `is_terminal`, `poll_after_seconds`, `result_available`, `can_download`,
  `can_read_outputs`, `outputs_url`, `download_url`, `links`, stdout/stderr
  previews, and no standalone user-facing log listing/download endpoints
- Frontend golden-path API contract documented for create function, upload
  source, poll build, invoke, poll invocation, read result/stdout/stderr/exit
  status, and download the invocation ZIP
- Backend and userservice OpenAPI schema/docs endpoints, including frontend
  schemas for functions, builds, invocation tokens, invocations, outputs,
  downloads, userservice auth, public keys, and JWKS
- Backend and userservice CORS middleware for configured frontend origins,
  bearer JWTs, invocation tokens, read tokens, and download headers
- Worker-side output validation for unsafe names, reserved names, file-count
  limit, per-file size limit, total-size limit, and no-upload-on-failure
- Worker tmpfs output mount, export-copy wrapper, Docker archive extraction
  from the stopped container, and no-upload-on-validation-failure behavior
- Transactional outbox rollback and Redis publication retry behavior
- Shadow orchestrator authority isolation and replay idempotency
- V1/V2 worker-placement equivalence across five policy scenarios
- Redis worker lease refresh, capacity updates, and race-safe stale expiry
- Heartbeat dual-write isolation and survival after transient transport errors
- Atomic V2 worker-Stream dispatch and pending-event recovery
- Duplicate/lost-response completion idempotency
- Build worker crash recovery and orphan-image cleanup
- Dispatch, delivery, claim, and running-transition stale-attempt fencing
- Asynchronous PostgreSQL projection and image visibility ordering
- Staged-output checksum and exact-manifest validation
- Hidden staged/committed artifacts before terminal projection
- Worker-death-after-upload behavior and staged artifact expiry
- Invocation completion/finalization lost-response idempotency
- Finalizer retry behavior after backend or orchestrator failure
- Orchestrator repair after crashes before finalization/projection publication
- Finalizer and projector pending-entry reclaim after restart
- Bounded cross-store mismatch repair and empty-audit query count
- Deterministic rollout, function canaries, and pilot kill switches
- Ordered access-tier cutover and incomplete-cutover V1 fallback rejection
- Redis-native monitoring counters and finalizing-age preservation
- V1 drain readiness and HTTP 410 retirement guards

## Important Current Limitations

- The deployment is a local Docker Compose prototype.
- There is one scheduler in local Compose; workers can be scaled with Docker
  Compose. Basic scheduler policy tests and one real concurrent invocation
  workload exist, but multi-worker failure testing is still limited.
- Runtime worker add/remove is supported for the first distributed prototype:
  workers self-register, heartbeat into Redis/orchestrator state, publish
  `draining` on shutdown, stop accepting new jobs, finish active jobs, then
  publish `offline`. See `docs/worker_scaling_operations.md`.
- A worker crash after accepting a job no longer loses the job immediately;
  stale-worker recovery requeues it from the processing queue with backoff.
- Jobs recovered too many times are moved to `dead_lettered` instead of being
  retried forever.
- The current recovery loop is coarse and heartbeat-based, so recovery is not
  instant.
- Durable jobs exist, but Redis is still the active queue transport.
- V2 build and invocation pilots are implemented. Local Compose now defaults
  both pilots to enabled and disables new V1 job creation; V1 coordination
  endpoints remain available only for compatibility while old work drains.
- V2 invocation inputs and durable artifact storage still use the backend, but
  staged artifacts remain hidden until the orchestrator receives a matching
  artifact commit and emits terminal state.
- Scheduler placement is queue-aware, build-aware, and warm-container-aware, but
  not yet capability-aware by runtime, memory class, CPU, cached image without a
  warm container, or supported runtime.
- Warm-aware scheduling currently learns warm-pool inventory through periodic
  worker heartbeats. The benchmark profile uses a faster heartbeat, but a better
  production design would publish small warm-pool updates immediately after
  container release.
- **`warm_pool_release_ms` is the time spent handing a warm container back to
  the warm pool after an invocation finishes. If it grows, the cleanup/reuse
  path is the bottleneck, not user code.**
- Guarded predictive sticky routing is implemented for testing, but benchmark
  results do not justify using it as the main warm-routing mechanism.
- Only Python image builds are currently implemented.
- Source bundles are retained forever by policy.
- Invocation inputs, outputs, and logs currently expire with the invocation
  after 7 days through cleanup commands.
- Function image replacement now has a safe active-version switch-over flow;
  registry deletion is scheduled through the `FunctionImage` ledger and run by
  `cleanup_function_images`.
- `/sandbox/output` is memory-backed tmpfs, so large declared outputs compete
  with function memory and should stay small in this prototype.
- The worker requires access to the Docker socket.
- Userservice now signs JWTs with RS256. The dev private key is persisted in a
  Docker volume; production still needs managed signing keys, rotation policy,
  and rollout procedure.
- The serverless backend still has a temporary local `accounts` app and accepts
  old local SimpleJWT tokens for compatibility. This should be retired after
  clients move to userservice-issued tokens.
- Serverless ownership still uses local shadow users and foreign keys during
  this bridge phase. The next identity migration should store userservice
  subjects directly on owned resources.
- Function invocation-token management APIs exist, but they do not yet have
  per-token usage analytics beyond `last_used_at`.
- There is no rate limiting for JWT-authenticated, token-based, or public invocations.
- Cleanup policy now exists for expired invocations, dead-letter jobs, and
  superseded function images.
- There is no production UI, dashboard, CI pipeline, or deployment manifest.

## Remaining Work in Recommended Order

### Priority 1: Complete Invocation Artifacts and Reliability

1. Add output MIME allow-listing if output content-type restrictions are needed.
2. Add any remaining frontend-driven export controls beyond the existing
   invocation ZIP download.
3. Decide later whether larger outputs need direct object-storage upload.
4. Add invocation cancellation.
5. Add admin/global defaults for invocation retry policy if per-version policy
   is not enough.
6. Make scheduler dispatch more strongly idempotent and duplicate-safe.

### Priority 2: Make Workers Truly Distributed

7. Report richer worker capabilities, including runtimes, memory classes, CPU,
   cached images, and supported runtime variants.
8. Route jobs to suitable workers using those capabilities.
9. Expand graceful shutdown testing to real multi-worker restart/drain
   scenarios, including remote workers stopped over SSH.
10. Test multiple workers and worker-failure scenarios.

### Priority 3: Security and Resource Isolation

11. Add rate limits for JWT-authenticated, token-based, and public invocations.
12. Add password reset and email verification if account UX remains in this backend.
13. Add CPU, process, disk, and output quotas.
14. Use a read-only function root filesystem where possible.
15. Add secret/environment-variable management for functions.
16. Plan an alternative to unrestricted Docker-socket access.
17. Add dependency and image scanning.

### Priority 4: Performance and Observability

18. Publish small warm-pool inventory updates immediately after container
    release, instead of relying only on periodic full heartbeats.
19. Add percentile latency histograms and explicit cold-start counters.
20. Add structured request/job IDs to platform logs.
21. Add operational alert rules on top of the new Grafana/Prometheus stack.
22. Consider proactive prewarming later if project scope expands.
23. Add scheduled cleanup runners for the existing cleanup commands.

### Priority 5: Evaluation and Project Completion

24. Add CI for backend, worker, and scheduler tests.
25. Create repeatable benchmark workloads.
26. Run performance, scaling, and failure-recovery experiments.
27. Analyze results against the proposal goals.
28. Write the final report, limitations, and future-work sections.

## Recommended Next Milestone

The next milestone should be:

`invocation download bundle and rate limits`

Function replacement, active-image promotion, object-storage-backed logs,
expired-invocation cleanup, dead-letter cleanup, and registry-image cleanup are
now in place for the prototype. The next practical product milestone should make
the platform easier and safer to use: add an invocation ZIP download containing
manifest, inputs, outputs, and logs, then add rate limits for JWT-authenticated,
token-based, and public invocation traffic.

Before exposing token-protected or public functions to real users, add rate
limits and basic abuse controls.
