# Invocation Wait Comparison Report

Date: 2026-06-27

This report compares two full invocation profiles with Docker's blocking wait
API against two control profiles after restoring the original 500 ms polling
loop. The worker currently uses polling.

The original latency report and baseline remain unchanged.

## Workload

Every profile created and built a fresh function, then ran:

| Scenario | Count | User sleep | Concurrency |
| --- | ---: | ---: | ---: |
| No-op sequential | 5 | 0s | 1 |
| One-second sequential | 5 | 1s | 1 |
| Three-second concurrent | 12 | 3s | 12 |

All 88 invocations across the four profiles succeeded.

## Verification

After the revert, source inspection confirmed the original loop:

```python
while time.monotonic() < deadline:
    container.reload()
    if not container.attrs["State"]["Running"]:
        return container.attrs["State"]["ExitCode"]
    time.sleep(0.5)
```

The restored worker suite passed:

```text
Ran 46 tests in 0.290s
OK
```

All three worker replicas were restarted before the polling controls.

## Median Results

| Scenario | Metric | Blocking 1 | Blocking 2 | Polling 1 | Polling 2 |
| --- | --- | ---: | ---: | ---: | ---: |
| No-op | Docker wait | 1833 ms | 1266 ms | 1371 ms | 1114 ms |
| No-op | Worker total | 3937 ms | 3366 ms | 3673 ms | 2618 ms |
| One-second | Docker wait | 2516 ms | 2463 ms | 2176 ms | 2825 ms |
| One-second | Worker total | 5320 ms | 5323 ms | 4224 ms | 5046 ms |
| Concurrent | Docker wait | 5468 ms | 5184 ms | 4929 ms | 5239 ms |
| Concurrent | Worker total | 13154 ms | 12129 ms | 11184 ms | 10834 ms |

## Noise Between Identical Polling Runs

No code changed between the two polling controls, yet their medians moved:

| Scenario | Polling worker total 1 | Polling worker total 2 | Difference |
| --- | ---: | ---: | ---: |
| No-op | 3673 ms | 2618 ms | -1055 ms |
| One-second | 4224 ms | 5046 ms | +822 ms |
| Concurrent | 11184 ms | 10834 ms | -350 ms |

The one-second Docker-wait median changed from 2176 ms to 2825 ms between
identical polling runs, a 649 ms swing. That variance is larger than the entire
0-500 ms polling-detection delay being investigated.

Other phases also changed significantly between runs, including container
create, container start, backend reporting, and queue delay. These phases do not
depend on how container exit is detected.

## Conclusion

The control profiles support the conclusion that the earlier broad slowdown was
mostly Docker host and full-stack run-to-run noise. The results do not show a
reliable performance advantage for either exit-detection implementation:

- blocking wait removes the known polling mechanism and its theoretical
  0-500 ms completion-detection delay;
- the full platform profile varies by more than that expected improvement;
- averaging only two runs per implementation still produces mixed results;
- the reverted polling implementation is currently active and functionally
  passes its tests.

A defensible timing answer requires a same-session alternating A/B
microbenchmark using identical prebuilt containers. That test would exclude
builds, API polling, scheduler delay, backend/database reporting, and most
changing Docker host conditions.

## Raw Results

- Original baseline: `docs/invocation_latency_profile_latest.json`
- Blocking run 1: `docs/invocation_latency_profile_blocking_wait.json`
- Blocking run 2: `docs/invocation_latency_profile_blocking_wait_repeat.json`
- Polling control 1: `docs/invocation_latency_profile_polling_control_after_revert.json`
- Polling control 2: `docs/invocation_latency_profile_polling_control_after_revert_repeat.json`

