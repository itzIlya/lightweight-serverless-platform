# Worker Concurrency Partial Results Report

Generated: 2026-09-01

## Purpose

This report preserves the worker-concurrency benchmark work that was partially completed before we stopped the run.

The important distinction:

- `Worker Invocation Concurrency` means how many invocation jobs each worker may execute at the same time.
- `Cluster Invocation Capacity` means `worker count * worker invocation concurrency`.
- `Saturation Concurrency` means how many client-side invocation requests the benchmark keeps in flight.

The older saturation benchmarks varied only client pressure. These worker-concurrency runs started varying the actual worker execution limit.

## Result Files

| File | Status | Runs | Successful invocations | Failures | Notes |
|---|---|---:|---:|---:|---|
| `distributed-worker-concurrency-benchmark.json` | Contaminated | 88 | 1579 | 1 | First attempt. It hit a benchmark/client/control-plane timeout while the backend was overloaded. Do not use for final tuning decisions. |
| `distributed-worker-concurrency-benchmark-clean.json` | Clean partial | 86 | 1420 | 0 | Long matrix after backend capacity was improved. It only reached worker concurrency `1` before we stopped. |
| `distributed-worker-concurrency-mixed80-focused.json` | Clean partial | 5 | 400 | 0 | Focused mixed-80 run at saturation `8`. It completed worker concurrency `1` and two repeats of worker concurrency `2`. |

## Control Plane Fix During Testing

During the first attempt, the backend became unhealthy under benchmark pressure. The backend was running Gunicorn with only two synchronous workers:

```text
gunicorn serverless_platform.wsgi:application --workers 2
```

Symptoms:

- worker heartbeat requests timed out
- finalizer requests to the backend timed out
- Nginx returned upstream timeouts
- some invocations stayed visible as `running` until reconciliation/finalization caught up

I changed the backend command to use a threaded Gunicorn worker pool:

```text
gunicorn serverless_platform.wsgi:application \
  --worker-class gthread \
  --workers 4 \
  --threads 4 \
  --timeout 120
```

After that, the clean benchmark runs completed without backend timeout failures.

## Clean Long Matrix

Source file:

```text
benchmark-results/distributed-worker-concurrency-benchmark-clean.json
```

This run only covered:

```text
Worker Invocation Concurrency: 1 per worker
Cluster Invocation Capacity:   2 total invocation slots
```

It still ran many saturation levels and workload types. All completed runs passed.

| Scenario | Worker Concurrency | Cluster Capacity | Saturation | Runs | Success | Fail | Median Wall s | Avg Throughput/s | Median Terminal s | P95 Terminal s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| single-tiny | 1 | 2 | 2 | 3 | 36 | 0 | 9.422 | 1.284 | 1.500 | 1.797 |
| single-tiny | 1 | 2 | 4 | 3 | 36 | 0 | 5.766 | 2.072 | 1.531 | 2.750 |
| single-tiny | 1 | 2 | 8 | 3 | 36 | 0 | 5.875 | 2.043 | 2.891 | 4.359 |
| single-tiny | 1 | 2 | 16 | 3 | 36 | 0 | 5.718 | 2.012 | 4.296 | 6.047 |
| single-sleep | 1 | 2 | 2 | 3 | 36 | 0 | 18.656 | 0.647 | 2.844 | 3.796 |
| single-sleep | 1 | 2 | 4 | 3 | 36 | 0 | 11.875 | 0.959 | 3.859 | 4.125 |
| single-sleep | 1 | 2 | 8 | 3 | 36 | 0 | 11.781 | 0.965 | 6.765 | 8.078 |
| single-sleep | 1 | 2 | 16 | 3 | 36 | 0 | 12.687 | 0.950 | 7.828 | 11.734 |
| single-dependency | 1 | 2 | 2 | 3 | 36 | 0 | 9.235 | 1.277 | 1.484 | 1.766 |
| single-dependency | 1 | 2 | 4 | 3 | 36 | 0 | 7.188 | 1.670 | 1.782 | 3.000 |
| single-dependency | 1 | 2 | 8 | 3 | 36 | 0 | 6.812 | 1.760 | 3.875 | 4.266 |
| single-dependency | 1 | 2 | 16 | 3 | 36 | 0 | 6.859 | 1.744 | 4.516 | 6.844 |
| single-output | 1 | 2 | 2 | 3 | 36 | 0 | 13.547 | 0.888 | 1.500 | 2.703 |
| single-output | 1 | 2 | 4 | 3 | 36 | 0 | 8.391 | 1.391 | 2.015 | 3.047 |
| single-output | 1 | 2 | 8 | 3 | 36 | 0 | 7.921 | 1.497 | 3.922 | 5.453 |
| single-output | 1 | 2 | 16 | 3 | 36 | 0 | 8.281 | 1.395 | 4.766 | 7.937 |
| single-input_output | 1 | 2 | 2 | 3 | 36 | 0 | 15.390 | 0.813 | 1.593 | 2.703 |
| single-input_output | 1 | 2 | 4 | 3 | 36 | 0 | 8.140 | 1.472 | 2.656 | 2.812 |
| single-input_output | 1 | 2 | 8 | 3 | 36 | 0 | 9.453 | 1.294 | 3.907 | 5.375 |
| single-input_output | 1 | 2 | 16 | 3 | 36 | 0 | 8.703 | 1.400 | 5.360 | 8.000 |
| mixed-15 | 1 | 2 | 2 | 3 | 45 | 0 | 15.219 | 0.982 | 1.640 | 2.828 |
| mixed-15 | 1 | 2 | 4 | 3 | 45 | 0 | 11.015 | 1.342 | 2.656 | 3.969 |
| mixed-15 | 1 | 2 | 8 | 3 | 45 | 0 | 10.437 | 1.456 | 4.218 | 6.422 |
| mixed-15 | 1 | 2 | 16 | 3 | 45 | 0 | 10.609 | 1.449 | 6.812 | 10.547 |
| mixed-30 | 1 | 2 | 2 | 3 | 90 | 0 | 32.469 | 0.938 | 1.562 | 3.468 |
| mixed-30 | 1 | 2 | 4 | 3 | 90 | 0 | 21.406 | 1.392 | 2.656 | 4.828 |
| mixed-30 | 1 | 2 | 8 | 3 | 90 | 0 | 19.391 | 1.593 | 4.015 | 7.328 |
| mixed-30 | 1 | 2 | 16 | 3 | 90 | 0 | 18.078 | 1.674 | 8.234 | 10.672 |
| mixed-80 | 1 | 2 | 2 | 2 | 160 | 0 | 86.891 | 0.899 | 1.703 | 3.719 |

