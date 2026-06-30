# Invocation Concurrency Sweep Report

Date: 2026-06-28

This report measures cold invocation behavior across client concurrency levels
1, 2, 4, 8, and 12 on one Docker Desktop host with three worker containers.
Every level ran 12 invocations of the same prebuilt function. The handler slept
for one second and measured its own execution time.

Two sweeps were run:

- ascending order: 1, 2, 4, 8, 12;
- descending control: 12, 8, 4, 2, 1.

An 11-second cooldown between levels allowed the scheduler's 10-second sticky
routing window to expire. All 120 invocations succeeded.

## Instrumentation

The generated `runner.py` now records:

- standard-library module imports;
- environment and event loading;
- sandbox setup;
- user handler import;
- user handler execution;
- result serialization;
- result file writing;
- total measured runner time.

The runner prints one internal `__FUNCTION_TIMING__` marker after the result.
The executor parses this marker into existing worker timing logs. It is not
added to the user's function result.

## Verification

The full worker suite passed inside Docker:

```text
Ran 50 tests in 0.276s
OK
```

Docker Desktop became unresponsive before the first run and was restarted. The
workers initially exited during a Redis/backend startup race, then remained
healthy after their dependencies were ready and the worker service was started
again. This is a separate startup-resilience issue worth fixing later.

## End-to-End Results

Throughput is completed invocations divided by scenario wall time.

| Concurrency | Ascending wall | Ascending throughput | Descending wall | Descending throughput |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 100500 ms | 0.12/s | 53844 ms | 0.22/s |
| 2 | 18875 ms | 0.64/s | 21812 ms | 0.55/s |
| 4 | 16844 ms | 0.71/s | 18234 ms | 0.66/s |
| 8 | 17030 ms | 0.70/s | 26015 ms | 0.46/s |
| 12 | 17312 ms | 0.69/s | 23047 ms | 0.52/s |

Concurrency 4 was the most consistent throughput point. Raising concurrency to
8 or 12 produced no reliable throughput gain and made results more variable.

The ascending concurrency-1 run contained a 22139 ms executor outlier and took
100.5 seconds. Its reverse-order control took 53.8 seconds. The ascending
concurrency-2 run also had unusually slow container create/start medians. These
differences confirm substantial time-order and Docker host variance.

## Reverse-Control Median Breakdown

The reverse run includes the refined module-import timestamp and is the clearest
phase breakdown.

| Phase | C1 | C2 | C4 | C8 | C12 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Queue to started | 462 | 3893 | 4432 | 5488 | 10434 |
| Worker total | 3274 | 7914 | 7091 | 8354 | 6932 |
| Sandbox preparation | 57 | 388 | 260 | 516 | 474 |
| Container create | 291 | 883 | 865 | 928 | 805 |
| Container start | 408 | 1014 | 872 | 999 | 868 |
| Docker wait | 1891 | 3025 | 2632 | 3002 | 2247 |
| Docker logs read | 190 | 336 | 292 | 383 | 259 |
| Docker export copy | 71 | 234 | 277 | 190 | 190 |
| Docker cleanup | 136 | 405 | 263 | 350 | 224 |
| Backend running report | 119 | 388 | 369 | 605 | 513 |
| Backend final report | 114 | 543 | 514 | 651 | 392 |

All values are milliseconds and are per-scenario medians.

## Inside Docker Wait

| Runner phase | C1 | C2 | C4 | C8 | C12 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Python module imports | 490 | 1196 | 1114 | 1278 | 894 |
| Handler import | 1 | 1 | 1 | 1 | 1 |
| Handler execution | 1000 | 1005 | 1001 | 1000 | 1001 |
| Runner total | 1507 | 2233 | 2118 | 2281 | 1899 |
| Docker wait outside measured runner | 384 | 792 | 514 | 721 | 348 |

Event loading, runner setup, serialization, and result writing normally rounded
to 0-1 ms. The handler itself remained stable. Most runner overhead came from
starting Python and importing the runner's standard-library modules, rising from
490 ms at concurrency 1 to approximately 0.9-1.3 seconds under contention.

The difference between Docker wait and runner total includes:

- Python interpreter bootstrap before the first runner timestamp;
- output printing and process shutdown;
- shell copying tmpfs outputs into the export volume;
- Docker exit notification and scheduling delay.

## Conclusions

1. User code is not mysteriously expanding. The one-second handler stays at
   approximately one second.
2. Cold Python startup is expensive on this Docker Desktop host. Module imports
   account for much of the previously unexplained Docker-wait remainder.
3. Container create/start roughly triples under modest contention.
4. Backend reports also grow from about 233 ms combined at concurrency 1 to
   roughly 0.9-1.3 seconds combined at higher levels.
5. Queue delay becomes severe at concurrency 12 even when worker execution time
   does not, showing that scheduler placement and effective worker capacity also
   shape user latency.
6. Concurrency 4 is the most defensible local-system operating point from these
   two sweeps. Concurrency 8 and 12 increase contention without stable throughput
   improvement.

This does not yet imply a per-worker limit of exactly four. With three workers,
the next configuration test should compare worker invocation limits of 1 and 2
per worker. That would cap physical cold starts at 3 and 6 respectively and show
whether lower worker-side concurrency improves both latency and throughput.

The highest-value architectural improvement remains warm execution environments:
they avoid repeated container create/start and Python module import costs. Before
that larger change, reducing local worker concurrency and removing backend
coordination from the critical path are the clearest incremental improvements.

## Reproduction

Ascending:

```powershell
python .\scripts\invocation_concurrency_sweep.py `
  --output-json .\docs\invocation_concurrency_sweep_2026-06-28.json `
  --count 12 --sleep-seconds 1 --cooldown-seconds 11
```

Descending:

```powershell
python .\scripts\invocation_concurrency_sweep.py `
  --output-json .\docs\invocation_concurrency_sweep_reverse_2026-06-28.json `
  --count 12 --sleep-seconds 1 --cooldown-seconds 11 `
  --levels 12,8,4,2,1
```

