# Warm Container Stage 1 Benchmark

Date: 2026-07-19

This benchmark measures Stage 1 reactive warm containers. Stage 1 is
worker-local: the scheduler does not yet know which worker has a warm container.

Raw measurements:

- `docs/warm_container_benchmark_noop_2026-07-19.json`
- `docs/warm_container_benchmark_sleep1_2026-07-19.json`
- `docs/warm_container_api_cold_2026-07-19.json`
- `docs/warm_container_api_warm_fixed_2026-07-19.json`

## Focused Executor Benchmark

The focused benchmark ran directly inside a one-off worker container against an
existing local function image:

`localhost:5000/functions/invocation-profile-e4f8c469:v32-v1`

Each cold run created and removed a container. Each warm run used one
`DockerExecutor`; the first invocation created the warm container, and the
remaining invocations reused it.

### No-Op Function

| Mode | Count | Median executor duration | Median wall with cleanup |
| --- | ---: | ---: | ---: |
| Cold | 6 | 3819 ms | 4043 ms |
| Warm, including first | 6 | 2517 ms | 3081 ms |
| Warm, steady-state only | 5 | 2572 ms | 3123 ms |

Median executor duration improved by about 32.7% for steady-state warm
invocations.

### One-Second Function

| Mode | Count | Median executor duration | Median wall with cleanup |
| --- | ---: | ---: | ---: |
| Cold | 6 | 4798 ms | 5122 ms |
| Warm, including first | 6 | 2800 ms | 3271 ms |
| Warm, steady-state only | 5 | 2695 ms | 3109 ms |

Median executor duration improved by about 43.8% for steady-state warm
invocations.

## API-Level Sequential Benchmark

The API benchmark ran six sequential no-op invocations through the normal
backend/scheduler/worker path with one active worker.

| Mode | Count | Client wall | Median queue-to-start | Median invocation duration |
| --- | ---: | ---: | ---: | ---: |
| Cold worker | 6 | 17625 ms | 514 ms | 1620 ms |
| Warm-enabled worker | 6 | 11968 ms | 286 ms | 925 ms |

The valid warm-enabled API run improved median invocation duration by about
42.9% and reduced client wall time by about 32.1%.

Worker logs confirmed the warm-enabled run used one warm container create,
followed by `warm_container_reused=1` for later invocations.

## Important Finding

The first API-level warm run did not reuse containers because the worker created
a new `DockerExecutor` for every job. That meant each job had its own empty warm
pool. I fixed this by creating one shared invocation executor per worker process
in `worker.py`.

The first warm API attempt also exposed a scheduler restart edge case: after the
worker was recreated, the scheduler briefly dispatched a build to the previous
worker name. Restarting the scheduler fixed the benchmark run. This should be
handled properly in the later scheduler-aware warm-container work.

## What Improved

Warm containers remove most repeated Docker container creation/start/removal
cost from repeated invocations of the same function version on the same worker.

The current warm path still pays for:

- Python process startup
- runner module imports
- handler import
- input copy into the container
- output copy out of the container
- sandbox cleanup before and after invocation

## Next Optimization Targets

1. Make the scheduler warm-aware so repeated invocations are routed to workers
   with matching idle warm containers.
2. Reduce warm sandbox cleanup cost.
3. Consider a Stage 2 hot runtime/agent if we want to avoid repeated Python
   imports, while accepting the extra isolation complexity.
