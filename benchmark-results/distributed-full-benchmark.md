# Distributed Platform Benchmark

Generated: 2026-08-31T19:47:10.871388+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- It is not worker execution concurrency. Worker execution concurrency was held constant during these runs; the deployed workers reported `max_invocation_concurrency: 2`.
- Use this report to understand saturation, queueing, throughput ceilings, and user-visible latency under request pressure. Use a separate worker-concurrency benchmark when tuning how many jobs each worker can execute at once.
- The embedded JSON still uses the historical field name `"concurrency"`; in this report that field means saturation/client-side concurrency.

## Built Functions

- `tiny`: function `22`, version `22`, image `10.42.1.22:5000/functions/bench-tiny-da38c273:v22-v1-a1-2c73acf36721-d1`
- `sleep`: function `23`, version `23`, image `10.42.1.22:5000/functions/bench-sleep-3c6aba6a:v23-v1-a1-c6e119cbd315-d1`
- `dependency`: function `24`, version `24`, image `10.42.1.22:5000/functions/bench-dependency-dbb79c6d:v24-v1-a1-5da6732cb5eb-d1`
- `output`: function `25`, version `25`, image `10.42.1.22:5000/functions/bench-output-dad34243:v25-v1-a1-1ae69f75a2ed-d1`
- `input_output`: function `26`, version `26`, image `10.42.1.22:5000/functions/bench-input_output-23085f2d:v26-v1-a1-ee1afcfffe0e-d1`

## Run Summary

| Scenario | Count | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| single-tiny | 12 | 2 | 1 | 12 | 0 | 11.844 | 1.013 | 1.5 | 3.047 | worker-1:5, worker-2:7 |
| single-tiny | 12 | 2 | 2 | 12 | 0 | 9.297 | 1.291 | 1.5 | 1.641 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 2 | 3 | 12 | 0 | 11.875 | 1.011 | 1.742 | 2.187 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 4 | 1 | 12 | 0 | 6.437 | 1.864 | 1.726 | 2.969 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 4 | 2 | 12 | 0 | 8.563 | 1.401 | 2.289 | 2.969 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 4 | 3 | 12 | 0 | 8.609 | 1.394 | 2.602 | 3.031 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 8 | 1 | 12 | 0 | 4.391 | 2.733 | 1.859 | 3.156 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 8 | 2 | 12 | 0 | 8.328 | 1.441 | 2.383 | 4.125 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 8 | 3 | 12 | 0 | 4.687 | 2.56 | 2.234 | 3.047 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 2 | 1 | 12 | 0 | 17.609 | 0.681 | 2.688 | 4.046 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 2 | 2 | 12 | 0 | 17.172 | 0.699 | 2.704 | 2.953 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 2 | 3 | 12 | 0 | 19.969 | 0.601 | 3.203 | 3.687 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 4 | 1 | 12 | 0 | 10.141 | 1.183 | 3.0 | 3.359 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 4 | 2 | 12 | 0 | 10.235 | 1.172 | 2.922 | 3.735 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 4 | 3 | 12 | 0 | 9.468 | 1.267 | 2.711 | 3.859 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 8 | 1 | 12 | 0 | 7.453 | 1.61 | 3.883 | 5.156 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 8 | 2 | 12 | 0 | 8.172 | 1.468 | 4.235 | 5.235 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 8 | 3 | 12 | 0 | 8.063 | 1.488 | 3.914 | 5.453 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 2 | 1 | 12 | 0 | 17.531 | 0.685 | 1.633 | 7.25 | worker-1:5, worker-2:7 |
| single-dependency | 12 | 2 | 2 | 12 | 0 | 11.016 | 1.089 | 1.562 | 1.672 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 2 | 3 | 12 | 0 | 10.187 | 1.178 | 1.61 | 1.984 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 4 | 1 | 12 | 0 | 7.312 | 1.641 | 2.289 | 3.328 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 4 | 2 | 12 | 0 | 6.25 | 1.92 | 1.594 | 2.828 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 4 | 3 | 12 | 0 | 7.735 | 1.551 | 2.344 | 2.765 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 8 | 1 | 12 | 0 | 6.172 | 1.944 | 3.086 | 4.375 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 8 | 2 | 12 | 0 | 5.781 | 2.076 | 2.75 | 2.984 | worker-1:7, worker-2:5 |
| single-dependency | 12 | 8 | 3 | 12 | 0 | 4.859 | 2.47 | 2.719 | 3.938 | worker-1:6, worker-2:6 |
| single-output | 12 | 2 | 1 | 12 | 0 | 14.219 | 0.844 | 2.039 | 2.641 | worker-1:5, worker-2:7 |
| single-output | 12 | 2 | 2 | 12 | 0 | 16.265 | 0.738 | 2.265 | 2.782 | worker-1:5, worker-2:7 |
| single-output | 12 | 2 | 3 | 12 | 0 | 19.86 | 0.604 | 1.898 | 3.079 | worker-1:5, worker-2:7 |
| single-output | 12 | 4 | 1 | 12 | 0 | 8.125 | 1.477 | 2.11 | 2.75 | worker-1:6, worker-2:6 |
| single-output | 12 | 4 | 2 | 12 | 0 | 9.079 | 1.322 | 2.109 | 2.782 | worker-1:6, worker-2:6 |
| single-output | 12 | 4 | 3 | 12 | 0 | 8.359 | 1.436 | 1.695 | 2.828 | worker-1:6, worker-2:6 |
| single-output | 12 | 8 | 1 | 12 | 0 | 8.719 | 1.376 | 3.032 | 4.266 | worker-1:6, worker-2:6 |
| single-output | 12 | 8 | 2 | 12 | 0 | 7.89 | 1.521 | 2.938 | 3.532 | worker-1:6, worker-2:6 |
| single-output | 12 | 8 | 3 | 12 | 0 | 8.281 | 1.449 | 3.117 | 3.453 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 2 | 1 | 8 | 4 | 14.813 | 0.54 | 2.469 | 3.641 | worker-1:4, worker-2:4 |
| single-input_output | 12 | 2 | 2 | 0 | 12 | 1.172 | 0.0 |  |  |  |
| single-input_output | 12 | 2 | 3 | 0 | 12 | 0.907 | 0.0 |  |  |  |
| single-input_output | 12 | 4 | 1 | 0 | 12 | 0.625 | 0.0 |  |  |  |
| single-input_output | 12 | 4 | 2 | 0 | 12 | 1.141 | 0.0 |  |  |  |
| single-input_output | 12 | 4 | 3 | 0 | 12 | 2.813 | 0.0 |  |  |  |

## Detailed JSON Summary

