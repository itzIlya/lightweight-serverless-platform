# Distributed Benchmark Combined Report

This report combines the valid single-function runs from `distributed-full-benchmark.json` with the refreshed-token resumed runs from `distributed-remaining-benchmark.json`.

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- It is not worker execution concurrency. Worker execution concurrency was held constant during these runs; the deployed workers reported `max_invocation_concurrency: 2`.
- Use this report to understand saturation, queueing, throughput ceilings, and user-visible latency under request pressure. Use a separate worker-concurrency benchmark when tuning how many jobs each worker can execute at once.
- The embedded JSON still uses the historical field name `"concurrency"`; in this report that field means saturation/client-side concurrency.

## Coverage

- Total clean runs: `72`
- Total invocations submitted: `1665`
- Total successful invocations: `1665`
- Total failed invocations inside clean runs: `0`

## Scenario Summary

| Scenario | Count | Saturation Concurrency | Runs | Success | Median wall s | Median throughput/s | Median terminal s | P95 terminal s | Worker spread |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mixed-15 | 15 | 2 | 3 | 45/45 | 15.094 | 0.994 | 1.578 | 2.719 | worker-1:22, worker-2:23 |
| mixed-15 | 15 | 4 | 3 | 45/45 | 9.563 | 1.569 | 2.625 | 2.781 | worker-1:21, worker-2:24 |
| mixed-15 | 15 | 8 | 3 | 45/45 | 6.954 | 2.157 | 2.829 | 4.235 | worker-1:22, worker-2:23 |
| mixed-30 | 30 | 2 | 3 | 90/90 | 32.094 | 0.935 | 1.601 | 2.813 | worker-1:43, worker-2:47 |
| mixed-30 | 30 | 4 | 3 | 90/90 | 16.391 | 1.83 | 1.601 | 2.812 | worker-1:43, worker-2:47 |
| mixed-30 | 30 | 8 | 3 | 90/90 | 13.016 | 2.305 | 2.821 | 4.828 | worker-1:44, worker-2:46 |
| mixed-80 | 80 | 2 | 3 | 240/240 | 83.329 | 0.96 | 1.578 | 2.859 | worker-1:118, worker-2:122 |
| mixed-80 | 80 | 4 | 3 | 240/240 | 44.313 | 1.805 | 2.047 | 2.75 | worker-1:119, worker-2:121 |
| mixed-80 | 80 | 8 | 3 | 240/240 | 30.375 | 2.634 | 2.774 | 4.157 | worker-1:118, worker-2:122 |
| single-dependency | 12 | 2 | 3 | 36/36 | 11.016 | 1.089 | 1.578 | 3.266 | worker-1:17, worker-2:19 |
| single-dependency | 12 | 4 | 3 | 36/36 | 7.312 | 1.641 | 2.015 | 3.328 | worker-1:18, worker-2:18 |
| single-dependency | 12 | 8 | 3 | 36/36 | 5.781 | 2.076 | 2.789 | 4.156 | worker-1:19, worker-2:17 |
| single-input_output | 12 | 2 | 3 | 36/36 | 15.532 | 0.773 | 1.797 | 2.688 | worker-1:18, worker-2:18 |
| single-input_output | 12 | 4 | 3 | 36/36 | 8.109 | 1.48 | 2.656 | 2.859 | worker-1:18, worker-2:18 |
| single-input_output | 12 | 8 | 3 | 36/36 | 6.281 | 1.911 | 2.766 | 4.234 | worker-1:18, worker-2:18 |
| single-output | 12 | 2 | 3 | 36/36 | 16.265 | 0.738 | 1.898 | 3.063 | worker-1:15, worker-2:21 |
| single-output | 12 | 4 | 3 | 36/36 | 8.359 | 1.436 | 1.695 | 2.812 | worker-1:18, worker-2:18 |
| single-output | 12 | 8 | 3 | 36/36 | 8.281 | 1.449 | 3.071 | 4.266 | worker-1:18, worker-2:18 |
| single-sleep | 12 | 2 | 3 | 36/36 | 17.609 | 0.681 | 2.742 | 4.046 | worker-1:17, worker-2:19 |
| single-sleep | 12 | 4 | 3 | 36/36 | 10.141 | 1.183 | 2.852 | 4.125 | worker-1:18, worker-2:18 |
| single-sleep | 12 | 8 | 3 | 36/36 | 8.063 | 1.488 | 3.977 | 5.5 | worker-1:18, worker-2:18 |
| single-tiny | 12 | 2 | 3 | 36/36 | 11.844 | 1.013 | 1.562 | 3.047 | worker-1:17, worker-2:19 |
| single-tiny | 12 | 4 | 3 | 36/36 | 8.563 | 1.401 | 2.281 | 3.0 | worker-1:18, worker-2:18 |
| single-tiny | 12 | 8 | 3 | 36/36 | 4.687 | 2.56 | 2.0 | 4.016 | worker-1:18, worker-2:18 |

## Worker Timing Medians By Scenario

