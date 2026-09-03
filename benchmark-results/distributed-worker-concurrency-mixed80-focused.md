# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T11:12:12.728962+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `57`, version `57`, image `10.42.1.22:5000/functions/bench-tiny-0efb6ea1:v57-v1-a1-6505896d55ae-d1`
- `sleep`: function `58`, version `58`, image `10.42.1.22:5000/functions/bench-sleep-b1bd2654:v58-v1-a1-9c37bc6b934c-d1`
- `dependency`: function `59`, version `59`, image `10.42.1.22:5000/functions/bench-dependency-660eee27:v59-v1-a1-70f42a8642cb-d1`
- `output`: function `60`, version `60`, image `10.42.1.22:5000/functions/bench-output-564dd2c7:v60-v1-a1-815eb92da052-d1`
- `input_output`: function `61`, version `61`, image `10.42.1.22:5000/functions/bench-input_output-a6fa5079:v61-v1-a1-54d236783951-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mixed-80 | 80 | 1 | 2 | 8 | 1 | 80 | 0 | 47.39 | 1.688 | 4.961 | 6.734 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 1 | 2 | 8 | 2 | 80 | 0 | 46.485 | 1.721 | 4.195 | 7.296 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 1 | 2 | 8 | 3 | 80 | 0 | 44.906 | 1.781 | 4.07 | 5.844 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 2 | 4 | 8 | 1 | 80 | 0 | 30.031 | 2.664 | 2.758 | 4.516 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 2 | 4 | 8 | 2 | 80 | 0 | 31.187 | 2.565 | 2.836 | 4.281 | worker-1:39, worker-2:41 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 47.39,
    "throughput_per_second": 1.688,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.5,
      "median": 4.961,
      "p90": 6.391,
      "p95": 6.734,
      "max": 8.781
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.312,
      "p95": 0.531,
      "max": 1.485
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
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
        "p95": 244.0,
        "max": 281.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 34.0,
        "max": 155.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 498.0,
        "median": 629.5,
        "p90": 1552.0,
        "p95": 1617.0,
        "max": 1924.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 554.0,
        "median": 693.0,
        "p90": 1613.0,
        "p95": 1686.0,
        "max": 2069.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 38.0,
        "max": 99.0
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
        "p95": 168.0,
        "max": 213.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 330.0,
        "median": 362.0,
        "p90": 410.0,
        "p95": 417.0,
        "max": 451.0
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
        "median": 401.0,
        "p90": 1354.0,
        "p95": 1395.0,
        "max": 1418.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 31.5,
        "p90": 69.0,
        "p95": 97.0,
        "max": 183.0
      },
      "warm_container_create_ms": {
        "count": 20,
        "min": 213.0,
        "median": 236.5,
        "p90": 256.0,
        "p95": 260.0,
        "max": 275.0
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
        "p90": 126.0,
        "p95": 131.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 411.0,
        "median": 499.0,
        "p90": 1445.0,
        "p95": 1505.0,
        "max": 1528.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.0,
        "p90": 67.0,
        "p95": 69.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 52.0,
        "median": 61.0,
        "p90": 68.0,
        "p95": 72.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 564.0,
        "median": 707.0,
        "p90": 1627.0,
        "p95": 1700.0,
        "max": 2085.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 46.485,
    "throughput_per_second": 1.721,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.468,
      "median": 4.195,
      "p90": 7.188,
      "p95": 7.296,
      "max": 7.625
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.313,
      "p95": 0.328,
      "max": 0.5
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.171,
      "median": 0.187,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.375
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
    },
    "cold_starts": 16,
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
        "p95": 237.0,
        "max": 271.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 31.0,
        "max": 38.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 16.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 500.0,
        "median": 618.0,
        "p90": 1565.0,
        "p95": 1616.0,
        "max": 1652.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 559.0,
        "median": 683.5,
        "p90": 1621.0,
        "p95": 1686.0,
        "max": 1728.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 26.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 49.0,
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
        "p95": 176.0,
        "max": 219.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 332.0,
        "median": 355.0,
        "p90": 408.0,
        "p95": 416.0,
        "max": 452.0
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
        "median": 386.5,
        "p90": 1358.0,
        "p95": 1409.0,
        "max": 1422.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 31.0,
        "p90": 58.0,
        "p95": 66.0,
        "max": 100.0
      },
      "warm_container_create_ms": {
        "count": 16,
        "min": 211.0,
        "median": 236.5,
        "p90": 251.0,
        "p95": 251.0,
        "max": 252.0
      },
      "warm_container_reused": {
        "count": 64,
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
        "p90": 125.0,
        "p95": 135.0,
        "max": 146.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 417.0,
        "median": 484.0,
        "p90": 1457.0,
        "p95": 1511.0,
        "max": 1536.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.0,
        "p90": 69.0,
        "p95": 70.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.0,
        "p90": 72.0,
        "p95": 74.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 571.0,
        "median": 699.5,
        "p90": 1635.0,
        "p95": 1700.0,
        "max": 1744.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 44.906,
    "throughput_per_second": 1.781,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.515,
      "median": 4.07,
      "p90": 5.375,
      "p95": 5.844,
      "max": 7.375
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.344,
      "p95": 0.437,
      "max": 1.235
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.125,
      "median": 0.172,
      "p90": 0.266,
      "p95": 0.328,
      "max": 0.328
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 16,
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
        "p95": 233.0,
        "max": 270.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 32.0,
        "max": 59.0
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
        "min": 503.0,
        "median": 642.0,
        "p90": 1542.0,
        "p95": 1597.0,
        "max": 1628.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 559.0,
        "median": 716.0,
        "p90": 1609.0,
        "p95": 1672.0,
        "max": 1709.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 13.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 13.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 174.0
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
        "p95": 177.0,
        "max": 218.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 334.0,
        "median": 352.0,
        "p90": 423.0,
        "p95": 427.0,
        "max": 459.0
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
        "min": 335.0,
        "median": 408.0,
        "p90": 1343.0,
        "p95": 1369.0,
        "max": 1425.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 33.5,
        "p90": 77.0,
        "p95": 107.0,
        "max": 126.0
      },
      "warm_container_create_ms": {
        "count": 16,
        "min": 214.0,
        "median": 237.5,
        "p90": 272.0,
        "p95": 272.0,
        "max": 275.0
      },
      "warm_container_reused": {
        "count": 64,
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
        "p90": 131.0,
        "p95": 137.0,
        "max": 157.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 417.0,
        "median": 509.5,
        "p90": 1435.0,
        "p95": 1460.0,
        "max": 1527.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 52.0,
        "median": 61.5,
        "p90": 70.0,
        "p95": 80.0,
        "max": 87.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 54.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 72.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 570.0,
        "median": 728.5,
        "p90": 1624.0,
        "p95": 1687.0,
        "max": 1720.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 1,
    "wall_seconds": 30.031,
    "throughput_per_second": 2.664,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.5,
      "median": 2.758,
      "p90": 4.047,
      "p95": 4.516,
      "max": 5.562
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.141,
      "median": 0.196,
      "p90": 0.437,
      "p95": 0.532,
      "max": 0.89
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.203,
      "p90": 0.329,
      "p95": 0.469,
      "max": 0.469
    },
    "workers": {
      "worker-1": 40,
      "worker-2": 40
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
        "p95": 237.0,
        "max": 272.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 45.0,
        "p95": 51.0,
        "max": 65.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 504.0,
        "median": 742.0,
        "p90": 1924.0,
        "p95": 1977.0,
        "max": 2047.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 558.0,
        "median": 955.0,
        "p90": 2093.0,
        "p95": 2174.0,
        "max": 2266.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 16.0,
        "max": 25.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 83.0
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 1.0,
        "p95": 196.0,
        "max": 288.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 330.0,
        "median": 388.5,
        "p90": 450.0,
        "p95": 469.0,
        "max": 520.0
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
        "min": 331.0,
        "median": 415.5,
        "p90": 1390.0,
        "p95": 1422.0,
        "max": 1522.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 22.0,
        "median": 39.0,
        "p90": 82.0,
        "p95": 105.0,
        "max": 232.0
      },
      "warm_container_create_ms": {
        "count": 36,
        "min": 220.0,
        "median": 267.5,
        "p90": 342.0,
        "p95": 349.0,
        "max": 370.0
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
        "p90": 157.0,
        "p95": 164.0,
        "max": 198.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 413.0,
        "median": 521.0,
        "p90": 1506.0,
        "p95": 1531.0,
        "max": 1641.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 64.0,
        "p90": 81.0,
        "p95": 86.0,
        "max": 101.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 65.0,
        "p90": 85.0,
        "p95": 88.0,
        "max": 91.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 570.0,
        "median": 967.5,
        "p90": 2121.0,
        "p95": 2190.0,
        "max": 2280.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 2,
    "cluster_invocation_capacity": 4,
    "repeat": 2,
    "wall_seconds": 31.187,
    "throughput_per_second": 2.565,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.453,
      "median": 2.836,
      "p90": 4.047,
      "p95": 4.281,
      "max": 5.078
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.218,
      "p90": 0.469,
      "p95": 0.641,
      "max": 1.0
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.703,
      "max": 0.703
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
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
        "p95": 274.0,
        "max": 308.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 41.0,
        "p95": 43.0,
        "max": 56.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 500.0,
        "median": 706.0,
        "p90": 1846.0,
        "p95": 1952.0,
        "max": 2100.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 557.0,
        "median": 924.5,
        "p90": 1963.0,
        "p95": 2032.0,
        "max": 2380.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
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
        "p95": 44.0,
        "max": 212.0
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
        "p95": 231.0,
        "max": 248.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 331.0,
        "median": 374.0,
        "p90": 438.0,
        "p95": 455.0,
        "max": 515.0
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
        "min": 332.0,
        "median": 411.0,
        "p90": 1381.0,
        "p95": 1394.0,
        "max": 1430.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 39.5,
        "p90": 84.0,
        "p95": 97.0,
        "max": 194.0
      },
      "warm_container_create_ms": {
        "count": 32,
        "min": 217.0,
        "median": 257.5,
        "p90": 296.0,
        "p95": 328.0,
        "max": 341.0
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
        "p90": 162.0,
        "p95": 172.0,
        "max": 274.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 417.0,
        "median": 516.5,
        "p90": 1484.0,
        "p95": 1504.0,
        "max": 1542.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 66.0,
        "p90": 79.0,
        "p95": 82.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 51.0,
        "median": 65.0,
        "p90": 80.0,
        "p95": 83.0,
        "max": 102.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 568.0,
        "median": 943.5,
        "p90": 1976.0,
        "p95": 2047.0,
        "max": 2403.0
      }
    }
  }
]
```
