# Warm Routing Stage 4 Benchmark

Date: 2026-07-19

This benchmark exercises the current V1 invocation path with two local workers,
warm containers enabled, and scheduler warm-aware routing. V2 was not enabled
for this benchmark.

## Files

- Cold baseline raw data: `docs/warm_routing_benchmark_cold_baseline_2026-07-19.json`
- Initial warm raw data: `docs/warm_routing_benchmark_2026-07-19.json`
- Tuned warm raw data: `docs/warm_routing_benchmark_tuned_2026-07-19.json`
- First predictive-sticky raw data: `docs/warm_routing_benchmark_sticky_tuned_2026-07-19.json`
- Guarded predictive-sticky raw data: `docs/warm_routing_benchmark_sticky_guarded_2026-07-19.json`
- Benchmark runner: `scripts/warm_routing_benchmark.py`
- Benchmark Compose override: `docker-compose.warm-benchmark.yml`

## Benchmark Setup

- Workers: 2
- Scheduler: 1
- Function runtime: `python3.13`
- Function behavior: no-op handler, returns immediately
- Output files: none
- Warm pool:
  - enabled for tuned run
  - max containers per worker: 2
  - max containers per function version per worker: 1
  - idle TTL: 120 seconds
  - max age: 900 seconds
  - max uses: 100
  - memory budget hint: 384 MB

The benchmark creates two functions:

- hot function: invoked repeatedly
- cold function: used to create warm-pool pressure between hot invocations

## Scenarios

| Scenario | Purpose |
| --- | --- |
| `hot_sequential` | Six sequential calls to the same function. This should benefit from warm reuse. |
| `cold_pressure` | Three sequential calls to another function. This checks that different functions do not reuse each other's containers. |
| `hot_after_pressure` | Four more hot-function calls after cold-function activity. This checks whether hot containers survive pressure. |
| `hot_burst` | Six hot-function calls at concurrency 3. This checks behavior when demand exceeds idle warm capacity. |

## Tuning Applied

The first warm run succeeded but only reused warm containers 2/6 times for
`hot_sequential`. The cause was not the warm pool itself; it was freshness of
scheduler metadata. Workers only published warm inventory every 10 seconds, so
the scheduler often routed before seeing the newly idle warm container.

For the benchmark override, worker heartbeat was reduced:

```yaml
WORKER_HEARTBEAT_SECONDS: 2
ORCHESTRATOR_WORKER_STALE_AFTER_SECONDS: 10
```

This keeps the protocol the same while making warm inventory visible faster.

## Predictive Sticky Routing Test

After the tuned heartbeat run, a predictive sticky fallback was added:

1. Known exact idle warm container still wins.
2. If no known warm match exists, the scheduler may reuse the most recent exact
   function-version route.
3. The hint is accepted only if the worker has no build pressure, has invocation
   capacity, and is not meaningfully more loaded than the best candidate.

The first version used the recent route too aggressively. It preserved sequential
warm behavior, but concentrated the burst on one worker:

| Scenario | First sticky warm reuses | First sticky worker split | First sticky median executor |
| --- | ---: | --- | ---: |
| `hot_sequential` | 4/6 | 3 / 3 | 1050 ms |
| `hot_after_pressure` | 4/4 | 1 / 3 | 901 ms |
| `hot_burst` | 2/6 | 5 / 1 | 4897 ms |

The policy was tightened with a local burst guard:

```text
exact warm match
-> guarded predictive sticky hint
-> least-loaded fallback
```

The guarded hint allows only a small amount of recent local dispatch pressure,
so repeated calls can still benefit but bursts should fall back to load-aware
routing sooner.

## Tuned Warm vs Guarded Predictive Sticky

| Scenario | Tuned warm median executor | Guarded sticky median executor | Tuned warm reuses | Guarded sticky reuses |
| --- | ---: | ---: | ---: | ---: |
| `hot_sequential` | 928 ms | 942 ms | 4/6 | 4/6 |
| `cold_pressure` | 1227 ms | 1632 ms | 1/3 | 1/3 |
| `hot_after_pressure` | 842 ms | 794 ms | 4/4 | 4/4 |
| `hot_burst` | 3610 ms | 4170 ms | 3/6 | 2/6 |

The guarded version is safe, but it is not a clear performance win over the
2-second heartbeat run. It helped `hot_after_pressure` slightly, roughly matched
`hot_sequential`, and remained worse for `hot_burst`.

The intended 10-second-heartbeat sticky benchmark could not be completed because
the local environment rejected the Docker-metadata approval needed by the Python
benchmark script. Based on the 2-second results, predictive sticky should remain
a fallback hint rather than the main fix for stale warm metadata.

## Cold Baseline vs Tuned Warm

| Scenario | Cold wall | Warm wall | Wall improvement | Cold median executor | Warm median executor | Executor improvement | Warm reuses |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `hot_sequential` | 19280 ms | 13515 ms | 29.9% | 2199 ms | 928 ms | 57.8% | 4/6 |
| `cold_pressure` | 11250 ms | 7281 ms | 35.3% | 2422 ms | 1227 ms | 49.3% | 1/3 |
| `hot_after_pressure` | 15234 ms | 7765 ms | 49.0% | 2609 ms | 842 ms | 67.7% | 4/4 |
| `hot_burst` | 10485 ms | 9561 ms | 8.8% | 5460 ms | 3610 ms | 33.9% | 3/6 |

## Initial Warm vs Tuned Warm

| Scenario | Initial warm reuses | Tuned warm reuses | Initial median executor | Tuned median executor |
| --- | ---: | ---: | ---: | ---: |
| `hot_sequential` | 2/6 | 4/6 | 1565 ms | 928 ms |
| `cold_pressure` | 0/3 | 1/3 | 1649 ms | 1227 ms |
| `hot_after_pressure` | 2/4 | 4/4 | 1349 ms | 842 ms |
| `hot_burst` | 1/6 | 3/6 | 4928 ms | 3610 ms |

## Correctness Results

All invocations in all completed benchmark runs ended with `succeeded`.

The tuned warm run also showed the expected warm inventory:

- one idle hot container on each online worker
- one idle cold container on one worker
- no cross-function container reuse
- hot containers survived cold-function pressure

## Interpretation

Warm containers are giving real benefit even on Docker Desktop:

- repeated no-op invocations dropped from about 2.2 seconds median executor time
  to under 1 second
- hot containers survived later cold-function traffic
- burst performance improved, but not as much as sequential performance

The burst case still creates cold starts because we allow only one warm container
per function version per worker. With two workers, the maximum idle warm capacity
for one function version is two containers. A concurrency-3 burst can therefore
reuse at most two immediately warm containers unless we raise the per-function
warm limit or later add proactive prewarming.

## Current Recommendation

Keep the faster heartbeat in the warm benchmark profile. For production defaults,
do not blindly set 2 seconds everywhere yet; instead make heartbeat interval a
deployment knob and choose based on worker count and Redis load.

Keep guarded predictive sticky as an experimental fallback, not as the primary
solution. The next useful performance step is not V2 yet. The next low-risk step
is to separate warm-pool inventory publication from full worker heartbeat, so a
worker can publish a small warm-pool update immediately after a container becomes
idle. That would make routing warm-aware without lowering every heartbeat
message or guessing from route history.
