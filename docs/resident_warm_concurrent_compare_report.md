# Resident Warm Runner Concurrent Comparison

Date: 2026-07-26

This compares the old warm path
(`python /runner.py` via Docker exec on every warm invocation)
with the resident warm runner
(`python /runner.py --serve`, then local HTTP calls inside the warm container).

The benchmark used one freshly built Python function image and ran each pattern
with 12 invocations at concurrency 4 after a warm-up hit for each mode.

## Results

| Pattern | Old scenario wall | New scenario wall | Old median wall | New median wall | Wall speedup |
| --- | ---: | ---: | ---: | ---: | ---: |
| No-op | 12.5 s | 3.8 s | 3918 ms | 88 ms | 44.52x |
| Sleep 3s | 22.1 s | 16.5 s | 7266 ms | 4997 ms | 1.45x |
| No-op with declared output | 11.9 s | 9.1 s | 3774 ms | 1457 ms | 2.59x |

## What Changed

- Resident warm no-op invocations are much faster because they avoid per-call
  Python startup and Docker exec overhead.
- Sleep-heavy invocations still spend most of their time in user code, so the
  improvement is modest.
- Output-producing invocations still pay for output export/copy work, so the
  gain is real but smaller than the no-op case.

## Notes

- `scenario wall` is the total elapsed time for the whole concurrent burst.
- `median wall` is the per-invocation executor wall time including cleanup.
- The output workload still shows export/copy as a meaningful bottleneck.
