# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T20:16:35.829924+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `72`, version `72`, image `10.42.1.22:5000/functions/bench-tiny-a1285269:v72-v1-a1-15705e4aa10d-d1`
- `sleep`: function `73`, version `73`, image `10.42.1.22:5000/functions/bench-sleep-324180fc:v73-v1-a1-b48ab50c7010-d1`
- `dependency`: function `74`, version `74`, image `10.42.1.22:5000/functions/bench-dependency-a358091f:v74-v1-a1-3c28601318b1-d1`
- `output`: function `75`, version `75`, image `10.42.1.22:5000/functions/bench-output-14992e18:v75-v1-a1-b02331f71096-d1`
- `input_output`: function `76`, version `76`, image `10.42.1.22:5000/functions/bench-input_output-40e71795:v76-v1-a1-74aef3889a41-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mixed-320 | 320 | 2 | 4 | 32 | 1 | 320 | 0 | 118.718 | 2.695 | 10.852 | 16.125 | worker-1:159, worker-2:161 |
| mixed-320 | 320 | 2 | 4 | 32 | 2 | 320 | 0 | 115.812 | 2.763 | 10.946 | 14.594 | worker-1:159, worker-2:161 |
| mixed-320 | 320 | 4 | 8 | 32 | 1 | 320 | 0 | 97.187 | 3.293 | 8.782 | 14.562 | worker-1:159, worker-2:161 |
| mixed-320 | 320 | 4 | 8 | 32 | 2 | 320 | 0 | 95.688 | 3.344 | 8.898 | 14.25 | worker-1:158, worker-2:162 |
| mixed-320 | 320 | 8 | 16 | 32 | 1 | 320 | 0 | 91.093 | 3.513 | 8.321 | 13.453 | worker-1:165, worker-2:155 |
| mixed-320 | 320 | 8 | 16 | 32 | 2 | 320 | 0 | 91.781 | 3.487 | 8.195 | 12.891 | worker-1:164, worker-2:156 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 1,
    "wall_seconds": 118.718,
    "throughput_per_second": 2.695,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.75,
      "median": 10.852,
      "p90": 14.656,
      "p95": 16.125,
      "max": 18.578
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.156,
      "median": 0.359,
      "p90": 0.812,
      "p95": 1.0,
      "max": 1.906
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.172,
      "median": 0.281,
      "p90": 0.531,
      "p95": 0.531,
      "max": 0.64
    },
    "workers": {
      "worker-1": 159,
      "worker-2": 161
    },
    "cold_starts": 148,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 244.0,
        "max": 349.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 43.0,
        "p95": 47.0,
        "max": 252.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 21.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 516.0,
        "median": 879.0,
        "p90": 1965.0,
        "p95": 2067.0,
        "max": 2803.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 577.0,
        "median": 1065.5,
        "p90": 2120.0,
        "p95": 2230.0,
        "max": 2994.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 3.0,
        "median": 7.0,
        "p90": 14.0,
        "p95": 16.0,
        "max": 29.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 16.0,
        "max": 35.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 145.0,
        "max": 618.0
      },
      "output_validation_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1002.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 2.0,
        "p95": 225.0,
        "max": 306.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 330.0,
        "median": 380.0,
        "p90": 453.0,
        "p95": 482.0,
        "max": 528.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 330.0,
        "median": 418.5,
        "p90": 1387.0,
        "p95": 1420.0,
        "max": 1503.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 22.0,
        "median": 111.0,
        "p90": 310.0,
        "p95": 393.0,
        "max": 844.0
      },
      "warm_container_create_ms": {
        "count": 148,
        "min": 204.0,
        "median": 256.0,
        "p90": 287.0,
        "p95": 305.0,
        "max": 365.0
      },
      "warm_container_reused": {
        "count": 172,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 152.0,
        "p95": 163.0,
        "max": 319.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 413.0,
        "median": 522.0,
        "p90": 1491.0,
        "p95": 1539.0,
        "max": 1618.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 51.0,
        "median": 64.0,
        "p90": 79.0,
        "p95": 83.0,
        "max": 118.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 54.0,
        "median": 65.0,
        "p90": 78.0,
        "p95": 84.0,
        "max": 107.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 593.0,
        "median": 1085.0,
        "p90": 2134.0,
        "p95": 2248.0,
        "max": 3018.0
      }
    }
  },
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 2,
    "wall_seconds": 115.812,
    "throughput_per_second": 2.763,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.562,
      "median": 10.946,
      "p90": 14.25,
      "p95": 14.594,
      "max": 16.203
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.156,
      "median": 0.328,
      "p90": 0.797,
      "p95": 1.437,
      "max": 2.312
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.156,
      "median": 0.336,
      "p90": 0.531,
      "p95": 0.547,
      "max": 0.578
    },
    "workers": {
      "worker-1": 159,
      "worker-2": 161
    },
    "cold_starts": 144,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 255.0,
        "max": 354.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 44.0,
        "p95": 48.0,
        "max": 68.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 18.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 531.0,
        "median": 880.0,
        "p90": 1931.0,
        "p95": 2030.0,
        "max": 2496.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 594.0,
        "median": 1086.0,
        "p90": 2063.0,
        "p95": 2219.0,
        "max": 2557.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 2.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 27.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 15.0,
        "max": 25.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 141.0,
        "max": 495.0
      },
      "output_validation_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1001.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 233.0,
        "max": 295.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 330.0,
        "median": 392.5,
        "p90": 470.0,
        "p95": 483.0,
        "max": 548.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_result_write_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 331.0,
        "median": 424.0,
        "p90": 1387.0,
        "p95": 1440.0,
        "max": 1550.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 20.0,
        "median": 94.5,
        "p90": 272.0,
        "p95": 373.0,
        "max": 773.0
      },
      "warm_container_create_ms": {
        "count": 144,
        "min": 207.0,
        "median": 254.0,
        "p90": 300.0,
        "p95": 308.0,
        "max": 366.0
      },
      "warm_container_reused": {
        "count": 176,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 155.0,
        "p95": 165.0,
        "max": 260.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 414.0,
        "median": 530.0,
        "p90": 1497.0,
        "p95": 1558.0,
        "max": 1663.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 51.0,
        "median": 65.5,
        "p90": 83.0,
        "p95": 88.0,
        "max": 110.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 53.0,
        "median": 67.0,
        "p90": 84.0,
        "p95": 88.0,
        "max": 106.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 609.0,
        "median": 1108.5,
        "p90": 2084.0,
        "p95": 2239.0,
        "max": 2576.0
      }
    }
  },
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 4,
    "cluster_invocation_capacity": 8,
    "repeat": 1,
    "wall_seconds": 97.187,
    "throughput_per_second": 3.293,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 1.859,
      "median": 8.782,
      "p90": 13.609,
      "p95": 14.562,
      "max": 16.109
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.156,
      "median": 0.437,
      "p90": 0.922,
      "p95": 1.5,
      "max": 2.969
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.157,
      "median": 0.446,
      "p90": 0.641,
      "p95": 0.656,
      "max": 1.5
    },
    "workers": {
      "worker-1": 159,
      "worker-2": 161
    },
    "cold_starts": 266,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 393.0,
        "max": 622.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 55.0,
        "p90": 95.0,
        "p95": 104.0,
        "max": 158.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 18.0,
        "max": 35.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 689.0,
        "median": 1579.0,
        "p90": 2480.0,
        "p95": 2603.0,
        "max": 3559.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 946.0,
        "median": 1982.5,
        "p90": 2808.0,
        "p95": 3153.0,
        "max": 4088.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 21.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 3.0,
        "median": 9.0,
        "p90": 15.0,
        "p95": 18.0,
        "max": 27.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 132.0,
        "max": 813.0
      },
      "output_validation_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_event_load_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1001.0,
        "max": 1003.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 3.0,
        "p95": 324.0,
        "max": 542.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 330.0,
        "median": 562.0,
        "p90": 764.0,
        "p95": 811.0,
        "max": 897.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_result_write_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 331.0,
        "median": 627.0,
        "p90": 1539.0,
        "p95": 1675.0,
        "max": 1898.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 22.0,
        "median": 153.0,
        "p90": 400.0,
        "p95": 506.0,
        "max": 1267.0
      },
      "warm_container_create_ms": {
        "count": 266,
        "min": 221.0,
        "median": 381.5,
        "p90": 531.0,
        "p95": 550.0,
        "max": 624.0
      },
      "warm_container_reused": {
        "count": 54,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 320,
        "min": 0.0,
        "median": 191.0,
        "p90": 333.0,
        "p95": 490.0,
        "max": 634.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 413.0,
        "median": 814.0,
        "p90": 1724.0,
        "p95": 1826.0,
        "max": 2185.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 55.0,
        "median": 109.5,
        "p90": 173.0,
        "p95": 187.0,
        "max": 256.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 54.0,
        "median": 99.0,
        "p90": 177.0,
        "p95": 188.0,
        "max": 228.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 967.0,
        "median": 2006.5,
        "p90": 2835.0,
        "p95": 3176.0,
        "max": 4109.0
      }
    }
  },
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 4,
    "cluster_invocation_capacity": 8,
    "repeat": 2,
    "wall_seconds": 95.688,
    "throughput_per_second": 3.344,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.219,
      "median": 8.898,
      "p90": 13.515,
      "p95": 14.25,
      "max": 15.672
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.156,
      "median": 0.437,
      "p90": 0.953,
      "p95": 1.36,
      "max": 2.328
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.172,
      "median": 0.398,
      "p90": 0.593,
      "p95": 0.672,
      "max": 0.718
    },
    "workers": {
      "worker-1": 158,
      "worker-2": 162
    },
    "cold_starts": 268,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 371.0,
        "max": 682.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 57.0,
        "p90": 95.0,
        "p95": 108.0,
        "max": 166.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.0,
        "p90": 14.0,
        "p95": 16.0,
        "max": 38.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 586.0,
        "median": 1603.5,
        "p90": 2384.0,
        "p95": 2585.0,
        "max": 3094.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 646.0,
        "median": 1927.0,
        "p90": 2773.0,
        "p95": 2958.0,
        "max": 3862.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.0,
        "p90": 12.0,
        "p95": 14.0,
        "max": 25.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 3.0,
        "median": 8.5,
        "p90": 14.0,
        "p95": 16.0,
        "max": 26.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 227.0,
        "max": 741.0
      },
      "output_validation_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "result_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1003.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 3.0,
        "p95": 306.0,
        "max": 497.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 335.0,
        "median": 552.0,
        "p90": 731.0,
        "p95": 766.0,
        "max": 985.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_result_write_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 5.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 335.0,
        "median": 633.5,
        "p90": 1549.0,
        "p95": 1609.0,
        "max": 1920.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 21.0,
        "median": 145.0,
        "p90": 355.0,
        "p95": 431.0,
        "max": 869.0
      },
      "warm_container_create_ms": {
        "count": 268,
        "min": 219.0,
        "median": 394.0,
        "p90": 524.0,
        "p95": 553.0,
        "max": 679.0
      },
      "warm_container_reused": {
        "count": 52,
        "min": 1.0,
        "median": 1.0,
        "p90": 1.0,
        "p95": 1.0,
        "max": 1.0
      },
      "warm_pool_release_ms": {
        "count": 320,
        "min": 0.0,
        "median": 187.5,
        "p90": 311.0,
        "p95": 421.0,
        "max": 623.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 424.0,
        "median": 810.5,
        "p90": 1711.0,
        "p95": 1838.0,
        "max": 2142.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 55.0,
        "median": 106.0,
        "p90": 170.0,
        "p95": 186.0,
        "max": 238.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 54.0,
        "median": 105.0,
        "p90": 172.0,
        "p95": 188.0,
        "max": 259.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 660.0,
        "median": 1953.5,
        "p90": 2793.0,
        "p95": 2980.0,
        "max": 3888.0
      }
    }
  },
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 8,
    "cluster_invocation_capacity": 16,
    "repeat": 1,
    "wall_seconds": 91.093,
    "throughput_per_second": 3.513,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.563,
      "median": 8.321,
      "p90": 12.782,
      "p95": 13.453,
      "max": 15.328
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.171,
      "median": 0.422,
      "p90": 1.0,
      "p95": 1.469,
      "max": 2.172
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.172,
      "median": 0.343,
      "p90": 0.672,
      "p95": 0.75,
      "max": 1.25
    },
    "workers": {
      "worker-1": 165,
      "worker-2": 155
    },
    "cold_starts": 313,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 715.0,
        "max": 994.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 167.0,
        "p90": 314.0,
        "p95": 356.0,
        "max": 489.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 16.0,
        "p90": 28.0,
        "p95": 33.0,
        "max": 55.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 571.0,
        "median": 3039.5,
        "p90": 4027.0,
        "p95": 4266.0,
        "max": 5749.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 625.0,
        "median": 3914.5,
        "p90": 5072.0,
        "p95": 5271.0,
        "max": 6594.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 3.0,
        "median": 9.0,
        "p90": 17.0,
        "p95": 19.0,
        "max": 33.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 4.0,
        "median": 10.0,
        "p90": 17.0,
        "p95": 21.0,
        "max": 36.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 268.0,
        "max": 529.0
      },
      "output_validation_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 4.0
      },
      "result_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_event_load_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1001.0,
        "max": 1004.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 6.0,
        "p95": 495.0,
        "max": 938.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 338.0,
        "median": 913.5,
        "p90": 1290.0,
        "p95": 1402.0,
        "max": 2064.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
      },
      "runner_result_write_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 1.0,
        "max": 4.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 5.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 338.0,
        "median": 1048.5,
        "p90": 1922.0,
        "p95": 2146.0,
        "max": 2991.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 22.0,
        "median": 156.5,
        "p90": 453.0,
        "p95": 591.0,
        "max": 992.0
      },
      "warm_container_create_ms": {
        "count": 313,
        "min": 204.0,
        "median": 823.0,
        "p90": 1184.0,
        "p95": 1277.0,
        "max": 1634.0
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
        "count": 320,
        "min": 0.0,
        "median": 476.5,
        "p90": 736.0,
        "p95": 814.0,
        "max": 1054.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 426.0,
        "median": 1440.5,
        "p90": 2329.0,
        "p95": 2549.0,
        "max": 3506.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 53.0,
        "median": 254.5,
        "p90": 393.0,
        "p95": 437.0,
        "max": 562.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 59.0,
        "median": 241.0,
        "p90": 388.0,
        "p95": 416.0,
        "max": 575.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 651.0,
        "median": 3943.5,
        "p90": 5102.0,
        "p95": 5303.0,
        "max": 6627.0
      }
    }
  },
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 8,
    "cluster_invocation_capacity": 16,
    "repeat": 2,
    "wall_seconds": 91.781,
    "throughput_per_second": 3.487,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.656,
      "median": 8.195,
      "p90": 12.515,
      "p95": 12.891,
      "max": 15.656
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.172,
      "median": 0.484,
      "p90": 0.891,
      "p95": 1.515,
      "max": 2.687
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.234,
      "median": 0.485,
      "p90": 0.766,
      "p95": 0.844,
      "max": 1.422
    },
    "workers": {
      "worker-1": 164,
      "worker-2": 156
    },
    "cold_starts": 306,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 625.0,
        "max": 1269.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 163.0,
        "p90": 314.0,
        "p95": 353.0,
        "max": 510.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 15.0,
        "p90": 28.0,
        "p95": 34.0,
        "max": 71.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 727.0,
        "median": 3032.5,
        "p90": 3987.0,
        "p95": 4239.0,
        "max": 5003.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 972.0,
        "median": 3926.5,
        "p90": 5057.0,
        "p95": 5424.0,
        "max": 6347.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 4.0,
        "median": 9.0,
        "p90": 15.0,
        "p95": 17.0,
        "max": 30.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 4.0,
        "median": 10.0,
        "p90": 16.0,
        "p95": 19.0,
        "max": 28.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 211.0,
        "max": 625.0
      },
      "output_validation_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 13.0
      },
      "result_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 5.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_event_load_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1001.0,
        "p95": 1002.0,
        "max": 1004.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 8.0,
        "p95": 516.0,
        "max": 806.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 357.0,
        "median": 900.5,
        "p90": 1292.0,
        "p95": 1377.0,
        "max": 1726.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 3.0
      },
      "runner_result_write_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 5.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 1.0,
        "max": 4.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 359.0,
        "median": 1055.0,
        "p90": 1877.0,
        "p95": 2064.0,
        "max": 2686.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 22.0,
        "median": 175.5,
        "p90": 441.0,
        "p95": 613.0,
        "max": 1258.0
      },
      "warm_container_create_ms": {
        "count": 306,
        "min": 233.0,
        "median": 840.0,
        "p90": 1184.0,
        "p95": 1250.0,
        "max": 1466.0
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
        "count": 320,
        "min": 0.0,
        "median": 488.0,
        "p90": 746.0,
        "p95": 828.0,
        "max": 955.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 471.0,
        "median": 1433.0,
        "p90": 2228.0,
        "p95": 2493.0,
        "max": 3312.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 54.0,
        "median": 251.0,
        "p90": 431.0,
        "p95": 462.0,
        "max": 627.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 56.0,
        "median": 233.0,
        "p90": 381.0,
        "p95": 434.0,
        "max": 565.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 993.0,
        "median": 3953.5,
        "p90": 5083.0,
        "p95": 5461.0,
        "max": 6373.0
      }
    }
  }
]
```
