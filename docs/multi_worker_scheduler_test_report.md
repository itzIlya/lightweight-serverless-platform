# Multi-Worker Scheduler Test Report

Date: 2026-06-26

This report documents the tests run after adding split build/invocation queues
and multi-worker scheduler placement.

## Scheduling Rules Under Test

The intended behavior is:

1. Builds and invocations enter separate scheduler queues:
   - `scheduler-pending-builds`
   - `scheduler-pending-invocations`
2. Each worker has separate input queues:
   - `worker:<name>:builds`
   - `worker:<name>:invocations`
3. Each worker keeps one shared processing queue:
   - `worker:<name>:processing`
4. Workers check invocation work before build work.
5. Scheduler uses short recent-function affinity for invocations when safe.
6. Scheduler avoids workers with active builds for invocations.
7. Scheduler sends builds only to idle workers.
8. Scheduler uses round-robin as a tie-breaker.

## Deterministic Unit Tests

Command:

```powershell
docker compose exec scheduler python -m unittest discover -s scheduler -p test_*.py -v
```

Result:

```text
17 tests, OK
```

Covered scheduler conditions:

| Test area | What it proves |
| --- | --- |
| Round-robin tie-breaker | Equal workers rotate instead of always choosing the first name. |
| Recent invocation affinity | A recently used light worker is reused for the same function version. |
| Expired affinity | Affinity older than the TTL is ignored. |
| Overloaded affinity | A recent worker is ignored when its invocation load is too high. |
| Active build avoidance | Invocation placement avoids workers currently building. |
| Build-queue avoidance | Invocation placement prefers workers with no queued builds. |
| All workers building | Invocation placement returns no worker rather than knowingly queueing behind builds. |
| Build placement | Builds go only to idle workers. |
| Build placement with no idle worker | Build placement returns no worker. |
| Dispatch queue selection | Build jobs are delivered to `worker:<name>:builds`. |
| Recovery queue selection | Recovered jobs go back to the matching scheduler pending queue. |
| Dead-letter recovery | Dead-lettered jobs are removed from processing and not requeued. |

Worker priority tests:

```powershell
docker compose exec worker python -m unittest discover -s worker -p test_*.py -v
```

Result:

```text
42 tests, OK
```

Covered worker conditions:

| Test area | What it proves |
| --- | --- |
| Split queue processing name | `invocations` and `builds` share the same worker processing queue. |
| Invocation priority | Worker checks invocation queue before build queue. |
| Build fallback | Worker checks build queue when invocation queue is empty. |
| Activity accounting | Worker heartbeat can report active jobs and active builds. |
| Existing execution tests | Build, invocation output, sandbox, and ACK behavior still pass. |

Backend tests:

```powershell
docker compose exec backend python manage.py test apps.accounts apps.functions apps.invocations apps.jobs apps.workers
```

Result:

```text
60 tests, OK
```

Migration drift:

```powershell
docker compose exec backend python manage.py makemigrations --check --dry-run
```

Result:

```text
No changes detected
```

## Live Docker Tests

### Test 1: One Worker Baseline

Setup:

```powershell
docker compose up -d --scale worker=1
```

After waiting for stale worker expiry, the backend worker registry showed one
online worker:

```text
e89ae35d78f6
```

Smoke command:

```powershell
python scripts\user_journey_smoke.py --base-url http://localhost:8000
```

Result:

```text
SMOKE TEST PASSED
function_id=16
version_id=23
invocation_id=26
```

Observed durable job assignment:

| Job | Status | Queue | Worker |
| --- | --- | --- | --- |
| Build | `succeeded` | `worker:e89ae35d78f6:builds` | `e89ae35d78f6` |
| Invocation | `succeeded` | `worker:e89ae35d78f6:invocations` | `e89ae35d78f6` |

Conclusion:

The single-worker path still works, and build/invocation jobs use the correct
split worker queues.

### Test 2: Two Workers

Setup:

```powershell
docker compose up -d --scale worker=2
```

Online workers:

```text
e2c711781095
e89ae35d78f6
```

Smoke command:

```powershell
python scripts\user_journey_smoke.py --base-url http://localhost:8000
```

Result:

```text
SMOKE TEST PASSED
function_id=17
version_id=24
invocation_id=27
```

Observed durable job assignment:

| Job | Status | Queue | Worker |
| --- | --- | --- | --- |
| Build | `succeeded` | `worker:e89ae35d78f6:builds` | `e89ae35d78f6` |
| Invocation | `succeeded` | `worker:e89ae35d78f6:invocations` | `e89ae35d78f6` |

Conclusion:

The two-worker stack handled build and invocation successfully. The sequential
smoke flow assigned both jobs to one suitable worker, which is allowed by the
current policy. Distribution across equally suitable workers is covered by the
round-robin unit tests.

### Test 3: Three Workers

Setup:

```powershell
docker compose up -d --scale worker=3
```

Online workers:

```text
877a2fcb7aed
e2c711781095
e89ae35d78f6
```

Smoke command:

```powershell
python scripts\user_journey_smoke.py --base-url http://localhost:8000
```

Result:

```text
SMOKE TEST PASSED
function_id=18
version_id=25
invocation_id=28
```

Observed durable job assignment:

| Job | Status | Queue | Worker |
| --- | --- | --- | --- |
| Build | `succeeded` | `worker:e89ae35d78f6:builds` | `e89ae35d78f6` |
| Invocation | `succeeded` | `worker:e89ae35d78f6:invocations` | `e89ae35d78f6` |

Conclusion:

The three-worker stack handled the full upload-build-invoke-output-download
flow successfully. All online workers registered with distinct names and
worker-specific queues.

## Observations

The scheduler logs showed a short window after worker recreation/scaling where
it reported:

```text
no online workers available; requeueing job_id=...
```

This did not lose jobs. The scheduler requeued them and later dispatched them
once worker registration/heartbeat state caught up. This is acceptable for the
prototype, but later we may want a cleaner startup readiness gate or faster
registration confirmation.

## Current Confidence

The current implementation passes:

- deterministic scheduler policy tests
- worker queue-priority tests
- backend enqueue/status tests
- one-worker live smoke
- two-worker live smoke
- three-worker live smoke

The remaining gap is not basic correctness; it is load behavior. We should later
add a burst/stress test that fires many invocations and builds concurrently, then
checks distribution, latency, and queue depths over time.
