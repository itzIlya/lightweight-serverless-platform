# Distributed Platform Benchmark

Generated: 2026-08-31T09:29:28.314492+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- It is not worker execution concurrency. Worker execution concurrency was held constant during this run; the deployed workers reported `max_invocation_concurrency: 2`.
- Use this report to understand saturation, queueing, throughput ceilings, and user-visible latency under request pressure. Use a separate worker-concurrency benchmark when tuning how many jobs each worker can execute at once.
- The embedded JSON still uses the historical field name `"concurrency"`; in this report that field means saturation/client-side concurrency.

## Built Functions

- `tiny`: function `12`, version `12`, image `10.42.1.22:5000/functions/bench-tiny-376a3aa4:v12-v1-a1-cc49a7594a25-d1`
- `sleep`: function `13`, version `13`, image `10.42.1.22:5000/functions/bench-sleep-190689dc:v13-v1-a1-edc98b185f8f-d1`
- `dependency`: function `14`, version `14`, image `10.42.1.22:5000/functions/bench-dependency-0322dc83:v14-v1-a1-244812c7b7e8-d1`
- `output`: function `15`, version `15`, image `10.42.1.22:5000/functions/bench-output-11592566:v15-v1-a1-e8067e369f2c-d1`
- `input_output`: function `16`, version `16`, image `10.42.1.22:5000/functions/bench-input_output-7ab677fc:v16-v1-a1-a54e68cd2e09-d1`

## Run Summary

