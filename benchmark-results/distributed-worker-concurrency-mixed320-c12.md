# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T20:29:59.256979+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `82`, version `82`, image `10.42.1.22:5000/functions/bench-tiny-4f3b989a:v82-v1-a1-4c521226b225-d1`
- `sleep`: function `83`, version `83`, image `10.42.1.22:5000/functions/bench-sleep-ce4d6f05:v83-v1-a1-fc3c234160f5-d1`
- `dependency`: function `84`, version `84`, image `10.42.1.22:5000/functions/bench-dependency-8dcc91f4:v84-v1-a1-5dbd9e6fd621-d1`
- `output`: function `85`, version `85`, image `10.42.1.22:5000/functions/bench-output-f049d0f2:v85-v1-a1-2af70e9a7f65-d1`
- `input_output`: function `86`, version `86`, image `10.42.1.22:5000/functions/bench-input_output-27fe0b26:v86-v1-a1-56d5fda7323b-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| mixed-320 | 320 | 12 | 24 | 32 | 1 | 320 | 0 | 95.093 | 3.365 | 8.571 | 14.063 | worker-1:165, worker-2:155 |
| mixed-320 | 320 | 12 | 24 | 32 | 2 | 320 | 0 | 91.563 | 3.495 | 7.898 | 13.593 | worker-1:172, worker-2:148 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 12,
    "cluster_invocation_capacity": 24,
    "repeat": 1,
    "wall_seconds": 95.093,
    "throughput_per_second": 3.365,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.312,
      "median": 8.571,
      "p90": 13.109,
      "p95": 14.063,
      "max": 16.297
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.156,
      "median": 0.422,
      "p90": 0.875,
      "p95": 1.437,
      "max": 2.469
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.172,
      "median": 0.406,
      "p90": 0.672,
      "p95": 0.687,
      "max": 0.765
    },
    "workers": {
      "worker-1": 165,
      "worker-2": 155
    },
    "cold_starts": 310,
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
        "p95": 733.0,
        "max": 1650.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 333.5,
        "p90": 785.0,
        "p95": 993.0,
        "max": 1742.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 20.0,
        "p90": 48.0,
        "p95": 57.0,
        "max": 108.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 678.0,
        "median": 4129.5,
        "p90": 6073.0,
        "p95": 6334.0,
        "max": 7287.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 744.0,
        "median": 5545.0,
        "p90": 7746.0,
        "p95": 8130.0,
        "max": 10178.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 3.0,
        "median": 10.0,
        "p90": 16.0,
        "p95": 20.0,
        "max": 34.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 4.0,
        "median": 11.0,
        "p90": 19.0,
        "p95": 22.0,
        "max": 32.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 251.0,
        "max": 999.0
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
        "max": 7.0
      },
      "runner_environment_read_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 4.0
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
        "p90": 1001.0,
        "p95": 1003.0,
        "max": 1006.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 7.0,
        "p95": 608.0,
        "max": 1327.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 336.0,
        "median": 1003.5,
        "p90": 1601.0,
        "p95": 1750.0,
        "max": 2561.0
      },
      "runner_result_serialize_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 2.0
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
        "max": 4.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 336.0,
        "median": 1144.5,
        "p90": 2125.0,
        "p95": 2450.0,
        "max": 3414.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 23.0,
        "median": 174.5,
        "p90": 465.0,
        "p95": 510.0,
        "max": 979.0
      },
      "warm_container_create_ms": {
        "count": 310,
        "min": 211.0,
        "median": 1301.0,
        "p90": 2179.0,
        "p95": 2316.0,
        "max": 2978.0
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
        "count": 320,
        "min": 0.0,
        "median": 754.0,
        "p90": 1378.0,
        "p95": 1576.0,
        "max": 2643.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 423.0,
        "median": 1618.0,
        "p90": 2721.0,
        "p95": 3253.0,
        "max": 4441.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 54.0,
        "median": 346.0,
        "p90": 608.0,
        "p95": 722.0,
        "max": 1120.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 55.0,
        "median": 354.5,
        "p90": 664.0,
        "p95": 766.0,
        "max": 944.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 766.0,
        "median": 5567.5,
        "p90": 7794.0,
        "p95": 8180.0,
        "max": 10246.0
      }
    }
  },
  {
    "scenario": "mixed-320",
    "count": 320,
    "concurrency": 32,
    "saturation_concurrency": 32,
    "worker_invocation_concurrency": 12,
    "cluster_invocation_capacity": 24,
    "repeat": 2,
    "wall_seconds": 91.563,
    "throughput_per_second": 3.495,
    "successes": 320,
    "failures": 0,
    "terminal_seconds": {
      "count": 320,
      "min": 2.953,
      "median": 7.898,
      "p90": 12.656,
      "p95": 13.593,
      "max": 15.25
    },
    "accept_seconds": {
      "count": 320,
      "min": 0.156,
      "median": 0.438,
      "p90": 0.875,
      "p95": 1.531,
      "max": 2.75
    },
    "output_download_seconds": {
      "count": 32,
      "min": 0.171,
      "median": 0.406,
      "p90": 0.687,
      "p95": 0.75,
      "max": 0.938
    },
    "workers": {
      "worker-1": 172,
      "worker-2": 148
    },
    "cold_starts": 309,
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
        "p95": 777.0,
        "max": 1607.0
      },
      "docker_image_pull_ms": {
        "count": 320,
        "min": 0.0,
        "median": 285.0,
        "p90": 745.0,
        "p95": 954.0,
        "max": 1390.0
      },
      "docker_input_copy_ms": {
        "count": 320,
        "min": 3.0,
        "median": 20.0,
        "p90": 46.0,
        "p95": 55.0,
        "max": 145.0
      },
      "executor_duration_ms": {
        "count": 320,
        "min": 748.0,
        "median": 3954.5,
        "p90": 5852.0,
        "p95": 6234.0,
        "max": 7293.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 320,
        "min": 852.0,
        "median": 5079.0,
        "p90": 7734.0,
        "p95": 8271.0,
        "max": 9832.0
      },
      "orchestrator_claim_ms": {
        "count": 320,
        "min": 3.0,
        "median": 9.0,
        "p90": 15.0,
        "p95": 19.0,
        "max": 38.0
      },
      "orchestrator_completion_ms": {
        "count": 320,
        "min": 4.0,
        "median": 10.0,
        "p90": 17.0,
        "p95": 20.0,
        "max": 35.0
      },
      "output_upload_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 252.0,
        "max": 1243.0
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
        "max": 6.0
      },
      "runner_handler_execution_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 1001.0,
        "p95": 1002.0,
        "max": 1008.0
      },
      "runner_handler_import_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 9.0,
        "p95": 630.0,
        "max": 1101.0
      },
      "runner_module_imports_ms": {
        "count": 320,
        "min": 349.0,
        "median": 988.0,
        "p90": 1665.0,
        "p95": 1793.0,
        "max": 2316.0
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
        "max": 5.0
      },
      "runner_setup_ms": {
        "count": 320,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 7.0
      },
      "runner_total_ms": {
        "count": 320,
        "min": 351.0,
        "median": 1181.0,
        "p90": 2151.0,
        "p95": 2374.0,
        "max": 3107.0
      },
      "sandbox_prepare_ms": {
        "count": 320,
        "min": 24.0,
        "median": 163.5,
        "p90": 403.0,
        "p95": 508.0,
        "max": 884.0
      },
      "warm_container_create_ms": {
        "count": 309,
        "min": 238.0,
        "median": 1190.0,
        "p90": 2203.0,
        "p95": 2661.0,
        "max": 3306.0
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
        "count": 320,
        "min": 0.0,
        "median": 719.0,
        "p90": 1413.0,
        "p95": 1636.0,
        "max": 2239.0
      },
      "warm_runner_exec_ms": {
        "count": 320,
        "min": 439.0,
        "median": 1645.5,
        "p90": 2779.0,
        "p95": 3063.0,
        "max": 3806.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 320,
        "min": 54.0,
        "median": 320.5,
        "p90": 603.0,
        "p95": 727.0,
        "max": 966.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 320,
        "min": 59.0,
        "median": 319.0,
        "p90": 617.0,
        "p95": 722.0,
        "max": 1004.0
      },
      "worker_process_total_ms": {
        "count": 320,
        "min": 872.0,
        "median": 5106.0,
        "p90": 7761.0,
        "p95": 8330.0,
        "max": 9863.0
      }
    }
  }
]
```
