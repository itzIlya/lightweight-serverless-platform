# Real Workload Test Report

Date: 2026-06-26

This report documents the first real concurrent workload pass after adding
multithreaded workers.

## Test Environment

- Docker Compose stack
- One backend service
- One scheduler service
- Three worker containers
- Worker settings:
  - `WORKER_MAX_CONCURRENCY=4`
  - `WORKER_MAX_INVOCATION_CONCURRENCY=4`
  - `WORKER_MAX_BUILD_CONCURRENCY=1`
- Redis queue transport
- Local Docker registry

Stack check:

```powershell
docker compose ps
```

Result: backend, scheduler, Redis, Postgres, registry, and three workers were
running.

## Workload Script

Added:

```text
scripts/concurrent_invocation_workload.py
```

The script performs a real user flow:

1. Register a user and receive JWT auth.
2. Create a private function.
3. Upload a Python function bundle.
4. Queue and complete a real Docker image build.
5. Submit N invocations concurrently through the public user API.
6. Poll invocation APIs until all invocations reach a terminal state.
7. Write a JSON summary.

The test function sleeps for the requested number of seconds and returns a JSON
result. This makes concurrency easy to see: 12 invocations with a 3 second sleep
would take at least 36 seconds if processed strictly one at a time.

Reproduce:

```powershell
python .\scripts\concurrent_invocation_workload.py `
  --base-url http://localhost:8000 `
  --count 12 `
  --sleep-seconds 3 `
  --output-json .\docs\concurrent_invocation_workload_final.json
```

## Initial Workload Result

Command:

```powershell
python .\scripts\concurrent_invocation_workload.py `
  --base-url http://localhost:8000 `
  --count 12 `
  --sleep-seconds 3 `
  --output-json .\docs\concurrent_invocation_workload_latest.json
```

Result:

| Metric | Value |
| --- | ---: |
| Invocations | 12 |
| Sleep per invocation | 3 seconds |
| Sequential sleep baseline | 36 seconds |
| Client submit time | 0.547 seconds |
| Client wall time | 21.188 seconds |
| Statuses | `succeeded` |
| Min worker duration | 5380 ms |
| Median worker duration | 7364 ms |
| Max worker duration | 8104 ms |

Internal worker assignment:

| Worker | Invocation count |
| --- | ---: |
| `31ccdbeea114` | 7 |
| `d2b25faa7a07` | 5 |
| `b768523affa2` | 0 |

Finding: correctness was good, but placement was not using all online workers.
The scheduler could dispatch a burst faster than worker heartbeat metadata could
show the new active jobs, so it underestimated immediate worker load.

## Scheduler Fix

Added scheduler-side recent dispatch load tracking.

Before the fix, scheduling load was mostly:

```text
worker active jobs from heartbeat + Redis queue length
```

That misses very recent dispatches when workers remove queue items before the
next heartbeat.

After the fix, invocation scheduling uses:

```text
worker active jobs from heartbeat + max(Redis queued invocations, local recent dispatches)
```

The local recent dispatch count is short-lived and exists only inside the
scheduler process. It does not change the durable job source of truth.

Added scheduler tests:

- `test_choose_invocation_worker_uses_local_dispatch_load_for_bursts`
- `test_choose_invocation_worker_does_not_stick_to_locally_loaded_worker`

## Final Workload Result

Command:

```powershell
python .\scripts\concurrent_invocation_workload.py `
  --base-url http://localhost:8000 `
  --count 12 `
  --sleep-seconds 3 `
  --output-json .\docs\concurrent_invocation_workload_final.json
```

Result:

| Metric | Value |
| --- | ---: |
| Invocations | 12 |
| Sleep per invocation | 3 seconds |
| Sequential sleep baseline | 36 seconds |
| Client submit time | 0.437 seconds |
| Client wall time | 17.703 seconds |
| Statuses | `succeeded` |
| Min worker duration | 5675 ms |
| Median worker duration | 6490 ms |
| Max worker duration | 7418 ms |

Internal worker assignment:

| Worker | Invocation count |
| --- | ---: |
| `d2b25faa7a07` | 5 |
| `b768523affa2` | 4 |
| `31ccdbeea114` | 3 |

The final run used all three workers and improved wall time from 21.188 seconds
to 17.703 seconds for the same workload shape.

## Queue Cleanup Check

Command:

```powershell
docker compose exec backend python manage.py shell -c `
  "import os, redis; r=redis.Redis.from_url(os.environ.get('REDIS_URL','redis://redis:6379/0'), decode_responses=True); keys=sorted(r.scan_iter('*')); interesting=[k for k in keys if any(part in k for part in ['scheduler-pending','worker:'])]; print({k:r.llen(k) for k in interesting if r.type(k)=='list'})"
```

Result:

```text
{}
```

No scheduler pending queues, worker invocation/build queues, or worker
processing queues were left with stuck messages after the workload.

## Regression Tests

Commands:

```powershell
docker compose exec scheduler python -m unittest discover -s scheduler -p test_*.py -v
docker compose exec backend python manage.py test apps.accounts apps.functions apps.invocations apps.jobs apps.workers
docker compose exec worker python -m unittest discover -s worker -p test_*.py -v
docker compose exec backend python manage.py makemigrations --check --dry-run
```

Results:

| Suite | Result |
| --- | --- |
| Scheduler tests | 19 passed |
| Backend tests | 60 passed |
| Worker tests | 46 passed |
| Migration check | No changes detected |

## Current Assessment

The platform now passes a real concurrent workload:

- real API calls
- real authentication
- real function upload
- real Docker image build
- real scheduler placement
- real worker queue consumption
- real Docker invocation execution
- real invocation polling
- real Redis cleanup verification

The behavior is correct: all invocations succeeded and no queue messages were
left stuck.

Performance is improved but not optimal. The 12 invocations did not finish near
the theoretical 3-8 second range because each invocation still pays heavy Docker
execution overhead. The next performance work should focus on warm containers,
image/cache awareness, and measuring Docker start/pull overhead separately from
function runtime.