## Focused Mixed-80 Comparison

Source file:

```text
benchmark-results/distributed-worker-concurrency-mixed80-focused.json
```

This was the shortened run requested after the full matrix was taking too long.

Fixed:

```text
Scenario:               mixed-80
Saturation Concurrency: 8
Workers:                2
```

Completed:

| Worker Concurrency | Cluster Capacity | Runs | Success | Fail | Median Wall s | Avg Throughput/s | Median Terminal s | P95 Terminal s |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 3 | 240 | 0 | 46.485 | 1.730 | 4.172 | 7.188 |
| 2 | 4 | 2 | 160 | 0 | 30.031 | 2.615 | 2.797 | 4.516 |

Early signal:

```text
Worker concurrency 1 -> 2 improved throughput substantially.
Wall time dropped from about 46.5s to about 30.0s.
Median terminal latency dropped from about 4.17s to about 2.80s.
Correctness stayed clean for all completed focused runs.
```

This is incomplete because we stopped before finishing:

```text
worker concurrency 2 repeat 3
worker concurrency 4
worker concurrency 8
```

## What The Partial Results Mean

The worker-concurrency-1 matrix tells us how the platform behaves when the whole cluster has only two invocation slots.

At saturation `2`, wall time is often high because the client is barely keeping the system fed. At saturation `4` or `8`, wall time usually improves because there is enough backlog to keep both worker slots busy.

But latency rises as saturation goes above capacity:

```text
mixed-30, worker concurrency 1:
saturation 2  -> median terminal 1.562s
saturation 4  -> median terminal 2.656s
saturation 8  -> median terminal 4.015s
saturation 16 -> median terminal 8.234s
```

That is queueing delay. The platform finishes the whole batch faster because the workers stay busy, but individual users wait longer because more requests are standing in line.

The focused mixed-80 comparison gives the first actual worker-concurrency signal:

```text
worker concurrency 1: cluster capacity 2, avg throughput 1.730/s
worker concurrency 2: cluster capacity 4, avg throughput 2.615/s
```

That is about a `51%` throughput improvement for doubling worker execution slots from two total to four total.

It is not linear, but it is meaningful.

## What We Still Do Not Know

We still do not know the true knee point because we did not finish worker concurrency `4` and `8`.

The unanswered question:

```text
Does worker concurrency 4 improve throughput further, or does Docker/CPU/RAM contention flatten the curve?
```

My expectation:

- `1 -> 2` is clearly useful.
- `2 -> 4` may improve throughput, but probably less cleanly.
- `4 -> 8` may flatten or regress depending on VM CPU and Docker pressure.

## Recommended Next Benchmark

Run only the focused benchmark, not the full matrix:

```powershell
python -u .\outputs\serverless-platform\scripts\distributed_platform_benchmark.py `
  --base-url http://37.32.36.255 `
  --ssh-key .\outputs\serverless-platform\local-ssh-keys\codex_deploy_ed25519 `
  --control-host 37.32.36.255 `
  --workers 10.42.1.56 10.42.1.149 `
  --repeats 3 `
  --worker-invocation-concurrency 2 4 8 `
  --concurrency 8 `
  --single-count 12 `
  --skip-single `
  --only-scenarios mixed-80 `
  --output .\outputs\serverless-platform\benchmark-results\distributed-worker-concurrency-mixed80-continuation.md
```

That skips the already-proven worker-concurrency-1 baseline and focuses on the missing worker execution settings.

## Current Worker Setting After Stop

After the interrupted focused run, both workers were left at:

```text
WORKER_MAX_CONCURRENCY=3
WORKER_MAX_INVOCATION_CONCURRENCY=2
WORKER_MAX_BUILD_CONCURRENCY=1
```

The platform state was checked after stopping:

```text
scheduler pending invocation queue: 0
worker invocation queues:          0
worker processing queues:          0
active queued/running/finalizing:  0
```

So the benchmark stop did not leave active work behind.

