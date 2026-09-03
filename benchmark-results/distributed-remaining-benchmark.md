# Distributed Platform Benchmark

Generated: 2026-08-31T20:12:54.680256+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- It is not worker execution concurrency. Worker execution concurrency was held constant during these runs; the deployed workers reported `max_invocation_concurrency: 2`.
- Use this report to understand saturation, queueing, throughput ceilings, and user-visible latency under request pressure. Use a separate worker-concurrency benchmark when tuning how many jobs each worker can execute at once.
- The embedded JSON still uses the historical field name `"concurrency"`; in this report that field means saturation/client-side concurrency.

## Built Functions

- `tiny`: function `27`, version `27`, image `10.42.1.22:5000/functions/bench-tiny-63283ba6:v27-v1-a1-88f7fcb35c93-d1`
- `sleep`: function `28`, version `28`, image `10.42.1.22:5000/functions/bench-sleep-fe16372d:v28-v1-a1-c10b59ed7c28-d1`
- `dependency`: function `29`, version `29`, image `10.42.1.22:5000/functions/bench-dependency-43656e8e:v29-v1-a1-18f35925de1d-d1`
- `output`: function `30`, version `30`, image `10.42.1.22:5000/functions/bench-output-2287a361:v30-v1-a1-4cda9bafc887-d1`
- `input_output`: function `31`, version `31`, image `10.42.1.22:5000/functions/bench-input_output-4e5479cf:v31-v1-a1-b4df4507c9a7-d1`

## Run Summary

