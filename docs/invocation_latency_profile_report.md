# Invocation Latency Profile Report

Date: 2026-06-26

This report measures where invocation time is spent. It focuses only on
invocation, not build latency.

## Instrumentation Added

Worker-side timing logs were added around invocation execution. These logs are
keyed by `request_id` and are not returned to the user function result.

Added:

- `ExecutionResult.timing_ms`
- executor phase timing logs in `worker/executor.py`
- worker report timing logs in `worker/worker.py`
- profiling script: `scripts/invocation_latency_profile.py`

The profiling script uses normal user-facing APIs for register, upload, build,
invoke, and poll. It then reads worker logs to attach internal phase timings to
the matching invocation request IDs.

Reproduce:

```powershell
python .\scripts\invocation_latency_profile.py `
  --base-url http://localhost:8000 `
  --output-json .\docs\invocation_latency_profile_latest.json
```

## Test Scenarios

The profiling function does no file output. It optionally sleeps inside the user
handler and returns its own measured user-code duration.

Scenarios:

| Scenario | Count | Sleep | Concurrency |
| --- | ---: | ---: | ---: |
| `noop_sequential` | 5 | 0s | 1 |
| `one_second_sequential` | 5 | 1s | 1 |
| `three_second_concurrent` | 12 | 3s | 12 |

## API and Database Timing Summary

These timings come from client measurements and persisted invocation timestamps.

| Scenario | Client Wall | Queue -> Started Median | Worker Duration Median | User Code Median | Worker Overhead Median |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noop_sequential` | 15030 ms | 376 ms | 1863 ms | 0 ms | 1863 ms |
| `one_second_sequential` | 23812 ms | 390 ms | 2531 ms | 1000 ms | 1531 ms |
| `three_second_concurrent` | 23468 ms | 8589 ms | 6502 ms | 3000 ms | 3502 ms |

Interpretation:

- Normal sequential queue/scheduler/worker-pickup latency is small: around
  376-390 ms median.
- Even a no-op function has around 1.8 seconds median worker-side overhead.
- Under a 12-invocation burst, queue-to-start time becomes the largest delay:
  8589 ms median and 15712 ms max.
- The concurrent 3-second case spends about 3.5 seconds median inside the
  worker beyond user code.

## Worker Phase Timing Summary

These timings come from worker logs.

### Sequential No-Op

| Phase | Median |
| --- | ---: |
| Sandbox preparation | 59 ms |
| Docker volume create | 24 ms |
| Docker container create | 158 ms |
| Docker input copy | 86 ms |
| Docker container start | 311 ms |
| Docker wait | 1065 ms |
| Docker logs read | 54 ms |
| Docker export copy | 69 ms |
| Docker cleanup | 117 ms |
| Backend running report | 84 ms |
| Backend final report | 138 ms |
| Executor duration | 1863 ms |
| Worker process total | 2215 ms |

Main point: Docker lifecycle dominates no-op invocation time. The largest single
phase is `docker_wait_ms`, but that includes runner startup, user code, output
copy inside the container, and the executor's current 500 ms polling interval.

### Sequential 1-Second Sleep

| Phase | Median |
| --- | ---: |
| Sandbox preparation | 50 ms |
| Docker container create | 234 ms |
| Docker input copy | 67 ms |
| Docker container start | 265 ms |
| Docker wait | 1691 ms |
| Docker cleanup | 177 ms |
| Backend running report | 86 ms |
| Backend final report | 82 ms |
| Executor duration | 2531 ms |
| Worker process total | 2924 ms |

Main point: the platform adds around 1.5 seconds median beyond a 1-second user
function. One run was an outlier with a 7819 ms worker duration, caused mostly
by `docker_wait_ms` reaching 6891 ms. That looks like Docker host contention or
a transient Docker delay, not application logic.

### Concurrent 3-Second Burst

| Phase | Median |
| --- | ---: |
| Sandbox preparation | 419 ms |
| Docker volume create | 75 ms |
| Docker container create | 581 ms |
| Docker input copy | 169 ms |
| Docker container start | 564 ms |
| Docker wait | 4390 ms |
| Docker logs read | 138 ms |
| Docker export copy | 137 ms |
| Docker cleanup | 202 ms |
| Backend running report | 445 ms |
| Backend final report | 172 ms |
| Executor duration | 6502 ms |
| Worker process total | 7300 ms |

Main point: concurrent Docker work is much more expensive than sequential Docker
work on this local host. Container create/start, sandbox prep, input copy, and
backend reports all slow down under load. The function sleeps for 3000 ms, but
the median worker executor duration is 6502 ms.

## Burst Placement

The 12-invocation burst was assigned across workers like this:

| Worker | Invocation Count |
| --- | ---: |
| `68d81e1c1e3d` | 6 |
| `f2027896c45d` | 3 |
| `34052c2de68d` | 3 |

This is a useful finding. The scheduler now uses all workers, but burst
placement is still not even enough. One worker received 6 jobs even though the
configured per-worker invocation concurrency is 4. That creates queue delay
inside that worker while other workers receive fewer jobs.

## Queue Cleanup Check

After the profiling workload:

```text
{}
```

No scheduler pending queues, worker queues, or processing queues were left with
stuck messages.

## Regression Tests

| Suite | Result |
| --- | --- |
| Worker tests | 46 passed |
| Scheduler tests | 19 passed |
| Backend tests | 60 passed |
| Migration check | No changes detected |

## Conclusions

The main invocation overheads are:

1. Docker lifecycle overhead for every invocation.
   Even no-op functions take around 1.8 seconds inside the worker.

2. Docker wait behavior.
   `_wait_for_exit` currently polls Docker every 500 ms. That can add delay and
   makes very short functions look worse. It also hides exactly how much of
   `docker_wait_ms` is Python runner startup versus polling delay.

3. Docker daemon contention under concurrency.
   In the 12-call burst, Docker create/start/wait and sandbox work all became
   slower. The host is doing a lot of container lifecycle work at once.

4. Burst scheduling is still imperfect.
   The scheduler uses all workers, but one worker still received too many jobs.
   This explains much of the 8589 ms median queue-to-start delay in the burst.

Backend API/report overhead exists but is not the largest problem. It becomes
more visible under concurrency, but Docker lifecycle and burst placement are the
dominant issues.

## Recommended Next Experiments

1. Replace the 500 ms container polling loop with Docker's blocking wait API or
   a much smaller polling interval.
2. Run the same profile with `WORKER_MAX_INVOCATION_CONCURRENCY=1`, `2`, and `4`
   to find the best local Docker throughput point.
3. Improve scheduler reservations so it never sends more than available
   invocation capacity to a worker during a burst.
4. Add warm-container reuse for Python functions.
5. Store invocation timing metrics in the database or a metrics sink instead of
   relying on log parsing.
