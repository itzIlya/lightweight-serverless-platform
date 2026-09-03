# Isolated Worker Concurrency Benchmark Report

Generated: 2026-09-01

## Goal

This benchmark isolates worker execution concurrency.

Only one variable changed:

```text
WORKER_MAX_INVOCATION_CONCURRENCY
```

Everything else was kept fixed:

```text
workers:                 2
workloads:               mixed-30, mixed-80
repeats per test:        2
saturation concurrency:  32
build concurrency:       1 per worker
warm containers:         enabled
control plane:           37.32.36.255
worker-1:                10.42.1.56
worker-2:                10.42.1.149
```

`Saturation Concurrency` means the benchmark client kept up to 32 invocation requests in flight. This was fixed for all runs, so it is not the test variable.

`Worker Invocation Concurrency` means how many invocation jobs each worker was allowed to execute at the same time. This was the test variable.

## Planned Matrix

| Workload | Invocation Count | Worker Concurrency Values | Repeats | Total Runs |
|---|---:|---|---:|---:|
| mixed-30 | 30 | 2, 4, 8, 16 | 2 | 8 |
| mixed-80 | 80 | 2, 4, 8, 16 | 2 | 8 |

Total:

```text
16 benchmark runs
880 invocations
```

## Completion

The benchmark completed all planned runs.

```text
Runs:        16/16
Invocations: 880
Successes:   880
Failures:    0
```

Raw generated files:

- `benchmark-results/distributed-worker-concurrency-isolated.md`
- `benchmark-results/distributed-worker-concurrency-isolated.json`

## Results

| Workload | Worker Concurrency | Cluster Capacity | Saturation | Runs | Success | Fail | Median Wall s | Avg Throughput/s | Median Terminal s | P95 Terminal s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mixed-30 | 2 | 4 | 32 | 2 | 60 | 0 | 11.922 | 2.310 | 7.730 | 11.910 |
| mixed-30 | 4 | 8 | 32 | 2 | 60 | 0 | 11.031 | 2.670 | 6.920 | 10.300 |
| mixed-30 | 8 | 16 | 32 | 2 | 60 | 0 | 9.796 | 2.910 | 7.280 | 9.340 |
| mixed-30 | 16 | 32 | 32 | 2 | 60 | 0 | 10.391 | 2.640 | 9.230 | 10.520 |
| mixed-80 | 2 | 4 | 32 | 2 | 160 | 0 | 29.906 | 2.500 | 10.030 | 12.920 |
| mixed-80 | 4 | 8 | 32 | 2 | 160 | 0 | 24.063 | 3.290 | 8.090 | 11.360 |
| mixed-80 | 8 | 16 | 32 | 2 | 160 | 0 | 23.813 | 3.300 | 7.770 | 12.170 |
| mixed-80 | 16 | 32 | 32 | 2 | 160 | 0 | 24.125 | 3.260 | 8.230 | 14.250 |

## Interpretation

The cleanest improvement was from worker concurrency `2` to `4`.

For `mixed-80`:

```text
worker concurrency 2:
  median wall:       29.906s
  avg throughput:    2.500/s
  median terminal:   10.030s

worker concurrency 4:
  median wall:       24.063s
  avg throughput:    3.290/s
  median terminal:   8.090s
```

That is a real gain:

```text
wall time improved by about 19.5%
throughput improved by about 31.6%
median terminal latency improved by about 19.3%
```

Going from worker concurrency `4` to `8` gave almost no additional throughput for `mixed-80`:

```text
worker concurrency 4 throughput: 3.290/s
worker concurrency 8 throughput: 3.300/s
```

That is effectively flat.

Going from worker concurrency `8` to `16` did not help:

```text
worker concurrency 8:
  mixed-80 median wall: 23.813s
  mixed-80 p95 terminal: 12.170s

worker concurrency 16:
  mixed-80 median wall: 24.125s
  mixed-80 p95 terminal: 14.250s
```

So worker concurrency `16` slightly worsened tail latency while providing no useful throughput improvement.

## Practical Conclusion

On the current two-worker deployment, the useful worker-concurrency range appears to be:

```text
WORKER_MAX_INVOCATION_CONCURRENCY=4
```

`8` is not clearly harmful, but it does not buy much. `16` is not worth using on the current machines.

Recommended current tuning:

```text
WORKER_MAX_CONCURRENCY=5
WORKER_MAX_INVOCATION_CONCURRENCY=4
WORKER_MAX_BUILD_CONCURRENCY=1
```

For now, `4` per worker gives most of the improvement without pushing Docker concurrency as aggressively as `8` or `16`.

## Why It Flattens

The flattening after worker concurrency `4` probably means the bottleneck is no longer the number of worker slots.

Likely limiting factors:

- Docker execution overhead inside each worker VM
- Python runner/import overhead per invocation
- CPU contention from many simultaneous containers
- object output/finalization overhead for the output-producing part of the mixed workload
- control-plane status polling and result reads under fixed saturation `32`

In other words, once each worker can run around four invocations at once, adding more slots does not make the host meaningfully faster. It mostly makes more containers compete for the same CPU, Docker daemon, filesystem, and network resources.

## Operational Note

After the benchmark, workers were restored to the normal setting:

```text
WORKER_MAX_CONCURRENCY=3
WORKER_MAX_INVOCATION_CONCURRENCY=2
WORKER_MAX_BUILD_CONCURRENCY=1
```

The final platform state was clean:

```text
scheduler pending invocation queue: 0
worker invocation queues:          0
worker processing queues:          0
active queued/running/finalizing:  0
```

## Suggested Next Step

If we want to adopt the benchmark result, run one shorter confirmation benchmark with:

```text
WORKER_MAX_INVOCATION_CONCURRENCY=4
saturation concurrency=32
mixed-80
3 repeats
```

If that remains clean, change the default worker deployment from `2` to `4`.