| Scenario | Count | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| single-tiny | 2 | 2 | 1 | 2 | 0 | 1.813 | 1.103 | 1.774 | 1.782 | worker-2:2 |
| single-sleep | 2 | 2 | 1 | 2 | 0 | 3.188 | 0.627 | 3.172 | 3.188 | worker-1:2 |
| single-dependency | 2 | 2 | 1 | 2 | 0 | 3.172 | 0.631 | 3.141 | 3.156 | worker-2:2 |
| single-output | 2 | 2 | 1 | 2 | 0 | 3.812 | 0.525 | 3.195 | 3.218 | worker-1:2 |
| single-input_output | 2 | 2 | 1 | 2 | 0 | 3.375 | 0.593 | 2.907 | 2.907 | worker-2:2 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "single-tiny",
    "count": 2,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 1.813,
    "throughput_per_second": 1.103,
    "successes": 2,
    "failures": 0,
    "terminal_seconds": {
      "count": 2,
      "min": 1.766,
      "median": 1.774,
      "p90": 1.782,
      "p95": 1.782,
      "max": 1.782
    },
    "accept_seconds": {
      "count": 2,
      "min": 0.25,
      "median": 0.25,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-2": 2
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 2,
        "min": 43.0,
        "median": 44.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 45.0
      },
      "docker_input_copy_ms": {
        "count": 2,
        "min": 7.0,
        "median": 7.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 2,
        "min": 963.0,
        "median": 983.5,
        "p90": 1004.0,
        "p95": 1004.0,
        "max": 1004.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 2,
        "min": 1039.0,
        "median": 1123.0,
        "p90": 1207.0,
        "p95": 1207.0,
        "max": 1207.0
      },
      "orchestrator_claim_ms": {
        "count": 2,
        "min": 5.0,
        "median": 5.5,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "orchestrator_completion_ms": {
        "count": 2,
        "min": 4.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "output_upload_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 2,
        "min": 373.0,
        "median": 383.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 393.0
      },
      "runner_result_serialize_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 2,
        "min": 374.0,
        "median": 384.0,
        "p90": 394.0,
        "p95": 394.0,
        "max": 394.0
      },
      "sandbox_prepare_ms": {
        "count": 2,
        "min": 25.0,
        "median": 25.5,
        "p90": 26.0,
        "p95": 26.0,
        "max": 26.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 332.0,
        "median": 338.5,
        "p90": 345.0,
        "p95": 345.0,
        "max": 345.0
      },
      "warm_pool_release_ms": {
        "count": 2,
        "min": 0.0,
        "median": 67.5,
        "p90": 135.0,
        "p95": 135.0,
        "max": 135.0
      },
      "warm_runner_exec_ms": {
        "count": 2,
        "min": 478.0,
        "median": 492.0,
        "p90": 506.0,
        "p95": 506.0,
        "max": 506.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 2,
        "min": 67.0,
        "median": 70.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 2,
        "min": 73.0,
        "median": 75.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 2,
        "min": 1054.0,
        "median": 1136.5,
        "p90": 1219.0,
        "p95": 1219.0,
        "max": 1219.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 2,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 3.188,
    "throughput_per_second": 0.627,
    "successes": 2,
    "failures": 0,
    "terminal_seconds": {
      "count": 2,
      "min": 3.156,
      "median": 3.172,
      "p90": 3.188,
      "p95": 3.188,
      "max": 3.188
    },
    "accept_seconds": {
      "count": 2,
      "min": 0.406,
      "median": 0.406,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.406
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 2
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 2,
        "min": 29.0,
        "median": 31.0,
        "p90": 33.0,
        "p95": 33.0,
        "max": 33.0
      },
      "docker_input_copy_ms": {
        "count": 2,
        "min": 6.0,
        "median": 6.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 2,
        "min": 1894.0,
        "median": 1899.0,
        "p90": 1904.0,
        "p95": 1904.0,
        "max": 1904.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 2,
        "min": 1968.0,
        "median": 2041.0,
        "p90": 2114.0,
        "p95": 2114.0,
        "max": 2114.0
      },
      "orchestrator_claim_ms": {
        "count": 2,
        "min": 4.0,
        "median": 4.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "orchestrator_completion_ms": {
        "count": 2,
        "min": 5.0,
        "median": 7.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 2,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 2,
        "min": 334.0,
        "median": 334.0,
        "p90": 334.0,
        "p95": 334.0,
        "max": 334.0
      },
      "runner_result_serialize_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 2,
        "min": 1335.0,
        "median": 1335.5,
        "p90": 1336.0,
        "p95": 1336.0,
        "max": 1336.0
      },
      "sandbox_prepare_ms": {
        "count": 2,
        "min": 23.0,
        "median": 26.0,
        "p90": 29.0,
        "p95": 29.0,
        "max": 29.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 322.0,
        "median": 328.5,
        "p90": 335.0,
        "p95": 335.0,
        "max": 335.0
      },
      "warm_pool_release_ms": {
        "count": 2,
        "min": 0.0,
        "median": 74.5,
        "p90": 149.0,
        "p95": 149.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 2,
        "min": 1425.0,
        "median": 1430.0,
        "p90": 1435.0,
        "p95": 1435.0,
        "max": 1435.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 2,
        "min": 62.0,
        "median": 66.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 2,
        "min": 72.0,
        "median": 73.5,
        "p90": 75.0,
        "p95": 75.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 2,
        "min": 1983.0,
        "median": 2056.5,
        "p90": 2130.0,
        "p95": 2130.0,
        "max": 2130.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 2,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 3.172,
    "throughput_per_second": 0.631,
    "successes": 2,
    "failures": 0,
    "terminal_seconds": {
      "count": 2,
      "min": 3.125,
      "median": 3.141,
      "p90": 3.156,
      "p95": 3.156,
      "max": 3.156
    },
    "accept_seconds": {
      "count": 2,
      "min": 0.313,
      "median": 0.313,
      "p90": 0.313,
      "p95": 0.313,
      "max": 0.313
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-2": 2
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 2,
        "min": 40.0,
        "median": 40.5,
        "p90": 41.0,
        "p95": 41.0,
        "max": 41.0
      },
      "docker_input_copy_ms": {
        "count": 2,
        "min": 6.0,
        "median": 6.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 2,
        "min": 1243.0,
        "median": 1266.0,
        "p90": 1289.0,
        "p95": 1289.0,
        "max": 1289.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 2,
        "min": 1527.0,
        "median": 1541.0,
        "p90": 1555.0,
        "p95": 1555.0,
        "max": 1555.0
      },
      "orchestrator_claim_ms": {
        "count": 2,
        "min": 6.0,
        "median": 6.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 2,
        "min": 4.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 2,
        "min": 246.0,
        "median": 248.5,
        "p90": 251.0,
        "p95": 251.0,
        "max": 251.0
      },
      "runner_module_imports_ms": {
        "count": 2,
        "min": 385.0,
        "median": 387.5,
        "p90": 390.0,
        "p95": 390.0,
        "max": 390.0
      },
      "runner_result_serialize_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 2,
        "min": 633.0,
        "median": 637.0,
        "p90": 641.0,
        "p95": 641.0,
        "max": 641.0
      },
      "sandbox_prepare_ms": {
        "count": 2,
        "min": 23.0,
        "median": 23.5,
        "p90": 24.0,
        "p95": 24.0,
        "max": 24.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 336.0,
        "median": 351.5,
        "p90": 367.0,
        "p95": 367.0,
        "max": 367.0
      },
      "warm_pool_release_ms": {
        "count": 2,
        "min": 182.0,
        "median": 194.5,
        "p90": 207.0,
        "p95": 207.0,
        "max": 207.0
      },
      "warm_runner_exec_ms": {
        "count": 2,
        "min": 757.0,
        "median": 765.5,
        "p90": 774.0,
        "p95": 774.0,
        "max": 774.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 2,
        "min": 76.0,
        "median": 79.5,
        "p90": 83.0,
        "p95": 83.0,
        "max": 83.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 2,
        "min": 76.0,
        "median": 76.0,
        "p90": 76.0,
        "p95": 76.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 2,
        "min": 1543.0,
        "median": 1556.0,
        "p90": 1569.0,
        "p95": 1569.0,
        "max": 1569.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 2,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 3.812,
    "throughput_per_second": 0.525,
    "successes": 2,
    "failures": 0,
    "terminal_seconds": {
      "count": 2,
      "min": 3.172,
      "median": 3.195,
      "p90": 3.218,
      "p95": 3.218,
      "max": 3.218
    },
    "accept_seconds": {
      "count": 2,
      "min": 0.328,
      "median": 0.328,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.328
    },
    "output_download_seconds": {
      "count": 2,
      "min": 0.297,
      "median": 0.297,
      "p90": 0.297,
      "p95": 0.297,
      "max": 0.297
    },
    "workers": {
      "worker-1": 2
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 2,
        "min": 258.0,
        "median": 269.0,
        "p90": 280.0,
        "p95": 280.0,
        "max": 280.0
      },
      "docker_image_pull_ms": {
        "count": 2,
        "min": 44.0,
        "median": 46.0,
        "p90": 48.0,
        "p95": 48.0,
        "max": 48.0
      },
      "docker_input_copy_ms": {
        "count": 2,
        "min": 6.0,
        "median": 7.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 2,
        "min": 987.0,
        "median": 1040.5,
        "p90": 1094.0,
        "p95": 1094.0,
        "max": 1094.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 2,
        "min": 1564.0,
        "median": 1599.5,
        "p90": 1635.0,
        "p95": 1635.0,
        "max": 1635.0
      },
      "orchestrator_claim_ms": {
        "count": 2,
        "min": 5.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 2,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 2,
        "min": 31.0,
        "median": 33.0,
        "p90": 35.0,
        "p95": 35.0,
        "max": 35.0
      },
      "output_validation_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 2,
        "min": 338.0,
        "median": 385.5,
        "p90": 433.0,
        "p95": 433.0,
        "max": 433.0
      },
      "runner_result_serialize_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 2,
        "min": 339.0,
        "median": 386.5,
        "p90": 434.0,
        "p95": 434.0,
        "max": 434.0
      },
      "sandbox_prepare_ms": {
        "count": 2,
        "min": 30.0,
        "median": 32.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 34.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 383.0,
        "median": 384.5,
        "p90": 386.0,
        "p95": 386.0,
        "max": 386.0
      },
      "warm_pool_release_ms": {
        "count": 2,
        "min": 163.0,
        "median": 179.5,
        "p90": 196.0,
        "p95": 196.0,
        "max": 196.0
      },
      "warm_runner_exec_ms": {
        "count": 2,
        "min": 452.0,
        "median": 496.0,
        "p90": 540.0,
        "p95": 540.0,
        "max": 540.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 2,
        "min": 63.0,
        "median": 74.5,
        "p90": 86.0,
        "p95": 86.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 2,
        "min": 64.0,
        "median": 73.5,
        "p90": 83.0,
        "p95": 83.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 2,
        "min": 1580.0,
        "median": 1614.5,
        "p90": 1649.0,
        "p95": 1649.0,
        "max": 1649.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 2,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 3.375,
    "throughput_per_second": 0.593,
    "successes": 2,
    "failures": 0,
    "terminal_seconds": {
      "count": 2,
      "min": 2.907,
      "median": 2.907,
      "p90": 2.907,
      "p95": 2.907,
      "max": 2.907
    },
    "accept_seconds": {
      "count": 2,
      "min": 0.266,
      "median": 0.274,
      "p90": 0.282,
      "p95": 0.282,
      "max": 0.282
    },
    "output_download_seconds": {
      "count": 2,
      "min": 0.25,
      "median": 0.25,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
    },
    "workers": {
      "worker-2": 2
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 2,
        "min": 268.0,
        "median": 278.5,
        "p90": 289.0,
        "p95": 289.0,
        "max": 289.0
      },
      "docker_image_pull_ms": {
        "count": 2,
        "min": 33.0,
        "median": 33.5,
        "p90": 34.0,
        "p95": 34.0,
        "max": 34.0
      },
      "docker_input_copy_ms": {
        "count": 2,
        "min": 6.0,
        "median": 6.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 2,
        "min": 1015.0,
        "median": 1040.5,
        "p90": 1066.0,
        "p95": 1066.0,
        "max": 1066.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 2,
        "min": 1625.0,
        "median": 1632.5,
        "p90": 1640.0,
        "p95": 1640.0,
        "max": 1640.0
      },
      "orchestrator_claim_ms": {
        "count": 2,
        "min": 3.0,
        "median": 4.5,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "orchestrator_completion_ms": {
        "count": 2,
        "min": 8.0,
        "median": 8.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 2,
        "min": 33.0,
        "median": 35.5,
        "p90": 38.0,
        "p95": 38.0,
        "max": 38.0
      },
      "output_validation_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 2,
        "min": 367.0,
        "median": 387.5,
        "p90": 408.0,
        "p95": 408.0,
        "max": 408.0
      },
      "runner_result_serialize_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 2,
        "min": 368.0,
        "median": 388.5,
        "p90": 409.0,
        "p95": 409.0,
        "max": 409.0
      },
      "sandbox_prepare_ms": {
        "count": 2,
        "min": 48.0,
        "median": 48.5,
        "p90": 49.0,
        "p95": 49.0,
        "max": 49.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 367.0,
        "median": 368.5,
        "p90": 370.0,
        "p95": 370.0,
        "max": 370.0
      },
      "warm_pool_release_ms": {
        "count": 2,
        "min": 165.0,
        "median": 194.5,
        "p90": 224.0,
        "p95": 224.0,
        "max": 224.0
      },
      "warm_runner_exec_ms": {
        "count": 2,
        "min": 480.0,
        "median": 501.0,
        "p90": 522.0,
        "p95": 522.0,
        "max": 522.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 2,
        "min": 78.0,
        "median": 80.5,
        "p90": 83.0,
        "p95": 83.0,
        "max": 83.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 2,
        "min": 72.0,
        "median": 80.0,
        "p90": 88.0,
        "p95": 88.0,
        "max": 88.0
      },
      "worker_process_total_ms": {
        "count": 2,
        "min": 1644.0,
        "median": 1648.5,
        "p90": 1653.0,
        "p95": 1653.0,
        "max": 1653.0
      }
    }
  }
]
```
