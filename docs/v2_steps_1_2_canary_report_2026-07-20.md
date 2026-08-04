# V2 Steps 1-2 Canary Report

Date: 2026-07-20

## Scope

This run covered the first two V2 implementation-plan steps:

1. Freeze V1 as the stable baseline.
2. Confirm the V2 execution path is green with a controlled canary.

## Step 1: V1 Baseline

V1 remains the default production path:

- `V2_BUILD_PILOT_ENABLED=false`
- `V2_INVOCATION_PILOT_ENABLED=false`
- `V1_JOB_CREATION_ENABLED=true`
- `V1_COORDINATION_ENDPOINTS_ENABLED=true`
- warm containers enabled in normal worker configuration

Baseline smoke test:

- Command: `python scripts\user_journey_smoke.py --base-url http://localhost:8000`
- Result: passed
- Covered: register, create function, upload version, build, invoke, list output, download output
- Invocation ID: `519`
- Output artifact: `report.txt`

## Step 2: Controlled V2 Canary

Canary command:

```powershell
python scripts\invocation_v1_v2_comparison.py --base-url http://localhost:8000 --output-json docs\invocation_v1_v2_comparison_2026-07-20.json
```

The canary ran:

- V1 invocation scenarios first.
- V2 private-owner invocation scenarios second.
- Builds stayed on V1 for this run.
- Backend was restored to V1-default flags after the canary.

Raw results:

- `docs/invocation_v1_v2_comparison_2026-07-20.json`

## Correctness Results

V1:

- Invocations: 22
- All succeeded: yes
- All results matched expected payloads: yes
- Coordination versions observed: `1`
- Recovery count: `0`

V2:

- Invocations: 22
- All succeeded: yes
- All results matched expected payloads: yes
- Coordination versions observed: `2`
- Recovery count: `0`
- Terminal succeeded delta: `22`
- Terminal failed delta: `0`
- Duplicate dispatches: `0`
- Duplicate claims: `0`
- Duplicate completions: `0`
- Duplicate finalizations: `0`

## Timing Summary

Median values from the scenario summary:

| Scenario | Protocol | Wall Time | Duration Median | Queued-To-Finished Median | Worker Overhead Median |
| --- | --- | ---: | ---: | ---: | ---: |
| noop sequential | V1 | 13155 ms | 2155 ms | 2563 ms | 2155 ms |
| noop sequential | V2 | 9687 ms | 896 ms | 1423 ms | 896 ms |
| one-second sequential | V1 | 14922 ms | 1996 ms | 2506 ms | 996 ms |
| one-second sequential | V2 | 13375 ms | 1801 ms | 2316 ms | 801 ms |
| three-second concurrent | V1 | 23343 ms | 6730 ms | 15060 ms | 3723 ms |
| three-second concurrent | V2 | 20905 ms | 10680 ms | 17367 ms | 7680 ms |

## Interpretation

The V2 control path is functionally green for this controlled invocation canary.
All V2 jobs used coordination version 2, all results were correct, no recovery
was needed, and no duplicate-related counters increased.

The performance result is mixed:

- V2 was faster than V1 for sequential no-op and one-second scenarios.
- V2 had worse median executor duration and worker overhead in the concurrent
  three-second burst.

The concurrent V2 slowdown appears to be execution/runtime overhead rather than
a correctness failure. The raw timing file should be used for the next tuning
pass, especially around Docker contention, warm tmpfs export, sandbox cleanup,
and finalization/projector timing.

## Current State After Run

After the canary, backend flags were checked and are back to the V1 baseline:

- V2 build pilot: off
- V2 invocation pilot: off
- V1 job creation: on
- V1 coordination endpoints: on

## Gate Result

Step 1: passed.

Step 2: passed for correctness, with a performance warning on concurrent V2
invocation workload.

