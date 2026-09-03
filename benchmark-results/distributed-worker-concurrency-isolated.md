# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T19:54:07.886813+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `62`, version `62`, image `10.42.1.22:5000/functions/bench-tiny-beafb7ef:v62-v1-a1-ca8ab54376fc-d1`
- `sleep`: function `63`, version `63`, image `10.42.1.22:5000/functions/bench-sleep-294b64c2:v63-v1-a1-a019785f0267-d1`
- `dependency`: function `64`, version `64`, image `10.42.1.22:5000/functions/bench-dependency-b4edb26d:v64-v1-a1-6b1d25ea3fcb-d1`
- `output`: function `65`, version `65`, image `10.42.1.22:5000/functions/bench-output-a5cbe4e3:v65-v1-a1-9bed13742536-d1`
- `input_output`: function `66`, version `66`, image `10.42.1.22:5000/functions/bench-input_output-b18d5f40:v66-v1-a1-b8a52d4d8f14-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mixed-30 | 30 | 2 | 4 | 32 | 1 | 30 | 0 | 14.313 | 2.096 | 7.93 | 13.266 | worker-1:16, worker-2:14 |
| mixed-30 | 30 | 2 | 4 | 32 | 2 | 30 | 0 | 11.922 | 2.516 | 7.258 | 11.703 | worker-1:16, worker-2:14 |
| mixed-80 | 80 | 2 | 4 | 32 | 1 | 80 | 0 | 34.36 | 2.328 | 9.984 | 13.047 | worker-1:41, worker-2:39 |
| mixed-80 | 80 | 2 | 4 | 32 | 2 | 80 | 0 | 29.906 | 2.675 | 10.078 | 12.844 | worker-1:39, worker-2:41 |
| mixed-30 | 30 | 4 | 8 | 32 | 1 | 30 | 0 | 11.453 | 2.619 | 7.062 | 10.25 | worker-1:17, worker-2:13 |
| mixed-30 | 30 | 4 | 8 | 32 | 2 | 30 | 0 | 11.031 | 2.72 | 6.586 | 10.625 | worker-1:14, worker-2:16 |
| mixed-80 | 80 | 4 | 8 | 32 | 1 | 80 | 0 | 24.063 | 3.325 | 8.188 | 10.797 | worker-1:41, worker-2:39 |
| mixed-80 | 80 | 4 | 8 | 32 | 2 | 80 | 0 | 24.625 | 3.249 | 8.054 | 11.547 | worker-1:42, worker-2:38 |
| mixed-30 | 30 | 8 | 16 | 32 | 1 | 30 | 0 | 9.796 | 3.062 | 6.508 | 9.266 | worker-1:16, worker-2:14 |
| mixed-30 | 30 | 8 | 16 | 32 | 2 | 30 | 0 | 10.891 | 2.755 | 7.539 | 10.14 | worker-1:15, worker-2:15 |
| mixed-80 | 80 | 8 | 16 | 32 | 1 | 80 | 0 | 23.813 | 3.36 | 7.594 | 12.156 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 8 | 16 | 32 | 2 | 80 | 0 | 24.641 | 3.247 | 7.804 | 12.171 | worker-1:39, worker-2:41 |
| mixed-30 | 30 | 16 | 32 | 32 | 1 | 30 | 0 | 10.391 | 2.887 | 9.235 | 10.172 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 16 | 32 | 32 | 2 | 30 | 0 | 12.547 | 2.391 | 9.031 | 11.047 | worker-1:12, worker-2:18 |
| mixed-80 | 80 | 16 | 32 | 32 | 1 | 80 | 0 | 24.953 | 3.206 | 8.234 | 13.781 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 16 | 32 | 32 | 2 | 80 | 0 | 24.125 | 3.316 | 8.234 | 14.25 | worker-1:43, worker-2:37 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 1,
    "wall_seconds": 14.313,
    "throughput_per_second": 2.096,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.266,
      "median": 7.93,
      "p90": 11.609,
      "p95": 13.266,
      "max": 14.297
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.187,
      "median": 0.804,
      "p90": 1.359,
      "p95": 1.453,
      "max": 1.484
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.125,
      "median": 0.156,
      "p90": 0.157,
      "p95": 0.157,
      "max": 0.157
    },
    "workers": {
      "worker-1": 16,
      "worker-2": 14
    },
    "cold_starts": 22,
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
        "median": 36.0,
        "p90": 169.0,
        "p95": 205.0,
        "max": 206.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 565.0,
        "median": 1024.0,
        "p90": 1916.0,
        "p95": 1999.0,
        "max": 2065.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 627.0,
        "median": 1293.0,
        "p90": 2065.0,
        "p95": 2103.0,
        "max": 2136.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 16.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 72.0
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
        "p95": 175.0,
        "max": 191.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 383.5,
        "p90": 438.0,
        "p95": 451.0,
        "max": 459.0
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
        "min": 337.0,
        "median": 422.0,
        "p90": 1380.0,
        "p95": 1399.0,
        "max": 1412.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 23.0,
        "median": 60.5,
        "p90": 286.0,
        "p95": 480.0,
        "max": 555.0
      },
      "warm_container_create_ms": {
        "count": 22,
        "min": 209.0,
        "median": 278.0,
        "p90": 328.0,
        "p95": 355.0,
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
        "count": 30,
        "min": 0.0,
        "median": 121.0,
        "p90": 155.0,
        "p95": 290.0,
        "max": 307.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 434.0,
        "median": 524.5,
        "p90": 1474.0,
        "p95": 1504.0,
        "max": 1524.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 65.5,
        "p90": 77.0,
        "p95": 81.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 67.5,
        "p90": 78.0,
        "p95": 82.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 640.0,
        "median": 1310.0,
        "p90": 2075.0,
        "p95": 2114.0,
        "max": 2158.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 2,
    "wall_seconds": 11.922,
    "throughput_per_second": 2.516,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.422,
      "median": 7.258,
      "p90": 11.125,
      "p95": 11.703,
      "max": 11.906
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.218,
      "median": 0.781,
      "p90": 1.515,
      "p95": 1.797,
      "max": 1.984
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.188,
      "median": 0.218,
      "p90": 0.235,
      "p95": 0.235,
      "max": 0.235
    },
    "workers": {
      "worker-1": 16,
      "worker-2": 14
    },
    "cold_starts": 14,
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
        "max": 257.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 39.0,
        "p95": 46.0,
        "max": 46.0
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
        "min": 509.0,
        "median": 913.5,
        "p90": 1926.0,
        "p95": 1986.0,
        "max": 2028.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 566.0,
        "median": 1177.5,
        "p90": 2119.0,
        "p95": 2198.0,
        "max": 2231.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 9.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 141.0,
        "max": 348.0
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
        "p95": 230.0,
        "max": 237.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 331.0,
        "median": 375.5,
        "p90": 444.0,
        "p95": 487.0,
        "max": 529.0
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
        "median": 427.5,
        "p90": 1383.0,
        "p95": 1394.0,
        "max": 1419.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 46.0,
        "p90": 443.0,
        "p95": 653.0,
        "max": 1098.0
      },
      "warm_container_create_ms": {
        "count": 14,
        "min": 231.0,
        "median": 260.0,
        "p90": 292.0,
        "p95": 292.0,
        "max": 294.0
      },
      "warm_container_reused": {
        "count": 16,
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
        "p90": 142.0,
        "p95": 149.0,
        "max": 158.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 417.0,
        "median": 521.5,
        "p90": 1493.0,
        "p95": 1521.0,
        "max": 1542.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 55.0,
        "median": 63.0,
        "p90": 75.0,
        "p95": 79.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 55.0,
        "median": 64.0,
        "p90": 75.0,
        "p95": 81.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 578.0,
        "median": 1199.5,
        "p90": 2132.0,
        "p95": 2213.0,
        "max": 2241.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 1,
    "wall_seconds": 34.36,
    "throughput_per_second": 2.328,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 2.985,
      "median": 9.984,
      "p90": 12.172,
      "p95": 13.047,
      "max": 29.594
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.171,
      "median": 0.438,
      "p90": 1.485,
      "p95": 1.938,
      "max": 2.141
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.235,
      "p90": 0.312,
      "p95": 0.625,
      "max": 0.625
    },
    "workers": {
      "worker-1": 41,
      "worker-2": 39
    },
    "cold_starts": 39,
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
        "p95": 240.0,
        "max": 278.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 42.0,
        "p95": 46.0,
        "max": 56.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 514.0,
        "median": 852.5,
        "p90": 1879.0,
        "p95": 1967.0,
        "max": 2068.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 590.0,
        "median": 1074.0,
        "p90": 2030.0,
        "p95": 2138.0,
        "max": 2471.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 14.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 7.0,
        "p90": 13.0,
        "p95": 15.0,
        "max": 22.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 78.0,
        "max": 707.0
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
        "p95": 219.0,
        "max": 263.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 329.0,
        "median": 379.5,
        "p90": 443.0,
        "p95": 467.0,
        "max": 488.0
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
        "min": 330.0,
        "median": 397.5,
        "p90": 1355.0,
        "p95": 1390.0,
        "max": 1454.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 22.0,
        "median": 76.5,
        "p90": 254.0,
        "p95": 318.0,
        "max": 647.0
      },
      "warm_container_create_ms": {
        "count": 39,
        "min": 216.0,
        "median": 260.0,
        "p90": 295.0,
        "p95": 312.0,
        "max": 325.0
      },
      "warm_container_reused": {
        "count": 41,
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
        "p90": 149.0,
        "p95": 155.0,
        "max": 286.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 415.0,
        "median": 502.0,
        "p90": 1456.0,
        "p95": 1492.0,
        "max": 1576.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 52.0,
        "median": 67.0,
        "p90": 78.0,
        "p95": 81.0,
        "max": 87.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 65.0,
        "p90": 80.0,
        "p95": 88.0,
        "max": 113.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 613.0,
        "median": 1088.0,
        "p90": 2043.0,
        "p95": 2159.0,
        "max": 2500.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 2,
    "wall_seconds": 29.906,
    "throughput_per_second": 2.675,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 2.297,
      "median": 10.078,
      "p90": 12.312,
      "p95": 12.844,
      "max": 14.703
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.156,
      "median": 0.391,
      "p90": 1.312,
      "p95": 1.468,
      "max": 1.828
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.172,
      "median": 0.235,
      "p90": 0.328,
      "p95": 0.359,
      "max": 0.359
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
        "p95": 238.0,
        "max": 284.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 45.0,
        "p95": 46.0,
        "max": 54.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 7.0,
        "max": 12.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 522.0,
        "median": 917.5,
        "p90": 1904.0,
        "p95": 1949.0,
        "max": 2165.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 576.0,
        "median": 1151.5,
        "p90": 2017.0,
        "p95": 2167.0,
        "max": 2238.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 17.0,
        "max": 23.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 13.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 70.0,
        "max": 522.0
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
        "max": 257.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 332.0,
        "median": 383.5,
        "p90": 440.0,
        "p95": 446.0,
        "max": 492.0
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
        "median": 408.0,
        "p90": 1365.0,
        "p95": 1403.0,
        "max": 1447.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 21.0,
        "median": 84.0,
        "p90": 325.0,
        "p95": 420.0,
        "max": 716.0
      },
      "warm_container_create_ms": {
        "count": 38,
        "min": 216.0,
        "median": 253.0,
        "p90": 278.0,
        "p95": 290.0,
        "max": 327.0
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
        "p90": 145.0,
        "p95": 152.0,
        "max": 254.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 421.0,
        "median": 511.0,
        "p90": 1480.0,
        "p95": 1502.0,
        "max": 1564.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 65.0,
        "p90": 75.0,
        "p95": 77.0,
        "max": 94.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 55.0,
        "median": 66.0,
        "p90": 79.0,
        "p95": 87.0,
        "max": 93.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 592.0,
        "median": 1171.5,
        "p90": 2047.0,
        "p95": 2180.0,
        "max": 2258.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 4,
    "cluster_invocation_capacity": 8,
    "repeat": 1,
    "wall_seconds": 11.453,
    "throughput_per_second": 2.619,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.844,
      "median": 7.062,
      "p90": 9.859,
      "p95": 10.25,
      "max": 10.406
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.375,
      "median": 1.024,
      "p90": 1.875,
      "p95": 2.203,
      "max": 2.703
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.172,
      "median": 0.235,
      "p90": 0.765,
      "p95": 0.765,
      "max": 0.765
    },
    "workers": {
      "worker-1": 17,
      "worker-2": 13
    },
    "cold_starts": 26,
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
        "p95": 264.0,
        "max": 279.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 57.0,
        "p90": 89.0,
        "p95": 94.0,
        "max": 103.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 13.0,
        "max": 19.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 749.0,
        "median": 1526.5,
        "p90": 2515.0,
        "p95": 2706.0,
        "max": 2980.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 1023.0,
        "median": 2015.5,
        "p90": 2772.0,
        "p95": 2783.0,
        "max": 3335.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 16.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 5.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 14.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 38.0,
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
        "p95": 1002.0,
        "max": 1003.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 320.0,
        "max": 343.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 366.0,
        "median": 545.0,
        "p90": 663.0,
        "p95": 745.0,
        "max": 761.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
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
        "min": 366.0,
        "median": 629.0,
        "p90": 1500.0,
        "p95": 1549.0,
        "max": 1587.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 27.0,
        "median": 90.0,
        "p90": 888.0,
        "p95": 1057.0,
        "max": 1196.0
      },
      "warm_container_create_ms": {
        "count": 26,
        "min": 247.0,
        "median": 409.0,
        "p90": 553.0,
        "p95": 554.0,
        "max": 579.0
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
        "count": 30,
        "min": 0.0,
        "median": 160.5,
        "p90": 285.0,
        "p95": 490.0,
        "max": 586.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 464.0,
        "median": 795.0,
        "p90": 1711.0,
        "p95": 1741.0,
        "max": 1785.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 90.5,
        "p90": 171.0,
        "p95": 177.0,
        "max": 185.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 58.0,
        "median": 98.5,
        "p90": 147.0,
        "p95": 194.0,
        "max": 206.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 1039.0,
        "median": 2033.0,
        "p90": 2798.0,
        "p95": 2805.0,
        "max": 3367.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 4,
    "cluster_invocation_capacity": 8,
    "repeat": 2,
    "wall_seconds": 11.031,
    "throughput_per_second": 2.72,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.547,
      "median": 6.586,
      "p90": 9.406,
      "p95": 10.625,
      "max": 10.687
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.312,
      "median": 1.015,
      "p90": 1.797,
      "p95": 2.0,
      "max": 2.234
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
      "worker-1": 14,
      "worker-2": 16
    },
    "cold_starts": 23,
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
        "p95": 330.0,
        "max": 510.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 53.5,
        "p90": 100.0,
        "p95": 101.0,
        "max": 131.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 7.0,
        "p90": 13.0,
        "p95": 16.0,
        "max": 19.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 742.0,
        "median": 1670.5,
        "p90": 2540.0,
        "p95": 2617.0,
        "max": 2750.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 939.0,
        "median": 1955.5,
        "p90": 2771.0,
        "p95": 2930.0,
        "max": 3160.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 13.0,
        "max": 20.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 18.0,
        "max": 21.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 40.0,
        "max": 43.0
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
        "max": 1.0
      },
      "runner_environment_read_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
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
        "p95": 1002.0,
        "max": 1002.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 3.0,
        "p95": 366.0,
        "max": 413.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 364.0,
        "median": 559.5,
        "p90": 763.0,
        "p95": 809.0,
        "max": 810.0
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
        "min": 442.0,
        "median": 630.5,
        "p90": 1615.0,
        "p95": 1709.0,
        "max": 1789.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 83.5,
        "p90": 395.0,
        "p95": 963.0,
        "max": 969.0
      },
      "warm_container_create_ms": {
        "count": 23,
        "min": 212.0,
        "median": 414.0,
        "p90": 570.0,
        "p95": 607.0,
        "max": 608.0
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
        "count": 30,
        "min": 0.0,
        "median": 197.0,
        "p90": 279.0,
        "p95": 330.0,
        "max": 533.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 556.0,
        "median": 815.0,
        "p90": 1732.0,
        "p95": 1943.0,
        "max": 1960.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 98.0,
        "p90": 146.0,
        "p95": 200.0,
        "max": 207.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 60.0,
        "median": 108.0,
        "p90": 157.0,
        "p95": 235.0,
        "max": 243.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 952.0,
        "median": 1985.0,
        "p90": 2785.0,
        "p95": 2955.0,
        "max": 3183.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 4,
    "cluster_invocation_capacity": 8,
    "repeat": 1,
    "wall_seconds": 24.063,
    "throughput_per_second": 3.325,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 3.625,
      "median": 8.188,
      "p90": 10.453,
      "p95": 10.797,
      "max": 12.11
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.171,
      "median": 0.446,
      "p90": 1.406,
      "p95": 1.547,
      "max": 1.859
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.157,
      "median": 0.234,
      "p90": 0.313,
      "p95": 0.344,
      "max": 0.344
    },
    "workers": {
      "worker-1": 41,
      "worker-2": 39
    },
    "cold_starts": 70,
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
        "p95": 358.0,
        "max": 477.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 55.5,
        "p90": 92.0,
        "p95": 104.0,
        "max": 147.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 4.0,
        "median": 8.0,
        "p90": 13.0,
        "p95": 18.0,
        "max": 23.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 737.0,
        "median": 1628.0,
        "p90": 2380.0,
        "p95": 2570.0,
        "max": 2686.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 1064.0,
        "median": 1937.0,
        "p90": 2756.0,
        "p95": 3065.0,
        "max": 3247.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 4.0,
        "median": 8.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 22.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 123.0,
        "max": 331.0
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
        "max": 2.0
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
        "p90": 3.0,
        "p95": 282.0,
        "max": 463.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 341.0,
        "median": 544.5,
        "p90": 671.0,
        "p95": 734.0,
        "max": 798.0
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
        "max": 1.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 395.0,
        "median": 622.0,
        "p90": 1537.0,
        "p95": 1572.0,
        "max": 1664.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 22.0,
        "median": 155.5,
        "p90": 384.0,
        "p95": 493.0,
        "max": 884.0
      },
      "warm_container_create_ms": {
        "count": 70,
        "min": 228.0,
        "median": 417.5,
        "p90": 500.0,
        "p95": 529.0,
        "max": 554.0
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
        "count": 80,
        "min": 0.0,
        "median": 196.0,
        "p90": 385.0,
        "p95": 469.0,
        "max": 538.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 513.0,
        "median": 790.5,
        "p90": 1713.0,
        "p95": 1756.0,
        "max": 1928.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 56.0,
        "median": 107.0,
        "p90": 190.0,
        "p95": 194.0,
        "max": 221.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 59.0,
        "median": 106.0,
        "p90": 167.0,
        "p95": 180.0,
        "max": 202.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 1091.0,
        "median": 1962.5,
        "p90": 2781.0,
        "p95": 3088.0,
        "max": 3271.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 4,
    "cluster_invocation_capacity": 8,
    "repeat": 2,
    "wall_seconds": 24.625,
    "throughput_per_second": 3.249,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 3.641,
      "median": 8.054,
      "p90": 10.61,
      "p95": 11.547,
      "max": 13.282
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.156,
      "median": 0.547,
      "p90": 2.562,
      "p95": 2.735,
      "max": 3.563
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.242,
      "p90": 0.328,
      "p95": 0.828,
      "max": 0.828
    },
    "workers": {
      "worker-1": 42,
      "worker-2": 38
    },
    "cold_starts": 62,
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
        "p95": 374.0,
        "max": 556.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 49.0,
        "p90": 87.0,
        "p95": 102.0,
        "max": 118.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 4.0,
        "median": 8.0,
        "p90": 13.0,
        "p95": 14.0,
        "max": 19.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 710.0,
        "median": 1660.0,
        "p90": 2592.0,
        "p95": 2791.0,
        "max": 4333.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 1014.0,
        "median": 1969.0,
        "p90": 3001.0,
        "p95": 3174.0,
        "max": 4443.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 15.0,
        "max": 26.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 18.0,
        "max": 34.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 49.0,
        "max": 500.0
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
        "p95": 1001.0,
        "max": 1002.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 4.0,
        "p95": 289.0,
        "max": 360.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 341.0,
        "median": 540.0,
        "p90": 716.0,
        "p95": 772.0,
        "max": 930.0
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
        "max": 2.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 394.0,
        "median": 654.5,
        "p90": 1512.0,
        "p95": 1614.0,
        "max": 1812.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 22.0,
        "median": 127.0,
        "p90": 717.0,
        "p95": 2236.0,
        "max": 2317.0
      },
      "warm_container_create_ms": {
        "count": 62,
        "min": 236.0,
        "median": 401.5,
        "p90": 464.0,
        "p95": 468.0,
        "max": 529.0
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
        "count": 80,
        "min": 0.0,
        "median": 186.5,
        "p90": 291.0,
        "p95": 307.0,
        "max": 537.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 488.0,
        "median": 843.0,
        "p90": 1682.0,
        "p95": 1771.0,
        "max": 1987.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 109.5,
        "p90": 164.0,
        "p95": 177.0,
        "max": 198.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 58.0,
        "median": 107.0,
        "p90": 167.0,
        "p95": 186.0,
        "max": 235.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 1027.0,
        "median": 1990.0,
        "p90": 3020.0,
        "p95": 3194.0,
        "max": 4473.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 8,
    "cluster_invocation_capacity": 16,
    "repeat": 1,
    "wall_seconds": 9.796,
    "throughput_per_second": 3.062,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 4.719,
      "median": 6.508,
      "p90": 9.172,
      "p95": 9.266,
      "max": 9.344
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.343,
      "median": 1.102,
      "p90": 1.563,
      "p95": 1.813,
      "max": 1.828
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.171,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 16,
      "worker-2": 14
    },
    "cold_starts": 27,
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
        "p95": 570.0,
        "max": 719.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 76.5,
        "p90": 207.0,
        "p95": 275.0,
        "max": 301.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 7.0,
        "median": 17.0,
        "p90": 23.0,
        "p95": 35.0,
        "max": 40.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 1966.0,
        "median": 2929.0,
        "p90": 3708.0,
        "p95": 3895.0,
        "max": 4149.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 2456.0,
        "median": 3606.0,
        "p90": 4123.0,
        "p95": 4449.0,
        "max": 4503.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 5.0,
        "median": 9.0,
        "p90": 14.0,
        "p95": 17.0,
        "max": 20.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 16.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 62.0,
        "max": 75.0
      },
      "output_validation_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
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
        "p95": 1003.0,
        "max": 1003.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 6.0,
        "p95": 533.0,
        "max": 577.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 787.0,
        "median": 1119.0,
        "p90": 1552.0,
        "p95": 1598.0,
        "max": 1638.0
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
        "max": 2.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 790.0,
        "median": 1219.5,
        "p90": 2086.0,
        "p95": 2329.0,
        "max": 2599.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 31.0,
        "median": 135.5,
        "p90": 270.0,
        "p95": 308.0,
        "max": 346.0
      },
      "warm_container_create_ms": {
        "count": 27,
        "min": 471.0,
        "median": 705.0,
        "p90": 997.0,
        "p95": 1035.0,
        "max": 1169.0
      },
      "warm_container_reused": {
        "count": 3,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 335.0,
        "p90": 530.0,
        "p95": 603.0,
        "max": 739.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 1079.0,
        "median": 1660.0,
        "p90": 2452.0,
        "p95": 2635.0,
        "max": 3047.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 75.0,
        "median": 202.0,
        "p90": 333.0,
        "p95": 338.0,
        "max": 389.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 100.0,
        "median": 254.0,
        "p90": 370.0,
        "p95": 412.0,
        "max": 458.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 2492.0,
        "median": 3628.5,
        "p90": 4148.0,
        "p95": 4479.0,
        "max": 4519.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 8,
    "cluster_invocation_capacity": 16,
    "repeat": 2,
    "wall_seconds": 10.891,
    "throughput_per_second": 2.755,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 4.578,
      "median": 7.539,
      "p90": 9.328,
      "p95": 10.14,
      "max": 10.86
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.406,
      "median": 1.414,
      "p90": 1.938,
      "p95": 2.032,
      "max": 2.156
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.812,
      "p90": 1.156,
      "p95": 1.156,
      "max": 1.156
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 29,
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
        "p95": 733.0,
        "max": 834.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 88.0,
        "p90": 147.0,
        "p95": 255.0,
        "max": 416.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 5.0,
        "median": 15.0,
        "p90": 29.0,
        "p95": 34.0,
        "max": 36.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 1548.0,
        "median": 2760.0,
        "p90": 3994.0,
        "p95": 4280.0,
        "max": 4367.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 1610.0,
        "median": 3435.0,
        "p90": 4572.0,
        "p95": 5238.0,
        "max": 5335.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 7.5,
        "p90": 11.0,
        "p95": 14.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 53.0,
        "max": 178.0
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
        "p90": 1002.0,
        "p95": 1003.0,
        "max": 1005.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 4.0,
        "p95": 431.0,
        "max": 606.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 387.0,
        "median": 1080.5,
        "p90": 1415.0,
        "p95": 1527.0,
        "max": 1534.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 1.0,
        "max": 3.0
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
        "min": 452.0,
        "median": 1158.5,
        "p90": 2032.0,
        "p95": 2177.0,
        "max": 2532.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 22.0,
        "median": 128.0,
        "p90": 587.0,
        "p95": 772.0,
        "max": 784.0
      },
      "warm_container_create_ms": {
        "count": 29,
        "min": 351.0,
        "median": 588.0,
        "p90": 1050.0,
        "p95": 1089.0,
        "max": 1262.0
      },
      "warm_container_reused": {
        "count": 1,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 393.0,
        "p90": 766.0,
        "p95": 1076.0,
        "max": 1317.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 594.0,
        "median": 1537.5,
        "p90": 2343.0,
        "p95": 2489.0,
        "max": 3029.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 60.0,
        "median": 233.0,
        "p90": 395.0,
        "p95": 428.0,
        "max": 547.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 74.0,
        "median": 255.5,
        "p90": 360.0,
        "p95": 435.0,
        "max": 563.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 1631.0,
        "median": 3455.0,
        "p90": 4595.0,
        "p95": 5261.0,
        "max": 5358.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 8,
    "cluster_invocation_capacity": 16,
    "repeat": 1,
    "wall_seconds": 23.813,
    "throughput_per_second": 3.36,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 3.86,
      "median": 7.594,
      "p90": 11.375,
      "p95": 12.156,
      "max": 14.75
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.219,
      "median": 0.656,
      "p90": 2.062,
      "p95": 2.281,
      "max": 3.188
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.516,
      "p90": 0.625,
      "p95": 0.719,
      "max": 0.719
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 76,
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
        "p95": 759.0,
        "max": 1008.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 167.0,
        "p90": 258.0,
        "p95": 269.0,
        "max": 357.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 4.0,
        "median": 16.0,
        "p90": 26.0,
        "p95": 30.0,
        "max": 51.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 1213.0,
        "median": 3125.5,
        "p90": 3923.0,
        "p95": 4042.0,
        "max": 5528.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 1274.0,
        "median": 3999.5,
        "p90": 4940.0,
        "p95": 5251.0,
        "max": 6189.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 10.0,
        "p90": 16.0,
        "p95": 17.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 10.0,
        "p90": 17.0,
        "p95": 18.0,
        "max": 23.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 48.0,
        "max": 701.0
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
        "max": 4.0
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
        "p95": 1001.0,
        "max": 1007.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 8.0,
        "p95": 624.0,
        "max": 774.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 407.0,
        "median": 973.0,
        "p90": 1269.0,
        "p95": 1297.0,
        "max": 1451.0
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
        "min": 407.0,
        "median": 1178.5,
        "p90": 1933.0,
        "p95": 2172.0,
        "max": 2271.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 25.0,
        "median": 184.0,
        "p90": 1090.0,
        "p95": 1257.0,
        "max": 1906.0
      },
      "warm_container_create_ms": {
        "count": 76,
        "min": 233.0,
        "median": 782.0,
        "p90": 1100.0,
        "p95": 1166.0,
        "max": 1364.0
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
        "count": 80,
        "min": 0.0,
        "median": 436.5,
        "p90": 689.0,
        "p95": 765.0,
        "max": 1230.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 549.0,
        "median": 1568.0,
        "p90": 2372.0,
        "p95": 2550.0,
        "max": 2716.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 58.0,
        "median": 243.0,
        "p90": 368.0,
        "p95": 421.0,
        "max": 480.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 59.0,
        "median": 247.5,
        "p90": 373.0,
        "p95": 392.0,
        "max": 442.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 1303.0,
        "median": 4025.0,
        "p90": 4967.0,
        "p95": 5283.0,
        "max": 6216.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 8,
    "cluster_invocation_capacity": 16,
    "repeat": 2,
    "wall_seconds": 24.641,
    "throughput_per_second": 3.247,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 3.078,
      "median": 7.804,
      "p90": 10.953,
      "p95": 12.171,
      "max": 12.469
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.188,
      "median": 0.625,
      "p90": 1.375,
      "p95": 1.578,
      "max": 2.297
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.157,
      "median": 0.492,
      "p90": 0.562,
      "p95": 1.282,
      "max": 1.282
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 76,
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
        "p95": 599.0,
        "max": 841.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 136.0,
        "p90": 279.0,
        "p95": 295.0,
        "max": 326.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 4.0,
        "median": 16.0,
        "p90": 28.0,
        "p95": 37.0,
        "max": 45.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 1025.0,
        "median": 3236.0,
        "p90": 4061.0,
        "p95": 4495.0,
        "max": 5018.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 1646.0,
        "median": 4021.0,
        "p90": 4873.0,
        "p95": 5092.0,
        "max": 5665.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 4.0,
        "median": 9.0,
        "p90": 16.0,
        "p95": 17.0,
        "max": 25.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 5.0,
        "median": 9.0,
        "p90": 16.0,
        "p95": 20.0,
        "max": 26.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 176.0,
        "max": 660.0
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
        "max": 3.0
      },
      "runner_environment_read_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 4.0
      },
      "runner_event_load_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_handler_execution_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1001.0,
        "max": 1003.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 6.0,
        "p95": 593.0,
        "max": 780.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 343.0,
        "median": 1125.5,
        "p90": 1471.0,
        "p95": 1524.0,
        "max": 1606.0
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
        "p90": 1.0,
        "p95": 2.0,
        "max": 6.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 2.0,
        "max": 3.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 344.0,
        "median": 1276.5,
        "p90": 2233.0,
        "p95": 2350.0,
        "max": 2442.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 30.0,
        "median": 202.5,
        "p90": 562.0,
        "p95": 693.0,
        "max": 898.0
      },
      "warm_container_create_ms": {
        "count": 76,
        "min": 203.0,
        "median": 878.5,
        "p90": 1117.0,
        "p95": 1227.0,
        "max": 1367.0
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
        "count": 80,
        "min": 0.0,
        "median": 435.0,
        "p90": 642.0,
        "p95": 683.0,
        "max": 828.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 449.0,
        "median": 1738.5,
        "p90": 2604.0,
        "p95": 2776.0,
        "max": 2908.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 55.0,
        "median": 238.0,
        "p90": 382.0,
        "p95": 409.0,
        "max": 428.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 67.0,
        "median": 262.0,
        "p90": 370.0,
        "p95": 400.0,
        "max": 451.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 1671.0,
        "median": 4042.5,
        "p90": 4908.0,
        "p95": 5121.0,
        "max": 5688.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 16,
    "cluster_invocation_capacity": 32,
    "repeat": 1,
    "wall_seconds": 10.391,
    "throughput_per_second": 2.887,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 6.282,
      "median": 9.235,
      "p90": 9.953,
      "p95": 10.172,
      "max": 10.375
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.469,
      "median": 1.086,
      "p90": 1.594,
      "p95": 1.86,
      "max": 2.047
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 30,
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
        "p95": 605.0,
        "max": 1267.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 45.0,
        "median": 101.0,
        "p90": 416.0,
        "p95": 548.0,
        "max": 767.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 8.0,
        "median": 36.0,
        "p90": 76.0,
        "p95": 90.0,
        "max": 96.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 2692.0,
        "median": 5110.5,
        "p90": 6443.0,
        "p95": 6865.0,
        "max": 6910.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 5203.0,
        "median": 6746.5,
        "p90": 7290.0,
        "p95": 7302.0,
        "max": 7319.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 4.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 13.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 6.0,
        "median": 10.5,
        "p90": 18.0,
        "p95": 23.0,
        "max": 26.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 105.0,
        "max": 252.0
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
        "max": 1.0
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
        "max": 3.0
      },
      "runner_handler_execution_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 1004.0,
        "p95": 1005.0,
        "max": 1007.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 7.0,
        "p95": 386.0,
        "max": 774.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 479.0,
        "median": 1228.0,
        "p90": 1829.0,
        "p95": 1851.0,
        "max": 1885.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 1.0,
        "max": 7.0
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
        "p95": 2.0,
        "max": 7.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 480.0,
        "median": 1507.5,
        "p90": 2234.0,
        "p95": 2513.0,
        "max": 2861.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 27.0,
        "median": 162.5,
        "p90": 341.0,
        "p95": 515.0,
        "max": 847.0
      },
      "warm_container_create_ms": {
        "count": 30,
        "min": 806.0,
        "median": 1212.0,
        "p90": 3030.0,
        "p95": 4366.0,
        "max": 4394.0
      },
      "warm_pool_release_ms": {
        "count": 30,
        "min": 0.0,
        "median": 936.0,
        "p90": 1787.0,
        "p95": 1933.0,
        "max": 2102.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 731.0,
        "median": 2432.0,
        "p90": 3188.0,
        "p95": 3235.0,
        "max": 3420.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 629.5,
        "p90": 1095.0,
        "p95": 1117.0,
        "max": 1202.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 165.0,
        "median": 635.5,
        "p90": 804.0,
        "p95": 1035.0,
        "max": 1119.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 5247.0,
        "median": 6774.5,
        "p90": 7316.0,
        "p95": 7326.0,
        "max": 7344.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 16,
    "cluster_invocation_capacity": 32,
    "repeat": 2,
    "wall_seconds": 12.547,
    "throughput_per_second": 2.391,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 4.859,
      "median": 9.031,
      "p90": 10.516,
      "p95": 11.047,
      "max": 11.313
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.359,
      "median": 1.118,
      "p90": 1.719,
      "p95": 2.016,
      "max": 2.172
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.157,
      "median": 0.593,
      "p90": 0.735,
      "p95": 0.735,
      "max": 0.735
    },
    "workers": {
      "worker-1": 12,
      "worker-2": 18
    },
    "cold_starts": 26,
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
        "p95": 489.0,
        "max": 1392.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 139.0,
        "p90": 801.0,
        "p95": 1323.0,
        "max": 1341.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 6.0,
        "median": 24.5,
        "p90": 68.0,
        "p95": 82.0,
        "max": 98.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 1962.0,
        "median": 4377.5,
        "p90": 6850.0,
        "p95": 7342.0,
        "max": 7651.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 2709.0,
        "median": 6299.5,
        "p90": 7630.0,
        "p95": 7991.0,
        "max": 8277.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 4.0,
        "median": 9.5,
        "p90": 17.0,
        "p95": 20.0,
        "max": 25.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 5.0,
        "median": 12.5,
        "p90": 21.0,
        "p95": 26.0,
        "max": 26.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 47.0,
        "max": 103.0
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
        "p95": 1002.0,
        "max": 1002.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 6.0,
        "p95": 516.0,
        "max": 606.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 520.0,
        "median": 1405.0,
        "p90": 1794.0,
        "p95": 1910.0,
        "max": 1935.0
      },
      "runner_result_serialize_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_result_write_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 6.0,
        "max": 7.0
      },
      "runner_setup_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 4.0
      },
      "runner_total_ms": {
        "count": 30,
        "min": 521.0,
        "median": 1601.0,
        "p90": 2068.0,
        "p95": 2820.0,
        "max": 2911.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 28.0,
        "median": 286.5,
        "p90": 1315.0,
        "p95": 1453.0,
        "max": 1468.0
      },
      "warm_container_create_ms": {
        "count": 26,
        "min": 446.0,
        "median": 912.0,
        "p90": 3790.0,
        "p95": 4110.0,
        "max": 4127.0
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
        "count": 30,
        "min": 0.0,
        "median": 617.5,
        "p90": 2300.0,
        "p95": 3036.0,
        "max": 3081.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 762.0,
        "median": 2144.0,
        "p90": 2903.0,
        "p95": 3730.0,
        "max": 4022.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 60.0,
        "median": 341.0,
        "p90": 944.0,
        "p95": 1084.0,
        "max": 1170.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 97.0,
        "median": 473.0,
        "p90": 676.0,
        "p95": 759.0,
        "max": 1166.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 2727.0,
        "median": 6330.5,
        "p90": 7655.0,
        "p95": 8046.0,
        "max": 8324.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 16,
    "cluster_invocation_capacity": 32,
    "repeat": 1,
    "wall_seconds": 24.953,
    "throughput_per_second": 3.206,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 2.969,
      "median": 8.234,
      "p90": 12.64,
      "p95": 13.781,
      "max": 14.797
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.156,
      "median": 0.563,
      "p90": 1.828,
      "p95": 2.171,
      "max": 2.421
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.313,
      "p90": 0.578,
      "p95": 0.578,
      "max": 0.578
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 78,
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
        "p95": 731.0,
        "max": 1237.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 225.0,
        "p90": 746.0,
        "p95": 821.0,
        "max": 936.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 4.0,
        "median": 19.0,
        "p90": 40.0,
        "p95": 53.0,
        "max": 125.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 1237.0,
        "median": 4153.5,
        "p90": 5690.0,
        "p95": 6585.0,
        "max": 7644.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 1743.0,
        "median": 5716.5,
        "p90": 7233.0,
        "p95": 7945.0,
        "max": 9247.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 5.0,
        "median": 9.0,
        "p90": 14.0,
        "p95": 18.0,
        "max": 27.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 5.0,
        "median": 9.0,
        "p90": 16.0,
        "p95": 20.0,
        "max": 27.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 175.0,
        "max": 616.0
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
        "max": 3.0
      },
      "runner_event_load_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_handler_execution_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1002.0,
        "max": 1004.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 9.0,
        "p95": 647.0,
        "max": 781.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 450.0,
        "median": 1159.0,
        "p90": 1500.0,
        "p95": 1860.0,
        "max": 2036.0
      },
      "runner_result_serialize_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 4.0
      },
      "runner_result_write_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 6.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 552.0,
        "median": 1357.0,
        "p90": 2099.0,
        "p95": 2250.0,
        "max": 2499.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 25.0,
        "median": 209.5,
        "p90": 730.0,
        "p95": 945.0,
        "max": 1457.0
      },
      "warm_container_create_ms": {
        "count": 78,
        "min": 236.0,
        "median": 998.5,
        "p90": 2715.0,
        "p95": 2826.0,
        "max": 3389.0
      },
      "warm_container_reused": {
        "count": 2,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 80,
        "min": 0.0,
        "median": 707.0,
        "p90": 1430.0,
        "p95": 1588.0,
        "max": 3167.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 774.0,
        "median": 1889.0,
        "p90": 2671.0,
        "p95": 2978.0,
        "max": 3201.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 57.0,
        "median": 338.0,
        "p90": 660.0,
        "p95": 827.0,
        "max": 1089.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 59.0,
        "median": 320.5,
        "p90": 602.0,
        "p95": 785.0,
        "max": 913.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 1765.0,
        "median": 5745.0,
        "p90": 7270.0,
        "p95": 7966.0,
        "max": 9293.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 16,
    "cluster_invocation_capacity": 32,
    "repeat": 2,
    "wall_seconds": 24.125,
    "throughput_per_second": 3.316,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 3.64,
      "median": 8.234,
      "p90": 12.844,
      "p95": 14.25,
      "max": 16.75
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.187,
      "median": 0.531,
      "p90": 1.422,
      "p95": 1.625,
      "max": 2.578
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.218,
      "median": 0.344,
      "p90": 0.453,
      "p95": 0.516,
      "max": 0.516
    },
    "workers": {
      "worker-1": 43,
      "worker-2": 37
    },
    "cold_starts": 73,
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
        "p95": 549.0,
        "max": 1053.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 148.0,
        "p90": 413.0,
        "p95": 515.0,
        "max": 802.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 5.0,
        "median": 16.5,
        "p90": 48.0,
        "p95": 73.0,
        "max": 98.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 1335.0,
        "median": 3337.5,
        "p90": 5804.0,
        "p95": 6489.0,
        "max": 6879.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 1444.0,
        "median": 4435.5,
        "p90": 7062.0,
        "p95": 7291.0,
        "max": 7856.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 4.0,
        "median": 9.0,
        "p90": 13.0,
        "p95": 15.0,
        "max": 24.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 9.0,
        "p90": 16.0,
        "p95": 19.0,
        "max": 27.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 310.0,
        "max": 700.0
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
        "max": 3.0
      },
      "runner_handler_execution_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1001.0,
        "max": 1003.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 4.0,
        "p95": 425.0,
        "max": 565.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 413.0,
        "median": 915.5,
        "p90": 1887.0,
        "p95": 1998.0,
        "max": 2173.0
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
        "max": 3.0
      },
      "runner_setup_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 1.0,
        "max": 2.0
      },
      "runner_total_ms": {
        "count": 80,
        "min": 480.0,
        "median": 1118.0,
        "p90": 2179.0,
        "p95": 2331.0,
        "max": 3108.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 33.0,
        "median": 164.5,
        "p90": 650.0,
        "p95": 859.0,
        "max": 1167.0
      },
      "warm_container_create_ms": {
        "count": 73,
        "min": 277.0,
        "median": 846.0,
        "p90": 1956.0,
        "p95": 2292.0,
        "max": 3600.0
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
        "count": 80,
        "min": 0.0,
        "median": 526.0,
        "p90": 1680.0,
        "p95": 1926.0,
        "max": 3777.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 604.0,
        "median": 1503.5,
        "p90": 3068.0,
        "p95": 3195.0,
        "max": 4094.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 57.0,
        "median": 246.0,
        "p90": 875.0,
        "p95": 944.0,
        "max": 1111.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 72.0,
        "median": 267.0,
        "p90": 897.0,
        "p95": 921.0,
        "max": 1025.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 1467.0,
        "median": 4466.0,
        "p90": 7083.0,
        "p95": 7317.0,
        "max": 7872.0
      }
    }
  }
]
```
