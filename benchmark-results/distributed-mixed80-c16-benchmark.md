# Distributed Platform Benchmark

Generated: 2026-08-31T20:27:04.908278+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- It is not worker execution concurrency. Worker execution concurrency was held constant during this run; the deployed workers reported `max_invocation_concurrency: 2`.
- Use this report to understand saturation, queueing, throughput ceilings, and user-visible latency under request pressure. Use a separate worker-concurrency benchmark when tuning how many jobs each worker can execute at once.
- The embedded JSON still uses the historical field name `"concurrency"`; in this report that field means saturation/client-side concurrency.

## Built Functions

- `tiny`: function `32`, version `32`, image `10.42.1.22:5000/functions/bench-tiny-57580412:v32-v1-a1-6b828c4cd0ce-d1`
- `sleep`: function `33`, version `33`, image `10.42.1.22:5000/functions/bench-sleep-5be9d7af:v33-v1-a1-01aaf848252b-d1`
- `dependency`: function `34`, version `34`, image `10.42.1.22:5000/functions/bench-dependency-8147c0c6:v34-v1-a1-6518653912fc-d1`
- `output`: function `35`, version `35`, image `10.42.1.22:5000/functions/bench-output-84b15bf6:v35-v1-a1-865294e3b83c-d1`
- `input_output`: function `36`, version `36`, image `10.42.1.22:5000/functions/bench-input_output-6327909c:v36-v1-a1-ba849f4e3226-d1`

## Run Summary

