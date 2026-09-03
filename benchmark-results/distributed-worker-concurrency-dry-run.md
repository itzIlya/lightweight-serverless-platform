# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T09:19:12.967492+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `37`, version `37`, image `10.42.1.22:5000/functions/bench-tiny-b6590c07:v37-v1-a1-9b4286a1c07b-d1`
- `sleep`: function `38`, version `38`, image `10.42.1.22:5000/functions/bench-sleep-be52c147:v38-v1-a1-e79fcb5dabde-d1`
- `dependency`: function `39`, version `39`, image `10.42.1.22:5000/functions/bench-dependency-eeeb0713:v39-v1-a1-915b9b7da4b8-d1`
- `output`: function `40`, version `40`, image `10.42.1.22:5000/functions/bench-output-7586c671:v40-v1-a1-fe357866a458-d1`
- `input_output`: function `41`, version `41`, image `10.42.1.22:5000/functions/bench-input_output-9f504906:v41-v1-a1-03a2310a6736-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| single-tiny | 2 | 1 | 2 | 2 | 1 | 2 | 0 | 2.672 | 0.749 | 2.093 | 2.656 | worker-1:1, worker-2:1 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "single-tiny",
    "count": 2,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 2.672,
    "throughput_per_second": 0.749,
    "successes": 2,
    "failures": 0,
    "terminal_seconds": {
      "count": 2,
      "min": 1.531,
      "median": 2.093,
      "p90": 2.656,
      "p95": 2.656,
      "max": 2.656
    },
    "accept_seconds": {
      "count": 2,
      "min": 0.156,
      "median": 0.179,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 1,
      "worker-2": 1
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
        "min": 28.0,
        "median": 87.0,
        "p90": 146.0,
        "p95": 146.0,
        "max": 146.0
      },
      "docker_input_copy_ms": {
        "count": 2,
        "min": 4.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 2,
        "min": 855.0,
        "median": 941.0,
        "p90": 1027.0,
        "p95": 1027.0,
        "max": 1027.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 2,
        "min": 917.0,
        "median": 1004.0,
        "p90": 1091.0,
        "p95": 1091.0,
        "max": 1091.0
      },
      "orchestrator_claim_ms": {
        "count": 2,
        "min": 8.0,
        "median": 9.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 2,
        "min": 5.0,
        "median": 5.5,
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
        "min": 334.0,
        "median": 345.5,
        "p90": 357.0,
        "p95": 357.0,
        "max": 357.0
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
        "min": 334.0,
        "median": 346.0,
        "p90": 358.0,
        "p95": 358.0,
        "max": 358.0
      },
      "sandbox_prepare_ms": {
        "count": 2,
        "min": 22.0,
        "median": 23.0,
        "p90": 24.0,
        "p95": 24.0,
        "max": 24.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 319.0,
        "median": 322.0,
        "p90": 325.0,
        "p95": 325.0,
        "max": 325.0
      },
      "warm_pool_release_ms": {
        "count": 2,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 2,
        "min": 418.0,
        "median": 437.5,
        "p90": 457.0,
        "p95": 457.0,
        "max": 457.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 2,
        "min": 62.0,
        "median": 62.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 63.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 2,
        "min": 61.0,
        "median": 64.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 2,
        "min": 935.0,
        "median": 1023.0,
        "p90": 1111.0,
        "p95": 1111.0,
        "max": 1111.0
      }
    }
  }
]
```
