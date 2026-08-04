# V2 Steps 4-5 Status Read And Canary Test Report

Date: 2026-07-20

## Scope

This report covers the next correctness checkpoint after adding the V2
Redis-first invocation read path:

1. Step 4: deterministic backend tests for V2 status/result/output reads.
2. Step 5: live V1/V2 canary with real API calls, scheduler, orchestrator,
   workers, finalizer, projector, Redis, PostgreSQL, and Docker execution.

The goal of this checkpoint was correctness, not tuning.

## Code Under Test

- `backend/apps/invocations/v2_reads.py`
  - Reads the V2 job state from Redis.
  - Overlays active V2 statuses onto `GET /api/invocations/{id}/`.
  - Publishes terminal results only after the backend has committed the matching
    staged completion.
  - Keeps staged outputs invisible until the Redis terminal state and committed
    backend artifact agree.
  - Falls back to projected PostgreSQL state if Redis state is absent or
    unavailable.

- `backend/apps/invocations/views.py`
  - Uses the V2 read adapter for invocation detail reads.
  - Uses the same publication rule for output listing and output download.

- `backend/apps/invocations/test_v2_reads.py`
  - Adds focused tests for Redis active status, committed terminal result reads,
    hidden staged outputs, read-token output access, and PostgreSQL fallback.

## Environment

Docker Compose services were already running with three workers:

- `backend`: healthy
- `redis`: healthy
- `postgres`: running
- `scheduler`: running
- `orchestrator`: healthy
- `invocation-finalizer`: running
- `orchestrator-projector`: running
- `worker`: 3 replicas running

After the canary, the backend was restored to the normal V1-default state:

```text
V2_BUILD_PILOT_ENABLED=false
V2_INVOCATION_PILOT_ENABLED=false
V1_JOB_CREATION_ENABLED=true
V1_COORDINATION_ENDPOINTS_ENABLED=true
V2_CUTOVER_STAGE=private
V2_INVOCATION_ROLLOUT_PERCENT=100
```

The rollout percentage remains configured at 100, but it is inactive while the
V2 invocation pilot flag is false.

## Commands Run

```powershell
docker compose ps
docker compose exec backend python manage.py test apps.invocations apps.jobs
docker compose exec backend python manage.py makemigrations --check --dry-run
python scripts\invocation_v1_v2_comparison.py --base-url http://localhost:8000 --output-json docs\invocation_v1_v2_status_reads_canary_2026-07-20.json
docker compose exec backend python manage.py shell -c "from django.conf import settings; print({...})"
docker compose exec backend python manage.py test apps.accounts apps.functions apps.invocations apps.workers apps.jobs
```

Raw live canary data:

- `docs/invocation_v1_v2_status_reads_canary_2026-07-20.json`

## Step 4: Backend Correctness Tests

### Focused Invocation And Job Tests

Result:

```text
Found 64 test(s).
Ran 64 tests in 3.361s
OK
```

This covered:

- V2 active Redis status overriding stale PostgreSQL state.
- Redis `dispatched` being exposed to users as `running`.
- Redis `running` being exposed as `running`.
- Redis `finalizing` remaining non-terminal from the user perspective.
- Terminal V2 results becoming visible only after artifact commit.
- Staged output files remaining invisible while uncommitted.
- Mismatched `artifact_commit_id` keeping results hidden.
- Invocation read-token access to committed V2 outputs.
- Fallback to PostgreSQL when Redis state is missing.
- Existing staging, commit, output visibility, ownership, token, and job rollout
  behavior.

### Broad Backend Regression Suite

Result:

```text
Found 94 test(s).
Ran 94 tests in 5.890s
OK
```

This confirms the new read path did not break accounts, functions,
invocations, workers, or jobs.

### Migration Check

Result:

```text
No changes detected
```

No database migration was needed for this checkpoint.

## Step 5: Live V1/V2 Canary

The live canary built one function version and executed both protocols through
the same scenarios:

| Scenario | Count | Function behavior | Client concurrency |
| --- | ---: | --- | ---: |
| `noop_sequential` | 5 | immediate return | 1 |
| `one_second_sequential` | 5 | sleeps 1 second | 1 |
| `three_second_concurrent` | 12 | sleeps 3 seconds | 12 |

Correctness result:

| Check | V1 | V2 |
| --- | --- | --- |
| Invocations completed | 22 / 22 | 22 / 22 |
| Final statuses | `succeeded` only | `succeeded` only |
| Results matched expected payloads | yes | yes |
| Coordination versions | `[1]` | `[2]` |
| Recovery count | 0 | 0 |

V2 orchestrator metrics during the canary:

| Metric | Delta |
| --- | ---: |
| `terminal_succeeded` | 22 |
| `terminal_failed` | 0 |
| `duplicate_dispatches` | 0 |
| `duplicate_claims` | 0 |
| `duplicate_completions` | 0 |
| `duplicate_finalizations` | 0 |
| `recovery_count` | 0 |

This is the important correctness signal: every V2 invocation reached a terminal
success through the orchestrator/finalizer path, and no duplicate or recovery
path was triggered.

## Live Timing Summary

These numbers are from the same canary run. They should be read as local Docker
Desktop measurements, not production performance numbers.

### Client Wall Time

| Scenario | V1 wall | V2 wall | Change |
| --- | ---: | ---: | ---: |
| `noop_sequential` | 14,813 ms | 9,764 ms | V2 faster by 34.1% |
| `one_second_sequential` | 16,952 ms | 14,891 ms | V2 faster by 12.2% |
| `three_second_concurrent` | 30,953 ms | 23,031 ms | V2 faster by 25.6% |

### Median End-To-End Per Invocation

Measured from API enqueue time to terminal result.

| Scenario | V1 median queued-to-finished | V2 median queued-to-finished |
| --- | ---: | ---: |
| `noop_sequential` | 1,920 ms | 1,464 ms |
| `one_second_sequential` | 2,596 ms | 2,573 ms |
| `three_second_concurrent` | 19,846 ms | 19,376 ms |

The end-to-end user-facing medians were equal or better for V2 in this run.

### Median Queue-To-Started

| Scenario | V1 | V2 |
| --- | ---: | ---: |
| `noop_sequential` | 352 ms | 170 ms |
| `one_second_sequential` | 246 ms | 310 ms |
| `three_second_concurrent` | 11,404 ms | 566 ms |

The biggest V2 win is scheduling/admission under concurrent pressure. The V2
orchestrator gets jobs into worker execution much earlier than the V1 path in
this particular run.

### Median Worker/Executor Duration

| Scenario | V1 | V2 |
| --- | ---: | ---: |
| `noop_sequential` | 1,249 ms | 1,074 ms |
| `one_second_sequential` | 2,174 ms | 2,095 ms |
| `three_second_concurrent` | 7,352 ms | 12,929 ms |

The concurrent executor duration is still worse for V2. This is not a correctness
failure, but it remains a tuning issue. In this run the V2 concurrent path spent
more time in Docker export/copy, sandbox preparation, warm container creation,
warm runner execution, and warm cleanup under host contention.

## Read-Path Correctness Interpretation

The new read path obeys the consistency model we wanted:

1. If a V2 job is active in Redis, the API can show the fresh active state even
   if PostgreSQL projection has not caught up.
2. If a V2 job is terminal in Redis but backend artifacts are not committed, the
   API does not expose the result or output files.
3. If Redis says terminal and the backend has a committed matching completion,
   the API can expose the terminal result and output files before waiting for
   PostgreSQL projection.
4. If Redis is unavailable or has no state for that job, the API falls back to
   PostgreSQL. This keeps projected terminal reads working.

The live canary repeatedly polled the public invocation detail endpoint and saw
normal user-facing transitions: `queued`, `running`, and `succeeded`. V2 jobs
were confirmed to use coordination version 2 and all returned correct results.

## What Was Not Tested In This Run

These are still important, but they are outside this checkpoint:

- Live Redis outage during an active read.
- Live projector outage during a V2 terminal read.
- Live finalizer outage while a job is stuck in `finalizing`.
- Process-kill tests at every V2 boundary.
- Long soak with V2 enabled for all new jobs.

The unit tests cover Redis-missing fallback and staged-output hiding, but the
live chaos/failure tests should still be run before retiring V1.

## Verdict

Step 4 passed.

Step 5 passed for correctness. The V2 path completed all 22 live canary
invocations successfully, produced matching results, used coordination version
2, and recorded no duplicate/recovery anomalies.

Performance still needs tuning, especially V2 concurrent worker execution under
Docker Desktop contention, but correctness is intact.