| Scenario | Count | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mixed-80 | 80 | 16 | 1 | 80 | 0 | 31.141 | 2.569 | 5.328 | 8.437 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 16 | 2 | 80 | 0 | 31.328 | 2.554 | 5.508 | 7.797 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 16 | 3 | 80 | 0 | 29.031 | 2.756 | 5.024 | 7.781 | worker-1:41, worker-2:39 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 16,
    "repeat": 1,
    "wall_seconds": 31.141,
    "throughput_per_second": 2.569,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.641,
      "median": 5.328,
      "p90": 7.641,
      "p95": 8.437,
      "max": 8.844
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.141,
      "median": 0.219,
      "p90": 0.797,
      "p95": 1.0,
      "max": 1.11
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.172,
      "median": 0.25,
      "p90": 0.297,
      "p95": 0.313,
      "max": 0.313
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 42,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 281.0,
        "max": 316.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 25.0,
        "p90": 45.0,
        "p95": 131.0,
        "max": 218.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 8.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 518.0,
        "median": 903.0,
        "p90": 1958.0,
        "p95": 2039.0,
        "max": 2122.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 576.0,
        "median": 1115.0,
        "p90": 2089.0,
        "p95": 2205.0,
        "max": 2377.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 12.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 22.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 47.0,
        "max": 135.0
      },
      "output_validation_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_event_load_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 217.0,
        "max": 297.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 340.0,
        "median": 409.0,
        "p90": 476.0,
        "p95": 495.0,
        "max": 526.0
      },
      "runner_result_serialize_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 340.0,
        "median": 443.5,
        "p90": 1396.0,
        "p95": 1428.0,
        "max": 1513.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 21.0,
        "median": 46.0,
        "p90": 120.0,
        "p95": 138.0,
        "max": 321.0
      },
      "warm_container_create_ms": {
        "count": 42,
        "min": 229.0,
        "median": 271.5,
        "p90": 317.0,
        "p95": 323.0,
        "max": 358.0
      },
      "warm_container_reused": {
        "count": 38,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 170.0,
        "p95": 175.0,
        "max": 337.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 431.0,
        "median": 553.0,
        "p90": 1498.0,
        "p95": 1553.0,
        "max": 1629.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 54.0,
        "median": 68.0,
        "p90": 83.0,
        "p95": 88.0,
        "max": 107.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 54.0,
        "median": 69.0,
        "p90": 82.0,
        "p95": 92.0,
        "max": 99.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 589.0,
        "median": 1133.5,
        "p90": 2102.0,
        "p95": 2227.0,
        "max": 2401.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 16,
    "repeat": 2,
    "wall_seconds": 31.328,
    "throughput_per_second": 2.554,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.797,
      "median": 5.508,
      "p90": 7.516,
      "p95": 7.797,
      "max": 8.735
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.219,
      "p90": 0.438,
      "p95": 0.531,
      "max": 0.828
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.172,
      "median": 0.234,
      "p90": 0.265,
      "p95": 0.391,
      "max": 0.391
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 43,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 263.0,
        "max": 338.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 29.0,
        "p90": 42.0,
        "p95": 45.0,
        "max": 60.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 545.0,
        "median": 905.0,
        "p90": 1912.0,
        "p95": 2051.0,
        "max": 2124.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 608.0,
        "median": 1158.0,
        "p90": 2029.0,
        "p95": 2156.0,
        "max": 2343.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 13.0,
        "max": 22.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 22.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 41.0,
        "max": 247.0
      },
      "output_validation_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_environment_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1002.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 2.0,
        "p95": 236.0,
        "max": 318.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 339.0,
        "median": 408.0,
        "p90": 489.0,
        "p95": 512.0,
        "max": 558.0
      },
      "runner_result_serialize_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 340.0,
        "median": 449.0,
        "p90": 1404.0,
        "p95": 1454.0,
        "max": 1553.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 21.0,
        "median": 47.0,
        "p90": 166.0,
        "p95": 251.0,
        "max": 520.0
      },
      "warm_container_create_ms": {
        "count": 43,
        "min": 217.0,
        "median": 269.0,
        "p90": 301.0,
        "p95": 310.0,
        "max": 358.0
      },
      "warm_container_reused": {
        "count": 37,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 80,
        "min": 0.0,
        "median": 61.0,
        "p90": 170.0,
        "p95": 193.0,
        "max": 304.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 429.0,
        "median": 555.5,
        "p90": 1503.0,
        "p95": 1579.0,
        "max": 1671.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 52.0,
        "median": 68.0,
        "p90": 83.0,
        "p95": 85.0,
        "max": 104.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 69.0,
        "p90": 89.0,
        "p95": 95.0,
        "max": 118.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 622.0,
        "median": 1175.5,
        "p90": 2044.0,
        "p95": 2171.0,
        "max": 2368.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 16,
    "repeat": 3,
    "wall_seconds": 29.031,
    "throughput_per_second": 2.756,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 2.125,
      "median": 5.024,
      "p90": 7.468,
      "p95": 7.781,
      "max": 8.766
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.484,
      "p95": 0.656,
      "max": 0.828
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.171,
      "p90": 0.203,
      "p95": 0.219,
      "max": 0.219
    },
    "workers": {
      "worker-1": 41,
      "worker-2": 39
    },
    "cold_starts": 36,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 247.0,
        "max": 288.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 43.0,
        "max": 53.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 8.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 500.0,
        "median": 867.0,
        "p90": 1920.0,
        "p95": 1978.0,
        "max": 2423.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 557.0,
        "median": 1078.0,
        "p90": 2039.0,
        "p95": 2078.0,
        "max": 2593.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 12.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 22.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 50.0,
        "max": 274.0
      },
      "output_validation_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 3.0,
        "p95": 205.0,
        "max": 288.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 332.0,
        "median": 399.0,
        "p90": 482.0,
        "p95": 498.0,
        "max": 547.0
      },
      "runner_result_serialize_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 333.0,
        "median": 435.5,
        "p90": 1395.0,
        "p95": 1417.0,
        "max": 1480.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 21.0,
        "median": 42.0,
        "p90": 249.0,
        "p95": 465.0,
        "max": 570.0
      },
      "warm_container_create_ms": {
        "count": 36,
        "min": 214.0,
        "median": 262.5,
        "p90": 304.0,
        "p95": 305.0,
        "max": 322.0
      },
      "warm_container_reused": {
        "count": 44,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 166.0,
        "p95": 173.0,
        "max": 185.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 418.0,
        "median": 539.0,
        "p90": 1509.0,
        "p95": 1527.0,
        "max": 1626.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 67.0,
        "p90": 84.0,
        "p95": 90.0,
        "max": 103.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 54.0,
        "median": 68.0,
        "p90": 88.0,
        "p95": 98.0,
        "max": 111.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 572.0,
        "median": 1089.5,
        "p90": 2056.0,
        "p95": 2092.0,
        "max": 2610.0
      }
    }
  }
]
```
