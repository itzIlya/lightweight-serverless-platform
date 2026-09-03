# Mixed-320 Worker Concurrency Benchmark

Generated: 2026-09-01

## Purpose

This benchmark extends the isolated worker-concurrency testing with a larger `mixed-320` workload.

The goal was to answer one narrow question:

> If the client-side saturation is held constant, how does changing per-worker invocation concurrency affect a larger mixed workload?

This test varies only the worker execution setting:

- `WORKER_MAX_INVOCATION_CONCURRENCY=2`
- `WORKER_MAX_INVOCATION_CONCURRENCY=4`
- `WORKER_MAX_INVOCATION_CONCURRENCY=8`
- `WORKER_MAX_INVOCATION_CONCURRENCY=12`

The benchmark ran against the distributed deployment:

- Control plane: one remote control-plane VM
- Workers: two remote worker VMs
- Saturation concurrency: `32`
- Repeats: `2` per worker-concurrency setting
- Scenario: `mixed-320`
- Total invocations: `2560`

## Terminology

- **Saturation concurrency** means how many client-side invocation requests the benchmark keeps active at once.
- **Worker invocation concurrency** means how many invocation jobs each worker process is allowed to execute at the same time.
- **Cluster invocation capacity** means `number of workers * worker invocation concurrency`.

In this benchmark there are two workers, so:

| Worker invocation concurrency | Cluster invocation capacity |
|---:|---:|
| 2 | 4 |
| 4 | 8 |
| 8 | 16 |
| 12 | 24 |

## Results

These aggregate rows average the two repeats for each worker-concurrency setting. The per-run values are listed in the next section.

| Scenario | Worker invocation concurrency | Cluster invocation capacity | Saturation concurrency | Runs | Success | Fail | Average wall time | Average throughput | Average median terminal latency | Average P95 terminal latency |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mixed-320 | 2 | 4 | 32 | 2 | 640 | 0 | 117.265s | 2.73/s | 10.90s | 15.36s |
| mixed-320 | 4 | 8 | 32 | 2 | 640 | 0 | 96.438s | 3.32/s | 8.84s | 14.41s |
| mixed-320 | 8 | 16 | 32 | 2 | 640 | 0 | 91.437s | 3.50/s | 8.26s | 13.17s |
| mixed-320 | 12 | 24 | 32 | 2 | 640 | 0 | 93.328s | 3.43/s | 8.23s | 13.83s |

Raw benchmark output:

- `benchmark-results/distributed-worker-concurrency-mixed320.md`
- `benchmark-results/distributed-worker-concurrency-mixed320.json`
- `benchmark-results/distributed-worker-concurrency-mixed320-c12.md`
- `benchmark-results/distributed-worker-concurrency-mixed320-c12.json`

## Per-Run Summary

| Worker invocation concurrency | Repeat | Success | Fail | Wall time | Throughput | Median terminal | P95 terminal | Worker split |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2 | 1 | 320 | 0 | 118.718s | 2.695/s | 10.852s | 16.125s | worker-1:159, worker-2:161 |
| 2 | 2 | 320 | 0 | 115.812s | 2.763/s | 10.946s | 14.594s | worker-1:159, worker-2:161 |
| 4 | 1 | 320 | 0 | 97.187s | 3.293/s | 8.782s | 14.562s | worker-1:159, worker-2:161 |
| 4 | 2 | 320 | 0 | 95.688s | 3.344/s | 8.898s | 14.250s | worker-1:158, worker-2:162 |
| 8 | 1 | 320 | 0 | 91.093s | 3.513/s | 8.321s | 13.453s | worker-1:165, worker-2:155 |
| 8 | 2 | 320 | 0 | 91.781s | 3.487/s | 8.195s | 12.891s | worker-1:164, worker-2:156 |
| 12 | 1 | 320 | 0 | 95.093s | 3.365/s | 8.571s | 14.063s | worker-1:165, worker-2:155 |
| 12 | 2 | 320 | 0 | 91.563s | 3.495/s | 7.898s | 13.593s | worker-1:172, worker-2:148 |

## Interpretation

Correctness looked solid:

- All 8 benchmark runs completed.
- All 2560 invocations succeeded.
- There were no failed invocations.
- Worker distribution stayed balanced across both workers.

Performance improved strongly from worker concurrency `2` to `4`:

- Average wall time improved from `117.265s` to `96.438s`.
- That is about a `17.8%` wall-time reduction.
- Average throughput improved from `2.73/s` to `3.32/s`.
- That is about a `21.6%` throughput improvement.

Performance improved only modestly from worker concurrency `4` to `8`:

- Average wall time improved from `96.438s` to `91.437s`.
- That is about a `5.2%` wall-time reduction.
- Average throughput improved from `3.32/s` to `3.50/s`.
- That is about a `5.4%` throughput improvement.

Worker concurrency `12` did not beat `8` overall:

- Average wall time worsened from `91.437s` to `93.328s`.
- Average throughput dropped from `3.50/s` to `3.43/s`.
- Average median terminal latency was basically tied: `8.26s` at concurrency `8` versus `8.23s` at concurrency `12`.
- Average P95 terminal latency worsened from `13.17s` to `13.83s`.

This means the larger workload still shows the same basic shape as the earlier `mixed-80` test:

- `2` is too conservative for throughput.
- `4` gives the biggest useful gain.
- `8` can still help on a long run, but the gain is much smaller.
- `12` appears to be past the useful knee for this two-worker setup.

## Recommendation

For the current two-worker deployment, worker invocation concurrency `4` looks like the best default candidate for a prototype benchmark profile.

Worker invocation concurrency `8` is worth keeping as a high-throughput option, but it should not become the normal default until we also watch CPU, memory, Docker latency, queue depth and backend pressure under longer workloads.

Worker invocation concurrency `12` should not be the default based on this benchmark. It adds more worker-side pressure without improving wall time, throughput or P95 latency compared with `8`.

For normal development mode, the workers were reset after the benchmark to:

```env
WORKER_MAX_CONCURRENCY=3
WORKER_MAX_INVOCATION_CONCURRENCY=2
WORKER_MAX_BUILD_CONCURRENCY=1
```

## Follow-Up

The benchmark script can reset worker concurrency, but doing so currently goes through the normal benchmark setup path and builds the standard test functions even when no benchmark scenarios are requested. That is unnecessary. We should add a small dedicated worker configuration/reset command so operational tuning does not accidentally create throwaway functions.
