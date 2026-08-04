# Resident Warm Runner Comparison

Date: 2026-07-26

This compares the old warm path
(`python /runner.py` via Docker exec on every warm invocation)
with the new resident warm runner
(`python /runner.py --serve`, then local HTTP calls inside the warm container).

The benchmark used one freshly built Python function image and ran each pattern
six times in both modes. Steady-state numbers below exclude the first cold run.

## Results

| Pattern | Old warm wall | New warm wall | Wall speedup | Old warm exec | New warm exec | Old export | New export |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No-op | 1288 ms | 53 ms | 24.3x | 790 ms | 5 ms | 344 ms | 0 ms |
| Sleep 1s | 2040 ms | 1017 ms | 2.01x | 1673 ms | 1002 ms | 227 ms | 0 ms |
| No-op with declared output | 1208 ms | 628 ms | 1.92x | 695 ms | 4 ms | 334 ms | 580 ms |

## What Changed

- The runner is now resident inside the warm container.
- Warm no-op invocations stopped paying per-invocation Python startup cost.
- Warm invocations with output files still pay Docker export/copy cost, so the
  improvement there is smaller.

## Note

The old `duration_ms` field is not the best comparison for output-producing
invocations because it is recorded before the export/copy cleanup path finishes.
For user-visible completion time, `executor_wall_with_cleanup_ms` is the better
number.