| Scenario | Count | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| single-input_output | 12 | 2 | 1 | 12 | 0 | 16.828 | 0.713 | 2.618 | 2.719 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 2 | 2 | 12 | 0 | 13.516 | 0.888 | 1.547 | 2.657 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 2 | 3 | 12 | 0 | 15.532 | 0.773 | 2.102 | 2.656 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 4 | 1 | 12 | 0 | 8.109 | 1.48 | 2.086 | 2.719 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 4 | 2 | 12 | 0 | 8.0 | 1.5 | 2.109 | 2.797 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 4 | 3 | 12 | 0 | 9.531 | 1.259 | 2.703 | 2.875 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 8 | 1 | 12 | 0 | 6.281 | 1.911 | 2.789 | 4.234 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 8 | 2 | 12 | 0 | 6.344 | 1.892 | 2.851 | 4.187 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 8 | 3 | 12 | 0 | 6.156 | 1.949 | 2.758 | 4.156 | worker-1:6, worker-2:6 |
| mixed-15 | 15 | 2 | 1 | 15 | 0 | 14.203 | 1.056 | 1.515 | 2.625 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 2 | 2 | 15 | 0 | 15.687 | 0.956 | 1.89 | 2.687 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 2 | 3 | 15 | 0 | 15.094 | 0.994 | 1.578 | 2.719 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 4 | 1 | 15 | 0 | 8.64 | 1.736 | 1.562 | 2.75 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 4 | 2 | 15 | 0 | 9.563 | 1.569 | 2.64 | 2.75 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 4 | 3 | 15 | 0 | 9.859 | 1.521 | 2.625 | 2.781 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 8 | 1 | 15 | 0 | 7.109 | 2.11 | 2.922 | 4.25 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 8 | 2 | 15 | 0 | 6.922 | 2.167 | 2.86 | 4.188 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 8 | 3 | 15 | 0 | 6.954 | 2.157 | 2.782 | 4.188 | worker-1:7, worker-2:8 |
| mixed-30 | 30 | 2 | 1 | 30 | 0 | 32.094 | 0.935 | 1.601 | 2.766 | worker-1:13, worker-2:17 |
| mixed-30 | 30 | 2 | 2 | 30 | 0 | 30.703 | 0.977 | 1.515 | 2.735 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 2 | 3 | 30 | 0 | 33.453 | 0.897 | 2.101 | 3.828 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 4 | 1 | 30 | 0 | 15.922 | 1.884 | 1.586 | 2.891 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 4 | 2 | 30 | 0 | 16.391 | 1.83 | 1.601 | 2.812 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 4 | 3 | 30 | 0 | 16.578 | 1.81 | 2.117 | 2.75 | worker-1:13, worker-2:17 |
| mixed-30 | 30 | 8 | 1 | 30 | 0 | 13.469 | 2.227 | 2.891 | 4.235 | worker-1:14, worker-2:16 |
| mixed-30 | 30 | 8 | 2 | 30 | 0 | 12.657 | 2.37 | 2.812 | 5.047 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 8 | 3 | 30 | 0 | 13.016 | 2.305 | 2.859 | 4.828 | worker-1:15, worker-2:15 |
| mixed-80 | 80 | 2 | 1 | 80 | 0 | 84.594 | 0.946 | 1.532 | 3.25 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 2 | 2 | 80 | 0 | 83.329 | 0.96 | 1.547 | 2.766 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 2 | 3 | 80 | 0 | 82.515 | 0.97 | 1.593 | 2.859 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 4 | 1 | 80 | 0 | 43.203 | 1.852 | 1.563 | 2.781 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 4 | 2 | 80 | 0 | 44.454 | 1.8 | 2.57 | 2.734 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 4 | 3 | 80 | 0 | 44.313 | 1.805 | 2.218 | 2.735 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 8 | 1 | 80 | 0 | 30.219 | 2.647 | 2.75 | 4.109 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 8 | 2 | 80 | 0 | 31.469 | 2.542 | 2.758 | 3.984 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 8 | 3 | 80 | 0 | 30.375 | 2.634 | 2.844 | 4.265 | worker-1:39, worker-2:41 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 16.828,
    "throughput_per_second": 0.713,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 2.618,
      "p90": 2.719,
      "p95": 2.719,
      "max": 2.968
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.484,
      "p95": 0.484,
      "max": 0.813
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.25
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
        "min": 229.0,
        "median": 255.0,
        "p90": 281.0,
        "p95": 281.0,
        "max": 291.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 12.0,
        "p90": 420.0,
        "p95": 420.0,
        "max": 425.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 555.0,
        "median": 782.5,
        "p90": 1397.0,
        "p95": 1397.0,
        "max": 1422.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 912.0,
        "median": 1160.5,
        "p90": 1779.0,
        "p95": 1779.0,
        "max": 1964.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 2.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 12.0,
        "p95": 12.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 30.0,
        "median": 35.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 70.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 1.0,
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
        "max": 1.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 342.0,
        "median": 374.5,
        "p90": 407.0,
        "p95": 407.0,
        "max": 443.0
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
        "min": 343.0,
        "median": 375.0,
        "p90": 408.0,
        "p95": 408.0,
        "max": 444.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 44.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 78.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 256.0,
        "median": 269.0,
        "p90": 318.0,
        "p95": 335.0,
        "max": 335.0
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
        "p90": 147.0,
        "p95": 147.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 441.0,
        "median": 477.5,
        "p90": 536.0,
        "p95": 536.0,
        "max": 575.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 65.5,
        "p90": 77.0,
        "p95": 77.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 64.0,
        "p90": 81.0,
        "p95": 81.0,
        "max": 94.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 930.0,
        "median": 1171.0,
        "p90": 1805.0,
        "p95": 1805.0,
        "max": 1986.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 13.516,
    "throughput_per_second": 0.888,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 1.547,
      "p90": 2.657,
      "p95": 2.657,
      "max": 2.688
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.188
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.188
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
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
        "min": 229.0,
        "median": 245.5,
        "p90": 267.0,
        "p95": 267.0,
        "max": 350.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 528.0,
        "median": 571.5,
        "p90": 639.0,
        "p95": 639.0,
        "max": 1040.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 857.0,
        "median": 943.0,
        "p90": 1095.0,
        "p95": 1095.0,
        "max": 1560.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 7.0,
        "p90": 13.0,
        "p95": 13.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 37.5,
        "p90": 98.0,
        "p95": 98.0,
        "max": 106.0
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
        "min": 335.0,
        "median": 362.5,
        "p90": 426.0,
        "p95": 426.0,
        "max": 451.0
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
        "min": 336.0,
        "median": 363.5,
        "p90": 427.0,
        "p95": 427.0,
        "max": 452.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 40.0,
        "median": 44.0,
        "p90": 53.0,
        "p95": 53.0,
        "max": 96.0
      },
      "warm_container_create_ms": {
        "count": 1,
        "min": 288.0,
        "median": 288.0,
        "p90": 288.0,
        "p95": 288.0,
        "max": 288.0
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
        "max": 155.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 422.0,
        "median": 455.0,
        "p90": 529.0,
        "p95": 529.0,
        "max": 549.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 870.0,
        "median": 960.5,
        "p90": 1109.0,
        "p95": 1109.0,
        "max": 1578.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 15.532,
    "throughput_per_second": 0.773,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 2.102,
      "p90": 2.656,
      "p95": 2.656,
      "max": 2.656
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.204
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 6,
      "worker-2": 6
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
        "min": 234.0,
        "median": 259.0,
        "p90": 287.0,
        "p95": 287.0,
        "max": 291.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.5,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 539.0,
        "median": 599.5,
        "p90": 714.0,
        "p95": 714.0,
        "max": 902.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 871.0,
        "median": 970.5,
        "p90": 1126.0,
        "p95": 1126.0,
        "max": 1391.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 34.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 44.0
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
        "median": 367.5,
        "p90": 431.0,
        "p95": 431.0,
        "max": 448.0
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
        "median": 368.5,
        "p90": 432.0,
        "p95": 432.0,
        "max": 449.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 38.0,
        "median": 45.0,
        "p90": 100.0,
        "p95": 100.0,
        "max": 112.0
      },
      "warm_container_create_ms": {
        "count": 1,
        "min": 293.0,
        "median": 293.0,
        "p90": 293.0,
        "p95": 293.0,
        "max": 293.0
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
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 429.0,
        "median": 468.0,
        "p90": 529.0,
        "p95": 529.0,
        "max": 561.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 62.5,
        "p90": 86.0,
        "p95": 86.0,
        "max": 97.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 64.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 885.0,
        "median": 983.0,
        "p90": 1150.0,
        "p95": 1150.0,
        "max": 1403.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 8.109,
    "throughput_per_second": 1.48,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.468,
      "median": 2.086,
      "p90": 2.719,
      "p95": 2.719,
      "max": 2.75
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.234,
      "p95": 0.234,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.422
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
        "min": 224.0,
        "median": 246.0,
        "p90": 273.0,
        "p95": 273.0,
        "max": 301.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 39.0,
        "p95": 39.0,
        "max": 51.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 515.0,
        "median": 629.5,
        "p90": 999.0,
        "p95": 999.0,
        "max": 1018.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 849.0,
        "median": 1030.0,
        "p90": 1501.0,
        "p95": 1501.0,
        "max": 1528.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 14.0,
        "p95": 14.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 37.0,
        "p90": 51.0,
        "p95": 51.0,
        "max": 77.0
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
        "min": 331.0,
        "median": 375.5,
        "p90": 409.0,
        "p95": 409.0,
        "max": 502.0
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
        "min": 332.0,
        "median": 376.0,
        "p90": 410.0,
        "p95": 410.0,
        "max": 503.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 38.0,
        "median": 54.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 170.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 250.0,
        "median": 286.0,
        "p90": 304.0,
        "p95": 304.0,
        "max": 304.0
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
        "p90": 142.0,
        "p95": 142.0,
        "max": 146.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 415.0,
        "median": 482.0,
        "p90": 508.0,
        "p95": 508.0,
        "max": 632.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 63.0,
        "p90": 76.0,
        "p95": 76.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 66.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 864.0,
        "median": 1055.5,
        "p90": 1517.0,
        "p95": 1517.0,
        "max": 1544.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 8.0,
    "throughput_per_second": 1.5,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.5,
      "median": 2.109,
      "p90": 2.797,
      "p95": 2.797,
      "max": 2.828
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.179,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
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
        "median": 242.5,
        "p90": 275.0,
        "p95": 275.0,
        "max": 324.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 39.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 539.0,
        "median": 683.0,
        "p90": 985.0,
        "p95": 985.0,
        "max": 989.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 862.0,
        "median": 1058.5,
        "p90": 1391.0,
        "p95": 1391.0,
        "max": 1548.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 16.0,
        "p95": 16.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 16.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 39.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 92.0
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
        "max": 1.0
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
        "min": 338.0,
        "median": 390.5,
        "p90": 417.0,
        "p95": 417.0,
        "max": 435.0
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
        "median": 391.0,
        "p90": 420.0,
        "p95": 420.0,
        "max": 436.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 48.5,
        "p90": 95.0,
        "p95": 95.0,
        "max": 110.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 281.0,
        "median": 297.0,
        "p90": 314.0,
        "p95": 314.0,
        "max": 314.0
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
        "max": 150.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 425.0,
        "median": 507.0,
        "p90": 538.0,
        "p95": 538.0,
        "max": 541.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 65.0,
        "p90": 82.0,
        "p95": 82.0,
        "max": 85.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 63.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 874.0,
        "median": 1073.5,
        "p90": 1418.0,
        "p95": 1418.0,
        "max": 1563.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 9.531,
    "throughput_per_second": 1.259,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.656,
      "median": 2.703,
      "p90": 2.875,
      "p95": 2.875,
      "max": 2.906
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.226,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.328
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "min": 236.0,
        "median": 254.0,
        "p90": 286.0,
        "p95": 286.0,
        "max": 288.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 44.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 584.0,
        "median": 748.5,
        "p90": 951.0,
        "p95": 951.0,
        "max": 1009.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 939.0,
        "median": 1111.0,
        "p90": 1486.0,
        "p95": 1486.0,
        "max": 1528.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 13.0,
        "p95": 13.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 30.0,
        "median": 33.5,
        "p90": 41.0,
        "p95": 41.0,
        "max": 66.0
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
        "min": 355.0,
        "median": 390.0,
        "p90": 450.0,
        "p95": 450.0,
        "max": 453.0
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
        "min": 356.0,
        "median": 391.0,
        "p90": 451.0,
        "p95": 451.0,
        "max": 454.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 44.5,
        "p90": 136.0,
        "p95": 136.0,
        "max": 165.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 240.0,
        "median": 279.0,
        "p90": 318.0,
        "p95": 318.0,
        "max": 318.0
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
        "p90": 143.0,
        "p95": 143.0,
        "max": 143.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 453.0,
        "median": 492.5,
        "p90": 558.0,
        "p95": 558.0,
        "max": 586.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 59.0,
        "median": 64.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 60.0,
        "median": 68.5,
        "p90": 78.0,
        "p95": 78.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 957.0,
        "median": 1129.0,
        "p90": 1502.0,
        "p95": 1502.0,
        "max": 1539.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 6.281,
    "throughput_per_second": 1.911,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.5,
      "median": 2.789,
      "p90": 4.234,
      "p95": 4.234,
      "max": 4.297
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.196,
      "p90": 0.281,
      "p95": 0.281,
      "max": 0.312
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.179,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.438
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
        "min": 233.0,
        "median": 260.5,
        "p90": 279.0,
        "p95": 279.0,
        "max": 283.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 36.0,
        "p95": 36.0,
        "max": 49.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 578.0,
        "median": 803.5,
        "p90": 997.0,
        "p95": 997.0,
        "max": 1054.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1028.0,
        "median": 1221.0,
        "p90": 1472.0,
        "p95": 1472.0,
        "max": 1597.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 8.0,
        "p90": 17.0,
        "p95": 17.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 35.0,
        "median": 61.0,
        "p90": 197.0,
        "p95": 197.0,
        "max": 205.0
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
        "median": 399.5,
        "p90": 440.0,
        "p95": 440.0,
        "max": 522.0
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
        "median": 400.5,
        "p90": 441.0,
        "p95": 441.0,
        "max": 523.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 42.0,
        "median": 81.0,
        "p90": 224.0,
        "p95": 224.0,
        "max": 368.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 231.0,
        "median": 295.5,
        "p90": 339.0,
        "p95": 339.0,
        "max": 339.0
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
        "p90": 151.0,
        "p95": 151.0,
        "max": 162.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 432.0,
        "median": 500.5,
        "p90": 558.0,
        "p95": 558.0,
        "max": 635.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 62.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 63.5,
        "p90": 81.0,
        "p95": 81.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1044.0,
        "median": 1239.0,
        "p90": 1482.0,
        "p95": 1482.0,
        "max": 1625.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 6.344,
    "throughput_per_second": 1.892,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.515,
      "median": 2.851,
      "p90": 4.187,
      "p95": 4.187,
      "max": 4.219
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.235,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.344
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.156,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.219
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
        "min": 229.0,
        "median": 257.5,
        "p90": 278.0,
        "p95": 278.0,
        "max": 286.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 38.0,
        "max": 58.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 15.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 604.0,
        "median": 690.0,
        "p90": 923.0,
        "p95": 923.0,
        "max": 1011.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 960.0,
        "median": 1094.0,
        "p90": 1371.0,
        "p95": 1371.0,
        "max": 1427.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 36.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 130.0
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
        "median": 396.5,
        "p90": 446.0,
        "p95": 446.0,
        "max": 484.0
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
        "median": 397.5,
        "p90": 447.0,
        "p95": 447.0,
        "max": 486.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 64.0,
        "p90": 148.0,
        "p95": 148.0,
        "max": 154.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 240.0,
        "median": 287.0,
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
        "p90": 138.0,
        "p95": 138.0,
        "max": 165.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 448.0,
        "median": 497.5,
        "p90": 556.0,
        "p95": 556.0,
        "max": 624.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 63.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 67.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 977.0,
        "median": 1116.0,
        "p90": 1385.0,
        "p95": 1385.0,
        "max": 1443.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 6.156,
    "throughput_per_second": 1.949,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.5,
      "median": 2.758,
      "p90": 4.156,
      "p95": 4.156,
      "max": 4.281
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.211,
      "p90": 0.391,
      "p95": 0.391,
      "max": 0.391
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.188
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
        "min": 222.0,
        "median": 244.5,
        "p90": 294.0,
        "p95": 294.0,
        "max": 307.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 29.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 13.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 522.0,
        "median": 779.5,
        "p90": 987.0,
        "p95": 987.0,
        "max": 1008.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 838.0,
        "median": 1145.5,
        "p90": 1421.0,
        "p95": 1421.0,
        "max": 1485.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 23.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 37.5,
        "p90": 62.0,
        "p95": 62.0,
        "max": 88.0
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
        "median": 379.0,
        "p90": 417.0,
        "p95": 417.0,
        "max": 422.0
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
        "median": 379.5,
        "p90": 418.0,
        "p95": 418.0,
        "max": 423.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 38.0,
        "median": 81.5,
        "p90": 280.0,
        "p95": 280.0,
        "max": 291.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 249.0,
        "median": 285.0,
        "p90": 311.0,
        "p95": 311.0,
        "max": 311.0
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
        "p90": 155.0,
        "p95": 155.0,
        "max": 162.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 414.0,
        "median": 479.0,
        "p90": 537.0,
        "p95": 537.0,
        "max": 557.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 66.5,
        "p90": 80.0,
        "p95": 80.0,
        "max": 103.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 851.0,
        "median": 1159.5,
        "p90": 1438.0,
        "p95": 1438.0,
        "max": 1494.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 14.203,
    "throughput_per_second": 1.056,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.437,
      "median": 1.515,
      "p90": 2.625,
      "p95": 2.625,
      "max": 2.625
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.218
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.141,
      "median": 0.141,
      "p90": 0.141,
      "p95": 0.141,
      "max": 0.141
    },
    "workers": {
      "worker-1": 8,
      "worker-2": 7
    },
    "cold_starts": 8,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 240.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 24.0,
        "p90": 146.0,
        "p95": 146.0,
        "max": 161.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 518.0,
        "median": 752.0,
        "p90": 1907.0,
        "p95": 1907.0,
        "max": 1913.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 577.0,
        "median": 943.0,
        "p90": 1991.0,
        "p95": 1991.0,
        "max": 2120.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 35.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 184.0,
        "p95": 184.0,
        "max": 216.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 336.0,
        "median": 366.0,
        "p90": 388.0,
        "p95": 388.0,
        "max": 422.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 336.0,
        "median": 372.0,
        "p90": 1345.0,
        "p95": 1345.0,
        "max": 1387.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 24.0,
        "p90": 32.0,
        "p95": 32.0,
        "max": 65.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 216.0,
        "median": 258.5,
        "p90": 265.0,
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 139.0,
        "p95": 139.0,
        "max": 147.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 426.0,
        "median": 461.0,
        "p90": 1453.0,
        "p95": 1453.0,
        "max": 1486.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 55.0,
        "median": 59.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 51.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 589.0,
        "median": 953.0,
        "p90": 2004.0,
        "p95": 2004.0,
        "max": 2133.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 15.687,
    "throughput_per_second": 0.956,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.438,
      "median": 1.89,
      "p90": 2.687,
      "p95": 2.687,
      "max": 3.406
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.468
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.187,
      "median": 0.187,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.187
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 5,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 278.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 39.0,
        "p95": 39.0,
        "max": 46.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 516.0,
        "median": 601.0,
        "p90": 1896.0,
        "p95": 1896.0,
        "max": 1965.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 571.0,
        "median": 670.0,
        "p90": 2102.0,
        "p95": 2102.0,
        "max": 2189.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 36.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 195.0,
        "p95": 195.0,
        "max": 197.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 337.0,
        "median": 377.0,
        "p90": 436.0,
        "p95": 436.0,
        "max": 451.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 338.0,
        "median": 380.0,
        "p90": 1411.0,
        "p95": 1411.0,
        "max": 1453.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 24.0,
        "p90": 42.0,
        "p95": 42.0,
        "max": 60.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 226.0,
        "median": 256.0,
        "p90": 269.0,
        "p95": 269.0,
        "max": 269.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 140.0,
        "p95": 140.0,
        "max": 155.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 424.0,
        "median": 480.0,
        "p90": 1518.0,
        "p95": 1518.0,
        "max": 1562.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 52.0,
        "median": 63.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 584.0,
        "median": 686.0,
        "p90": 2112.0,
        "p95": 2112.0,
        "max": 2207.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 15.094,
    "throughput_per_second": 0.994,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.484,
      "median": 1.578,
      "p90": 2.719,
      "p95": 2.719,
      "max": 2.75
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.187,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.766
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.157,
      "median": 0.157,
      "p90": 0.157,
      "p95": 0.157,
      "max": 0.157
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 5,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 231.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 517.0,
        "median": 575.0,
        "p90": 1853.0,
        "p95": 1853.0,
        "max": 1919.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 574.0,
        "median": 647.0,
        "p90": 2078.0,
        "p95": 2078.0,
        "max": 2133.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 31.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 198.0,
        "p95": 198.0,
        "max": 206.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 338.0,
        "median": 359.0,
        "p90": 402.0,
        "p95": 402.0,
        "max": 413.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 339.0,
        "median": 376.0,
        "p90": 1380.0,
        "p95": 1380.0,
        "max": 1404.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 26.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 54.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 250.0,
        "median": 276.0,
        "p90": 293.0,
        "p95": 293.0,
        "max": 293.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 156.0,
        "p95": 156.0,
        "max": 164.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 424.0,
        "median": 466.0,
        "p90": 1473.0,
        "p95": 1473.0,
        "max": 1503.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 55.0,
        "median": 61.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 61.0,
        "p90": 80.0,
        "p95": 80.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 589.0,
        "median": 660.0,
        "p90": 2098.0,
        "p95": 2098.0,
        "max": 2153.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 8.64,
    "throughput_per_second": 1.736,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 1.562,
      "p90": 2.75,
      "p95": 2.75,
      "max": 3.844
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.171,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.187,
      "median": 0.187,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.187
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 8,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 234.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 25.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 493.0,
        "median": 862.0,
        "p90": 1913.0,
        "p95": 1913.0,
        "max": 2034.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 549.0,
        "median": 1081.0,
        "p90": 2261.0,
        "p95": 2261.0,
        "max": 2297.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 35.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 177.0,
        "p95": 177.0,
        "max": 258.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 330.0,
        "median": 386.0,
        "p90": 466.0,
        "p95": 466.0,
        "max": 490.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 331.0,
        "median": 410.0,
        "p90": 1376.0,
        "p95": 1376.0,
        "max": 1468.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 20.0,
        "median": 24.0,
        "p90": 38.0,
        "p95": 38.0,
        "max": 44.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 233.0,
        "median": 266.5,
        "p90": 282.0,
        "p95": 320.0,
        "max": 320.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 270.0,
        "p95": 270.0,
        "max": 315.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 414.0,
        "median": 503.0,
        "p90": 1489.0,
        "p95": 1489.0,
        "max": 1575.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 56.0,
        "median": 64.0,
        "p90": 83.0,
        "p95": 83.0,
        "max": 87.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 55.0,
        "median": 63.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 563.0,
        "median": 1099.0,
        "p90": 2277.0,
        "p95": 2277.0,
        "max": 2310.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 9.563,
    "throughput_per_second": 1.569,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 2.64,
      "p90": 2.75,
      "p95": 2.75,
      "max": 2.75
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.219
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.172,
      "median": 0.172,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 9,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 234.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 25.0,
        "p90": 49.0,
        "p95": 49.0,
        "max": 51.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 583.0,
        "median": 896.0,
        "p90": 1839.0,
        "p95": 1839.0,
        "max": 1963.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 647.0,
        "median": 1143.0,
        "p90": 1895.0,
        "p95": 1895.0,
        "max": 2026.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 79.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 169.0,
        "p95": 169.0,
        "max": 201.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 339.0,
        "median": 398.0,
        "p90": 445.0,
        "p95": 445.0,
        "max": 471.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 354.0,
        "median": 421.0,
        "p90": 1355.0,
        "p95": 1355.0,
        "max": 1416.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 24.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 43.0
      },
      "warm_container_create_ms": {
        "count": 9,
        "min": 226.0,
        "median": 277.0,
        "p90": 302.0,
        "p95": 306.0,
        "max": 306.0
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
        "count": 15,
        "min": 0.0,
        "median": 130.0,
        "p90": 163.0,
        "p95": 163.0,
        "max": 291.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 445.0,
        "median": 523.0,
        "p90": 1453.0,
        "p95": 1453.0,
        "max": 1536.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 61.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 85.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 70.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 659.0,
        "median": 1164.0,
        "p90": 1906.0,
        "p95": 1906.0,
        "max": 2042.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 9.859,
    "throughput_per_second": 1.521,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.469,
      "median": 2.625,
      "p90": 2.781,
      "p95": 2.781,
      "max": 3.797
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.14,
      "median": 0.14,
      "p90": 0.14,
      "p95": 0.14,
      "max": 0.14
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 9,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 238.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 27.0,
        "p90": 42.0,
        "p95": 42.0,
        "max": 47.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 589.0,
        "median": 902.0,
        "p90": 1843.0,
        "p95": 1843.0,
        "max": 2033.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 656.0,
        "median": 1114.0,
        "p90": 1903.0,
        "p95": 1903.0,
        "max": 2098.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 5.0,
        "median": 7.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 34.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 181.0,
        "p95": 181.0,
        "max": 239.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 350.0,
        "median": 395.0,
        "p90": 439.0,
        "p95": 439.0,
        "max": 456.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 369.0,
        "median": 433.0,
        "p90": 1371.0,
        "p95": 1371.0,
        "max": 1457.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 19.0,
        "median": 23.0,
        "p90": 43.0,
        "p95": 43.0,
        "max": 62.0
      },
      "warm_container_create_ms": {
        "count": 9,
        "min": 218.0,
        "median": 275.0,
        "p90": 313.0,
        "p95": 350.0,
        "max": 350.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 153.0,
        "p95": 153.0,
        "max": 295.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 464.0,
        "median": 526.0,
        "p90": 1459.0,
        "p95": 1459.0,
        "max": 1576.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 62.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 56.0,
        "median": 66.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 87.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 670.0,
        "median": 1127.0,
        "p90": 1917.0,
        "p95": 1917.0,
        "max": 2114.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 7.109,
    "throughput_per_second": 2.11,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.656,
      "median": 2.922,
      "p90": 4.25,
      "p95": 4.25,
      "max": 5.328
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.265,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.437
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.172,
      "median": 0.172,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 8,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 233.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 26.0,
        "p90": 49.0,
        "p95": 49.0,
        "max": 54.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 611.0,
        "median": 931.0,
        "p90": 1860.0,
        "p95": 1860.0,
        "max": 1908.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 690.0,
        "median": 1088.0,
        "p90": 1933.0,
        "p95": 1933.0,
        "max": 2259.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 33.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 201.0,
        "p95": 201.0,
        "max": 246.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 357.0,
        "median": 418.0,
        "p90": 448.0,
        "p95": 448.0,
        "max": 510.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 358.0,
        "median": 444.0,
        "p90": 1368.0,
        "p95": 1368.0,
        "max": 1369.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 33.0,
        "p90": 109.0,
        "p95": 109.0,
        "max": 112.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 227.0,
        "median": 277.0,
        "p90": 320.0,
        "p95": 334.0,
        "max": 334.0
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
        "count": 15,
        "min": 0.0,
        "median": 141.0,
        "p90": 162.0,
        "p95": 162.0,
        "max": 296.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 452.0,
        "median": 562.0,
        "p90": 1465.0,
        "p95": 1465.0,
        "max": 1466.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 55.0,
        "median": 71.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 85.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 51.0,
        "median": 68.0,
        "p90": 81.0,
        "p95": 81.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 702.0,
        "median": 1107.0,
        "p90": 1955.0,
        "p95": 1955.0,
        "max": 2279.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 6.922,
    "throughput_per_second": 2.167,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.547,
      "median": 2.86,
      "p90": 4.188,
      "p95": 4.188,
      "max": 4.235
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.157,
      "median": 0.219,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.375
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.203,
      "median": 0.203,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
    },
    "workers": {
      "worker-1": 8,
      "worker-2": 7
    },
    "cold_starts": 7,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 244.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 52.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 522.0,
        "median": 811.0,
        "p90": 1910.0,
        "p95": 1910.0,
        "max": 1983.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 639.0,
        "median": 925.0,
        "p90": 2055.0,
        "p95": 2055.0,
        "max": 2104.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 40.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 232.0,
        "p95": 232.0,
        "max": 264.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 333.0,
        "median": 387.0,
        "p90": 463.0,
        "p95": 463.0,
        "max": 475.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 333.0,
        "median": 458.0,
        "p90": 1393.0,
        "p95": 1393.0,
        "max": 1414.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 27.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 146.0
      },
      "warm_container_create_ms": {
        "count": 7,
        "min": 220.0,
        "median": 275.0,
        "p90": 297.0,
        "p95": 333.0,
        "max": 333.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 164.0,
        "p95": 164.0,
        "max": 274.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 420.0,
        "median": 554.0,
        "p90": 1488.0,
        "p95": 1488.0,
        "max": 1541.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 56.0,
        "median": 64.0,
        "p90": 95.0,
        "p95": 95.0,
        "max": 96.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 65.0,
        "p90": 83.0,
        "p95": 83.0,
        "max": 85.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 655.0,
        "median": 936.0,
        "p90": 2069.0,
        "p95": 2069.0,
        "max": 2121.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 6.954,
    "throughput_per_second": 2.157,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.562,
      "median": 2.782,
      "p90": 4.188,
      "p95": 4.188,
      "max": 4.204
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.219,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.375
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.172,
      "median": 0.172,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 10,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 312.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 31.0,
        "p90": 46.0,
        "p95": 46.0,
        "max": 64.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 599.0,
        "median": 934.0,
        "p90": 1887.0,
        "p95": 1887.0,
        "max": 1913.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 660.0,
        "median": 1165.0,
        "p90": 1970.0,
        "p95": 1970.0,
        "max": 2262.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 13.0,
        "p95": 13.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 33.0
      },
      "output_validation_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 174.0,
        "p95": 174.0,
        "max": 253.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 343.0,
        "median": 391.0,
        "p90": 438.0,
        "p95": 438.0,
        "max": 486.0
      },
      "runner_result_serialize_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 15,
        "min": 344.0,
        "median": 422.0,
        "p90": 1364.0,
        "p95": 1364.0,
        "max": 1422.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 18.0,
        "median": 24.0,
        "p90": 110.0,
        "p95": 110.0,
        "max": 139.0
      },
      "warm_container_create_ms": {
        "count": 10,
        "min": 229.0,
        "median": 293.5,
        "p90": 316.0,
        "p95": 318.0,
        "max": 318.0
      },
      "warm_container_reused": {
        "count": 5,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 307.0,
        "p95": 307.0,
        "max": 317.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 446.0,
        "median": 529.0,
        "p90": 1494.0,
        "p95": 1494.0,
        "max": 1529.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 58.0,
        "median": 69.0,
        "p90": 82.0,
        "p95": 82.0,
        "max": 91.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 55.0,
        "median": 68.0,
        "p90": 79.0,
        "p95": 79.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 688.0,
        "median": 1177.0,
        "p90": 1985.0,
        "p95": 1985.0,
        "max": 2283.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 32.094,
    "throughput_per_second": 0.935,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.453,
      "median": 1.601,
      "p90": 2.672,
      "p95": 2.766,
      "max": 2.813
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.297
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.172,
      "median": 0.172,
      "p90": 1.156,
      "p95": 1.156,
      "max": 1.156
    },
    "workers": {
      "worker-1": 13,
      "worker-2": 17
    },
    "cold_starts": 13,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 256.0,
        "max": 262.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 40.0,
        "max": 40.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 9.0,
        "max": 14.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 518.0,
        "median": 731.5,
        "p90": 1784.0,
        "p95": 1947.0,
        "max": 1990.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 580.0,
        "median": 1026.5,
        "p90": 1840.0,
        "p95": 2042.0,
        "max": 2054.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 10.0,
        "max": 28.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 33.0,
        "max": 37.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 194.0,
        "max": 221.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 340.0,
        "median": 399.5,
        "p90": 431.0,
        "p95": 462.0,
        "max": 474.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 340.0,
        "median": 405.0,
        "p90": 1366.0,
        "p95": 1426.0,
        "max": 1463.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 19.0,
        "median": 24.0,
        "p90": 37.0,
        "p95": 46.0,
        "max": 46.0
      },
      "warm_container_create_ms": {
        "count": 13,
        "min": 229.0,
        "median": 277.0,
        "p90": 307.0,
        "p95": 307.0,
        "max": 330.0
      },
      "warm_container_reused": {
        "count": 17,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 158.0,
        "p95": 163.0,
        "max": 171.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 427.0,
        "median": 510.5,
        "p90": 1486.0,
        "p95": 1530.0,
        "max": 1564.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 56.0,
        "median": 65.0,
        "p90": 75.0,
        "p95": 83.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 55.0,
        "median": 66.0,
        "p90": 79.0,
        "p95": 80.0,
        "max": 89.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 591.0,
        "median": 1040.5,
        "p90": 1852.0,
        "p95": 2059.0,
        "max": 2066.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 30.703,
    "throughput_per_second": 0.977,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.438,
      "median": 1.515,
      "p90": 2.672,
      "p95": 2.735,
      "max": 2.797
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.187,
      "p95": 0.203,
      "max": 0.265
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 13,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 245.0,
        "max": 257.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 45.0,
        "max": 49.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 502.0,
        "median": 822.5,
        "p90": 1765.0,
        "p95": 1821.0,
        "max": 2044.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 559.0,
        "median": 946.0,
        "p90": 1877.0,
        "p95": 2108.0,
        "max": 2109.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 12.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 35.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 216.0,
        "max": 218.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 335.0,
        "median": 392.5,
        "p90": 458.0,
        "p95": 498.0,
        "max": 501.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 336.0,
        "median": 420.5,
        "p90": 1349.0,
        "p95": 1457.0,
        "max": 1502.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 25.0,
        "p90": 43.0,
        "p95": 46.0,
        "max": 58.0
      },
      "warm_container_create_ms": {
        "count": 13,
        "min": 223.0,
        "median": 276.0,
        "p90": 309.0,
        "p95": 309.0,
        "max": 311.0
      },
      "warm_container_reused": {
        "count": 17,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 169.0,
        "p95": 180.0,
        "max": 281.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 418.0,
        "median": 522.0,
        "p90": 1438.0,
        "p95": 1582.0,
        "max": 1606.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 55.0,
        "median": 65.5,
        "p90": 74.0,
        "p95": 78.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 67.5,
        "p90": 85.0,
        "p95": 96.0,
        "max": 99.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 569.0,
        "median": 962.0,
        "p90": 1891.0,
        "p95": 2121.0,
        "max": 2122.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 33.453,
    "throughput_per_second": 0.897,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.437,
      "median": 2.101,
      "p90": 2.984,
      "p95": 3.828,
      "max": 4.407
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.125,
      "median": 0.157,
      "p90": 0.313,
      "p95": 0.5,
      "max": 1.485
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.14,
      "p90": 0.156,
      "p95": 0.156,
      "max": 0.156
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 12,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 244.0,
        "max": 257.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 39.0,
        "max": 43.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 9.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 497.0,
        "median": 740.0,
        "p90": 1624.0,
        "p95": 1890.0,
        "max": 1936.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 554.0,
        "median": 939.0,
        "p90": 1806.0,
        "p95": 2146.0,
        "max": 2149.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 33.0,
        "max": 36.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 206.0,
        "max": 240.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 331.0,
        "median": 383.5,
        "p90": 419.0,
        "p95": 435.0,
        "max": 481.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 332.0,
        "median": 394.5,
        "p90": 1390.0,
        "p95": 1409.0,
        "max": 1420.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 25.0,
        "p90": 43.0,
        "p95": 57.0,
        "max": 58.0
      },
      "warm_container_create_ms": {
        "count": 12,
        "min": 221.0,
        "median": 267.5,
        "p90": 303.0,
        "p95": 303.0,
        "max": 314.0
      },
      "warm_container_reused": {
        "count": 18,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 159.0,
        "p95": 169.0,
        "max": 191.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 416.0,
        "median": 502.5,
        "p90": 1492.0,
        "p95": 1510.0,
        "max": 1525.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 62.0,
        "p90": 76.0,
        "p95": 80.0,
        "max": 93.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.5,
        "p90": 71.0,
        "p95": 78.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 566.0,
        "median": 951.0,
        "p90": 1818.0,
        "p95": 2161.0,
        "max": 2162.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 15.922,
    "throughput_per_second": 1.884,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.422,
      "median": 1.586,
      "p90": 2.688,
      "p95": 2.891,
      "max": 3.75
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.188,
      "p95": 0.234,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.125,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 13,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 235.0,
        "max": 307.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 41.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 501.0,
        "median": 737.5,
        "p90": 1843.0,
        "p95": 1927.0,
        "max": 1933.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 555.0,
        "median": 967.0,
        "p90": 1957.0,
        "p95": 2161.0,
        "max": 2246.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 45.0,
        "max": 46.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 212.0,
        "max": 242.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 332.0,
        "median": 387.5,
        "p90": 470.0,
        "p95": 492.0,
        "max": 522.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 333.0,
        "median": 412.5,
        "p90": 1378.0,
        "p95": 1454.0,
        "max": 1471.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 25.5,
        "p90": 54.0,
        "p95": 99.0,
        "max": 124.0
      },
      "warm_container_create_ms": {
        "count": 13,
        "min": 209.0,
        "median": 252.0,
        "p90": 293.0,
        "p95": 293.0,
        "max": 320.0
      },
      "warm_container_reused": {
        "count": 17,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 150.0,
        "p95": 166.0,
        "max": 264.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 416.0,
        "median": 514.0,
        "p90": 1491.0,
        "p95": 1566.0,
        "max": 1569.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 51.0,
        "median": 60.0,
        "p90": 73.0,
        "p95": 80.0,
        "max": 83.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 62.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 85.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 569.0,
        "median": 983.0,
        "p90": 1976.0,
        "p95": 2175.0,
        "max": 2256.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 16.391,
    "throughput_per_second": 1.83,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.344,
      "median": 1.601,
      "p90": 2.734,
      "p95": 2.812,
      "max": 3.797
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.282
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.172,
      "p90": 1.172,
      "p95": 1.172,
      "max": 1.172
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 12,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 244.0,
        "max": 263.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 39.0,
        "p95": 48.0,
        "max": 54.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 9.0,
        "p95": 10.0,
        "max": 12.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 503.0,
        "median": 710.5,
        "p90": 1878.0,
        "p95": 2025.0,
        "max": 2037.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 565.0,
        "median": 932.5,
        "p90": 1939.0,
        "p95": 2186.0,
        "max": 2273.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 12.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 69.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 257.0,
        "max": 283.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 395.0,
        "p90": 442.0,
        "p95": 488.0,
        "max": 499.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 331.0,
        "median": 418.5,
        "p90": 1409.0,
        "p95": 1443.0,
        "max": 1501.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 26.5,
        "p90": 48.0,
        "p95": 52.0,
        "max": 87.0
      },
      "warm_container_create_ms": {
        "count": 12,
        "min": 216.0,
        "median": 244.0,
        "p90": 326.0,
        "p95": 326.0,
        "max": 335.0
      },
      "warm_container_reused": {
        "count": 18,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 151.0,
        "p95": 170.0,
        "max": 269.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 412.0,
        "median": 520.5,
        "p90": 1542.0,
        "p95": 1546.0,
        "max": 1617.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 64.0,
        "p90": 77.0,
        "p95": 83.0,
        "max": 91.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 66.0,
        "p90": 79.0,
        "p95": 92.0,
        "max": 111.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 573.0,
        "median": 943.5,
        "p90": 1953.0,
        "p95": 2209.0,
        "max": 2289.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 16.578,
    "throughput_per_second": 1.81,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.437,
      "median": 2.117,
      "p90": 2.688,
      "p95": 2.75,
      "max": 3.89
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.204,
      "p95": 0.234,
      "max": 0.265
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 13,
      "worker-2": 17
    },
    "cold_starts": 16,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 262.0,
        "max": 310.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 24.5,
        "p90": 37.0,
        "p95": 43.0,
        "max": 55.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 544.0,
        "median": 796.0,
        "p90": 1806.0,
        "p95": 1933.0,
        "max": 2013.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 627.0,
        "median": 1008.0,
        "p90": 2020.0,
        "p95": 2094.0,
        "max": 2109.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 9.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 42.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 174.0,
        "max": 184.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 335.0,
        "median": 391.0,
        "p90": 449.0,
        "p95": 462.0,
        "max": 485.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 347.0,
        "median": 420.0,
        "p90": 1359.0,
        "p95": 1392.0,
        "max": 1463.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 23.0,
        "p90": 42.0,
        "p95": 53.0,
        "max": 56.0
      },
      "warm_container_create_ms": {
        "count": 16,
        "min": 225.0,
        "median": 249.0,
        "p90": 308.0,
        "p95": 308.0,
        "max": 327.0
      },
      "warm_container_reused": {
        "count": 14,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 164.0,
        "p95": 254.0,
        "max": 289.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 432.0,
        "median": 524.0,
        "p90": 1454.0,
        "p95": 1511.0,
        "max": 1585.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 55.0,
        "median": 65.0,
        "p90": 81.0,
        "p95": 83.0,
        "max": 84.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 64.0,
        "p90": 74.0,
        "p95": 78.0,
        "max": 88.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 642.0,
        "median": 1023.0,
        "p90": 2031.0,
        "p95": 2105.0,
        "max": 2120.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 13.469,
    "throughput_per_second": 2.227,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.484,
      "median": 2.891,
      "p90": 3.985,
      "p95": 4.235,
      "max": 4.281
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.187,
      "p90": 1.469,
      "p95": 1.531,
      "max": 1.547
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.187,
      "median": 0.188,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.219
    },
    "workers": {
      "worker-1": 14,
      "worker-2": 16
    },
    "cold_starts": 13,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 293.0,
        "max": 300.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 43.0,
        "max": 44.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 584.0,
        "median": 872.0,
        "p90": 1828.0,
        "p95": 1908.0,
        "max": 1961.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 648.0,
        "median": 1075.5,
        "p90": 1907.0,
        "p95": 2146.0,
        "max": 2173.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.5,
        "p90": 11.0,
        "p95": 15.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 45.0,
        "max": 91.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 262.0,
        "max": 325.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 350.0,
        "median": 403.0,
        "p90": 451.0,
        "p95": 457.0,
        "max": 482.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 351.0,
        "median": 419.5,
        "p90": 1374.0,
        "p95": 1411.0,
        "max": 1441.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 32.5,
        "p90": 62.0,
        "p95": 83.0,
        "max": 97.0
      },
      "warm_container_create_ms": {
        "count": 13,
        "min": 237.0,
        "median": 276.0,
        "p90": 301.0,
        "p95": 301.0,
        "max": 314.0
      },
      "warm_container_reused": {
        "count": 17,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 159.0,
        "p95": 167.0,
        "max": 182.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 446.0,
        "median": 526.0,
        "p90": 1482.0,
        "p95": 1520.0,
        "max": 1549.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 59.0,
        "median": 69.0,
        "p90": 78.0,
        "p95": 82.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 58.0,
        "median": 72.5,
        "p90": 80.0,
        "p95": 88.0,
        "max": 91.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 668.0,
        "median": 1089.5,
        "p90": 1919.0,
        "p95": 2168.0,
        "max": 2188.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 12.657,
    "throughput_per_second": 2.37,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.532,
      "median": 2.812,
      "p90": 4.203,
      "p95": 5.047,
      "max": 5.234
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.141,
      "median": 0.195,
      "p90": 0.297,
      "p95": 0.36,
      "max": 0.516
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.218
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 12,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 265.0,
        "max": 300.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 43.0,
        "p95": 48.0,
        "max": 55.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 514.0,
        "median": 737.5,
        "p90": 1974.0,
        "p95": 1991.0,
        "max": 2062.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 570.0,
        "median": 968.5,
        "p90": 2062.0,
        "p95": 2079.0,
        "max": 2268.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 12.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 14.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 44.0,
        "max": 64.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 222.0,
        "max": 234.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 341.0,
        "median": 403.0,
        "p90": 462.0,
        "p95": 480.0,
        "max": 484.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 341.0,
        "median": 431.5,
        "p90": 1417.0,
        "p95": 1445.0,
        "max": 1485.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 37.5,
        "p90": 54.0,
        "p95": 87.0,
        "max": 101.0
      },
      "warm_container_create_ms": {
        "count": 12,
        "min": 260.0,
        "median": 288.5,
        "p90": 301.0,
        "p95": 301.0,
        "max": 329.0
      },
      "warm_container_reused": {
        "count": 18,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 170.0,
        "p95": 181.0,
        "max": 185.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 426.0,
        "median": 539.5,
        "p90": 1529.0,
        "p95": 1571.0,
        "max": 1603.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 55.0,
        "median": 70.5,
        "p90": 84.0,
        "p95": 87.0,
        "max": 92.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 55.0,
        "median": 69.0,
        "p90": 85.0,
        "p95": 88.0,
        "max": 90.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 580.0,
        "median": 984.0,
        "p90": 2077.0,
        "p95": 2093.0,
        "max": 2288.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 13.016,
    "throughput_per_second": 2.305,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.469,
      "median": 2.859,
      "p90": 4.188,
      "p95": 4.828,
      "max": 5.078
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.179,
      "p90": 0.297,
      "p95": 0.36,
      "max": 0.375
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 15,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 271.0,
        "max": 358.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 14.0,
        "p90": 39.0,
        "p95": 49.0,
        "max": 50.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 9.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 528.0,
        "median": 837.0,
        "p90": 1971.0,
        "p95": 2044.0,
        "max": 2076.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 590.0,
        "median": 1059.5,
        "p90": 2069.0,
        "p95": 2222.0,
        "max": 2265.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 12.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 13.0,
        "p95": 15.0,
        "max": 16.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 53.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 2.0,
        "p95": 250.0,
        "max": 275.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 333.0,
        "median": 402.5,
        "p90": 479.0,
        "p95": 510.0,
        "max": 560.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 334.0,
        "median": 430.5,
        "p90": 1455.0,
        "p95": 1479.0,
        "max": 1561.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 19.0,
        "median": 26.0,
        "p90": 79.0,
        "p95": 137.0,
        "max": 232.0
      },
      "warm_container_create_ms": {
        "count": 15,
        "min": 231.0,
        "median": 288.0,
        "p90": 332.0,
        "p95": 332.0,
        "max": 363.0
      },
      "warm_container_reused": {
        "count": 15,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 172.0,
        "p95": 181.0,
        "max": 308.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 423.0,
        "median": 538.5,
        "p90": 1570.0,
        "p95": 1608.0,
        "max": 1668.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 56.0,
        "median": 69.0,
        "p90": 85.0,
        "p95": 100.0,
        "max": 111.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 56.0,
        "median": 70.0,
        "p90": 78.0,
        "p95": 96.0,
        "max": 109.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 606.0,
        "median": 1075.0,
        "p90": 2096.0,
        "p95": 2236.0,
        "max": 2280.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 2,
    "repeat": 1,
    "wall_seconds": 84.594,
    "throughput_per_second": 0.946,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.422,
      "median": 1.532,
      "p90": 2.688,
      "p95": 3.25,
      "max": 3.828
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.188,
      "p95": 0.218,
      "max": 0.5
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.203,
      "max": 0.203
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 25,
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
        "p95": 279.0,
        "max": 293.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 35.0,
        "p95": 38.0,
        "max": 43.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 7.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 518.0,
        "median": 653.5,
        "p90": 1673.0,
        "p95": 1871.0,
        "max": 1954.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 578.0,
        "median": 733.0,
        "p90": 1749.0,
        "p95": 2068.0,
        "max": 2174.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 37.0,
        "max": 42.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 206.0,
        "max": 217.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 343.0,
        "median": 390.0,
        "p90": 448.0,
        "p95": 454.0,
        "max": 505.0
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
        "min": 344.0,
        "median": 431.5,
        "p90": 1386.0,
        "p95": 1408.0,
        "max": 1460.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 25.0,
        "p90": 43.0,
        "p95": 49.0,
        "max": 53.0
      },
      "warm_container_create_ms": {
        "count": 25,
        "min": 226.0,
        "median": 268.0,
        "p90": 292.0,
        "p95": 300.0,
        "max": 331.0
      },
      "warm_container_reused": {
        "count": 55,
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
        "p90": 161.0,
        "p95": 167.0,
        "max": 174.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 435.0,
        "median": 535.5,
        "p90": 1491.0,
        "p95": 1506.0,
        "max": 1568.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 57.0,
        "median": 64.0,
        "p90": 75.0,
        "p95": 78.0,
        "max": 94.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 56.0,
        "median": 63.5,
        "p90": 79.0,
        "p95": 81.0,
        "max": 90.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 590.0,
        "median": 746.5,
        "p90": 1764.0,
        "p95": 2084.0,
        "max": 2193.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 2,
    "repeat": 2,
    "wall_seconds": 83.329,
    "throughput_per_second": 0.96,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.438,
      "median": 1.547,
      "p90": 2.687,
      "p95": 2.766,
      "max": 4.156
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.125,
      "median": 0.172,
      "p90": 0.188,
      "p95": 0.281,
      "max": 1.172
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.187,
      "p95": 0.547,
      "max": 0.547
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 19,
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
        "p95": 255.0,
        "max": 296.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 40.0,
        "max": 45.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 7.0,
        "max": 13.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 532.0,
        "median": 673.5,
        "p90": 1600.0,
        "p95": 1626.0,
        "max": 1952.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 596.0,
        "median": 751.5,
        "p90": 1665.0,
        "p95": 1693.0,
        "max": 2148.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 10.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 34.0,
        "max": 62.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 211.0,
        "max": 305.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 345.0,
        "median": 400.0,
        "p90": 439.0,
        "p95": 462.0,
        "max": 482.0
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
        "min": 346.0,
        "median": 422.0,
        "p90": 1401.0,
        "p95": 1410.0,
        "max": 1427.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 28.0,
        "p90": 46.0,
        "p95": 54.0,
        "max": 64.0
      },
      "warm_container_create_ms": {
        "count": 19,
        "min": 244.0,
        "median": 266.0,
        "p90": 299.0,
        "p95": 299.0,
        "max": 318.0
      },
      "warm_container_reused": {
        "count": 61,
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
        "p90": 151.0,
        "p95": 160.0,
        "max": 165.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 437.0,
        "median": 531.5,
        "p90": 1498.0,
        "p95": 1517.0,
        "max": 1526.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 64.0,
        "p90": 75.0,
        "p95": 79.0,
        "max": 101.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 57.0,
        "median": 64.0,
        "p90": 78.0,
        "p95": 81.0,
        "max": 91.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 609.0,
        "median": 768.0,
        "p90": 1680.0,
        "p95": 1707.0,
        "max": 2165.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 2,
    "repeat": 3,
    "wall_seconds": 82.515,
    "throughput_per_second": 0.97,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.437,
      "median": 1.593,
      "p90": 2.719,
      "p95": 2.859,
      "max": 4.579
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.266,
      "max": 1.235
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.203,
      "max": 0.203
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 20,
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
        "p95": 249.0,
        "max": 291.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 33.0,
        "max": 53.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 529.0,
        "median": 615.0,
        "p90": 1687.0,
        "p95": 1822.0,
        "max": 1930.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 587.0,
        "median": 682.5,
        "p90": 1765.0,
        "p95": 2023.0,
        "max": 2137.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 37.0,
        "max": 55.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 201.0,
        "max": 266.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 346.0,
        "median": 390.0,
        "p90": 425.0,
        "p95": 432.0,
        "max": 485.0
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
        "min": 347.0,
        "median": 404.5,
        "p90": 1376.0,
        "p95": 1405.0,
        "max": 1480.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 26.0,
        "p90": 42.0,
        "p95": 44.0,
        "max": 50.0
      },
      "warm_container_create_ms": {
        "count": 20,
        "min": 227.0,
        "median": 257.5,
        "p90": 277.0,
        "p95": 281.0,
        "max": 284.0
      },
      "warm_container_reused": {
        "count": 60,
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
        "p90": 146.0,
        "p95": 156.0,
        "max": 277.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 435.0,
        "median": 503.5,
        "p90": 1486.0,
        "p95": 1507.0,
        "max": 1579.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 63.0,
        "p90": 73.0,
        "p95": 77.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 56.0,
        "median": 64.0,
        "p90": 78.0,
        "p95": 82.0,
        "max": 90.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 599.0,
        "median": 697.5,
        "p90": 1780.0,
        "p95": 2038.0,
        "max": 2155.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 4,
    "repeat": 1,
    "wall_seconds": 43.203,
    "throughput_per_second": 1.852,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.437,
      "median": 1.563,
      "p90": 2.719,
      "p95": 2.781,
      "max": 3.984
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.171,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.219
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.187,
      "max": 0.187
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 29,
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
        "p95": 253.0,
        "max": 291.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 44.0,
        "max": 56.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 7.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 525.0,
        "median": 692.5,
        "p90": 1851.0,
        "p95": 1904.0,
        "max": 2040.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 584.0,
        "median": 891.5,
        "p90": 1932.0,
        "p95": 2063.0,
        "max": 2418.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 10.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 72.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 191.0,
        "max": 239.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 346.0,
        "median": 393.5,
        "p90": 448.0,
        "p95": 470.0,
        "max": 503.0
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
        "min": 349.0,
        "median": 410.0,
        "p90": 1396.0,
        "p95": 1420.0,
        "max": 1449.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 19.0,
        "median": 29.0,
        "p90": 42.0,
        "p95": 48.0,
        "max": 72.0
      },
      "warm_container_create_ms": {
        "count": 29,
        "min": 234.0,
        "median": 263.0,
        "p90": 307.0,
        "p95": 310.0,
        "max": 320.0
      },
      "warm_container_reused": {
        "count": 51,
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
        "p90": 163.0,
        "p95": 171.0,
        "max": 299.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 435.0,
        "median": 519.5,
        "p90": 1498.0,
        "p95": 1527.0,
        "max": 1559.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 67.0,
        "p90": 78.0,
        "p95": 80.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 56.0,
        "median": 64.0,
        "p90": 79.0,
        "p95": 83.0,
        "max": 103.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 595.0,
        "median": 904.0,
        "p90": 1949.0,
        "p95": 2077.0,
        "max": 2433.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 4,
    "repeat": 2,
    "wall_seconds": 44.454,
    "throughput_per_second": 1.8,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.437,
      "median": 2.57,
      "p90": 2.718,
      "p95": 2.734,
      "max": 3.781
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.171,
      "p90": 0.219,
      "p95": 0.296,
      "max": 1.172
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 32,
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
        "p95": 280.0,
        "max": 314.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 47.0,
        "max": 78.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 14.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 532.0,
        "median": 895.5,
        "p90": 1630.0,
        "p95": 1844.0,
        "max": 2058.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 592.0,
        "median": 1008.0,
        "p90": 1763.0,
        "p95": 2026.0,
        "max": 2271.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 10.0,
        "max": 29.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 40.0,
        "max": 77.0
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
        "p90": 0.0,
        "p95": 205.0,
        "max": 240.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 351.0,
        "median": 394.5,
        "p90": 457.0,
        "p95": 485.0,
        "max": 537.0
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
        "min": 353.0,
        "median": 423.0,
        "p90": 1381.0,
        "p95": 1431.0,
        "max": 1466.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 19.0,
        "median": 27.5,
        "p90": 49.0,
        "p95": 60.0,
        "max": 77.0
      },
      "warm_container_create_ms": {
        "count": 32,
        "min": 227.0,
        "median": 279.5,
        "p90": 324.0,
        "p95": 328.0,
        "max": 339.0
      },
      "warm_container_reused": {
        "count": 48,
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
        "p90": 173.0,
        "p95": 289.0,
        "max": 316.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 443.0,
        "median": 525.0,
        "p90": 1483.0,
        "p95": 1542.0,
        "max": 1581.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 67.0,
        "p90": 78.0,
        "p95": 83.0,
        "max": 89.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 58.0,
        "median": 68.0,
        "p90": 81.0,
        "p95": 83.0,
        "max": 96.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 602.0,
        "median": 1025.0,
        "p90": 1779.0,
        "p95": 2042.0,
        "max": 2292.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 4,
    "repeat": 3,
    "wall_seconds": 44.313,
    "throughput_per_second": 1.805,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.407,
      "median": 2.218,
      "p90": 2.718,
      "p95": 2.735,
      "max": 3.672
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.125,
      "median": 0.157,
      "p90": 0.297,
      "p95": 0.594,
      "max": 0.813
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.172,
      "p95": 0.187,
      "max": 0.187
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 29,
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
        "p95": 267.0,
        "max": 313.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 46.0,
        "max": 64.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 17.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 529.0,
        "median": 764.0,
        "p90": 1618.0,
        "p95": 1906.0,
        "max": 2090.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 591.0,
        "median": 996.0,
        "p90": 1791.0,
        "p95": 2003.0,
        "max": 2157.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 24.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 40.0
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
        "p90": 2.0,
        "p95": 187.0,
        "max": 233.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 346.0,
        "median": 385.0,
        "p90": 468.0,
        "p95": 491.0,
        "max": 599.0
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
        "min": 346.0,
        "median": 421.0,
        "p90": 1386.0,
        "p95": 1425.0,
        "max": 1510.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 27.0,
        "p90": 50.0,
        "p95": 73.0,
        "max": 103.0
      },
      "warm_container_create_ms": {
        "count": 29,
        "min": 218.0,
        "median": 274.0,
        "p90": 320.0,
        "p95": 368.0,
        "max": 383.0
      },
      "warm_container_reused": {
        "count": 51,
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
        "p90": 157.0,
        "p95": 177.0,
        "max": 332.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 433.0,
        "median": 534.5,
        "p90": 1497.0,
        "p95": 1540.0,
        "max": 1629.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 65.5,
        "p90": 81.0,
        "p95": 85.0,
        "max": 106.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 55.0,
        "median": 67.0,
        "p90": 84.0,
        "p95": 90.0,
        "max": 102.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 605.0,
        "median": 1009.5,
        "p90": 1804.0,
        "p95": 2019.0,
        "max": 2170.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "repeat": 1,
    "wall_seconds": 30.219,
    "throughput_per_second": 2.647,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.485,
      "median": 2.75,
      "p90": 3.953,
      "p95": 4.109,
      "max": 5.109
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.187,
      "p90": 0.266,
      "p95": 0.328,
      "max": 0.547
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.188,
      "max": 0.188
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 41,
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
        "p95": 277.0,
        "max": 344.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 25.5,
        "p90": 43.0,
        "p95": 51.0,
        "max": 54.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 571.0,
        "median": 952.5,
        "p90": 1773.0,
        "p95": 1994.0,
        "max": 2076.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 631.0,
        "median": 1109.5,
        "p90": 2014.0,
        "p95": 2074.0,
        "max": 2287.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 26.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 16.0,
        "max": 28.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 42.0,
        "max": 92.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 250.0,
        "max": 277.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 349.0,
        "median": 426.5,
        "p90": 493.0,
        "p95": 498.0,
        "max": 524.0
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
        "max": 2.0
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
        "min": 350.0,
        "median": 446.5,
        "p90": 1421.0,
        "p95": 1454.0,
        "max": 1526.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 30.5,
        "p90": 108.0,
        "p95": 132.0,
        "max": 189.0
      },
      "warm_container_create_ms": {
        "count": 41,
        "min": 227.0,
        "median": 281.0,
        "p90": 306.0,
        "p95": 312.0,
        "max": 326.0
      },
      "warm_container_reused": {
        "count": 39,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 80,
        "min": 0.0,
        "median": 67.5,
        "p90": 162.0,
        "p95": 166.0,
        "max": 341.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 440.0,
        "median": 561.0,
        "p90": 1534.0,
        "p95": 1574.0,
        "max": 1635.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 57.0,
        "median": 71.0,
        "p90": 84.0,
        "p95": 89.0,
        "max": 107.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 57.0,
        "median": 72.0,
        "p90": 88.0,
        "p95": 91.0,
        "max": 111.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 654.0,
        "median": 1126.0,
        "p90": 2028.0,
        "p95": 2087.0,
        "max": 2306.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "repeat": 2,
    "wall_seconds": 31.469,
    "throughput_per_second": 2.542,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.484,
      "median": 2.758,
      "p90": 3.953,
      "p95": 3.984,
      "max": 4.438
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.297,
      "p95": 0.343,
      "max": 0.516
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.25,
      "p95": 0.297,
      "max": 0.297
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 45,
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
        "p95": 257.0,
        "max": 299.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 28.0,
        "p90": 43.0,
        "p95": 49.0,
        "max": 55.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 11.0,
        "max": 20.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 553.0,
        "median": 955.5,
        "p90": 1825.0,
        "p95": 2014.0,
        "max": 2150.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 612.0,
        "median": 1118.0,
        "p90": 2008.0,
        "p95": 2088.0,
        "max": 2401.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 13.0,
        "max": 20.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 76.0
      },
      "output_validation_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 2.0,
        "p95": 220.0,
        "max": 265.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 354.0,
        "median": 412.0,
        "p90": 468.0,
        "p95": 486.0,
        "max": 512.0
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
        "min": 355.0,
        "median": 442.5,
        "p90": 1431.0,
        "p95": 1457.0,
        "max": 1487.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 34.5,
        "p90": 102.0,
        "p95": 147.0,
        "max": 265.0
      },
      "warm_container_create_ms": {
        "count": 45,
        "min": 218.0,
        "median": 277.0,
        "p90": 300.0,
        "p95": 306.0,
        "max": 348.0
      },
      "warm_container_reused": {
        "count": 35,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 80,
        "min": 0.0,
        "median": 131.0,
        "p90": 172.0,
        "p95": 307.0,
        "max": 344.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 442.0,
        "median": 553.5,
        "p90": 1535.0,
        "p95": 1566.0,
        "max": 1601.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 56.0,
        "median": 70.0,
        "p90": 86.0,
        "p95": 87.0,
        "max": 103.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 55.0,
        "median": 70.5,
        "p90": 89.0,
        "p95": 93.0,
        "max": 104.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 631.0,
        "median": 1140.0,
        "p90": 2024.0,
        "p95": 2105.0,
        "max": 2421.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "repeat": 3,
    "wall_seconds": 30.375,
    "throughput_per_second": 2.634,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.547,
      "median": 2.844,
      "p90": 4.016,
      "p95": 4.265,
      "max": 4.828
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.141,
      "median": 0.234,
      "p90": 0.453,
      "p95": 1.203,
      "max": 1.547
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.157,
      "median": 0.188,
      "p90": 0.219,
      "p95": 0.344,
      "max": 0.344
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 38,
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
        "p95": 259.0,
        "max": 289.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 48.0,
        "p95": 51.0,
        "max": 77.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 13.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 525.0,
        "median": 908.0,
        "p90": 1719.0,
        "p95": 2014.0,
        "max": 2111.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 587.0,
        "median": 1091.5,
        "p90": 1950.0,
        "p95": 2119.0,
        "max": 2355.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 20.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 65.0
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
        "p90": 0.0,
        "p95": 225.0,
        "max": 286.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 345.0,
        "median": 414.0,
        "p90": 490.0,
        "p95": 504.0,
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
        "min": 345.0,
        "median": 434.5,
        "p90": 1425.0,
        "p95": 1463.0,
        "max": 1518.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 33.0,
        "p90": 81.0,
        "p95": 89.0,
        "max": 129.0
      },
      "warm_container_create_ms": {
        "count": 38,
        "min": 240.0,
        "median": 280.0,
        "p90": 305.0,
        "p95": 308.0,
        "max": 318.0
      },
      "warm_container_reused": {
        "count": 42,
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
        "p90": 179.0,
        "p95": 194.0,
        "max": 299.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 432.0,
        "median": 549.5,
        "p90": 1557.0,
        "p95": 1580.0,
        "max": 1634.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 69.0,
        "p90": 82.0,
        "p95": 84.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 55.0,
        "median": 69.5,
        "p90": 81.0,
        "p95": 86.0,
        "max": 97.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 601.0,
        "median": 1107.5,
        "p90": 1970.0,
        "p95": 2132.0,
        "max": 2380.0
      }
    }
  }
]
```
