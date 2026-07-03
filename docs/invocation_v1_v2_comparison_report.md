# V1 and V2 Invocation Comparison

Date: 2026-07-02

## Purpose

This benchmark compares the original V1 coordination path with the V2
orchestrator protocol under a real Docker workload. Both protocols invoked the
same function version and immutable image on the same three-worker local Docker
Desktop stack.

Raw measurements are in `invocation_v1_v2_comparison_2026-07-02.json`.

## Workload

| Scenario | Requests | User work | Client concurrency |
|---|---:|---:|---:|
| No-op sequential | 5 | 0 seconds | 1 |
| One-second sequential | 5 | 1 second sleep | 1 |
| Three-second concurrent | 12 | 3 second sleep | 12 |

The harness built the profiling function once under V1, ran all V1 scenarios,
recreated only the backend with private invocation rollout set to 100% V2, and
ran the same scenarios again. It restored the backend to V1 afterward.

## Correctness Gate

| Check | V1 | V2 |
|---|---:|---:|
| Measured invocations | 22 | 22 |
| All terminal statuses succeeded | Yes | Yes |
| All returned results matched inputs | Yes | Yes |
| Observed coordination version | 1 only | 2 only |
| Benchmark-job recoveries | 0 | 0 |
| Duplicate dispatch/claim/completion/finalization delta | N/A | 0 |
| Finalization lag after run | N/A | 0 |
| Projection lag after run | N/A | 0 |

The global V2 recovery metric increased by two during the run, but every one of
the 22 measured V2 jobs recorded `recovery_count=0`. Those two recoveries belong
to other stale jobs in the persistent test environment and are not benchmark
failures.

## End-to-End Results

All latency values below are medians except wall time and throughput.

| Scenario | Protocol | Wall time | Throughput | Queue to start | Worker executor | Queue to terminal |
|---|---|---:|---:|---:|---:|---:|
| No-op sequential | V1 | 57.08 s | 0.088/s | 1.51 s | 7.06 s | 9.18 s |
| No-op sequential | V2 | 54.14 s | 0.092/s | 0.64 s | 7.70 s | 9.94 s |
| One-second sequential | V1 | 60.75 s | 0.082/s | 1.05 s | 9.56 s | 11.47 s |
| One-second sequential | V2 | 58.95 s | 0.085/s | 0.59 s | 8.75 s | 10.90 s |
| Three-second concurrent | V1 | 87.55 s | 0.137/s | 38.44 s | 16.86 s | 58.59 s |
| Three-second concurrent | V2 | 62.23 s | 0.193/s | 1.25 s | 30.37 s | 47.16 s |

V2 reduced total wall time by 5.1%, 3.0%, and 28.9% respectively. Its largest
gain was dispatch: median queue-to-start fell 57.8%, 44.0%, and 96.8%.

The concurrent V2 executor median was 80.1% slower than V1. This is not V2
coordination time. V2 released all 12 jobs to the three workers quickly, causing
much heavier simultaneous Docker Desktop activity. V1 left requests queued for
much longer, indirectly throttling Docker.

## Worker Phase Medians

### Sequential One-Second Function

| Phase | V1 | V2 |
|---|---:|---:|
| Sandbox preparation | 187 ms | 220 ms |
| Docker volume create | 214 ms | 193 ms |
| Docker container create | 1,933 ms | 1,567 ms |
| Docker input copy | 478 ms | 448 ms |
| Docker container start | 1,490 ms | 1,201 ms |
| Docker wait | 3,617 ms | 3,393 ms |
| Docker logs read | 896 ms | 606 ms |
| Docker export copy | 309 ms | 389 ms |
| Docker cleanup | 640 ms | 890 ms |
| Runner module imports | 1,837 ms | 1,644 ms |
| Runner handler work | 1,000 ms | 1,000 ms |
| V1 backend running report | 288 ms | 0 ms |
| V1 backend final report | 284 ms | 0 ms |
| V2 orchestrator claim | 0 ms | 38 ms |
| V2 orchestrator completion | 0 ms | 61 ms |
| V2 finalizer total | N/A | 332 ms |

For this low-contention scenario, replacing two backend reports with the V2
claim/completion path reduced direct worker coordination from 572 ms to 99 ms.
V2 then spent a median 332 ms finalizing asynchronously. The worker had already
transferred durable completion responsibility before that finalization step.

### Concurrent Three-Second Function

| Phase | V1 | V2 |
|---|---:|---:|
| Sandbox preparation | 1,577 ms | 3,074 ms |
| Docker container create | 2,831 ms | 5,681 ms |
| Docker container start | 2,356 ms | 5,758 ms |
| Docker wait | 6,733 ms | 10,578 ms |
| Docker logs read | 1,184 ms | 1,715 ms |
| Docker cleanup | 1,062 ms | 1,486 ms |
| Runner module imports | 2,436 ms | 4,877 ms |
| Runner handler work | 3,001 ms | 3,006 ms |
| V1 backend running + final reports | 3,512 ms | 0 ms |
| V2 orchestrator claim + completion | 0 ms | 381 ms |
| V2 finalizer total | N/A | 1,797 ms |

The user handler remained accurate at about three seconds. The extra V2 worker
time came primarily from Docker create/start/wait and Python import slowdown
under genuine concurrency, not from Redis orchestration.

## Interpretation

V2 passed the functional equivalence gate and materially improved admission and
dispatch throughput. It also removed PostgreSQL-backed running and completion
reports from the worker's critical path. V2 coordination was small relative to
container execution: 99 ms median sequentially and 381 ms during the burst.

The local Docker runtime is still the dominant bottleneck. Faster dispatch can
make per-request execution latency worse when too many cold containers contend
for the same host. The next performance control should therefore be explicit
per-worker execution concurrency or resource-aware admission, while preserving
V2's fast orchestration path.

The run verified that terminal projection lag returned to zero, but the raw
projector log collector did not capture per-event PostgreSQL projection
durations. Projection is asynchronous and outside the result-read critical
path, so this does not invalidate the end-to-end or worker measurements; it is
a remaining observability gap for the next profiling run.

This was one ordered run, V1 followed by V2, on Windows Docker Desktop. Host
load varied significantly, so Docker phase deltas should not be treated as a
microbenchmark of protocol code. The coordination and correctness observations
are much stronger because they are measured directly at their boundaries.

## Reproduce

From the project root with the Compose stack running:

```powershell
python -u scripts\invocation_v1_v2_comparison.py `
  --base-url http://127.0.0.1:8000 `
  --output-json docs\invocation_v1_v2_comparison_2026-07-02.json
```

The script temporarily recreates the backend to select each protocol and
restores V1 settings in a `finally` block.