```json
[
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 11.844,
    "throughput_per_second": 1.013,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.5,
      "p90": 3.047,
      "p95": 3.047,
      "max": 3.078
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.179,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.359
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
    },
    "cold_starts": 5,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 182.0,
        "p95": 182.0,
        "max": 339.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 509.0,
        "median": 663.0,
        "p90": 1029.0,
        "p95": 1029.0,
        "max": 1232.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 566.0,
        "median": 730.5,
        "p90": 1263.0,
        "p95": 1263.0,
        "max": 1293.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 336.0,
        "median": 368.5,
        "p90": 441.0,
        "p95": 441.0,
        "max": 445.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 337.0,
        "median": 369.0,
        "p90": 442.0,
        "p95": 442.0,
        "max": 446.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 24.5,
        "p90": 31.0,
        "p95": 31.0,
        "max": 33.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 289.0,
        "median": 297.0,
        "p90": 359.0,
        "p95": 359.0,
        "max": 359.0
      },
      "warm_container_reused": {
        "count": 7,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 146.0,
        "p95": 146.0,
        "max": 163.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 426.0,
        "median": 484.5,
        "p90": 540.0,
        "p95": 540.0,
        "max": 566.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 64.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 69.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 578.0,
        "median": 745.5,
        "p90": 1278.0,
        "p95": 1278.0,
        "max": 1309.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 9.297,
    "throughput_per_second": 1.291,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.5,
      "p90": 1.641,
      "p95": 1.641,
      "max": 1.75
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.188
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 0,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 512.0,
        "median": 564.5,
        "p90": 619.0,
        "p95": 619.0,
        "max": 632.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 568.0,
        "median": 624.5,
        "p90": 686.0,
        "p95": 686.0,
        "max": 691.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 334.0,
        "median": 369.5,
        "p90": 410.0,
        "p95": 410.0,
        "max": 421.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 334.0,
        "median": 370.5,
        "p90": 411.0,
        "p95": 411.0,
        "max": 422.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 32.0,
        "p90": 55.0,
        "p95": 55.0,
        "max": 55.0
      },
      "warm_container_reused": {
        "count": 12,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 416.0,
        "median": 469.0,
        "p90": 508.0,
        "p95": 508.0,
        "max": 529.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 59.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 84.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 582.0,
        "median": 636.5,
        "p90": 704.0,
        "p95": 704.0,
        "max": 704.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 11.875,
    "throughput_per_second": 1.011,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.438,
      "median": 1.742,
      "p90": 2.187,
      "p95": 2.187,
      "max": 3.391
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.242,
      "p90": 0.36,
      "p95": 0.36,
      "max": 0.531
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 0,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 511.0,
        "median": 554.5,
        "p90": 604.0,
        "p95": 604.0,
        "max": 612.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 567.0,
        "median": 615.5,
        "p90": 664.0,
        "p95": 664.0,
        "max": 672.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 342.0,
        "median": 366.0,
        "p90": 399.0,
        "p95": 399.0,
        "max": 407.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 342.0,
        "median": 366.0,
        "p90": 400.0,
        "p95": 400.0,
        "max": 408.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 25.5,
        "p90": 33.0,
        "p95": 33.0,
        "max": 37.0
      },
      "warm_container_reused": {
        "count": 12,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 428.0,
        "median": 459.0,
        "p90": 495.0,
        "p95": 495.0,
        "max": 512.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 581.0,
        "median": 628.0,
        "p90": 676.0,
        "p95": 676.0,
        "max": 687.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 6.437,
    "throughput_per_second": 1.864,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.454,
      "median": 1.726,
      "p90": 2.969,
      "p95": 2.969,
      "max": 3.0
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.265,
      "p95": 0.265,
      "max": 0.421
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 517.0,
        "median": 635.5,
        "p90": 931.0,
        "p95": 931.0,
        "max": 959.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 577.0,
        "median": 699.0,
        "p90": 1142.0,
        "p95": 1142.0,
        "max": 1191.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 340.0,
        "median": 371.5,
        "p90": 429.0,
        "p95": 429.0,
        "max": 461.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 340.0,
        "median": 372.5,
        "p90": 430.0,
        "p95": 430.0,
        "max": 462.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 30.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 64.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 261.0,
        "median": 311.0,
        "p90": 345.0,
        "p95": 345.0,
        "max": 345.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 149.0,
        "p95": 149.0,
        "max": 168.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 426.0,
        "median": 470.0,
        "p90": 534.0,
        "p95": 534.0,
        "max": 558.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 61.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 68.0,
        "p90": 80.0,
        "p95": 80.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 588.0,
        "median": 716.5,
        "p90": 1162.0,
        "p95": 1162.0,
        "max": 1210.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 8.563,
    "throughput_per_second": 1.401,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.609,
      "median": 2.289,
      "p90": 2.969,
      "p95": 2.969,
      "max": 3.0
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.243,
      "p90": 0.547,
      "p95": 0.547,
      "max": 1.281
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 47.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 565.0,
        "median": 651.0,
        "p90": 953.0,
        "p95": 953.0,
        "max": 1001.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 626.0,
        "median": 724.5,
        "p90": 1171.0,
        "p95": 1171.0,
        "max": 1211.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 367.0,
        "median": 404.5,
        "p90": 482.0,
        "p95": 482.0,
        "max": 496.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 368.0,
        "median": 405.5,
        "p90": 483.0,
        "p95": 483.0,
        "max": 497.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 27.0,
        "p90": 48.0,
        "p95": 48.0,
        "max": 50.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 258.0,
        "median": 291.5,
        "p90": 295.0,
        "p95": 295.0,
        "max": 295.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 147.0,
        "p95": 147.0,
        "max": 152.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 458.0,
        "median": 506.5,
        "p90": 589.0,
        "p95": 589.0,
        "max": 606.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 64.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 63.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 88.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 639.0,
        "median": 740.5,
        "p90": 1181.0,
        "p95": 1181.0,
        "max": 1227.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 8.609,
    "throughput_per_second": 1.394,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.672,
      "median": 2.602,
      "p90": 3.031,
      "p95": 3.031,
      "max": 3.203
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.188,
      "median": 0.266,
      "p90": 0.953,
      "p95": 0.953,
      "max": 1.016
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 48.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 517.0,
        "median": 641.0,
        "p90": 947.0,
        "p95": 947.0,
        "max": 1024.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 573.0,
        "median": 725.5,
        "p90": 1165.0,
        "p95": 1165.0,
        "max": 1225.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 335.0,
        "median": 381.5,
        "p90": 453.0,
        "p95": 453.0,
        "max": 524.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 335.0,
        "median": 382.5,
        "p90": 454.0,
        "p95": 454.0,
        "max": 526.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 32.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 63.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 271.0,
        "median": 321.0,
        "p90": 325.0,
        "p95": 325.0,
        "max": 325.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 144.0,
        "p95": 144.0,
        "max": 145.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 421.0,
        "median": 486.5,
        "p90": 550.0,
        "p95": 550.0,
        "max": 625.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 61.5,
        "p90": 93.0,
        "p95": 93.0,
        "max": 100.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 65.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 586.0,
        "median": 744.5,
        "p90": 1182.0,
        "p95": 1182.0,
        "max": 1238.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 4.391,
    "throughput_per_second": 2.733,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.578,
      "median": 1.859,
      "p90": 3.156,
      "p95": 3.156,
      "max": 3.219
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.282,
      "p90": 0.359,
      "p95": 0.359,
      "max": 1.172
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 24.0,
        "p95": 24.0,
        "max": 31.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 548.0,
        "median": 621.0,
        "p90": 876.0,
        "p95": 876.0,
        "max": 1017.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 624.0,
        "median": 767.5,
        "p90": 944.0,
        "p95": 944.0,
        "max": 1084.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 8.5,
        "p90": 12.0,
        "p95": 12.0,
        "max": 26.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 340.0,
        "median": 391.0,
        "p90": 464.0,
        "p95": 464.0,
        "max": 482.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 341.0,
        "median": 392.0,
        "p90": 464.0,
        "p95": 464.0,
        "max": 483.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 28.5,
        "p90": 174.0,
        "p95": 174.0,
        "max": 195.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 295.0,
        "median": 330.0,
        "p90": 365.0,
        "p95": 365.0,
        "max": 365.0
      },
      "warm_container_reused": {
        "count": 10,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 152.0,
        "p95": 152.0,
        "max": 178.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 427.0,
        "median": 486.5,
        "p90": 583.0,
        "p95": 583.0,
        "max": 586.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 64.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 67.0,
        "p90": 81.0,
        "p95": 81.0,
        "max": 85.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 639.0,
        "median": 786.0,
        "p90": 963.0,
        "p95": 963.0,
        "max": 1116.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 8.328,
    "throughput_per_second": 1.441,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.687,
      "median": 2.383,
      "p90": 4.125,
      "p95": 4.125,
      "max": 6.641
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.187,
      "median": 0.305,
      "p90": 0.953,
      "p95": 0.953,
      "max": 1.0
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 31.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 530.0,
        "median": 666.5,
        "p90": 930.0,
        "p95": 930.0,
        "max": 1041.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 588.0,
        "median": 765.5,
        "p90": 1004.0,
        "p95": 1004.0,
        "max": 1113.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 348.0,
        "median": 414.0,
        "p90": 461.0,
        "p95": 461.0,
        "max": 471.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 349.0,
        "median": 414.0,
        "p90": 462.0,
        "p95": 462.0,
        "max": 472.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 33.5,
        "p90": 95.0,
        "p95": 95.0,
        "max": 112.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 325.0,
        "median": 334.0,
        "p90": 343.0,
        "p95": 343.0,
        "max": 343.0
      },
      "warm_container_reused": {
        "count": 10,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 153.0,
        "p95": 153.0,
        "max": 161.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 440.0,
        "median": 514.0,
        "p90": 577.0,
        "p95": 577.0,
        "max": 584.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 69.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 58.0,
        "median": 68.0,
        "p90": 85.0,
        "p95": 85.0,
        "max": 88.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 599.0,
        "median": 777.0,
        "p90": 1024.0,
        "p95": 1024.0,
        "max": 1129.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 4.687,
    "throughput_per_second": 2.56,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.546,
      "median": 2.234,
      "p90": 3.047,
      "p95": 3.047,
      "max": 3.375
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.219,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.343
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 48.0,
        "p95": 48.0,
        "max": 48.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 531.0,
        "median": 684.5,
        "p90": 970.0,
        "p95": 970.0,
        "max": 1044.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 588.0,
        "median": 785.0,
        "p90": 1079.0,
        "p95": 1079.0,
        "max": 1121.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 345.0,
        "median": 413.0,
        "p90": 455.0,
        "p95": 455.0,
        "max": 519.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 346.0,
        "median": 413.0,
        "p90": 456.0,
        "p95": 456.0,
        "max": 520.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 31.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 87.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 273.0,
        "median": 310.0,
        "p90": 344.0,
        "p95": 344.0,
        "max": 344.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 146.0,
        "p95": 146.0,
        "max": 169.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 447.0,
        "median": 512.5,
        "p90": 588.0,
        "p95": 588.0,
        "max": 633.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 70.0,
        "p90": 85.0,
        "p95": 85.0,
        "max": 97.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 71.0,
        "p90": 81.0,
        "p95": 81.0,
        "max": 87.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 602.0,
        "median": 800.5,
        "p90": 1093.0,
        "p95": 1093.0,
        "max": 1138.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 17.609,
    "throughput_per_second": 0.681,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.61,
      "median": 2.688,
      "p90": 4.046,
      "p95": 4.046,
      "max": 4.109
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.234,
      "p95": 0.234,
      "max": 0.234
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 6,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 13.0,
        "p90": 414.0,
        "p95": 414.0,
        "max": 418.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1515.0,
        "median": 1777.5,
        "p90": 2364.0,
        "p95": 2364.0,
        "max": 2432.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1571.0,
        "median": 1922.5,
        "p90": 2530.0,
        "p95": 2530.0,
        "max": 2621.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 340.0,
        "median": 367.0,
        "p90": 436.0,
        "p95": 436.0,
        "max": 482.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1341.0,
        "median": 1368.5,
        "p90": 1437.0,
        "p95": 1437.0,
        "max": 1484.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 24.0,
        "p90": 28.0,
        "p95": 28.0,
        "max": 29.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 267.0,
        "median": 286.0,
        "p90": 351.0,
        "p95": 368.0,
        "max": 368.0
      },
      "warm_container_reused": {
        "count": 6,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 154.0,
        "p95": 154.0,
        "max": 177.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1427.0,
        "median": 1472.0,
        "p90": 1557.0,
        "p95": 1557.0,
        "max": 1585.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.5,
        "p90": 81.0,
        "p95": 81.0,
        "max": 97.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 70.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1582.0,
        "median": 1937.0,
        "p90": 2547.0,
        "p95": 2547.0,
        "max": 2634.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 17.172,
    "throughput_per_second": 0.699,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.125,
      "median": 2.704,
      "p90": 2.953,
      "p95": 2.953,
      "max": 3.703
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.281
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 0,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1531.0,
        "median": 1581.5,
        "p90": 1618.0,
        "p95": 1618.0,
        "max": 1638.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1591.0,
        "median": 1641.5,
        "p90": 1679.0,
        "p95": 1679.0,
        "max": 1706.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 353.0,
        "median": 379.0,
        "p90": 396.0,
        "p95": 396.0,
        "max": 421.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1354.0,
        "median": 1380.0,
        "p90": 1398.0,
        "p95": 1398.0,
        "max": 1422.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 27.5,
        "p90": 44.0,
        "p95": 44.0,
        "max": 54.0
      },
      "warm_container_reused": {
        "count": 12,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1445.0,
        "median": 1478.5,
        "p90": 1512.0,
        "p95": 1512.0,
        "max": 1551.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 58.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1603.0,
        "median": 1653.0,
        "p90": 1691.0,
        "p95": 1691.0,
        "max": 1719.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 19.969,
    "throughput_per_second": 0.601,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.438,
      "median": 3.203,
      "p90": 3.687,
      "p95": 3.687,
      "max": 4.235
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.274,
      "p90": 0.984,
      "p95": 0.984,
      "max": 1.157
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
    },
    "cold_starts": 1,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 26.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1518.0,
        "median": 1564.5,
        "p90": 1591.0,
        "p95": 1591.0,
        "max": 1908.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1576.0,
        "median": 1630.0,
        "p90": 1660.0,
        "p95": 1660.0,
        "max": 2127.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 340.0,
        "median": 369.5,
        "p90": 392.0,
        "p95": 392.0,
        "max": 409.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1341.0,
        "median": 1370.5,
        "p90": 1394.0,
        "p95": 1394.0,
        "max": 1411.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 23.0,
        "p90": 44.0,
        "p95": 44.0,
        "max": 45.0
      },
      "warm_container_create_ms": {
        "count": 1,
        "min": 279.0,
        "median": 279.0,
        "p90": 279.0,
        "p95": 279.0,
        "max": 279.0
      },
      "warm_container_reused": {
        "count": 11,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 156.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1427.0,
        "median": 1467.0,
        "p90": 1492.0,
        "p95": 1492.0,
        "max": 1511.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 61.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 78.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1589.0,
        "median": 1644.5,
        "p90": 1678.0,
        "p95": 1678.0,
        "max": 2137.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 10.141,
    "throughput_per_second": 1.183,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.766,
      "median": 3.0,
      "p90": 3.359,
      "p95": 3.359,
      "max": 4.125
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.235,
      "p90": 0.578,
      "p95": 0.578,
      "max": 0.625
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 6,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 13.0,
        "p90": 43.0,
        "p95": 43.0,
        "max": 54.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1537.0,
        "median": 1769.5,
        "p90": 1965.0,
        "p95": 1965.0,
        "max": 2012.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1607.0,
        "median": 1912.0,
        "p90": 2197.0,
        "p95": 2197.0,
        "max": 2242.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 337.0,
        "median": 402.5,
        "p90": 455.0,
        "p95": 455.0,
        "max": 537.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1338.0,
        "median": 1404.0,
        "p90": 1457.0,
        "p95": 1457.0,
        "max": 1539.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 24.5,
        "p90": 42.0,
        "p95": 42.0,
        "max": 47.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 230.0,
        "median": 292.5,
        "p90": 313.0,
        "p95": 361.0,
        "max": 361.0
      },
      "warm_container_reused": {
        "count": 6,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 66.5,
        "p90": 156.0,
        "p95": 156.0,
        "max": 166.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1426.0,
        "median": 1508.0,
        "p90": 1566.0,
        "p95": 1566.0,
        "max": 1644.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 65.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 71.0,
        "p90": 87.0,
        "p95": 87.0,
        "max": 104.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1619.0,
        "median": 1929.0,
        "p90": 2209.0,
        "p95": 2209.0,
        "max": 2263.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 10.235,
    "throughput_per_second": 1.172,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.781,
      "median": 2.922,
      "p90": 3.735,
      "p95": 3.735,
      "max": 4.156
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.211,
      "p90": 0.281,
      "p95": 0.281,
      "max": 0.843
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 6,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 13.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 33.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1519.0,
        "median": 1768.0,
        "p90": 1896.0,
        "p95": 1896.0,
        "max": 1924.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1580.0,
        "median": 1903.5,
        "p90": 2109.0,
        "p95": 2109.0,
        "max": 2150.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 343.0,
        "median": 389.5,
        "p90": 432.0,
        "p95": 432.0,
        "max": 474.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1345.0,
        "median": 1391.0,
        "p90": 1433.0,
        "p95": 1433.0,
        "max": 1476.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 24.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 58.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 240.0,
        "median": 267.5,
        "p90": 289.0,
        "p95": 315.0,
        "max": 315.0
      },
      "warm_container_reused": {
        "count": 6,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 70.5,
        "p90": 150.0,
        "p95": 150.0,
        "max": 158.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1433.0,
        "median": 1484.5,
        "p90": 1566.0,
        "p95": 1566.0,
        "max": 1603.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 61.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 65.5,
        "p90": 77.0,
        "p95": 77.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1594.0,
        "median": 1915.5,
        "p90": 2126.0,
        "p95": 2126.0,
        "max": 2164.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 9.468,
    "throughput_per_second": 1.267,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.625,
      "median": 2.711,
      "p90": 3.859,
      "p95": 3.859,
      "max": 4.203
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.171,
      "p90": 0.265,
      "p95": 0.265,
      "max": 0.562
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 5,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 45.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1537.0,
        "median": 1684.0,
        "p90": 1974.0,
        "p95": 1974.0,
        "max": 1986.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1609.0,
        "median": 1769.0,
        "p90": 2197.0,
        "p95": 2197.0,
        "max": 2201.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 15.0,
        "p95": 15.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 16.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 337.0,
        "median": 401.5,
        "p90": 437.0,
        "p95": 437.0,
        "max": 511.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1338.0,
        "median": 1403.0,
        "p90": 1438.0,
        "p95": 1438.0,
        "max": 1513.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 23.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 84.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 237.0,
        "median": 286.0,
        "p90": 296.0,
        "p95": 296.0,
        "max": 296.0
      },
      "warm_container_reused": {
        "count": 7,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 155.0,
        "p95": 155.0,
        "max": 162.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1429.0,
        "median": 1510.5,
        "p90": 1547.0,
        "p95": 1547.0,
        "max": 1606.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 58.0,
        "median": 65.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 65.5,
        "p90": 78.0,
        "p95": 78.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1618.0,
        "median": 1782.5,
        "p90": 2213.0,
        "p95": 2213.0,
        "max": 2228.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 7.453,
    "throughput_per_second": 1.61,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.89,
      "median": 3.883,
      "p90": 5.156,
      "p95": 5.156,
      "max": 5.843
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.265,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.422
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 33.0,
        "p95": 33.0,
        "max": 45.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1520.0,
        "median": 1633.5,
        "p90": 1857.0,
        "p95": 1857.0,
        "max": 2000.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1633.0,
        "median": 1732.0,
        "p90": 2066.0,
        "p95": 2066.0,
        "max": 2074.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 345.0,
        "median": 384.0,
        "p90": 447.0,
        "p95": 447.0,
        "max": 498.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1346.0,
        "median": 1385.0,
        "p90": 1448.0,
        "p95": 1448.0,
        "max": 1500.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 24.5,
        "p90": 44.0,
        "p95": 44.0,
        "max": 51.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 266.0,
        "median": 278.0,
        "p90": 326.0,
        "p95": 326.0,
        "max": 326.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 161.0,
        "p95": 161.0,
        "max": 170.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1435.0,
        "median": 1484.5,
        "p90": 1546.0,
        "p95": 1546.0,
        "max": 1606.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 64.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 62.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1642.0,
        "median": 1744.5,
        "p90": 2080.0,
        "p95": 2080.0,
        "max": 2091.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 8.172,
    "throughput_per_second": 1.468,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.828,
      "median": 4.235,
      "p90": 5.235,
      "p95": 5.235,
      "max": 5.5
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.398,
      "p90": 0.609,
      "p95": 0.609,
      "max": 0.64
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 30.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1538.0,
        "median": 1658.5,
        "p90": 1888.0,
        "p95": 1888.0,
        "max": 1925.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1633.0,
        "median": 1758.5,
        "p90": 1992.0,
        "p95": 1992.0,
        "max": 2085.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 337.0,
        "median": 411.0,
        "p90": 448.0,
        "p95": 448.0,
        "max": 521.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1338.0,
        "median": 1412.0,
        "p90": 1449.0,
        "p95": 1449.0,
        "max": 1522.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 29.5,
        "p90": 45.0,
        "p95": 45.0,
        "max": 48.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 260.0,
        "median": 310.0,
        "p90": 319.0,
        "p95": 319.0,
        "max": 319.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 154.0,
        "p95": 154.0,
        "max": 185.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1437.0,
        "median": 1507.5,
        "p90": 1560.0,
        "p95": 1560.0,
        "max": 1616.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 62.5,
        "p90": 69.0,
        "p95": 69.0,
        "max": 78.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 60.0,
        "median": 67.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 91.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1647.0,
        "median": 1772.5,
        "p90": 2008.0,
        "p95": 2008.0,
        "max": 2103.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 8.063,
    "throughput_per_second": 1.488,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.86,
      "median": 3.914,
      "p90": 5.453,
      "p95": 5.453,
      "max": 5.797
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.211,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.453
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 42.0,
        "p95": 42.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1527.0,
        "median": 1628.0,
        "p90": 1881.0,
        "p95": 1881.0,
        "max": 2006.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1614.0,
        "median": 1784.0,
        "p90": 2042.0,
        "p95": 2042.0,
        "max": 2084.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 1000.0,
        "median": 1000.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 339.0,
        "median": 376.0,
        "p90": 434.0,
        "p95": 434.0,
        "max": 447.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 1340.0,
        "median": 1377.0,
        "p90": 1436.0,
        "p95": 1436.0,
        "max": 1448.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 26.0,
        "p90": 199.0,
        "p95": 199.0,
        "max": 201.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 259.0,
        "median": 273.0,
        "p90": 319.0,
        "p95": 319.0,
        "max": 319.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 156.0,
        "p95": 156.0,
        "max": 176.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1437.0,
        "median": 1476.5,
        "p90": 1537.0,
        "p95": 1537.0,
        "max": 1539.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 60.0,
        "median": 63.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 65.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1625.0,
        "median": 1798.5,
        "p90": 2059.0,
        "p95": 2059.0,
        "max": 2101.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 17.531,
    "throughput_per_second": 0.685,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.633,
      "p90": 7.25,
      "p95": 7.25,
      "max": 7.265
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.157,
      "p90": 0.234,
      "p95": 0.234,
      "max": 0.36
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
    },
    "cold_starts": 5,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 1975.0,
        "p95": 1975.0,
        "max": 5128.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 677.0,
        "median": 905.5,
        "p90": 6050.0,
        "p95": 6050.0,
        "max": 6227.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 732.0,
        "median": 1072.5,
        "p90": 6268.0,
        "p95": 6268.0,
        "max": 6294.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 165.0,
        "median": 199.0,
        "p90": 272.0,
        "p95": 272.0,
        "max": 273.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 363.0,
        "p90": 423.0,
        "p95": 423.0,
        "max": 479.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 496.0,
        "median": 578.5,
        "p90": 697.0,
        "p95": 697.0,
        "max": 740.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 25.5,
        "p90": 52.0,
        "p95": 52.0,
        "max": 53.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 287.0,
        "median": 365.0,
        "p90": 3276.0,
        "p95": 3276.0,
        "max": 3276.0
      },
      "warm_container_reused": {
        "count": 7,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 172.0,
        "p95": 172.0,
        "max": 195.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 591.0,
        "median": 698.0,
        "p90": 846.0,
        "p95": 846.0,
        "max": 873.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 64.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 95.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 65.5,
        "p90": 86.0,
        "p95": 86.0,
        "max": 97.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 745.0,
        "median": 1092.0,
        "p90": 6280.0,
        "p95": 6280.0,
        "max": 6308.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 11.016,
    "throughput_per_second": 1.089,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 1.562,
      "p90": 1.672,
      "p95": 1.672,
      "max": 3.266
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.219
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 0,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 675.0,
        "median": 805.5,
        "p90": 878.0,
        "p95": 878.0,
        "max": 926.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 736.0,
        "median": 867.5,
        "p90": 947.0,
        "p95": 947.0,
        "max": 988.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 165.0,
        "median": 178.5,
        "p90": 214.0,
        "p95": 214.0,
        "max": 219.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 329.0,
        "median": 351.5,
        "p90": 435.0,
        "p95": 435.0,
        "max": 457.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 494.0,
        "median": 530.5,
        "p90": 648.0,
        "p95": 648.0,
        "max": 672.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 28.0,
        "p90": 46.0,
        "p95": 46.0,
        "max": 52.0
      },
      "warm_container_reused": {
        "count": 12,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 587.0,
        "median": 632.0,
        "p90": 769.0,
        "p95": 769.0,
        "max": 786.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 60.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 749.0,
        "median": 883.5,
        "p90": 966.0,
        "p95": 966.0,
        "max": 999.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 10.187,
    "throughput_per_second": 1.178,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.5,
      "median": 1.61,
      "p90": 1.984,
      "p95": 1.984,
      "max": 2.078
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.195,
      "p90": 0.578,
      "p95": 0.578,
      "max": 0.641
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 0,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 694.0,
        "median": 744.0,
        "p90": 858.0,
        "p95": 858.0,
        "max": 864.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 749.0,
        "median": 804.5,
        "p90": 917.0,
        "p95": 917.0,
        "max": 934.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 169.0,
        "median": 184.0,
        "p90": 193.0,
        "p95": 193.0,
        "max": 216.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 335.0,
        "median": 361.0,
        "p90": 423.0,
        "p95": 423.0,
        "max": 444.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 505.0,
        "median": 544.0,
        "p90": 630.0,
        "p95": 630.0,
        "max": 640.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 27.5,
        "p90": 41.0,
        "p95": 41.0,
        "max": 44.0
      },
      "warm_container_reused": {
        "count": 12,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 598.0,
        "median": 648.0,
        "p90": 739.0,
        "p95": 739.0,
        "max": 760.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 761.0,
        "median": 819.0,
        "p90": 928.0,
        "p95": 928.0,
        "max": 946.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 7.312,
    "throughput_per_second": 1.641,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 2.289,
      "p90": 3.328,
      "p95": 3.328,
      "max": 3.765
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.344,
      "p90": 1.219,
      "p95": 1.219,
      "max": 1.36
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 39.0,
        "p95": 39.0,
        "max": 45.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 687.0,
        "median": 861.5,
        "p90": 1249.0,
        "p95": 1249.0,
        "max": 1294.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 745.0,
        "median": 977.0,
        "p90": 1389.0,
        "p95": 1389.0,
        "max": 1467.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 168.0,
        "median": 193.5,
        "p90": 234.0,
        "p95": 234.0,
        "max": 311.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 336.0,
        "median": 368.5,
        "p90": 445.0,
        "p95": 445.0,
        "max": 466.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 505.0,
        "median": 576.0,
        "p90": 667.0,
        "p95": 667.0,
        "max": 778.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 26.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 72.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 271.0,
        "median": 320.0,
        "p90": 365.0,
        "p95": 365.0,
        "max": 365.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 150.0,
        "p95": 150.0,
        "max": 159.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 600.0,
        "median": 686.5,
        "p90": 774.0,
        "p95": 774.0,
        "max": 918.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 63.0,
        "p90": 85.0,
        "p95": 85.0,
        "max": 94.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 58.0,
        "median": 64.5,
        "p90": 98.0,
        "p95": 98.0,
        "max": 124.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 756.0,
        "median": 993.5,
        "p90": 1408.0,
        "p95": 1408.0,
        "max": 1478.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 6.25,
    "throughput_per_second": 1.92,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.438,
      "median": 1.594,
      "p90": 2.828,
      "p95": 2.828,
      "max": 2.969
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.219
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 65.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 681.0,
        "median": 863.0,
        "p90": 1191.0,
        "p95": 1191.0,
        "max": 1289.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 740.0,
        "median": 1004.0,
        "p90": 1325.0,
        "p95": 1325.0,
        "max": 1508.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 166.0,
        "median": 203.0,
        "p90": 247.0,
        "p95": 247.0,
        "max": 263.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 332.0,
        "median": 385.0,
        "p90": 448.0,
        "p95": 448.0,
        "max": 457.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 499.0,
        "median": 596.5,
        "p90": 659.0,
        "p95": 659.0,
        "max": 696.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 25.0,
        "p90": 46.0,
        "p95": 46.0,
        "max": 71.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 265.0,
        "median": 269.5,
        "p90": 336.0,
        "p95": 336.0,
        "max": 336.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 158.0,
        "p95": 158.0,
        "max": 161.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 593.0,
        "median": 711.5,
        "p90": 803.0,
        "p95": 803.0,
        "max": 839.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 64.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 101.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 58.0,
        "median": 66.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 751.0,
        "median": 1020.5,
        "p90": 1340.0,
        "p95": 1340.0,
        "max": 1528.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 7.735,
    "throughput_per_second": 1.551,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.562,
      "median": 2.344,
      "p90": 2.765,
      "p95": 2.765,
      "max": 3.391
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.305,
      "p90": 0.625,
      "p95": 0.625,
      "max": 0.703
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 26.0,
        "p95": 26.0,
        "max": 39.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 684.0,
        "median": 823.0,
        "p90": 1093.0,
        "p95": 1093.0,
        "max": 1264.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 739.0,
        "median": 956.5,
        "p90": 1300.0,
        "p95": 1300.0,
        "max": 1356.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 167.0,
        "median": 195.0,
        "p90": 229.0,
        "p95": 229.0,
        "max": 234.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 334.0,
        "median": 384.0,
        "p90": 419.0,
        "p95": 419.0,
        "max": 441.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 505.0,
        "median": 569.5,
        "p90": 641.0,
        "p95": 641.0,
        "max": 671.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 29.5,
        "p90": 50.0,
        "p95": 50.0,
        "max": 60.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 314.0,
        "median": 320.0,
        "p90": 326.0,
        "p95": 326.0,
        "max": 326.0
      },
      "warm_container_reused": {
        "count": 10,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 142.0,
        "p95": 142.0,
        "max": 174.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 599.0,
        "median": 686.5,
        "p90": 794.0,
        "p95": 794.0,
        "max": 800.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 63.5,
        "p90": 92.0,
        "p95": 92.0,
        "max": 99.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 63.0,
        "p90": 84.0,
        "p95": 84.0,
        "max": 84.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 752.0,
        "median": 973.0,
        "p90": 1318.0,
        "p95": 1318.0,
        "max": 1375.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 6.172,
    "throughput_per_second": 1.944,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.687,
      "median": 3.086,
      "p90": 4.375,
      "p95": 4.375,
      "max": 4.468
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.336,
      "p90": 0.64,
      "p95": 0.64,
      "max": 0.812
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 51.0,
        "p95": 51.0,
        "max": 55.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 820.0,
        "median": 987.5,
        "p90": 1170.0,
        "p95": 1170.0,
        "max": 1230.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 917.0,
        "median": 1090.5,
        "p90": 1311.0,
        "p95": 1311.0,
        "max": 1382.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 177.0,
        "median": 230.5,
        "p90": 281.0,
        "p95": 281.0,
        "max": 296.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 342.0,
        "median": 376.0,
        "p90": 467.0,
        "p95": 467.0,
        "max": 488.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 520.0,
        "median": 607.5,
        "p90": 750.0,
        "p95": 750.0,
        "max": 785.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 34.5,
        "p90": 98.0,
        "p95": 98.0,
        "max": 109.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 262.0,
        "median": 290.5,
        "p90": 336.0,
        "p95": 336.0,
        "max": 336.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 149.0,
        "p95": 149.0,
        "max": 164.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 619.0,
        "median": 719.5,
        "p90": 906.0,
        "p95": 906.0,
        "max": 906.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 59.0,
        "median": 68.0,
        "p90": 80.0,
        "p95": 80.0,
        "max": 96.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 68.0,
        "p90": 80.0,
        "p95": 80.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 932.0,
        "median": 1105.5,
        "p90": 1325.0,
        "p95": 1325.0,
        "max": 1396.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 5.781,
    "throughput_per_second": 2.076,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.703,
      "median": 2.75,
      "p90": 2.984,
      "p95": 2.984,
      "max": 4.156
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.227,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.297
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 5
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 52.0,
        "p95": 52.0,
        "max": 61.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 707.0,
        "median": 871.5,
        "p90": 1097.0,
        "p95": 1097.0,
        "max": 1195.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 813.0,
        "median": 969.0,
        "p90": 1167.0,
        "p95": 1167.0,
        "max": 1258.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 14.0,
        "p95": 14.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 171.0,
        "median": 226.0,
        "p90": 263.0,
        "p95": 263.0,
        "max": 288.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 334.0,
        "median": 367.0,
        "p90": 407.0,
        "p95": 407.0,
        "max": 464.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 509.0,
        "median": 592.5,
        "p90": 655.0,
        "p95": 655.0,
        "max": 753.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 32.0,
        "p90": 49.0,
        "p95": 49.0,
        "max": 80.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 253.0,
        "median": 297.0,
        "p90": 333.0,
        "p95": 333.0,
        "max": 333.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 151.0,
        "p95": 151.0,
        "max": 164.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 602.0,
        "median": 708.0,
        "p90": 769.0,
        "p95": 769.0,
        "max": 904.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 65.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 62.0,
        "median": 66.5,
        "p90": 83.0,
        "p95": 83.0,
        "max": 105.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 830.0,
        "median": 987.0,
        "p90": 1189.0,
        "p95": 1189.0,
        "max": 1272.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 4.859,
    "throughput_per_second": 2.47,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.531,
      "median": 2.719,
      "p90": 3.938,
      "p95": 3.938,
      "max": 4.047
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.289,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.422
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 27.0,
        "max": 52.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 758.0,
        "median": 848.5,
        "p90": 1043.0,
        "p95": 1043.0,
        "max": 1225.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 824.0,
        "median": 957.5,
        "p90": 1110.0,
        "p95": 1110.0,
        "max": 1299.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 20.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 23.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 174.0,
        "median": 225.5,
        "p90": 241.0,
        "p95": 241.0,
        "max": 250.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 339.0,
        "median": 383.0,
        "p90": 403.0,
        "p95": 403.0,
        "max": 416.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 532.0,
        "median": 615.5,
        "p90": 643.0,
        "p95": 643.0,
        "max": 652.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 34.5,
        "p90": 91.0,
        "p95": 91.0,
        "max": 108.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 267.0,
        "median": 293.5,
        "p90": 320.0,
        "p95": 320.0,
        "max": 320.0
      },
      "warm_container_reused": {
        "count": 10,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 165.0,
        "p95": 165.0,
        "max": 176.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 637.0,
        "median": 733.5,
        "p90": 763.0,
        "p95": 763.0,
        "max": 794.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 70.5,
        "p90": 98.0,
        "p95": 98.0,
        "max": 108.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 67.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 125.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 834.0,
        "median": 969.0,
        "p90": 1123.0,
        "p95": 1123.0,
        "max": 1315.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 14.219,
    "throughput_per_second": 0.844,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 2.039,
      "p90": 2.641,
      "p95": 2.641,
      "max": 2.672
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.141,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.188
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
    },
    "cold_starts": 5,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 226.0,
        "median": 256.0,
        "p90": 286.0,
        "p95": 286.0,
        "max": 299.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 431.0,
        "p95": 431.0,
        "max": 438.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 14.0,
        "p95": 14.0,
        "max": 17.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 513.0,
        "median": 652.5,
        "p90": 1408.0,
        "p95": 1408.0,
        "max": 1476.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 836.0,
        "median": 1113.5,
        "p90": 1852.0,
        "p95": 1852.0,
        "max": 1968.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 37.0,
        "p90": 39.0,
        "p95": 39.0,
        "max": 42.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 337.0,
        "median": 370.5,
        "p90": 452.0,
        "p95": 452.0,
        "max": 506.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 338.0,
        "median": 371.5,
        "p90": 453.0,
        "p95": 453.0,
        "max": 507.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 25.5,
        "p90": 31.0,
        "p95": 31.0,
        "max": 33.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 280.0,
        "median": 333.0,
        "p90": 367.0,
        "p95": 367.0,
        "max": 367.0
      },
      "warm_container_reused": {
        "count": 7,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 149.0,
        "p95": 149.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 427.0,
        "median": 475.0,
        "p90": 572.0,
        "p95": 572.0,
        "max": 605.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 62.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 64.5,
        "p90": 75.0,
        "p95": 75.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 849.0,
        "median": 1126.5,
        "p90": 1866.0,
        "p95": 1866.0,
        "max": 1986.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 16.265,
    "throughput_per_second": 0.738,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.531,
      "median": 2.265,
      "p90": 2.782,
      "p95": 2.782,
      "max": 2.859
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.188,
      "p90": 0.969,
      "p95": 0.969,
      "max": 1.329
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.781
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
    },
    "cold_starts": 1,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 223.0,
        "median": 241.0,
        "p90": 273.0,
        "p95": 273.0,
        "max": 290.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 39.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 515.0,
        "median": 563.0,
        "p90": 751.0,
        "p95": 751.0,
        "max": 985.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 847.0,
        "median": 907.0,
        "p90": 1329.0,
        "p95": 1329.0,
        "max": 1374.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 36.0,
        "p90": 53.0,
        "p95": 53.0,
        "max": 53.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 342.0,
        "median": 362.0,
        "p90": 426.0,
        "p95": 426.0,
        "max": 546.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 342.0,
        "median": 363.0,
        "p90": 427.0,
        "p95": 427.0,
        "max": 547.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 25.0,
        "p90": 29.0,
        "p95": 29.0,
        "max": 33.0
      },
      "warm_container_create_ms": {
        "count": 1,
        "min": 301.0,
        "median": 301.0,
        "p90": 301.0,
        "p95": 301.0,
        "max": 301.0
      },
      "warm_container_reused": {
        "count": 11,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 174.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 432.0,
        "median": 460.0,
        "p90": 544.0,
        "p95": 544.0,
        "max": 656.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 62.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 861.0,
        "median": 922.0,
        "p90": 1345.0,
        "p95": 1345.0,
        "max": 1388.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 19.86,
    "throughput_per_second": 0.604,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.578,
      "median": 1.898,
      "p90": 3.079,
      "p95": 3.079,
      "max": 4.281
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.204,
      "p90": 0.375,
      "p95": 0.375,
      "max": 1.172
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.203,
      "p90": 1.141,
      "p95": 1.141,
      "max": 1.813
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
    },
    "cold_starts": 1,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 225.0,
        "median": 245.0,
        "p90": 262.0,
        "p95": 262.0,
        "max": 266.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 516.0,
        "median": 552.5,
        "p90": 803.0,
        "p95": 803.0,
        "max": 956.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 844.0,
        "median": 911.0,
        "p90": 1149.0,
        "p95": 1149.0,
        "max": 1488.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 30.0,
        "median": 34.5,
        "p90": 37.0,
        "p95": 37.0,
        "max": 57.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 338.0,
        "median": 360.5,
        "p90": 447.0,
        "p95": 447.0,
        "max": 511.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 339.0,
        "median": 361.5,
        "p90": 448.0,
        "p95": 448.0,
        "max": 512.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 25.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 33.0
      },
      "warm_container_create_ms": {
        "count": 1,
        "min": 270.0,
        "median": 270.0,
        "p90": 270.0,
        "p95": 270.0,
        "max": 270.0
      },
      "warm_container_reused": {
        "count": 11,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 157.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 421.0,
        "median": 454.0,
        "p90": 548.0,
        "p95": 548.0,
        "max": 616.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 62.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 855.0,
        "median": 924.5,
        "p90": 1165.0,
        "p95": 1165.0,
        "max": 1503.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 8.125,
    "throughput_per_second": 1.477,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.468,
      "median": 2.11,
      "p90": 2.75,
      "p95": 2.75,
      "max": 2.797
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.266
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.297
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 230.0,
        "median": 248.5,
        "p90": 272.0,
        "p95": 272.0,
        "max": 298.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 44.0,
        "p95": 44.0,
        "max": 45.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 541.0,
        "median": 706.5,
        "p90": 958.0,
        "p95": 958.0,
        "max": 992.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 872.0,
        "median": 1072.5,
        "p90": 1471.0,
        "p95": 1471.0,
        "max": 1529.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 36.0,
        "p90": 57.0,
        "p95": 57.0,
        "max": 58.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 339.0,
        "median": 399.0,
        "p90": 483.0,
        "p95": 483.0,
        "max": 498.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 340.0,
        "median": 400.0,
        "p90": 484.0,
        "p95": 484.0,
        "max": 499.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 28.5,
        "p90": 103.0,
        "p95": 103.0,
        "max": 108.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 238.0,
        "median": 295.0,
        "p90": 299.0,
        "p95": 299.0,
        "max": 299.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 153.0,
        "p95": 153.0,
        "max": 158.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 431.0,
        "median": 496.0,
        "p90": 609.0,
        "p95": 609.0,
        "max": 612.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 62.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 66.0,
        "p90": 84.0,
        "p95": 84.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 885.0,
        "median": 1094.5,
        "p90": 1495.0,
        "p95": 1495.0,
        "max": 1542.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 9.079,
    "throughput_per_second": 1.322,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 2.109,
      "p90": 2.782,
      "p95": 2.782,
      "max": 2.812
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.265,
      "p95": 0.265,
      "max": 0.281
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.204,
      "p95": 0.204,
      "max": 0.25
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 225.0,
        "median": 248.0,
        "p90": 279.0,
        "p95": 279.0,
        "max": 299.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 34.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 537.0,
        "median": 631.0,
        "p90": 863.0,
        "p95": 863.0,
        "max": 919.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 865.0,
        "median": 1000.0,
        "p90": 1358.0,
        "p95": 1358.0,
        "max": 1450.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 34.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 100.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 339.0,
        "median": 370.0,
        "p90": 410.0,
        "p95": 410.0,
        "max": 430.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 340.0,
        "median": 370.5,
        "p90": 411.0,
        "p95": 411.0,
        "max": 431.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 28.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 84.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 268.0,
        "median": 280.0,
        "p90": 323.0,
        "p95": 323.0,
        "max": 323.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 157.0,
        "p95": 157.0,
        "max": 159.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 439.0,
        "median": 467.0,
        "p90": 511.0,
        "p95": 511.0,
        "max": 557.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 61.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 63.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 879.0,
        "median": 1018.0,
        "p90": 1368.0,
        "p95": 1368.0,
        "max": 1463.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 8.359,
    "throughput_per_second": 1.436,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.547,
      "median": 1.695,
      "p90": 2.828,
      "p95": 2.828,
      "max": 2.844
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.234,
      "p95": 0.234,
      "max": 0.235
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.188,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.328
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 225.0,
        "median": 251.0,
        "p90": 268.0,
        "p95": 268.0,
        "max": 282.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 50.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 505.0,
        "median": 633.5,
        "p90": 926.0,
        "p95": 926.0,
        "max": 951.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 822.0,
        "median": 992.0,
        "p90": 1443.0,
        "p95": 1443.0,
        "max": 1516.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 35.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 76.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 338.0,
        "median": 398.0,
        "p90": 434.0,
        "p95": 434.0,
        "max": 446.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 338.0,
        "median": 399.0,
        "p90": 435.0,
        "p95": 435.0,
        "max": 447.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 25.0,
        "p90": 33.0,
        "p95": 33.0,
        "max": 40.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 243.0,
        "median": 291.5,
        "p90": 294.0,
        "p95": 294.0,
        "max": 294.0
      },
      "warm_container_reused": {
        "count": 8,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 147.0,
        "p95": 147.0,
        "max": 160.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 423.0,
        "median": 500.5,
        "p90": 544.0,
        "p95": 544.0,
        "max": 561.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 62.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 58.0,
        "median": 62.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 836.0,
        "median": 1003.5,
        "p90": 1462.0,
        "p95": 1462.0,
        "max": 1532.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 8.719,
    "throughput_per_second": 1.376,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.625,
      "median": 3.032,
      "p90": 4.266,
      "p95": 4.266,
      "max": 4.453
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.32,
      "p90": 0.485,
      "p95": 0.485,
      "max": 1.218
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.219,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.657
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 233.0,
        "median": 250.0,
        "p90": 284.0,
        "p95": 284.0,
        "max": 297.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 32.0,
        "p95": 32.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 517.0,
        "median": 715.5,
        "p90": 840.0,
        "p95": 840.0,
        "max": 946.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 887.0,
        "median": 1127.0,
        "p90": 1346.0,
        "p95": 1346.0,
        "max": 1597.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.5,
        "p90": 20.0,
        "p95": 20.0,
        "max": 21.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 39.5,
        "p90": 156.0,
        "p95": 156.0,
        "max": 285.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 332.0,
        "median": 378.0,
        "p90": 402.0,
        "p95": 402.0,
        "max": 457.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 333.0,
        "median": 378.5,
        "p90": 403.0,
        "p95": 403.0,
        "max": 458.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 64.5,
        "p90": 185.0,
        "p95": 185.0,
        "max": 203.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 272.0,
        "median": 287.0,
        "p90": 305.0,
        "p95": 305.0,
        "max": 305.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 162.0,
        "p95": 162.0,
        "max": 169.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 418.0,
        "median": 477.0,
        "p90": 504.0,
        "p95": 504.0,
        "max": 572.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 64.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 67.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 899.0,
        "median": 1142.0,
        "p90": 1359.0,
        "p95": 1359.0,
        "max": 1616.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 7.89,
    "throughput_per_second": 1.521,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.656,
      "median": 2.938,
      "p90": 3.532,
      "p95": 3.532,
      "max": 4.5
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.204,
      "median": 0.312,
      "p90": 0.422,
      "p95": 0.422,
      "max": 0.594
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.211,
      "p90": 0.312,
      "p95": 0.312,
      "max": 3.296
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 2,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 227.0,
        "median": 249.5,
        "p90": 287.0,
        "p95": 287.0,
        "max": 297.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 31.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 525.0,
        "median": 612.0,
        "p90": 858.0,
        "p95": 858.0,
        "max": 982.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 848.0,
        "median": 1047.0,
        "p90": 1261.0,
        "p95": 1261.0,
        "max": 1405.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 14.0,
        "p95": 14.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 38.5,
        "p90": 49.0,
        "p95": 49.0,
        "max": 51.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 332.0,
        "median": 366.5,
        "p90": 418.0,
        "p95": 418.0,
        "max": 449.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 333.0,
        "median": 367.5,
        "p90": 419.0,
        "p95": 419.0,
        "max": 450.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 32.0,
        "p90": 112.0,
        "p95": 112.0,
        "max": 173.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 287.0,
        "median": 299.5,
        "p90": 312.0,
        "p95": 312.0,
        "max": 312.0
      },
      "warm_container_reused": {
        "count": 10,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 169.0,
        "p95": 169.0,
        "max": 177.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 418.0,
        "median": 475.0,
        "p90": 524.0,
        "p95": 524.0,
        "max": 578.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 66.5,
        "p90": 71.0,
        "p95": 71.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 66.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 864.0,
        "median": 1069.0,
        "p90": 1284.0,
        "p95": 1284.0,
        "max": 1437.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 8.281,
    "throughput_per_second": 1.449,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.656,
      "median": 3.117,
      "p90": 3.453,
      "p95": 3.453,
      "max": 4.0
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.29,
      "p90": 0.75,
      "p95": 0.75,
      "max": 0.75
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.242,
      "p90": 0.343,
      "p95": 0.343,
      "max": 1.156
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
    },
    "cold_starts": 3,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 12,
        "min": 233.0,
        "median": 257.5,
        "p90": 309.0,
        "p95": 309.0,
        "max": 329.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 52.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 561.0,
        "median": 669.5,
        "p90": 932.0,
        "p95": 932.0,
        "max": 1094.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 928.0,
        "median": 1068.0,
        "p90": 1451.0,
        "p95": 1451.0,
        "max": 1508.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 8.5,
        "p90": 17.0,
        "p95": 17.0,
        "max": 21.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 36.0,
        "p90": 48.0,
        "p95": 48.0,
        "max": 57.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 357.0,
        "median": 392.0,
        "p90": 465.0,
        "p95": 465.0,
        "max": 468.0
      },
      "runner_result_serialize_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_setup_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 12,
        "min": 358.0,
        "median": 393.0,
        "p90": 466.0,
        "p95": 466.0,
        "max": 471.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 27.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 162.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 275.0,
        "median": 295.0,
        "p90": 357.0,
        "p95": 357.0,
        "max": 357.0
      },
      "warm_container_reused": {
        "count": 9,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 164.0,
        "p95": 164.0,
        "max": 176.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 456.0,
        "median": 507.5,
        "p90": 573.0,
        "p95": 573.0,
        "max": 586.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 65.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 92.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 58.0,
        "median": 69.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 943.0,
        "median": 1084.0,
        "p90": 1470.0,
        "p95": 1470.0,
        "max": 1542.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 14.813,
    "throughput_per_second": 0.54,
    "successes": 8,
    "failures": 4,
    "terminal_seconds": {
      "count": 8,
      "min": 1.531,
      "median": 2.469,
      "p90": 3.375,
      "p95": 3.641,
      "max": 3.641
    },
    "accept_seconds": {
      "count": 8,
      "min": 0.172,
      "median": 0.211,
      "p90": 1.203,
      "p95": 1.219,
      "max": 1.219
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.218,
      "p90": 0.234,
      "p95": 0.297,
      "max": 0.297
    },
    "workers": {
      "worker-1": 4,
      "worker-2": 4
    },
    "cold_starts": 4,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 8,
        "min": 233.0,
        "median": 268.0,
        "p90": 300.0,
        "p95": 301.0,
        "max": 301.0
      },
      "docker_image_pull_ms": {
        "count": 8,
        "min": 0.0,
        "median": 19.0,
        "p90": 183.0,
        "p95": 372.0,
        "max": 372.0
      },
      "docker_input_copy_ms": {
        "count": 8,
        "min": 4.0,
        "median": 7.0,
        "p90": 9.0,
        "p95": 10.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 8,
        "min": 546.0,
        "median": 825.0,
        "p90": 1061.0,
        "p95": 1246.0,
        "max": 1246.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 8,
        "min": 870.0,
        "median": 1231.0,
        "p90": 1582.0,
        "p95": 1750.0,
        "max": 1750.0
      },
      "orchestrator_claim_ms": {
        "count": 8,
        "min": 3.0,
        "median": 7.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 8,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 9.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 8,
        "min": 32.0,
        "median": 34.0,
        "p90": 38.0,
        "p95": 38.0,
        "max": 38.0
      },
      "output_validation_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 1.0,
        "max": 1.0
      },
      "runner_module_imports_ms": {
        "count": 8,
        "min": 336.0,
        "median": 371.0,
        "p90": 421.0,
        "p95": 425.0,
        "max": 425.0
      },
      "runner_result_serialize_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 8,
        "min": 337.0,
        "median": 372.0,
        "p90": 422.0,
        "p95": 426.0,
        "max": 426.0
      },
      "sandbox_prepare_ms": {
        "count": 8,
        "min": 38.0,
        "median": 42.5,
        "p90": 48.0,
        "p95": 77.0,
        "max": 77.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 307.0,
        "median": 331.0,
        "p90": 348.0,
        "p95": 348.0,
        "max": 348.0
      },
      "warm_container_reused": {
        "count": 4,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 8,
        "min": 0.0,
        "median": 0.0,
        "p90": 146.0,
        "p95": 167.0,
        "max": 167.0
      },
      "warm_runner_exec_ms": {
        "count": 8,
        "min": 437.0,
        "median": 469.5,
        "p90": 537.0,
        "p95": 538.0,
        "max": 538.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 8,
        "min": 54.0,
        "median": 70.0,
        "p90": 75.0,
        "p95": 81.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 8,
        "min": 59.0,
        "median": 66.0,
        "p90": 76.0,
        "p95": 82.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 8,
        "min": 885.0,
        "median": 1244.5,
        "p90": 1595.0,
        "p95": 1765.0,
        "max": 1765.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 1.172,
    "throughput_per_second": 0.0,
    "successes": 0,
    "failures": 12,
    "terminal_seconds": {
      "count": 0
    },
    "accept_seconds": {
      "count": 0
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {},
    "cold_starts": 0,
    "worker_timing_ms": {}
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 0.907,
    "throughput_per_second": 0.0,
    "successes": 0,
    "failures": 12,
    "terminal_seconds": {
      "count": 0
    },
    "accept_seconds": {
      "count": 0
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {},
    "cold_starts": 0,
    "worker_timing_ms": {}
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 0.625,
    "throughput_per_second": 0.0,
    "successes": 0,
    "failures": 12,
    "terminal_seconds": {
      "count": 0
    },
    "accept_seconds": {
      "count": 0
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {},
    "cold_starts": 0,
    "worker_timing_ms": {}
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 1.141,
    "throughput_per_second": 0.0,
    "successes": 0,
    "failures": 12,
    "terminal_seconds": {
      "count": 0
    },
    "accept_seconds": {
      "count": 0
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {},
    "cold_starts": 0,
    "worker_timing_ms": {}
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 2.813,
    "throughput_per_second": 0.0,
    "successes": 0,
    "failures": 12,
    "terminal_seconds": {
      "count": 0
    },
    "accept_seconds": {
      "count": 0
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {},
    "cold_starts": 0,
    "worker_timing_ms": {}
  }
]
```