| Scenario | Saturation Concurrency | worker_process_total_ms | executor_wall_with_cleanup_ms | executor_duration_ms | runner_total_ms | warm_runner_exec_ms | sandbox_prepare_ms | docker_image_pull_ms | docker_input_copy_ms | docker_export_copy_ms | output_upload_ms | orchestrator_claim_ms | orchestrator_completion_ms |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mixed-15 | 2 | 686.0 | 670.0 | 585.0 | 376.0 | 470.0 | 24.0 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 6.0 |
| mixed-15 | 4 | 1123.0 | 1098.0 | 866.0 | 423.0 | 523.0 | 24.0 | 25.0 | 4.0 | 0.0 | 0.0 | 5.0 | 6.0 |
| mixed-15 | 8 | 1081.0 | 1070.0 | 883.0 | 439.0 | 561.0 | 27.0 | 26.0 | 4.0 | 0.0 | 0.0 | 6.0 | 6.0 |
| mixed-30 | 2 | 968.5 | 951.0 | 776.5 | 413.5 | 511.5 | 25.0 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 5.0 |
| mixed-30 | 4 | 978.5 | 959.0 | 737.5 | 416.0 | 518.5 | 25.0 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 5.0 |
| mixed-30 | 8 | 1059.0 | 1038.5 | 837.0 | 422.0 | 531.5 | 30.5 | 0.0 | 5.0 | 0.0 | 0.0 | 5.0 | 6.0 |
| mixed-80 | 2 | 743.0 | 728.5 | 649.0 | 418.0 | 522.0 | 27.0 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 6.0 |
| mixed-80 | 4 | 983.0 | 967.5 | 778.5 | 419.5 | 524.0 | 27.0 | 0.0 | 4.0 | 0.0 | 0.0 | 5.5 | 6.0 |
| mixed-80 | 8 | 1131.5 | 1115.0 | 939.5 | 440.5 | 554.0 | 33.0 | 26.0 | 5.0 | 0.0 | 0.0 | 6.0 | 6.0 |
| single-dependency | 2 | 869.0 | 848.5 | 780.0 | 552.5 | 660.5 | 27.0 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 6.0 |
| single-dependency | 4 | 990.5 | 975.5 | 857.0 | 588.0 | 699.0 | 26.5 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 5.5 |
| single-dependency | 8 | 1049.0 | 1028.0 | 866.0 | 602.5 | 718.5 | 33.5 | 0.0 | 4.0 | 0.0 | 0.0 | 6.5 | 5.0 |
| single-input_output | 2 | 994.0 | 979.5 | 602.5 | 370.5 | 471.5 | 45.0 | 0.0 | 5.0 | 250.5 | 35.0 | 5.0 | 6.0 |
| single-input_output | 4 | 1102.5 | 1086.5 | 702.0 | 389.5 | 491.5 | 48.0 | 0.0 | 5.0 | 246.0 | 36.5 | 6.0 | 6.0 |
| single-input_output | 8 | 1173.5 | 1158.5 | 779.5 | 397.5 | 498.5 | 71.5 | 0.0 | 5.0 | 255.5 | 38.0 | 6.5 | 6.0 |
| single-output | 2 | 934.5 | 921.5 | 576.5 | 363.5 | 457.5 | 25.5 | 0.0 | 4.0 | 247.5 | 35.5 | 5.0 | 5.0 |
| single-output | 4 | 1021.5 | 1004.5 | 640.5 | 376.5 | 480.0 | 27.5 | 0.0 | 4.0 | 248.5 | 34.5 | 5.5 | 6.0 |
| single-output | 8 | 1104.5 | 1083.0 | 670.0 | 382.5 | 489.0 | 33.0 | 0.0 | 4.0 | 252.5 | 37.0 | 7.0 | 6.0 |
| single-sleep | 2 | 1654.0 | 1641.5 | 1578.0 | 1374.5 | 1472.5 | 25.5 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 5.5 |
| single-sleep | 4 | 1820.0 | 1808.0 | 1741.0 | 1404.0 | 1507.5 | 24.0 | 0.0 | 4.0 | 0.0 | 0.0 | 6.0 | 6.0 |
| single-sleep | 8 | 1764.5 | 1750.5 | 1645.5 | 1385.0 | 1484.5 | 25.5 | 0.0 | 4.0 | 0.0 | 0.0 | 6.0 | 5.0 |
| single-tiny | 2 | 641.5 | 630.5 | 572.0 | 370.5 | 469.0 | 25.5 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 6.0 |
| single-tiny | 4 | 725.0 | 709.0 | 635.5 | 389.0 | 489.5 | 30.5 | 0.0 | 4.0 | 0.0 | 0.0 | 5.0 | 5.0 |
| single-tiny | 8 | 790.0 | 777.5 | 665.0 | 404.0 | 504.5 | 30.5 | 0.0 | 4.5 | 0.0 | 0.0 | 7.0 | 5.0 |

## Notes

- The first full run was stopped after token expiry affected input/output runs. The benchmark client now refreshes JWTs before each isolated run.
- Every clean run performed preflight and post-run isolation checks: queues empty, workers online, worker active counters zero, and no active invocations.
- Worker timing fields are read from worker logs after each run, keyed by invocation request id.
