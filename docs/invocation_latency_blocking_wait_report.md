# Invocation Latency After Blocking Docker Wait

Date: 2026-06-27

This report preserves the original polling baseline in
`docs/invocation_latency_profile_report.md` and measures the worker after
replacing 500 ms container-state polling with Docker's blocking wait API.

## Change

Previous behavior:

```python
while time.monotonic() < deadline:
    container.reload()
    if not container.attrs["State"]["Running"]:
        return container.attrs["State"]["ExitCode"]
    time.sleep(0.5)
```

New behavior:

```python
try:
    wait_result = container.wait(timeout=timeout_seconds)
except ReadTimeout:
    container.kill()
    raise ExecutionError(...)
return wait_result.get("StatusCode")
```

Docker now wakes the worker when the container exits. There is no repeated
`reload()` request and no artificial 0-500 ms delay before noticing completion.
The configured function timeout remains enforced, and a timed-out container is
killed before the invocation is reported as failed.

## Verification

The complete worker unit suite passed:

```text
Ran 47 tests in 0.853s
OK
```

New focused coverage verifies:

- one blocking `container.wait(timeout=...)` call returns the Docker exit code;
- no container kill occurs after a normal exit;
- a Docker read timeout kills the container;
- the timeout becomes an `ExecutionError` with the configured duration.

Three worker replicas were restarted and both live profile runs completed with
all 22 invocations succeeding in each run.

## Profile Workload

The same script and scenarios as the original report were used:

| Scenario | Count | User sleep | Concurrency |
| --- | ---: | ---: | ---: |
| No-op sequential | 5 | 0s | 1 |
| One-second sequential | 5 | 1s | 1 |
| Three-second concurrent | 12 | 3s | 12 |

Raw results:

- Original polling baseline: `docs/invocation_latency_profile_latest.json`
- Blocking wait run 1: `docs/invocation_latency_profile_blocking_wait.json`
- Blocking wait run 2: `docs/invocation_latency_profile_blocking_wait_repeat.json`

## Median Results

The repeat is shown as the primary blocking result because Docker was less slow
than during the first blocking run.

| Scenario | Metric | Polling baseline | Blocking repeat | Difference |
| --- | --- | ---: | ---: | ---: |
| No-op | Docker wait | 1065 ms | 1266 ms | +201 ms |
| No-op | Executor duration | 1863 ms | 2715 ms | +852 ms |
| No-op | Worker total | 2215 ms | 3366 ms | +1151 ms |
| One-second | Docker wait | 1691 ms | 2463 ms | +772 ms |
| One-second | Executor duration | 2531 ms | 4714 ms | +2183 ms |
| One-second | Worker total | 2924 ms | 5323 ms | +2399 ms |
| Concurrent | Docker wait | 4390 ms | 5184 ms | +794 ms |
| Concurrent | Executor duration | 6502 ms | 9741 ms | +3239 ms |
| Concurrent | Worker total | 7300 ms | 12129 ms | +4829 ms |

## Why This Does Not Show an Isolated Wait Regression

The blocking profiles ran while the whole Docker host was substantially slower.
Operations that happen before `container.wait()` also regressed:

| Concurrent median phase | Polling baseline | Blocking repeat |
| --- | ---: | ---: |
| Container create | 581 ms | 1050 ms |
| Container start | 564 ms | 1138 ms |
| Backend running report | 445 ms | 1003 ms |
| Queue to started | 8589 ms | 16051 ms |

`container.wait()` cannot cause the earlier container-create, container-start,
or backend-running-report measurements for the same invocation. Their broad
slowdown shows that the historical baseline and the new runs were not under
equivalent host conditions. The two blocking runs also differed materially,
with total profile time falling from 135.5 seconds to 110.8 seconds on the
immediate repeat.

Therefore the observed full-stack numbers do not demonstrate that blocking wait
is slower, but they also do not empirically demonstrate its expected latency
gain. They demonstrate high run-to-run Docker Desktop contention and variance.

## Conclusion

The implementation is functionally correct and removes the deterministic
polling weakness. The theoretical completion-detection improvement is 0-500 ms
per invocation, about 250 ms on average, but it is currently smaller than the
noise caused by Docker host contention.

For a defensible performance comparison, the next measurement should be a
same-session A/B microbenchmark that runs identical prebuilt containers and
alternates polling and blocking detection. That isolates exit detection from
function builds, scheduling, backend load, and changing Docker host conditions.

