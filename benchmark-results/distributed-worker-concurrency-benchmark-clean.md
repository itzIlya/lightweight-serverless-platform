# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T11:05:56.951731+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `52`, version `52`, image `10.42.1.22:5000/functions/bench-tiny-58ce155b:v52-v1-a1-a7a74d20c5ef-d1`
- `sleep`: function `53`, version `53`, image `10.42.1.22:5000/functions/bench-sleep-51f2fc9a:v53-v1-a1-e11cf7ffde66-d1`
- `dependency`: function `54`, version `54`, image `10.42.1.22:5000/functions/bench-dependency-f002d1d0:v54-v1-a1-65e9e54c08a6-d1`
- `output`: function `55`, version `55`, image `10.42.1.22:5000/functions/bench-output-baa7a7ce:v55-v1-a1-01047a986228-d1`
- `input_output`: function `56`, version `56`, image `10.42.1.22:5000/functions/bench-input_output-0a99c638:v56-v1-a1-e4f8c6e2a784-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| single-tiny | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 9.093 | 1.32 | 1.477 | 1.563 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 9.422 | 1.274 | 1.516 | 1.797 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 9.532 | 1.259 | 1.492 | 2.063 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 5.766 | 2.081 | 1.531 | 2.656 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 5.75 | 2.087 | 1.523 | 2.703 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 5.859 | 2.048 | 1.547 | 2.781 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 5.953 | 2.016 | 2.876 | 4.281 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 5.875 | 2.043 | 2.929 | 4.359 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 5.797 | 2.07 | 2.969 | 4.297 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 5.718 | 2.099 | 3.734 | 5.687 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 6.672 | 1.799 | 3.867 | 6.25 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 5.609 | 2.139 | 3.75 | 5.421 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 19.281 | 0.622 | 2.914 | 3.796 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 17.734 | 0.677 | 2.718 | 3.063 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 18.656 | 0.643 | 2.899 | 3.641 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 11.812 | 1.016 | 3.867 | 4.0 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 14.093 | 0.851 | 3.812 | 4.125 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 11.875 | 1.011 | 3.86 | 3.954 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 13.984 | 0.858 | 6.633 | 8.437 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 11.781 | 1.019 | 6.648 | 7.937 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 11.781 | 1.019 | 6.789 | 7.984 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 13.953 | 0.86 | 7.5 | 11.734 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 11.484 | 1.045 | 7.032 | 11.281 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 12.687 | 0.946 | 7.336 | 11.563 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 10.141 | 1.183 | 1.5 | 2.609 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 8.906 | 1.347 | 1.476 | 1.5 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 9.235 | 1.299 | 1.476 | 1.563 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 7.453 | 1.61 | 1.727 | 2.843 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 7.188 | 1.669 | 2.078 | 2.735 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 6.937 | 1.73 | 1.961 | 2.812 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 6.781 | 1.77 | 3.867 | 4.266 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 6.859 | 1.75 | 3.899 | 4.265 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 6.812 | 1.762 | 3.812 | 4.172 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 6.859 | 1.75 | 4.546 | 6.671 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 6.922 | 1.734 | 4.453 | 6.844 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 6.859 | 1.75 | 4.516 | 6.797 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 15.5 | 0.774 | 2.078 | 2.703 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 11.938 | 1.005 | 1.485 | 1.516 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 13.547 | 0.886 | 1.5 | 2.641 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 8.391 | 1.43 | 1.641 | 2.813 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 8.344 | 1.438 | 2.156 | 2.875 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 9.204 | 1.304 | 2.382 | 3.204 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 8.391 | 1.43 | 3.984 | 5.172 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 7.921 | 1.515 | 3.922 | 5.89 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 7.766 | 1.545 | 3.883 | 5.344 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 9.562 | 1.255 | 4.992 | 8.031 | worker-1:5, worker-2:7 |
| single-output | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 8.11 | 1.48 | 4.586 | 7.375 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 8.281 | 1.449 | 5.211 | 6.859 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 15.703 | 0.764 | 1.82 | 2.703 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 15.39 | 0.78 | 1.633 | 2.703 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 13.421 | 0.894 | 1.562 | 2.672 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 8.235 | 1.457 | 2.64 | 2.797 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 8.078 | 1.486 | 2.657 | 2.765 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 8.14 | 1.474 | 2.234 | 2.812 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 9.844 | 1.219 | 4.055 | 5.281 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 8.609 | 1.394 | 3.946 | 5.328 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 9.453 | 1.269 | 3.656 | 4.875 | worker-1:5, worker-2:7 |
| single-input_output | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 8.313 | 1.444 | 4.852 | 7.922 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 8.703 | 1.379 | 5.023 | 7.234 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 8.703 | 1.379 | 5.375 | 7.235 | worker-1:6, worker-2:6 |
| mixed-15 | 15 | 1 | 2 | 2 | 1 | 15 | 0 | 14.718 | 1.019 | 1.609 | 2.656 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 2 | 2 | 15 | 0 | 15.219 | 0.986 | 1.64 | 2.656 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 1 | 2 | 2 | 3 | 15 | 0 | 15.953 | 0.94 | 1.891 | 2.859 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 4 | 1 | 15 | 0 | 10.75 | 1.395 | 2.625 | 3.89 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 4 | 2 | 15 | 0 | 11.015 | 1.362 | 2.672 | 3.828 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 4 | 3 | 15 | 0 | 11.828 | 1.268 | 2.766 | 3.969 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 8 | 1 | 15 | 0 | 10.437 | 1.437 | 4.218 | 6.25 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 1 | 2 | 8 | 2 | 15 | 0 | 10.687 | 1.404 | 4.234 | 6.422 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 8 | 3 | 15 | 0 | 9.828 | 1.526 | 4.125 | 5.938 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 16 | 1 | 15 | 0 | 9.844 | 1.524 | 6.063 | 9.454 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 1 | 2 | 16 | 2 | 15 | 0 | 10.64 | 1.41 | 6.672 | 10.547 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 16 | 3 | 15 | 0 | 10.609 | 1.414 | 6.953 | 9.422 | worker-1:7, worker-2:8 |
| mixed-30 | 30 | 1 | 2 | 2 | 1 | 30 | 0 | 30.86 | 0.972 | 1.539 | 2.937 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 2 | 2 | 30 | 0 | 32.734 | 0.916 | 1.554 | 3.813 | worker-1:16, worker-2:14 |
| mixed-30 | 30 | 1 | 2 | 2 | 3 | 30 | 0 | 32.469 | 0.924 | 1.82 | 3.468 | worker-1:14, worker-2:16 |
| mixed-30 | 30 | 1 | 2 | 4 | 1 | 30 | 0 | 23.437 | 1.28 | 2.664 | 4.953 | worker-1:14, worker-2:16 |
| mixed-30 | 30 | 1 | 2 | 4 | 2 | 30 | 0 | 20.079 | 1.494 | 2.656 | 3.843 | worker-1:14, worker-2:16 |
| mixed-30 | 30 | 1 | 2 | 4 | 3 | 30 | 0 | 21.406 | 1.401 | 2.523 | 4.828 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 8 | 1 | 30 | 0 | 19.391 | 1.547 | 4.156 | 6.344 | worker-1:14, worker-2:16 |
| mixed-30 | 30 | 1 | 2 | 8 | 2 | 30 | 0 | 19.453 | 1.542 | 4.25 | 8.578 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 8 | 3 | 30 | 0 | 17.765 | 1.689 | 3.914 | 6.281 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 16 | 1 | 30 | 0 | 18.078 | 1.659 | 8.242 | 10.515 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 16 | 2 | 30 | 0 | 17.265 | 1.738 | 7.648 | 9.938 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 16 | 3 | 30 | 0 | 18.468 | 1.624 | 8.563 | 11.031 | worker-1:15, worker-2:15 |
| mixed-80 | 80 | 1 | 2 | 2 | 1 | 80 | 0 | 91.14 | 0.878 | 1.688 | 3.828 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 1 | 2 | 2 | 2 | 80 | 0 | 86.891 | 0.921 | 1.835 | 2.953 | worker-1:38, worker-2:42 |

## Detailed JSON Summary

```json
[
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 9.093,
    "throughput_per_second": 1.32,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.477,
      "p90": 1.563,
      "p95": 1.563,
      "max": 1.594
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.25
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
        "p90": 32.0,
        "p95": 32.0,
        "max": 138.0
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
        "min": 502.0,
        "median": 543.0,
        "p90": 894.0,
        "p95": 894.0,
        "max": 907.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 563.0,
        "median": 605.5,
        "p90": 959.0,
        "p95": 959.0,
        "max": 961.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
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
        "min": 329.0,
        "median": 345.0,
        "p90": 372.0,
        "p95": 372.0,
        "max": 374.0
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
        "min": 329.0,
        "median": 346.0,
        "p90": 373.0,
        "p95": 373.0,
        "max": 375.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 29.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 47.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 248.0,
        "median": 279.0,
        "p90": 310.0,
        "p95": 310.0,
        "max": 310.0
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
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 413.0,
        "median": 436.5,
        "p90": 468.0,
        "p95": 468.0,
        "max": 472.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 84.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 576.0,
        "median": 618.0,
        "p90": 974.0,
        "p95": 974.0,
        "max": 980.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 9.422,
    "throughput_per_second": 1.274,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.468,
      "median": 1.516,
      "p90": 1.797,
      "p95": 1.797,
      "max": 1.797
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.179,
      "p90": 0.297,
      "p95": 0.297,
      "max": 0.328
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 507.0,
        "median": 545.5,
        "p90": 602.0,
        "p95": 602.0,
        "max": 637.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 562.0,
        "median": 607.5,
        "p90": 668.0,
        "p95": 668.0,
        "max": 703.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
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
        "median": 357.5,
        "p90": 383.0,
        "p95": 383.0,
        "max": 392.0
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
        "median": 358.0,
        "p90": 384.0,
        "p95": 384.0,
        "max": 393.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 34.5,
        "p90": 59.0,
        "p95": 59.0,
        "max": 72.0
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
        "median": 449.5,
        "p90": 487.0,
        "p95": 487.0,
        "max": 492.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 574.0,
        "median": 626.5,
        "p90": 684.0,
        "p95": 684.0,
        "max": 715.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 9.532,
    "throughput_per_second": 1.259,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.492,
      "p90": 2.063,
      "p95": 2.063,
      "max": 2.078
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.188,
      "p95": 0.188,
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 510.0,
        "median": 565.5,
        "p90": 606.0,
        "p95": 606.0,
        "max": 627.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 565.0,
        "median": 622.0,
        "p90": 669.0,
        "p95": 669.0,
        "max": 689.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
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
        "min": 336.0,
        "median": 363.0,
        "p90": 391.0,
        "p95": 391.0,
        "max": 403.0
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
        "median": 364.0,
        "p90": 392.0,
        "p95": 392.0,
        "max": 404.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 30.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 56.0
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
        "min": 424.0,
        "median": 459.5,
        "p90": 494.0,
        "p95": 494.0,
        "max": 500.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 61.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 578.0,
        "median": 638.5,
        "p90": 681.0,
        "p95": 681.0,
        "max": 706.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 5.766,
    "throughput_per_second": 2.081,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.531,
      "p90": 2.656,
      "p95": 2.656,
      "max": 2.718
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.187,
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 497.0,
        "median": 556.0,
        "p90": 598.0,
        "p95": 598.0,
        "max": 657.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 555.0,
        "median": 614.0,
        "p90": 665.0,
        "p95": 665.0,
        "max": 716.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
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
        "median": 356.5,
        "p90": 408.0,
        "p95": 408.0,
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
        "min": 332.0,
        "median": 357.0,
        "p90": 409.0,
        "p95": 409.0,
        "max": 448.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 25.0,
        "p90": 52.0,
        "p95": 52.0,
        "max": 61.0
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
        "min": 415.0,
        "median": 447.0,
        "p90": 504.0,
        "p95": 504.0,
        "max": 546.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 565.0,
        "median": 632.5,
        "p90": 678.0,
        "p95": 678.0,
        "max": 728.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 5.75,
    "throughput_per_second": 2.087,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 1.523,
      "p90": 2.703,
      "p95": 2.703,
      "max": 2.719
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 512.0,
        "median": 552.0,
        "p90": 591.0,
        "p95": 591.0,
        "max": 597.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 573.0,
        "median": 611.0,
        "p90": 655.0,
        "p95": 655.0,
        "max": 666.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 12.0,
        "p95": 12.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 9.0,
        "p90": 16.0,
        "p95": 16.0,
        "max": 21.0
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
        "min": 335.0,
        "median": 346.5,
        "p90": 382.0,
        "p95": 382.0,
        "max": 385.0
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
        "median": 347.5,
        "p90": 382.0,
        "p95": 382.0,
        "max": 386.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 36.5,
        "p90": 59.0,
        "p95": 59.0,
        "max": 74.0
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
        "min": 418.0,
        "median": 444.5,
        "p90": 479.0,
        "p95": 479.0,
        "max": 492.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 591.0,
        "median": 626.0,
        "p90": 679.0,
        "p95": 679.0,
        "max": 685.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 5.859,
    "throughput_per_second": 2.048,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.438,
      "median": 1.547,
      "p90": 2.781,
      "p95": 2.781,
      "max": 2.781
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.188,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.25
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
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 498.0,
        "median": 567.5,
        "p90": 611.0,
        "p95": 611.0,
        "max": 647.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 549.0,
        "median": 626.0,
        "p90": 685.0,
        "p95": 685.0,
        "max": 717.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 19.0,
        "p95": 19.0,
        "max": 21.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 17.0
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
        "min": 331.0,
        "median": 353.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 400.0
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
        "min": 331.0,
        "median": 354.0,
        "p90": 394.0,
        "p95": 394.0,
        "max": 401.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 31.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 113.0
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
        "min": 418.0,
        "median": 452.0,
        "p90": 491.0,
        "p95": 491.0,
        "max": 499.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 50.0,
        "median": 62.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 61.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 558.0,
        "median": 647.5,
        "p90": 696.0,
        "p95": 696.0,
        "max": 756.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 5.953,
    "throughput_per_second": 2.016,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.61,
      "median": 2.876,
      "p90": 4.281,
      "p95": 4.281,
      "max": 4.344
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.25,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.36
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 508.0,
        "median": 557.0,
        "p90": 644.0,
        "p95": 644.0,
        "max": 663.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 566.0,
        "median": 620.5,
        "p90": 702.0,
        "p95": 702.0,
        "max": 735.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
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
        "median": 342.0,
        "p90": 381.0,
        "p95": 381.0,
        "max": 385.0
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
        "median": 342.0,
        "p90": 381.0,
        "p95": 381.0,
        "max": 386.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 37.0,
        "p90": 127.0,
        "p95": 127.0,
        "max": 128.0
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
        "min": 425.0,
        "median": 439.0,
        "p90": 475.0,
        "p95": 475.0,
        "max": 475.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 582.0,
        "median": 638.5,
        "p90": 720.0,
        "p95": 720.0,
        "max": 760.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 5.875,
    "throughput_per_second": 2.043,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.703,
      "median": 2.929,
      "p90": 4.359,
      "p95": 4.359,
      "max": 4.484
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.304,
      "p90": 0.343,
      "p95": 0.343,
      "max": 0.359
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
        "min": 506.0,
        "median": 549.5,
        "p90": 633.0,
        "p95": 633.0,
        "max": 756.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 562.0,
        "median": 609.0,
        "p90": 689.0,
        "p95": 689.0,
        "max": 816.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 21.0,
        "p95": 21.0,
        "max": 25.0
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
        "min": 337.0,
        "median": 344.0,
        "p90": 370.0,
        "p95": 370.0,
        "max": 386.0
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
        "median": 345.0,
        "p90": 371.0,
        "p95": 371.0,
        "max": 387.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 41.5,
        "p90": 145.0,
        "p95": 145.0,
        "max": 229.0
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
        "min": 421.0,
        "median": 437.0,
        "p90": 462.0,
        "p95": 462.0,
        "max": 479.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 60.0,
        "p95": 60.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 575.0,
        "median": 623.0,
        "p90": 717.0,
        "p95": 717.0,
        "max": 849.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 5.797,
    "throughput_per_second": 2.07,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.547,
      "median": 2.969,
      "p90": 4.297,
      "p95": 4.297,
      "max": 4.406
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.321,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.391
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 504.0,
        "median": 555.5,
        "p90": 629.0,
        "p95": 629.0,
        "max": 661.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 563.0,
        "median": 617.5,
        "p90": 689.0,
        "p95": 689.0,
        "max": 721.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 18.0,
        "p95": 18.0,
        "max": 19.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
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
        "min": 333.0,
        "median": 345.0,
        "p90": 384.0,
        "p95": 384.0,
        "max": 406.0
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
        "median": 346.0,
        "p90": 385.0,
        "p95": 385.0,
        "max": 407.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 28.0,
        "p90": 138.0,
        "p95": 138.0,
        "max": 149.0
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
        "min": 418.0,
        "median": 438.0,
        "p90": 483.0,
        "p95": 483.0,
        "max": 504.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 62.0,
        "p95": 62.0,
        "max": 65.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 573.0,
        "median": 630.0,
        "p90": 715.0,
        "p95": 715.0,
        "max": 749.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 5.718,
    "throughput_per_second": 2.099,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.781,
      "median": 3.734,
      "p90": 5.687,
      "p95": 5.687,
      "max": 5.703
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.187,
      "median": 0.414,
      "p90": 0.625,
      "p95": 0.625,
      "max": 0.688
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
        "min": 501.0,
        "median": 581.0,
        "p90": 715.0,
        "p95": 715.0,
        "max": 721.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 560.0,
        "median": 644.0,
        "p90": 778.0,
        "p95": 778.0,
        "max": 782.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 15.0,
        "p95": 15.0,
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 330.0,
        "median": 347.0,
        "p90": 381.0,
        "p95": 381.0,
        "max": 394.0
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
        "min": 330.0,
        "median": 348.0,
        "p90": 382.0,
        "p95": 382.0,
        "max": 394.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 48.5,
        "p90": 178.0,
        "p95": 178.0,
        "max": 229.0
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
        "min": 417.0,
        "median": 440.5,
        "p90": 485.0,
        "p95": 485.0,
        "max": 491.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 60.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 570.0,
        "median": 660.0,
        "p90": 794.0,
        "p95": 794.0,
        "max": 814.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 6.672,
    "throughput_per_second": 1.799,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.765,
      "median": 3.867,
      "p90": 6.25,
      "p95": 6.25,
      "max": 6.656
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.351,
      "p90": 0.484,
      "p95": 0.484,
      "max": 0.515
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 510.0,
        "median": 589.5,
        "p90": 670.0,
        "p95": 670.0,
        "max": 727.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 567.0,
        "median": 648.5,
        "p90": 728.0,
        "p95": 728.0,
        "max": 792.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 20.0
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
        "min": 330.0,
        "median": 363.0,
        "p90": 400.0,
        "p95": 400.0,
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
        "min": 331.0,
        "median": 363.5,
        "p90": 401.0,
        "p95": 401.0,
        "max": 408.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 34.5,
        "p90": 170.0,
        "p95": 170.0,
        "max": 179.0
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
        "median": 459.0,
        "p90": 499.0,
        "p95": 499.0,
        "max": 500.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 64.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 580.0,
        "median": 663.5,
        "p90": 747.0,
        "p95": 747.0,
        "max": 809.0
      }
    }
  },
  {
    "scenario": "single-tiny",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 5.609,
    "throughput_per_second": 2.139,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.734,
      "median": 3.75,
      "p90": 5.421,
      "p95": 5.421,
      "max": 5.609
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.374,
      "p90": 0.5,
      "p95": 0.5,
      "max": 0.937
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
        "min": 503.0,
        "median": 568.0,
        "p90": 644.0,
        "p95": 644.0,
        "max": 765.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 557.0,
        "median": 632.5,
        "p90": 715.0,
        "p95": 715.0,
        "max": 825.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 8.5,
        "p90": 16.0,
        "p95": 16.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 13.0,
        "p95": 13.0,
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
        "median": 344.0,
        "p90": 399.0,
        "p95": 399.0,
        "max": 400.0
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
        "median": 345.0,
        "p90": 400.0,
        "p95": 400.0,
        "max": 401.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 51.5,
        "p90": 147.0,
        "p95": 147.0,
        "max": 204.0
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
        "min": 414.0,
        "median": 444.5,
        "p90": 495.0,
        "p95": 495.0,
        "max": 498.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 56.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 570.0,
        "median": 651.5,
        "p90": 732.0,
        "p95": 732.0,
        "max": 848.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 19.281,
    "throughput_per_second": 0.622,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.61,
      "median": 2.914,
      "p90": 3.796,
      "p95": 3.796,
      "max": 4.375
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.164,
      "p90": 0.359,
      "p95": 0.359,
      "max": 0.36
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
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
        "p90": 25.0,
        "p95": 25.0,
        "max": 165.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1505.0,
        "median": 1565.0,
        "p90": 1801.0,
        "p95": 1801.0,
        "max": 2060.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1560.0,
        "median": 1634.5,
        "p90": 1859.0,
        "p95": 1859.0,
        "max": 2126.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 5.5,
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
        "min": 332.0,
        "median": 369.0,
        "p90": 401.0,
        "p95": 401.0,
        "max": 406.0
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
        "min": 1333.0,
        "median": 1370.5,
        "p90": 1402.0,
        "p95": 1402.0,
        "max": 1407.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 27.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 48.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 244.0,
        "median": 270.0,
        "p90": 296.0,
        "p95": 296.0,
        "max": 296.0
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
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 1418.0,
        "median": 1465.5,
        "p90": 1501.0,
        "p95": 1501.0,
        "max": 1505.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1573.0,
        "median": 1647.5,
        "p90": 1876.0,
        "p95": 1876.0,
        "max": 2141.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 17.734,
    "throughput_per_second": 0.677,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.609,
      "median": 2.718,
      "p90": 3.063,
      "p95": 3.063,
      "max": 4.031
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.36
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
        "min": 1501.0,
        "median": 1586.5,
        "p90": 1632.0,
        "p95": 1632.0,
        "max": 1647.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1561.0,
        "median": 1649.5,
        "p90": 1698.0,
        "p95": 1698.0,
        "max": 1708.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
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
        "min": 331.0,
        "median": 351.0,
        "p90": 397.0,
        "p95": 397.0,
        "max": 431.0
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
        "min": 1332.0,
        "median": 1352.0,
        "p90": 1399.0,
        "p95": 1399.0,
        "max": 1432.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 29.0,
        "p90": 42.0,
        "p95": 42.0,
        "max": 46.0
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
        "min": 1415.0,
        "median": 1447.5,
        "p90": 1521.0,
        "p95": 1521.0,
        "max": 1529.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 63.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1573.0,
        "median": 1661.5,
        "p90": 1712.0,
        "p95": 1712.0,
        "max": 1721.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 18.656,
    "throughput_per_second": 0.643,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.593,
      "median": 2.899,
      "p90": 3.641,
      "p95": 3.641,
      "max": 3.796
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.625,
      "p95": 0.625,
      "max": 1.688
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1497.0,
        "median": 1536.5,
        "p90": 1594.0,
        "p95": 1594.0,
        "max": 1597.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1551.0,
        "median": 1600.0,
        "p90": 1656.0,
        "p95": 1656.0,
        "max": 1661.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
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
        "min": 331.0,
        "median": 354.0,
        "p90": 384.0,
        "p95": 384.0,
        "max": 402.0
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
        "min": 1332.0,
        "median": 1355.0,
        "p90": 1385.0,
        "p95": 1385.0,
        "max": 1403.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 28.0,
        "p90": 33.0,
        "p95": 33.0,
        "max": 49.0
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
        "min": 1414.0,
        "median": 1446.5,
        "p90": 1491.0,
        "p95": 1491.0,
        "max": 1500.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 57.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 60.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1564.0,
        "median": 1615.5,
        "p90": 1676.0,
        "p95": 1676.0,
        "max": 1682.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 11.812,
    "throughput_per_second": 1.016,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.672,
      "median": 3.867,
      "p90": 4.0,
      "p95": 4.0,
      "max": 4.125
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1518.0,
        "median": 1569.0,
        "p90": 1598.0,
        "p95": 1598.0,
        "max": 1600.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1573.0,
        "median": 1628.0,
        "p90": 1661.0,
        "p95": 1661.0,
        "max": 1663.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 8.0,
        "p90": 16.0,
        "p95": 16.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
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
        "min": 333.0,
        "median": 348.5,
        "p90": 387.0,
        "p95": 387.0,
        "max": 411.0
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
        "min": 1334.0,
        "median": 1349.5,
        "p90": 1388.0,
        "p95": 1388.0,
        "max": 1412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 38.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 68.0
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
        "min": 1420.0,
        "median": 1441.0,
        "p90": 1481.0,
        "p95": 1481.0,
        "max": 1507.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1585.0,
        "median": 1645.0,
        "p90": 1678.0,
        "p95": 1678.0,
        "max": 1683.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 14.093,
    "throughput_per_second": 0.851,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.704,
      "median": 3.812,
      "p90": 4.125,
      "p95": 4.125,
      "max": 6.156
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.375
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
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
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1507.0,
        "median": 1553.5,
        "p90": 1608.0,
        "p95": 1608.0,
        "max": 1614.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1565.0,
        "median": 1621.5,
        "p90": 1674.0,
        "p95": 1674.0,
        "max": 1690.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 13.0,
        "p95": 13.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 8.0,
        "p90": 10.0,
        "p95": 10.0,
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
        "min": 333.0,
        "median": 346.0,
        "p90": 392.0,
        "p95": 392.0,
        "max": 399.0
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
        "min": 1334.0,
        "median": 1347.0,
        "p90": 1393.0,
        "p95": 1393.0,
        "max": 1400.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 34.5,
        "p90": 59.0,
        "p95": 59.0,
        "max": 87.0
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
        "min": 1424.0,
        "median": 1443.5,
        "p90": 1493.0,
        "p95": 1493.0,
        "max": 1500.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 62.5,
        "p90": 83.0,
        "p95": 83.0,
        "max": 85.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1581.0,
        "median": 1634.0,
        "p90": 1699.0,
        "p95": 1699.0,
        "max": 1708.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 11.875,
    "throughput_per_second": 1.011,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.657,
      "median": 3.86,
      "p90": 3.954,
      "p95": 3.954,
      "max": 4.046
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.204
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1498.0,
        "median": 1531.0,
        "p90": 1608.0,
        "p95": 1608.0,
        "max": 1637.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1552.0,
        "median": 1592.0,
        "p90": 1675.0,
        "p95": 1675.0,
        "max": 1713.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
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
        "min": 332.0,
        "median": 350.5,
        "p90": 402.0,
        "p95": 402.0,
        "max": 402.0
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
        "min": 1333.0,
        "median": 1351.5,
        "p90": 1403.0,
        "p95": 1403.0,
        "max": 1403.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 28.5,
        "p90": 36.0,
        "p95": 36.0,
        "max": 68.0
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
        "min": 1416.0,
        "median": 1440.0,
        "p90": 1497.0,
        "p95": 1497.0,
        "max": 1509.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 57.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1566.0,
        "median": 1607.5,
        "p90": 1688.0,
        "p95": 1688.0,
        "max": 1726.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 13.984,
    "throughput_per_second": 0.858,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.812,
      "median": 6.633,
      "p90": 8.437,
      "p95": 8.437,
      "max": 9.547
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.265,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.453
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 12.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1543.0,
        "median": 1571.0,
        "p90": 1626.0,
        "p95": 1626.0,
        "max": 1706.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1601.0,
        "median": 1635.0,
        "p90": 1687.0,
        "p95": 1687.0,
        "max": 1795.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 13.0,
        "p95": 13.0,
        "max": 15.0
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
        "min": 334.0,
        "median": 351.5,
        "p90": 392.0,
        "p95": 392.0,
        "max": 400.0
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
        "min": 1335.0,
        "median": 1352.5,
        "p90": 1393.0,
        "p95": 1393.0,
        "max": 1402.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 26.0,
        "median": 52.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 184.0
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
        "min": 1429.0,
        "median": 1452.0,
        "p90": 1495.0,
        "p95": 1495.0,
        "max": 1532.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 59.5,
        "p90": 78.0,
        "p95": 78.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 62.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 87.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1612.0,
        "median": 1656.0,
        "p90": 1706.0,
        "p95": 1706.0,
        "max": 1821.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 11.781,
    "throughput_per_second": 1.019,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.734,
      "median": 6.648,
      "p90": 7.937,
      "p95": 7.937,
      "max": 8.078
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.234,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1508.0,
        "median": 1568.5,
        "p90": 1656.0,
        "p95": 1656.0,
        "max": 1717.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1564.0,
        "median": 1627.0,
        "p90": 1712.0,
        "p95": 1712.0,
        "max": 1779.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 16.0,
        "p95": 16.0,
        "max": 17.0
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
        "min": 331.0,
        "median": 349.5,
        "p90": 388.0,
        "p95": 388.0,
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
        "min": 1332.0,
        "median": 1350.5,
        "p90": 1389.0,
        "p95": 1389.0,
        "max": 1411.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 56.5,
        "p90": 124.0,
        "p95": 124.0,
        "max": 174.0
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
        "min": 1417.0,
        "median": 1446.0,
        "p90": 1491.0,
        "p95": 1491.0,
        "max": 1517.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 60.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 85.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1586.0,
        "median": 1644.5,
        "p90": 1727.0,
        "p95": 1727.0,
        "max": 1795.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 11.781,
    "throughput_per_second": 1.019,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.812,
      "median": 6.789,
      "p90": 7.984,
      "p95": 7.984,
      "max": 8.047
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.351,
      "p90": 0.453,
      "p95": 0.453,
      "max": 0.469
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1523.0,
        "median": 1578.0,
        "p90": 1650.0,
        "p95": 1650.0,
        "max": 1675.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1577.0,
        "median": 1639.5,
        "p90": 1722.0,
        "p95": 1722.0,
        "max": 1740.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
        "p90": 9.0,
        "p95": 9.0,
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
        "min": 332.0,
        "median": 355.0,
        "p90": 396.0,
        "p95": 396.0,
        "max": 413.0
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
        "min": 1333.0,
        "median": 1356.0,
        "p90": 1397.0,
        "p95": 1397.0,
        "max": 1414.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 25.0,
        "median": 43.0,
        "p90": 141.0,
        "p95": 141.0,
        "max": 154.0
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
        "min": 1422.0,
        "median": 1449.0,
        "p90": 1512.0,
        "p95": 1512.0,
        "max": 1512.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1590.0,
        "median": 1654.5,
        "p90": 1735.0,
        "p95": 1735.0,
        "max": 1762.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 13.953,
    "throughput_per_second": 0.86,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 3.453,
      "median": 7.5,
      "p90": 11.734,
      "p95": 11.734,
      "max": 13.953
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.344,
      "median": 0.5,
      "p90": 0.719,
      "p95": 0.719,
      "max": 0.719
    },
    "output_download_seconds": {
      "count": 0
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
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
        "min": 1508.0,
        "median": 1589.5,
        "p90": 1672.0,
        "p95": 1672.0,
        "max": 1707.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1566.0,
        "median": 1656.0,
        "p90": 1728.0,
        "p95": 1728.0,
        "max": 1777.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 6.0,
        "p95": 6.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
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
        "min": 334.0,
        "median": 366.5,
        "p90": 403.0,
        "p95": 403.0,
        "max": 403.0
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
        "min": 1335.0,
        "median": 1367.5,
        "p90": 1404.0,
        "p95": 1404.0,
        "max": 1404.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 26.5,
        "p90": 123.0,
        "p95": 123.0,
        "max": 187.0
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
        "min": 1420.0,
        "median": 1465.0,
        "p90": 1505.0,
        "p95": 1505.0,
        "max": 1505.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 62.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1578.0,
        "median": 1670.5,
        "p90": 1746.0,
        "p95": 1746.0,
        "max": 1792.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 11.484,
    "throughput_per_second": 1.045,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.594,
      "median": 7.032,
      "p90": 11.281,
      "p95": 11.281,
      "max": 11.484
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.297,
      "median": 0.414,
      "p90": 0.547,
      "p95": 0.547,
      "max": 0.578
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
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1502.0,
        "median": 1573.5,
        "p90": 1686.0,
        "p95": 1686.0,
        "max": 1688.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1559.0,
        "median": 1637.0,
        "p90": 1742.0,
        "p95": 1742.0,
        "max": 1747.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
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
        "min": 329.0,
        "median": 346.0,
        "p90": 396.0,
        "p95": 396.0,
        "max": 410.0
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
        "min": 1330.0,
        "median": 1347.0,
        "p90": 1397.0,
        "p95": 1397.0,
        "max": 1411.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 32.5,
        "p90": 120.0,
        "p95": 120.0,
        "max": 197.0
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
        "min": 1418.0,
        "median": 1437.5,
        "p90": 1500.0,
        "p95": 1500.0,
        "max": 1502.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 62.0,
        "p90": 76.0,
        "p95": 76.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1570.0,
        "median": 1649.0,
        "p90": 1759.0,
        "p95": 1759.0,
        "max": 1767.0
      }
    }
  },
  {
    "scenario": "single-sleep",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 12.687,
    "throughput_per_second": 0.946,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.922,
      "median": 7.336,
      "p90": 11.563,
      "p95": 11.563,
      "max": 12.672
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.508,
      "p90": 0.954,
      "p95": 0.954,
      "max": 0.985
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
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1509.0,
        "median": 1535.5,
        "p90": 1665.0,
        "p95": 1665.0,
        "max": 1829.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1563.0,
        "median": 1605.0,
        "p90": 1726.0,
        "p95": 1726.0,
        "max": 1888.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
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
        "min": 332.0,
        "median": 343.5,
        "p90": 411.0,
        "p95": 411.0,
        "max": 413.0
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
        "min": 1333.0,
        "median": 1344.5,
        "p90": 1413.0,
        "p95": 1413.0,
        "max": 1414.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 36.0,
        "p90": 148.0,
        "p95": 148.0,
        "max": 236.0
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
        "min": 1421.0,
        "median": 1435.0,
        "p90": 1526.0,
        "p95": 1526.0,
        "max": 1534.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1575.0,
        "median": 1616.5,
        "p90": 1743.0,
        "p95": 1743.0,
        "max": 1906.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 10.141,
    "throughput_per_second": 1.183,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.438,
      "median": 1.5,
      "p90": 2.609,
      "p95": 2.609,
      "max": 2.687
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.203
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
        "p90": 36.0,
        "p95": 36.0,
        "max": 134.0
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
        "min": 676.0,
        "median": 756.0,
        "p90": 1068.0,
        "p95": 1068.0,
        "max": 1070.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 730.0,
        "median": 821.0,
        "p90": 1124.0,
        "p95": 1124.0,
        "max": 1128.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 163.0,
        "median": 174.0,
        "p90": 196.0,
        "p95": 196.0,
        "max": 199.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 346.0,
        "p90": 384.0,
        "p95": 384.0,
        "max": 401.0
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
        "min": 497.0,
        "median": 522.0,
        "p90": 580.0,
        "p95": 580.0,
        "max": 598.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 28.5,
        "p90": 37.0,
        "p95": 37.0,
        "max": 47.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 229.0,
        "median": 265.5,
        "p90": 302.0,
        "p95": 302.0,
        "max": 302.0
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
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 592.0,
        "median": 622.5,
        "p90": 685.0,
        "p95": 685.0,
        "max": 703.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 51.0,
        "median": 58.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 743.0,
        "median": 835.0,
        "p90": 1134.0,
        "p95": 1134.0,
        "max": 1145.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 8.906,
    "throughput_per_second": 1.347,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.476,
      "p90": 1.5,
      "p95": 1.5,
      "max": 1.5
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.157,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 676.0,
        "median": 730.5,
        "p90": 803.0,
        "p95": 803.0,
        "max": 805.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 735.0,
        "median": 788.5,
        "p90": 865.0,
        "p95": 865.0,
        "max": 868.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
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
        "min": 165.0,
        "median": 173.5,
        "p90": 195.0,
        "p95": 195.0,
        "max": 200.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 353.5,
        "p90": 406.0,
        "p95": 406.0,
        "max": 414.0
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
        "min": 497.0,
        "median": 527.0,
        "p90": 597.0,
        "p95": 597.0,
        "max": 615.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 25.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 41.0
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
        "min": 589.0,
        "median": 632.5,
        "p90": 710.0,
        "p95": 710.0,
        "max": 718.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 59.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 747.0,
        "median": 800.5,
        "p90": 879.0,
        "p95": 879.0,
        "max": 880.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 9.235,
    "throughput_per_second": 1.299,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.476,
      "p90": 1.563,
      "p95": 1.563,
      "max": 1.766
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.469
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 679.0,
        "median": 740.0,
        "p90": 812.0,
        "p95": 812.0,
        "max": 843.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 734.0,
        "median": 798.5,
        "p90": 874.0,
        "p95": 874.0,
        "max": 909.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
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
        "min": 165.0,
        "median": 175.5,
        "p90": 203.0,
        "p95": 203.0,
        "max": 234.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 361.5,
        "p90": 402.0,
        "p95": 402.0,
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
        "min": 499.0,
        "median": 543.0,
        "p90": 599.0,
        "p95": 599.0,
        "max": 603.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 31.5,
        "p90": 54.0,
        "p95": 54.0,
        "max": 68.0
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
        "min": 590.0,
        "median": 643.0,
        "p90": 709.0,
        "p95": 709.0,
        "max": 718.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 748.0,
        "median": 814.0,
        "p90": 885.0,
        "p95": 885.0,
        "max": 928.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 7.453,
    "throughput_per_second": 1.61,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 1.727,
      "p90": 2.843,
      "p95": 2.843,
      "max": 3.063
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.211,
      "p90": 0.329,
      "p95": 0.329,
      "max": 0.594
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 678.0,
        "median": 724.5,
        "p90": 766.0,
        "p95": 766.0,
        "max": 767.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 736.0,
        "median": 804.0,
        "p90": 830.0,
        "p95": 830.0,
        "max": 839.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 2.0,
        "median": 6.0,
        "p90": 17.0,
        "p95": 17.0,
        "max": 20.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
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
        "median": 170.5,
        "p90": 189.0,
        "p95": 189.0,
        "max": 192.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 332.0,
        "median": 339.5,
        "p90": 371.0,
        "p95": 371.0,
        "max": 375.0
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
        "median": 509.5,
        "p90": 561.0,
        "p95": 561.0,
        "max": 569.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 30.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 76.0
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
        "max": 1.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 592.0,
        "median": 611.5,
        "p90": 663.0,
        "p95": 663.0,
        "max": 667.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 90.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 752.0,
        "median": 821.0,
        "p90": 852.0,
        "p95": 852.0,
        "max": 868.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 7.188,
    "throughput_per_second": 1.669,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 2.078,
      "p90": 2.735,
      "p95": 2.735,
      "max": 3.0
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 687.0,
        "median": 714.0,
        "p90": 761.0,
        "p95": 761.0,
        "max": 769.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 740.0,
        "median": 776.0,
        "p90": 832.0,
        "p95": 832.0,
        "max": 837.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.5,
        "p90": 10.0,
        "p95": 10.0,
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
        "min": 165.0,
        "median": 172.0,
        "p90": 188.0,
        "p95": 188.0,
        "max": 193.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 333.0,
        "median": 339.0,
        "p90": 369.0,
        "p95": 369.0,
        "max": 376.0
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
        "min": 498.0,
        "median": 514.5,
        "p90": 559.0,
        "p95": 559.0,
        "max": 570.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 37.5,
        "p90": 54.0,
        "p95": 54.0,
        "max": 60.0
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
        "min": 590.0,
        "median": 614.0,
        "p90": 664.0,
        "p95": 664.0,
        "max": 670.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.5,
        "p90": 61.0,
        "p95": 61.0,
        "max": 62.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 757.0,
        "median": 787.5,
        "p90": 846.0,
        "p95": 846.0,
        "max": 853.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 6.937,
    "throughput_per_second": 1.73,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.406,
      "median": 1.961,
      "p90": 2.812,
      "p95": 2.812,
      "max": 3.031
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.36,
      "p95": 0.36,
      "max": 0.625
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 685.0,
        "median": 712.5,
        "p90": 759.0,
        "p95": 759.0,
        "max": 788.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 745.0,
        "median": 773.5,
        "p90": 819.0,
        "p95": 819.0,
        "max": 851.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 168.0,
        "median": 171.5,
        "p90": 190.0,
        "p95": 190.0,
        "max": 190.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 334.0,
        "median": 340.0,
        "p90": 369.0,
        "p95": 369.0,
        "max": 386.0
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
        "median": 511.0,
        "p90": 561.0,
        "p95": 561.0,
        "max": 566.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 31.0,
        "p90": 40.0,
        "p95": 40.0,
        "max": 40.0
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
        "min": 599.0,
        "median": 612.0,
        "p90": 668.0,
        "p95": 668.0,
        "max": 674.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 757.0,
        "median": 792.5,
        "p90": 833.0,
        "p95": 833.0,
        "max": 861.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 6.781,
    "throughput_per_second": 1.77,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.579,
      "median": 3.867,
      "p90": 4.266,
      "p95": 4.266,
      "max": 5.266
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.289,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.36
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
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 683.0,
        "median": 745.5,
        "p90": 805.0,
        "p95": 805.0,
        "max": 815.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 738.0,
        "median": 803.0,
        "p90": 870.0,
        "p95": 870.0,
        "max": 879.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
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
        "median": 174.5,
        "p90": 196.0,
        "p95": 196.0,
        "max": 198.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 333.0,
        "median": 348.0,
        "p90": 382.0,
        "p95": 382.0,
        "max": 382.0
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
        "min": 501.0,
        "median": 522.5,
        "p90": 573.0,
        "p95": 573.0,
        "max": 581.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 45.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 77.0
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
        "min": 593.0,
        "median": 624.0,
        "p90": 684.0,
        "p95": 684.0,
        "max": 691.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 756.0,
        "median": 818.0,
        "p90": 885.0,
        "p95": 885.0,
        "max": 894.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 6.859,
    "throughput_per_second": 1.75,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.515,
      "median": 3.899,
      "p90": 4.265,
      "p95": 4.265,
      "max": 4.343
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.265,
      "p90": 0.297,
      "p95": 0.297,
      "max": 0.313
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 677.0,
        "median": 730.0,
        "p90": 813.0,
        "p95": 813.0,
        "max": 857.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 733.0,
        "median": 787.5,
        "p90": 872.0,
        "p95": 872.0,
        "max": 919.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 14.0
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
        "median": 174.0,
        "p90": 198.0,
        "p95": 198.0,
        "max": 202.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 333.0,
        "median": 345.5,
        "p90": 387.0,
        "p95": 387.0,
        "max": 424.0
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
        "min": 503.0,
        "median": 519.0,
        "p90": 586.0,
        "p95": 586.0,
        "max": 614.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 36.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 73.0
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
        "min": 594.0,
        "median": 619.0,
        "p90": 689.0,
        "p95": 689.0,
        "max": 717.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 744.0,
        "median": 802.0,
        "p90": 886.0,
        "p95": 886.0,
        "max": 940.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 6.812,
    "throughput_per_second": 1.762,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.515,
      "median": 3.812,
      "p90": 4.172,
      "p95": 4.172,
      "max": 4.218
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.266,
      "p90": 0.359,
      "p95": 0.359,
      "max": 0.359
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 681.0,
        "median": 727.5,
        "p90": 797.0,
        "p95": 797.0,
        "max": 819.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 735.0,
        "median": 788.0,
        "p90": 861.0,
        "p95": 861.0,
        "max": 877.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 166.0,
        "median": 172.5,
        "p90": 194.0,
        "p95": 194.0,
        "max": 201.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 333.0,
        "median": 343.0,
        "p90": 385.0,
        "p95": 385.0,
        "max": 387.0
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
        "min": 500.0,
        "median": 517.5,
        "p90": 581.0,
        "p95": 581.0,
        "max": 587.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 31.0,
        "p90": 58.0,
        "p95": 58.0,
        "max": 66.0
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
        "min": 593.0,
        "median": 615.0,
        "p90": 685.0,
        "p95": 685.0,
        "max": 695.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 746.0,
        "median": 802.5,
        "p90": 871.0,
        "p95": 871.0,
        "max": 890.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 6.859,
    "throughput_per_second": 1.75,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.687,
      "median": 4.546,
      "p90": 6.671,
      "p95": 6.671,
      "max": 6.843
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.437,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 683.0,
        "median": 747.0,
        "p90": 911.0,
        "p95": 911.0,
        "max": 923.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 739.0,
        "median": 813.5,
        "p90": 976.0,
        "p95": 976.0,
        "max": 983.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
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
        "min": 167.0,
        "median": 174.0,
        "p90": 204.0,
        "p95": 204.0,
        "max": 206.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 336.0,
        "median": 349.0,
        "p90": 413.0,
        "p95": 413.0,
        "max": 455.0
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
        "median": 526.5,
        "p90": 620.0,
        "p95": 620.0,
        "max": 658.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 32.5,
        "p90": 115.0,
        "p95": 115.0,
        "max": 128.0
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
        "median": 630.0,
        "p90": 738.0,
        "p95": 738.0,
        "max": 763.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 754.0,
        "median": 827.5,
        "p90": 993.0,
        "p95": 993.0,
        "max": 1004.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 6.922,
    "throughput_per_second": 1.734,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.875,
      "median": 4.453,
      "p90": 6.844,
      "p95": 6.844,
      "max": 6.922
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.438,
      "p90": 0.625,
      "p95": 0.625,
      "max": 0.766
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 681.0,
        "median": 769.0,
        "p90": 813.0,
        "p95": 813.0,
        "max": 1028.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 738.0,
        "median": 829.0,
        "p90": 870.0,
        "p95": 870.0,
        "max": 1090.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 11.0
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
        "median": 175.5,
        "p90": 196.0,
        "p95": 196.0,
        "max": 205.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 336.0,
        "median": 361.5,
        "p90": 392.0,
        "p95": 392.0,
        "max": 411.0
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
        "min": 504.0,
        "median": 539.0,
        "p90": 590.0,
        "p95": 590.0,
        "max": 600.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 38.0,
        "p90": 131.0,
        "p95": 131.0,
        "max": 252.0
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
        "min": 601.0,
        "median": 639.0,
        "p90": 696.0,
        "p95": 696.0,
        "max": 707.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 58.5,
        "p90": 62.0,
        "p95": 62.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 748.0,
        "median": 843.0,
        "p90": 886.0,
        "p95": 886.0,
        "max": 1108.0
      }
    }
  },
  {
    "scenario": "single-dependency",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 6.859,
    "throughput_per_second": 1.75,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.703,
      "median": 4.516,
      "p90": 6.797,
      "p95": 6.797,
      "max": 6.859
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.344,
      "p90": 0.359,
      "p95": 0.359,
      "max": 0.391
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 683.0,
        "median": 765.5,
        "p90": 826.0,
        "p95": 826.0,
        "max": 923.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 740.0,
        "median": 827.5,
        "p90": 883.0,
        "p95": 883.0,
        "max": 987.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
        "p90": 13.0,
        "p95": 13.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 163.0,
        "median": 175.0,
        "p90": 204.0,
        "p95": 204.0,
        "max": 208.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 355.0,
        "p90": 390.0,
        "p95": 390.0,
        "max": 399.0
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
        "min": 495.0,
        "median": 534.5,
        "p90": 599.0,
        "p95": 599.0,
        "max": 604.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 36.5,
        "p90": 145.0,
        "p95": 145.0,
        "max": 197.0
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
        "min": 588.0,
        "median": 632.0,
        "p90": 707.0,
        "p95": 707.0,
        "max": 716.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 65.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 752.0,
        "median": 845.5,
        "p90": 897.0,
        "p95": 897.0,
        "max": 1006.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 15.5,
    "throughput_per_second": 0.774,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 2.078,
      "p90": 2.703,
      "p95": 2.703,
      "max": 2.797
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.547,
      "p95": 0.547,
      "max": 0.657
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.156,
      "p90": 0.296,
      "p95": 0.296,
      "max": 0.546
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
        "min": 224.0,
        "median": 243.5,
        "p90": 274.0,
        "p95": 274.0,
        "max": 298.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 36.0,
        "p95": 36.0,
        "max": 157.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 504.0,
        "median": 559.0,
        "p90": 823.0,
        "p95": 823.0,
        "max": 1029.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 830.0,
        "median": 909.5,
        "p90": 1164.0,
        "p95": 1164.0,
        "max": 1405.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
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
        "min": 33.0,
        "median": 37.5,
        "p90": 43.0,
        "p95": 43.0,
        "max": 50.0
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
        "median": 353.5,
        "p90": 395.0,
        "p95": 395.0,
        "max": 402.0
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
        "median": 354.5,
        "p90": 396.0,
        "p95": 396.0,
        "max": 403.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 25.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 58.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 250.0,
        "median": 272.0,
        "p90": 294.0,
        "p95": 294.0,
        "max": 294.0
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
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 416.0,
        "median": 446.5,
        "p90": 496.0,
        "p95": 496.0,
        "max": 503.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 82.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 842.0,
        "median": 926.5,
        "p90": 1177.0,
        "p95": 1177.0,
        "max": 1418.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 11.938,
    "throughput_per_second": 1.005,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.485,
      "p90": 1.516,
      "p95": 1.516,
      "max": 2.625
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
      "median": 0.157,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.188
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
        "min": 223.0,
        "median": 240.5,
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
        "max": 0.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 501.0,
        "median": 519.0,
        "p90": 587.0,
        "p95": 587.0,
        "max": 587.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 816.0,
        "median": 862.0,
        "p90": 954.0,
        "p95": 954.0,
        "max": 956.0
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
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 40.5,
        "p90": 46.0,
        "p95": 46.0,
        "max": 49.0
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
        "min": 329.0,
        "median": 340.0,
        "p90": 390.0,
        "p95": 390.0,
        "max": 395.0
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
        "min": 330.0,
        "median": 341.0,
        "p90": 390.0,
        "p95": 390.0,
        "max": 396.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 25.0,
        "p90": 29.0,
        "p95": 29.0,
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
        "min": 412.0,
        "median": 427.0,
        "p90": 488.0,
        "p95": 488.0,
        "max": 492.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 82.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 828.0,
        "median": 873.5,
        "p90": 966.0,
        "p95": 966.0,
        "max": 976.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 13.547,
    "throughput_per_second": 0.886,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.5,
      "p90": 2.641,
      "p95": 2.641,
      "max": 2.75
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.407,
      "p95": 0.407,
      "max": 0.437
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.187
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
        "min": 225.0,
        "median": 234.5,
        "p90": 275.0,
        "p95": 275.0,
        "max": 280.0
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 514.0,
        "median": 553.5,
        "p90": 596.0,
        "p95": 596.0,
        "max": 724.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 838.0,
        "median": 905.5,
        "p90": 1052.0,
        "p95": 1052.0,
        "max": 1105.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.0,
        "p90": 8.0,
        "p95": 8.0,
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
        "min": 33.0,
        "median": 36.0,
        "p90": 59.0,
        "p95": 59.0,
        "max": 204.0
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
        "median": 369.0,
        "p90": 390.0,
        "p95": 390.0,
        "max": 395.0
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
        "median": 370.0,
        "p90": 391.0,
        "p95": 391.0,
        "max": 396.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 25.0,
        "p90": 35.0,
        "p95": 35.0,
        "max": 40.0
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
        "min": 426.0,
        "median": 463.0,
        "p90": 488.0,
        "p95": 488.0,
        "max": 491.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 850.0,
        "median": 923.0,
        "p90": 1065.0,
        "p95": 1065.0,
        "max": 1117.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 8.391,
    "throughput_per_second": 1.43,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.468,
      "median": 1.641,
      "p90": 2.813,
      "p95": 2.813,
      "max": 2.828
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.235
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.453
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
        "min": 224.0,
        "median": 237.5,
        "p90": 280.0,
        "p95": 280.0,
        "max": 282.0
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
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 505.0,
        "median": 557.5,
        "p90": 619.0,
        "p95": 619.0,
        "max": 629.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 830.0,
        "median": 892.5,
        "p90": 1020.0,
        "p95": 1020.0,
        "max": 1025.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 42.0,
        "p90": 58.0,
        "p95": 58.0,
        "max": 60.0
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
        "median": 355.0,
        "p90": 378.0,
        "p95": 378.0,
        "max": 391.0
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
        "median": 356.0,
        "p90": 379.0,
        "p95": 379.0,
        "max": 392.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 33.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 86.0
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
        "min": 418.0,
        "median": 449.0,
        "p90": 479.0,
        "p95": 479.0,
        "max": 491.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 71.0,
        "p95": 71.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 841.0,
        "median": 912.5,
        "p90": 1034.0,
        "p95": 1034.0,
        "max": 1040.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 8.344,
    "throughput_per_second": 1.438,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 2.156,
      "p90": 2.875,
      "p95": 2.875,
      "max": 2.891
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.313,
      "p95": 0.313,
      "max": 0.329
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.164,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.203
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
        "min": 222.0,
        "median": 229.0,
        "p90": 264.0,
        "p95": 264.0,
        "max": 265.0
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 496.0,
        "median": 571.5,
        "p90": 619.0,
        "p95": 619.0,
        "max": 668.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 817.0,
        "median": 907.0,
        "p90": 1007.0,
        "p95": 1007.0,
        "max": 1037.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 40.0,
        "p90": 48.0,
        "p95": 48.0,
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
        "min": 331.0,
        "median": 347.0,
        "p90": 413.0,
        "p95": 413.0,
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
        "min": 331.0,
        "median": 348.0,
        "p90": 413.0,
        "p95": 413.0,
        "max": 441.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 30.5,
        "p90": 59.0,
        "p95": 59.0,
        "max": 66.0
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
        "min": 413.0,
        "median": 451.0,
        "p90": 512.0,
        "p95": 512.0,
        "max": 548.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 88.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 826.0,
        "median": 924.0,
        "p90": 1023.0,
        "p95": 1023.0,
        "max": 1051.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 9.204,
    "throughput_per_second": 1.304,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.563,
      "median": 2.382,
      "p90": 3.204,
      "p95": 3.204,
      "max": 3.25
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.211,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.359
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.343,
      "p95": 0.343,
      "max": 0.375
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
        "min": 228.0,
        "median": 246.0,
        "p90": 273.0,
        "p95": 273.0,
        "max": 295.0
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
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 513.0,
        "median": 563.0,
        "p90": 609.0,
        "p95": 609.0,
        "max": 659.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 849.0,
        "median": 930.5,
        "p90": 989.0,
        "p95": 989.0,
        "max": 1073.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 46.5,
        "p90": 60.0,
        "p95": 60.0,
        "max": 94.0
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
        "median": 353.0,
        "p90": 401.0,
        "p95": 401.0,
        "max": 420.0
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
        "median": 354.0,
        "p90": 402.0,
        "p95": 402.0,
        "max": 421.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 25.0,
        "median": 41.0,
        "p90": 57.0,
        "p95": 57.0,
        "max": 63.0
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
        "min": 423.0,
        "median": 449.5,
        "p90": 496.0,
        "p95": 496.0,
        "max": 539.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 62.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 866.0,
        "median": 952.0,
        "p90": 1006.0,
        "p95": 1006.0,
        "max": 1087.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 8.391,
    "throughput_per_second": 1.43,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.594,
      "median": 3.984,
      "p90": 5.172,
      "p95": 5.172,
      "max": 5.359
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.196,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.609
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.171,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.203
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
        "min": 223.0,
        "median": 234.5,
        "p90": 267.0,
        "p95": 267.0,
        "max": 285.0
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 499.0,
        "median": 555.0,
        "p90": 629.0,
        "p95": 629.0,
        "max": 636.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 824.0,
        "median": 903.5,
        "p90": 994.0,
        "p95": 994.0,
        "max": 1053.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 37.5,
        "p90": 53.0,
        "p95": 53.0,
        "max": 81.0
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
        "min": 330.0,
        "median": 339.5,
        "p90": 395.0,
        "p95": 395.0,
        "max": 403.0
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
        "min": 331.0,
        "median": 340.5,
        "p90": 396.0,
        "p95": 396.0,
        "max": 404.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 34.5,
        "p90": 83.0,
        "p95": 83.0,
        "max": 89.0
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
        "min": 413.0,
        "median": 429.0,
        "p90": 492.0,
        "p95": 492.0,
        "max": 512.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 83.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 836.0,
        "median": 922.5,
        "p90": 1006.0,
        "p95": 1006.0,
        "max": 1066.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 7.921,
    "throughput_per_second": 1.515,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.062,
      "median": 3.922,
      "p90": 5.89,
      "p95": 5.89,
      "max": 5.984
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.648,
      "p90": 0.734,
      "p95": 0.734,
      "max": 0.734
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.18,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
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
        "min": 227.0,
        "median": 249.5,
        "p90": 271.0,
        "p95": 271.0,
        "max": 278.0
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
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 517.0,
        "median": 554.0,
        "p90": 630.0,
        "p95": 630.0,
        "max": 635.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 869.0,
        "median": 912.5,
        "p90": 1047.0,
        "p95": 1047.0,
        "max": 1055.0
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
        "min": 5.0,
        "median": 7.0,
        "p90": 17.0,
        "p95": 17.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 42.0,
        "p90": 85.0,
        "p95": 85.0,
        "max": 159.0
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
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 335.0,
        "median": 354.5,
        "p90": 417.0,
        "p95": 417.0,
        "max": 419.0
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
        "median": 355.5,
        "p90": 418.0,
        "p95": 418.0,
        "max": 420.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 37.0,
        "p90": 57.0,
        "p95": 57.0,
        "max": 63.0
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
        "min": 420.0,
        "median": 445.5,
        "p90": 519.0,
        "p95": 519.0,
        "max": 522.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 58.0,
        "median": 64.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 57.0,
        "median": 61.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 884.0,
        "median": 933.0,
        "p90": 1063.0,
        "p95": 1063.0,
        "max": 1074.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 7.766,
    "throughput_per_second": 1.545,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.547,
      "median": 3.883,
      "p90": 5.344,
      "p95": 5.344,
      "max": 5.453
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.266,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.359
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.297
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
        "min": 223.0,
        "median": 236.5,
        "p90": 279.0,
        "p95": 279.0,
        "max": 282.0
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
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 510.0,
        "median": 542.0,
        "p90": 646.0,
        "p95": 646.0,
        "max": 654.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 832.0,
        "median": 891.5,
        "p90": 1041.0,
        "p95": 1041.0,
        "max": 1052.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 36.5,
        "p90": 48.0,
        "p95": 48.0,
        "max": 61.0
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
        "median": 354.0,
        "p90": 401.0,
        "p95": 401.0,
        "max": 436.0
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
        "median": 355.0,
        "p90": 402.0,
        "p95": 402.0,
        "max": 437.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 31.0,
        "p90": 85.0,
        "p95": 85.0,
        "max": 86.0
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
        "min": 422.0,
        "median": 448.5,
        "p90": 504.0,
        "p95": 504.0,
        "max": 540.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 63.0,
        "p90": 76.0,
        "p95": 76.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 93.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 852.0,
        "median": 905.0,
        "p90": 1060.0,
        "p95": 1060.0,
        "max": 1062.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 9.562,
    "throughput_per_second": 1.255,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.796,
      "median": 4.992,
      "p90": 8.031,
      "p95": 8.031,
      "max": 9.25
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.289,
      "p90": 0.671,
      "p95": 0.671,
      "max": 0.672
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.375
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
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
        "min": 225.0,
        "median": 241.5,
        "p90": 259.0,
        "p95": 259.0,
        "max": 269.0
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
        "median": 3.5,
        "p90": 4.0,
        "p95": 4.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 509.0,
        "median": 568.5,
        "p90": 598.0,
        "p95": 598.0,
        "max": 679.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 841.0,
        "median": 932.5,
        "p90": 1011.0,
        "p95": 1011.0,
        "max": 1066.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 47.0,
        "p90": 86.0,
        "p95": 86.0,
        "max": 152.0
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
        "median": 374.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 395.0
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
        "median": 375.0,
        "p90": 394.0,
        "p95": 394.0,
        "max": 396.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 26.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 81.0
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
        "min": 417.0,
        "median": 469.0,
        "p90": 493.0,
        "p95": 493.0,
        "max": 512.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 63.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 62.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 858.0,
        "median": 947.5,
        "p90": 1021.0,
        "p95": 1021.0,
        "max": 1088.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 8.11,
    "throughput_per_second": 1.48,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.969,
      "median": 4.586,
      "p90": 7.375,
      "p95": 7.375,
      "max": 7.407
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.282,
      "median": 0.5,
      "p90": 0.547,
      "p95": 0.547,
      "max": 0.61
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.226,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.375
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
        "min": 223.0,
        "median": 238.0,
        "p90": 254.0,
        "p95": 254.0,
        "max": 263.0
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
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 511.0,
        "median": 567.0,
        "p90": 662.0,
        "p95": 662.0,
        "max": 700.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 834.0,
        "median": 924.0,
        "p90": 1041.0,
        "p95": 1041.0,
        "max": 1045.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 36.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 79.0
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
        "median": 354.5,
        "p90": 428.0,
        "p95": 428.0,
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
        "median": 355.5,
        "p90": 429.0,
        "p95": 429.0,
        "max": 446.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 39.0,
        "p90": 76.0,
        "p95": 76.0,
        "max": 88.0
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
        "min": 422.0,
        "median": 447.0,
        "p90": 542.0,
        "p95": 542.0,
        "max": 556.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 848.0,
        "median": 941.0,
        "p90": 1062.0,
        "p95": 1062.0,
        "max": 1077.0
      }
    }
  },
  {
    "scenario": "single-output",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 8.281,
    "throughput_per_second": 1.449,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.172,
      "median": 5.211,
      "p90": 6.859,
      "p95": 6.859,
      "max": 7.937
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.336,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.593
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.156,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.203
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
        "min": 226.0,
        "median": 242.5,
        "p90": 266.0,
        "p95": 266.0,
        "max": 293.0
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 518.0,
        "median": 549.0,
        "p90": 573.0,
        "p95": 573.0,
        "max": 643.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 844.0,
        "median": 905.5,
        "p90": 965.0,
        "p95": 965.0,
        "max": 1035.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 14.0,
        "p95": 14.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 38.0,
        "p90": 101.0,
        "p95": 101.0,
        "max": 104.0
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
        "max": 2.0
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
        "min": 333.0,
        "median": 344.0,
        "p90": 380.0,
        "p95": 380.0,
        "max": 381.0
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
        "median": 344.5,
        "p90": 381.0,
        "p95": 381.0,
        "max": 382.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 38.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 148.0
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
        "min": 418.0,
        "median": 435.0,
        "p90": 472.0,
        "p95": 472.0,
        "max": 472.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.5,
        "p90": 62.0,
        "p95": 62.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.0,
        "p90": 61.0,
        "p95": 61.0,
        "max": 65.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 856.0,
        "median": 923.0,
        "p90": 990.0,
        "p95": 990.0,
        "max": 1051.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 15.703,
    "throughput_per_second": 0.764,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 1.82,
      "p90": 2.703,
      "p95": 2.703,
      "max": 2.719
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.195,
      "p90": 0.719,
      "p95": 0.719,
      "max": 0.734
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.468
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
        "min": 225.0,
        "median": 236.0,
        "p90": 265.0,
        "p95": 265.0,
        "max": 267.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 38.0,
        "max": 135.0
      },
      "docker_input_copy_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 525.0,
        "median": 577.0,
        "p90": 964.0,
        "p95": 964.0,
        "max": 988.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 861.0,
        "median": 943.0,
        "p90": 1295.0,
        "p95": 1295.0,
        "max": 1334.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
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
        "min": 33.0,
        "median": 38.5,
        "p90": 57.0,
        "p95": 57.0,
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
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 335.0,
        "median": 343.0,
        "p90": 384.0,
        "p95": 384.0,
        "max": 393.0
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
        "median": 344.0,
        "p90": 385.0,
        "p95": 385.0,
        "max": 394.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 50.5,
        "p90": 125.0,
        "p95": 125.0,
        "max": 150.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 282.0,
        "median": 309.0,
        "p90": 336.0,
        "p95": 336.0,
        "max": 336.0
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
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 417.0,
        "median": 432.0,
        "p90": 479.0,
        "p95": 479.0,
        "max": 489.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 61.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 874.0,
        "median": 962.0,
        "p90": 1304.0,
        "p95": 1304.0,
        "max": 1352.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 15.39,
    "throughput_per_second": 0.78,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 1.633,
      "p90": 2.703,
      "p95": 2.703,
      "max": 2.719
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.359
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.203
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
        "min": 224.0,
        "median": 238.0,
        "p90": 276.0,
        "p95": 276.0,
        "max": 320.0
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
        "median": 4.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 518.0,
        "median": 579.0,
        "p90": 629.0,
        "p95": 629.0,
        "max": 661.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 846.0,
        "median": 929.0,
        "p90": 1028.0,
        "p95": 1028.0,
        "max": 1049.0
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
        "median": 8.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 25.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 39.5,
        "p90": 49.0,
        "p95": 49.0,
        "max": 83.0
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
        "min": 333.0,
        "median": 368.0,
        "p90": 399.0,
        "p95": 399.0,
        "max": 429.0
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
        "median": 369.0,
        "p90": 400.0,
        "p95": 400.0,
        "max": 430.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 38.0,
        "median": 49.0,
        "p90": 60.0,
        "p95": 60.0,
        "max": 63.0
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
        "median": 465.0,
        "p90": 501.0,
        "p95": 501.0,
        "max": 541.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 64.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 861.0,
        "median": 940.5,
        "p90": 1064.0,
        "p95": 1064.0,
        "max": 1068.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 13.421,
    "throughput_per_second": 0.894,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.485,
      "median": 1.562,
      "p90": 2.672,
      "p95": 2.672,
      "max": 2.687
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.187,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.219
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "min": 224.0,
        "median": 232.5,
        "p90": 276.0,
        "p95": 276.0,
        "max": 292.0
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
        "min": 4.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 547.0,
        "median": 572.0,
        "p90": 610.0,
        "p95": 610.0,
        "max": 621.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 866.0,
        "median": 920.0,
        "p90": 998.0,
        "p95": 998.0,
        "max": 1006.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 14.0,
        "p95": 14.0,
        "max": 16.0
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
        "min": 32.0,
        "median": 37.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 52.0
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
        "median": 340.5,
        "p90": 346.0,
        "p95": 346.0,
        "max": 395.0
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
        "median": 341.5,
        "p90": 347.0,
        "p95": 347.0,
        "max": 396.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 43.0,
        "median": 63.5,
        "p90": 92.0,
        "p95": 92.0,
        "max": 95.0
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
        "min": 422.0,
        "median": 438.5,
        "p90": 446.0,
        "p95": 446.0,
        "max": 493.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 61.0,
        "p90": 76.0,
        "p95": 76.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 63.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 84.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 879.0,
        "median": 938.5,
        "p90": 1016.0,
        "p95": 1016.0,
        "max": 1023.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 8.235,
    "throughput_per_second": 1.457,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.485,
      "median": 2.64,
      "p90": 2.797,
      "p95": 2.797,
      "max": 2.875
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.188,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.25
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.235
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
        "min": 226.0,
        "median": 248.0,
        "p90": 274.0,
        "p95": 274.0,
        "max": 277.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 532.0,
        "median": 596.5,
        "p90": 693.0,
        "p95": 693.0,
        "max": 728.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 873.0,
        "median": 966.0,
        "p90": 1055.0,
        "p95": 1055.0,
        "max": 1117.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 38.0,
        "p90": 94.0,
        "p95": 94.0,
        "max": 190.0
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
        "median": 355.5,
        "p90": 386.0,
        "p95": 386.0,
        "max": 397.0
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
        "median": 356.5,
        "p90": 387.0,
        "p95": 387.0,
        "max": 398.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 43.0,
        "median": 73.0,
        "p90": 159.0,
        "p95": 159.0,
        "max": 237.0
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
        "min": 420.0,
        "median": 458.5,
        "p90": 475.0,
        "p95": 475.0,
        "max": 493.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 62.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 62.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 884.0,
        "median": 981.5,
        "p90": 1076.0,
        "p95": 1076.0,
        "max": 1134.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 8.078,
    "throughput_per_second": 1.486,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 2.657,
      "p90": 2.765,
      "p95": 2.765,
      "max": 2.766
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.203,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.234
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.203
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
        "min": 226.0,
        "median": 235.0,
        "p90": 262.0,
        "p95": 262.0,
        "max": 279.0
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
        "min": 519.0,
        "median": 579.5,
        "p90": 603.0,
        "p95": 603.0,
        "max": 669.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 870.0,
        "median": 938.5,
        "p90": 989.0,
        "p95": 989.0,
        "max": 1049.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
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
        "min": 34.0,
        "median": 44.5,
        "p90": 57.0,
        "p95": 57.0,
        "max": 108.0
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
        "min": 333.0,
        "median": 349.0,
        "p90": 380.0,
        "p95": 380.0,
        "max": 390.0
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
        "median": 350.0,
        "p90": 381.0,
        "p95": 381.0,
        "max": 391.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 42.0,
        "median": 57.0,
        "p90": 102.0,
        "p95": 102.0,
        "max": 109.0
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
        "min": 417.0,
        "median": 448.5,
        "p90": 473.0,
        "p95": 473.0,
        "max": 489.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 57.0,
        "median": 64.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 83.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 882.0,
        "median": 951.0,
        "p90": 1004.0,
        "p95": 1004.0,
        "max": 1063.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 8.14,
    "throughput_per_second": 1.474,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.531,
      "median": 2.234,
      "p90": 2.812,
      "p95": 2.812,
      "max": 2.859
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.179,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.234
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
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
        "min": 226.0,
        "median": 236.0,
        "p90": 268.0,
        "p95": 268.0,
        "max": 268.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 523.0,
        "median": 569.5,
        "p90": 653.0,
        "p95": 653.0,
        "max": 658.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 846.0,
        "median": 916.0,
        "p90": 1040.0,
        "p95": 1040.0,
        "max": 1053.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 43.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 97.0
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
        "median": 346.0,
        "p90": 405.0,
        "p95": 405.0,
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
        "min": 336.0,
        "median": 347.0,
        "p90": 406.0,
        "p95": 406.0,
        "max": 408.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 52.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 103.0
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
        "min": 419.0,
        "median": 442.5,
        "p90": 503.0,
        "p95": 503.0,
        "max": 521.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 857.0,
        "median": 929.5,
        "p90": 1059.0,
        "p95": 1059.0,
        "max": 1071.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 9.844,
    "throughput_per_second": 1.219,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.578,
      "median": 4.055,
      "p90": 5.281,
      "p95": 5.281,
      "max": 5.437
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.234,
      "p90": 0.359,
      "p95": 0.359,
      "max": 0.375
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.563
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
        "min": 226.0,
        "median": 240.5,
        "p90": 274.0,
        "p95": 274.0,
        "max": 282.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 525.0,
        "median": 614.5,
        "p90": 646.0,
        "p95": 646.0,
        "max": 658.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 867.0,
        "median": 956.5,
        "p90": 1019.0,
        "p95": 1019.0,
        "max": 1039.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 44.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 96.0
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
        "median": 345.5,
        "p90": 409.0,
        "p95": 409.0,
        "max": 411.0
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
        "median": 346.5,
        "p90": 410.0,
        "p95": 410.0,
        "max": 412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 43.0,
        "median": 57.5,
        "p90": 135.0,
        "p95": 135.0,
        "max": 138.0
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
        "min": 419.0,
        "median": 440.0,
        "p90": 515.0,
        "p95": 515.0,
        "max": 529.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 61.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 84.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 885.0,
        "median": 971.5,
        "p90": 1032.0,
        "p95": 1032.0,
        "max": 1052.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 8.609,
    "throughput_per_second": 1.394,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.531,
      "median": 3.946,
      "p90": 5.328,
      "p95": 5.328,
      "max": 5.375
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.25,
      "p90": 0.313,
      "p95": 0.313,
      "max": 0.313
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.234
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
        "min": 220.0,
        "median": 236.0,
        "p90": 278.0,
        "p95": 278.0,
        "max": 279.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 530.0,
        "median": 564.0,
        "p90": 711.0,
        "p95": 711.0,
        "max": 747.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 857.0,
        "median": 917.5,
        "p90": 1087.0,
        "p95": 1087.0,
        "max": 1128.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 37.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 80.0
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
        "min": 330.0,
        "median": 345.0,
        "p90": 403.0,
        "p95": 403.0,
        "max": 425.0
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
        "min": 331.0,
        "median": 346.0,
        "p90": 404.0,
        "p95": 404.0,
        "max": 426.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 54.5,
        "p90": 138.0,
        "p95": 138.0,
        "max": 199.0
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
        "min": 415.0,
        "median": 443.0,
        "p90": 502.0,
        "p95": 502.0,
        "max": 528.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 875.0,
        "median": 934.0,
        "p90": 1106.0,
        "p95": 1106.0,
        "max": 1143.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 9.453,
    "throughput_per_second": 1.269,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.703,
      "median": 3.656,
      "p90": 4.875,
      "p95": 4.875,
      "max": 6.469
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.282,
      "p90": 0.672,
      "p95": 0.672,
      "max": 0.703
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.359,
      "p90": 0.641,
      "p95": 0.641,
      "max": 0.734
    },
    "workers": {
      "worker-1": 5,
      "worker-2": 7
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
        "min": 223.0,
        "median": 232.0,
        "p90": 255.0,
        "p95": 255.0,
        "max": 263.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 518.0,
        "median": 581.5,
        "p90": 659.0,
        "p95": 659.0,
        "max": 768.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 835.0,
        "median": 951.5,
        "p90": 1025.0,
        "p95": 1025.0,
        "max": 1118.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 37.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 86.0
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
        "min": 333.0,
        "median": 360.5,
        "p90": 390.0,
        "p95": 390.0,
        "max": 406.0
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
        "median": 361.5,
        "p90": 391.0,
        "p95": 391.0,
        "max": 407.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 47.0,
        "p90": 127.0,
        "p95": 127.0,
        "max": 210.0
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
        "median": 456.0,
        "p90": 490.0,
        "p95": 490.0,
        "max": 503.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 61.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 61.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 845.0,
        "median": 964.0,
        "p90": 1038.0,
        "p95": 1038.0,
        "max": 1145.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 8.313,
    "throughput_per_second": 1.444,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.813,
      "median": 4.852,
      "p90": 7.922,
      "p95": 7.922,
      "max": 8.0
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.469,
      "p90": 0.782,
      "p95": 0.782,
      "max": 0.813
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.438
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
        "min": 223.0,
        "median": 240.0,
        "p90": 261.0,
        "p95": 261.0,
        "max": 263.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 539.0,
        "median": 590.5,
        "p90": 755.0,
        "p95": 755.0,
        "max": 789.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 870.0,
        "median": 951.0,
        "p90": 1075.0,
        "p95": 1075.0,
        "max": 1158.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 8.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 45.5,
        "p90": 77.0,
        "p95": 77.0,
        "max": 80.0
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
        "median": 355.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 397.0
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
        "median": 356.0,
        "p90": 394.0,
        "p95": 394.0,
        "max": 398.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 43.0,
        "median": 65.0,
        "p90": 227.0,
        "p95": 227.0,
        "max": 277.0
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
        "min": 418.0,
        "median": 446.0,
        "p90": 493.0,
        "p95": 493.0,
        "max": 494.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 61.5,
        "p90": 69.0,
        "p95": 69.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 885.0,
        "median": 964.0,
        "p90": 1095.0,
        "p95": 1095.0,
        "max": 1175.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 8.703,
    "throughput_per_second": 1.379,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.984,
      "median": 5.023,
      "p90": 7.234,
      "p95": 7.234,
      "max": 8.391
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.218,
      "median": 0.343,
      "p90": 0.547,
      "p95": 0.547,
      "max": 0.547
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.265,
      "p95": 0.265,
      "max": 0.343
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
        "min": 222.0,
        "median": 235.0,
        "p90": 248.0,
        "p95": 248.0,
        "max": 265.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 536.0,
        "median": 620.0,
        "p90": 813.0,
        "p95": 813.0,
        "max": 814.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 869.0,
        "median": 1003.5,
        "p90": 1140.0,
        "p95": 1140.0,
        "max": 1170.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 15.0,
        "p95": 15.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 45.0,
        "p90": 114.0,
        "p95": 114.0,
        "max": 203.0
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
        "median": 375.0,
        "p90": 414.0,
        "p95": 414.0,
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
        "min": 332.0,
        "median": 375.5,
        "p90": 415.0,
        "p95": 415.0,
        "max": 417.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 71.5,
        "p90": 230.0,
        "p95": 230.0,
        "max": 290.0
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
        "min": 414.0,
        "median": 459.5,
        "p90": 515.0,
        "p95": 515.0,
        "max": 519.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 61.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 882.0,
        "median": 1017.5,
        "p90": 1156.0,
        "p95": 1156.0,
        "max": 1189.0
      }
    }
  },
  {
    "scenario": "single-input_output",
    "count": 12,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 8.703,
    "throughput_per_second": 1.379,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.141,
      "median": 5.375,
      "p90": 7.235,
      "p95": 7.235,
      "max": 8.359
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.399,
      "p90": 0.578,
      "p95": 0.578,
      "max": 0.61
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.656,
      "p95": 0.656,
      "max": 0.766
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
        "min": 220.0,
        "median": 237.5,
        "p90": 269.0,
        "p95": 269.0,
        "max": 276.0
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
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 518.0,
        "median": 622.0,
        "p90": 864.0,
        "p95": 864.0,
        "max": 878.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 830.0,
        "median": 966.5,
        "p90": 1239.0,
        "p95": 1239.0,
        "max": 1255.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 13.0,
        "p95": 13.0,
        "max": 19.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 12.0,
        "p95": 12.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 35.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 72.0
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
        "median": 350.0,
        "p90": 400.0,
        "p95": 400.0,
        "max": 413.0
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
        "median": 351.0,
        "p90": 401.0,
        "p95": 401.0,
        "max": 414.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 41.0,
        "median": 80.0,
        "p90": 318.0,
        "p95": 318.0,
        "max": 385.0
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
        "min": 417.0,
        "median": 448.5,
        "p90": 493.0,
        "p95": 493.0,
        "max": 514.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 844.0,
        "median": 980.5,
        "p90": 1272.0,
        "p95": 1272.0,
        "max": 1280.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 14.718,
    "throughput_per_second": 1.019,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 1.609,
      "p90": 2.656,
      "p95": 2.656,
      "max": 2.828
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.204,
      "p95": 0.204,
      "max": 0.453
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.156,
      "median": 0.156,
      "p90": 0.156,
      "p95": 0.156,
      "max": 0.156
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
        "max": 249.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 27.0,
        "p90": 35.0,
        "p95": 35.0,
        "max": 39.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 572.0,
        "median": 816.0,
        "p90": 1829.0,
        "p95": 1829.0,
        "max": 1844.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 630.0,
        "median": 944.0,
        "p90": 1943.0,
        "p95": 1943.0,
        "max": 2033.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 19.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 15.0
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
        "p90": 169.0,
        "p95": 169.0,
        "max": 205.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 332.0,
        "median": 373.0,
        "p90": 397.0,
        "p95": 397.0,
        "max": 423.0
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
        "min": 332.0,
        "median": 394.0,
        "p90": 1336.0,
        "p95": 1336.0,
        "max": 1347.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 25.0,
        "p90": 54.0,
        "p95": 54.0,
        "max": 57.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 212.0,
        "median": 248.5,
        "p90": 299.0,
        "p95": 311.0,
        "max": 311.0
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
        "p90": 138.0,
        "p95": 138.0,
        "max": 142.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 419.0,
        "median": 497.0,
        "p90": 1425.0,
        "p95": 1425.0,
        "max": 1441.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 55.0,
        "median": 61.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 63.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 643.0,
        "median": 955.0,
        "p90": 1955.0,
        "p95": 1955.0,
        "max": 2050.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 15.219,
    "throughput_per_second": 0.986,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.437,
      "median": 1.64,
      "p90": 2.656,
      "p95": 2.656,
      "max": 2.719
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.265,
      "p95": 0.265,
      "max": 0.437
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.156,
      "median": 0.156,
      "p90": 0.156,
      "p95": 0.156,
      "max": 0.156
    },
    "workers": {
      "worker-1": 8,
      "worker-2": 7
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
        "max": 237.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 46.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 513.0,
        "median": 606.0,
        "p90": 1843.0,
        "p95": 1843.0,
        "max": 1894.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 568.0,
        "median": 666.0,
        "p90": 2026.0,
        "p95": 2026.0,
        "max": 2111.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 9.0
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
        "p90": 168.0,
        "p95": 168.0,
        "max": 173.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 339.0,
        "median": 350.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 423.0
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
        "min": 340.0,
        "median": 361.0,
        "p90": 1351.0,
        "p95": 1351.0,
        "max": 1394.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 23.0,
        "p90": 59.0,
        "p95": 59.0,
        "max": 95.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 241.0,
        "median": 265.0,
        "p90": 277.0,
        "p95": 277.0,
        "max": 277.0
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
        "p90": 142.0,
        "p95": 142.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 429.0,
        "median": 448.0,
        "p90": 1444.0,
        "p95": 1444.0,
        "max": 1494.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 56.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 581.0,
        "median": 692.0,
        "p90": 2039.0,
        "p95": 2039.0,
        "max": 2124.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 15.953,
    "throughput_per_second": 0.94,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 1.891,
      "p90": 2.859,
      "p95": 2.859,
      "max": 2.906
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.437,
      "p95": 0.437,
      "max": 0.5
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
        "max": 228.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 31.0,
        "max": 38.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 509.0,
        "median": 564.0,
        "p90": 1823.0,
        "p95": 1823.0,
        "max": 1868.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 563.0,
        "median": 625.0,
        "p90": 2002.0,
        "p95": 2002.0,
        "max": 2010.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 37.0
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
        "max": 177.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 342.0,
        "p90": 389.0,
        "p95": 389.0,
        "max": 389.0
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
        "min": 332.0,
        "median": 363.0,
        "p90": 1342.0,
        "p95": 1342.0,
        "max": 1390.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 28.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 50.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 224.0,
        "median": 247.0,
        "p90": 254.0,
        "p95": 254.0,
        "max": 254.0
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
        "p90": 131.0,
        "p95": 131.0,
        "max": 145.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 422.0,
        "median": 454.0,
        "p90": 1430.0,
        "p95": 1430.0,
        "max": 1488.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 58.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 60.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 574.0,
        "median": 641.0,
        "p90": 2014.0,
        "p95": 2014.0,
        "max": 2023.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 10.75,
    "throughput_per_second": 1.395,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 2.625,
      "p90": 3.89,
      "p95": 3.89,
      "max": 3.938
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.171,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.281
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
        "max": 233.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 514.0,
        "median": 589.0,
        "p90": 1790.0,
        "p95": 1790.0,
        "max": 1876.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 576.0,
        "median": 659.0,
        "p90": 2000.0,
        "p95": 2000.0,
        "max": 2071.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 15.0,
        "p95": 15.0,
        "max": 22.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
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
        "p90": 166.0,
        "p95": 166.0,
        "max": 183.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 332.0,
        "median": 357.0,
        "p90": 386.0,
        "p95": 386.0,
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
        "min": 338.0,
        "median": 386.0,
        "p90": 1358.0,
        "p95": 1358.0,
        "max": 1374.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 20.0,
        "median": 29.0,
        "p90": 50.0,
        "p95": 50.0,
        "max": 78.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 220.0,
        "median": 240.0,
        "p90": 284.0,
        "p95": 284.0,
        "max": 284.0
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
        "p90": 139.0,
        "p95": 139.0,
        "max": 164.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 427.0,
        "median": 480.0,
        "p90": 1445.0,
        "p95": 1445.0,
        "max": 1471.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 61.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 60.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 589.0,
        "median": 674.0,
        "p90": 2012.0,
        "p95": 2012.0,
        "max": 2097.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 11.015,
    "throughput_per_second": 1.362,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 2.672,
      "p90": 3.828,
      "p95": 3.828,
      "max": 4.125
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.188,
      "p90": 0.281,
      "p95": 0.281,
      "max": 0.296
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
    "cold_starts": 6,
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
        "max": 242.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 31.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 506.0,
        "median": 613.0,
        "p90": 1777.0,
        "p95": 1777.0,
        "max": 1821.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 563.0,
        "median": 675.0,
        "p90": 1992.0,
        "p95": 1992.0,
        "max": 2021.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 16.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 41.0
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
        "p90": 167.0,
        "p95": 167.0,
        "max": 180.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 332.0,
        "median": 352.0,
        "p90": 414.0,
        "p95": 414.0,
        "max": 417.0
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
        "median": 397.0,
        "p90": 1340.0,
        "p95": 1340.0,
        "max": 1355.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 31.0,
        "p90": 81.0,
        "p95": 81.0,
        "max": 183.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 212.0,
        "median": 235.0,
        "p90": 257.0,
        "p95": 265.0,
        "max": 265.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 145.0,
        "p95": 145.0,
        "max": 162.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 416.0,
        "median": 499.0,
        "p90": 1431.0,
        "p95": 1431.0,
        "max": 1450.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 61.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 52.0,
        "median": 59.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 574.0,
        "median": 686.0,
        "p90": 2005.0,
        "p95": 2005.0,
        "max": 2047.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 11.828,
    "throughput_per_second": 1.268,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.516,
      "median": 2.766,
      "p90": 3.969,
      "p95": 3.969,
      "max": 4.422
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.75
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
        "max": 235.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 499.0,
        "median": 592.0,
        "p90": 1822.0,
        "p95": 1822.0,
        "max": 1906.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 552.0,
        "median": 663.0,
        "p90": 2024.0,
        "p95": 2024.0,
        "max": 2122.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
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
        "p90": 171.0,
        "p95": 171.0,
        "max": 181.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 351.0,
        "p90": 398.0,
        "p95": 398.0,
        "max": 405.0
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
        "min": 332.0,
        "median": 381.0,
        "p90": 1337.0,
        "p95": 1337.0,
        "max": 1407.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 24.0,
        "p90": 58.0,
        "p95": 58.0,
        "max": 89.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 208.0,
        "median": 244.0,
        "p90": 281.0,
        "p95": 281.0,
        "max": 281.0
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
        "p90": 142.0,
        "p95": 142.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 413.0,
        "median": 471.0,
        "p90": 1425.0,
        "p95": 1425.0,
        "max": 1510.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 59.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 61.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 564.0,
        "median": 678.0,
        "p90": 2033.0,
        "p95": 2033.0,
        "max": 2139.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 10.437,
    "throughput_per_second": 1.437,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.578,
      "median": 4.218,
      "p90": 6.25,
      "p95": 6.25,
      "max": 6.547
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.156,
      "median": 0.218,
      "p90": 0.297,
      "p95": 0.297,
      "max": 0.312
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
      "worker-1": 8,
      "worker-2": 7
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
        "max": 230.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 39.0,
        "p95": 39.0,
        "max": 40.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 502.0,
        "median": 606.0,
        "p90": 1860.0,
        "p95": 1860.0,
        "max": 1889.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 557.0,
        "median": 683.0,
        "p90": 2053.0,
        "p95": 2053.0,
        "max": 2075.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 37.0
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
        "max": 183.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 336.0,
        "median": 355.0,
        "p90": 409.0,
        "p95": 409.0,
        "max": 410.0
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
        "min": 337.0,
        "median": 399.0,
        "p90": 1350.0,
        "p95": 1350.0,
        "max": 1356.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 26.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 73.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 226.0,
        "median": 233.0,
        "p90": 302.0,
        "p95": 302.0,
        "max": 302.0
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
        "p90": 131.0,
        "p95": 131.0,
        "max": 134.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 419.0,
        "median": 507.0,
        "p90": 1442.0,
        "p95": 1442.0,
        "max": 1453.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 61.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 78.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 55.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 571.0,
        "median": 699.0,
        "p90": 2071.0,
        "p95": 2071.0,
        "max": 2088.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 10.687,
    "throughput_per_second": 1.404,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.578,
      "median": 4.234,
      "p90": 6.422,
      "p95": 6.422,
      "max": 6.609
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.156,
      "median": 0.203,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.359
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
    "cold_starts": 4,
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
        "p90": 32.0,
        "p95": 32.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 504.0,
        "median": 606.0,
        "p90": 1771.0,
        "p95": 1771.0,
        "max": 1832.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 560.0,
        "median": 690.0,
        "p90": 1956.0,
        "p95": 1956.0,
        "max": 2022.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
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
        "p90": 169.0,
        "p95": 169.0,
        "max": 192.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 332.0,
        "median": 340.0,
        "p90": 426.0,
        "p95": 426.0,
        "max": 436.0
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
        "median": 417.0,
        "p90": 1342.0,
        "p95": 1342.0,
        "max": 1349.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 29.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 112.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 231.0,
        "median": 242.0,
        "p90": 255.0,
        "p95": 255.0,
        "max": 255.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 130.0,
        "p95": 130.0,
        "max": 136.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 416.0,
        "median": 517.0,
        "p90": 1438.0,
        "p95": 1438.0,
        "max": 1441.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 52.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 52.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 573.0,
        "median": 702.0,
        "p90": 1969.0,
        "p95": 1969.0,
        "max": 2044.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 9.828,
    "throughput_per_second": 1.526,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 2.625,
      "median": 4.125,
      "p90": 5.938,
      "p95": 5.938,
      "max": 5.953
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.688,
      "p90": 1.453,
      "p95": 1.453,
      "max": 1.453
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
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 3,
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
        "max": 224.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 31.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 499.0,
        "median": 574.0,
        "p90": 1606.0,
        "p95": 1606.0,
        "max": 1805.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 555.0,
        "median": 635.0,
        "p90": 1674.0,
        "p95": 1674.0,
        "max": 1988.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 32.0
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
        "max": 211.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 347.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 402.0
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
        "min": 332.0,
        "median": 385.0,
        "p90": 1359.0,
        "p95": 1359.0,
        "max": 1404.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 20.0,
        "median": 28.0,
        "p90": 53.0,
        "p95": 53.0,
        "max": 87.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 219.0,
        "median": 258.0,
        "p90": 259.0,
        "p95": 259.0,
        "max": 259.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 134.0,
        "p95": 134.0,
        "max": 135.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 414.0,
        "median": 483.0,
        "p90": 1454.0,
        "p95": 1454.0,
        "max": 1516.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 58.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 572.0,
        "median": 649.0,
        "p90": 1687.0,
        "p95": 1687.0,
        "max": 2006.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 9.844,
    "throughput_per_second": 1.524,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 2.047,
      "median": 6.063,
      "p90": 9.454,
      "p95": 9.454,
      "max": 9.594
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.219,
      "median": 0.563,
      "p90": 0.86,
      "p95": 0.86,
      "max": 1.016
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
      "worker-1": 8,
      "worker-2": 7
    },
    "cold_starts": 3,
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
        "median": 0.0,
        "p90": 29.0,
        "p95": 29.0,
        "max": 31.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 537.0,
        "median": 603.0,
        "p90": 1775.0,
        "p95": 1775.0,
        "max": 1783.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 593.0,
        "median": 671.0,
        "p90": 1846.0,
        "p95": 1846.0,
        "max": 1993.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 8.0,
        "p90": 13.0,
        "p95": 13.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 39.0
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
        "max": 184.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 367.0,
        "p90": 412.0,
        "p95": 412.0,
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
        "min": 332.0,
        "median": 402.0,
        "p90": 1349.0,
        "p95": 1349.0,
        "max": 1392.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 30.0,
        "p90": 246.0,
        "p95": 246.0,
        "max": 288.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 229.0,
        "median": 246.0,
        "p90": 278.0,
        "p95": 278.0,
        "max": 278.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 128.0,
        "p95": 128.0,
        "max": 139.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 415.0,
        "median": 503.0,
        "p90": 1446.0,
        "p95": 1446.0,
        "max": 1488.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 51.0,
        "median": 63.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 610.0,
        "median": 686.0,
        "p90": 1865.0,
        "p95": 1865.0,
        "max": 2009.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 10.64,
    "throughput_per_second": 1.41,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.812,
      "median": 6.672,
      "p90": 10.547,
      "p95": 10.547,
      "max": 10.64
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.187,
      "median": 0.406,
      "p90": 0.578,
      "p95": 0.578,
      "max": 0.656
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.219,
      "median": 0.219,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.219
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 6,
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
        "max": 261.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 493.0,
        "median": 699.0,
        "p90": 1802.0,
        "p95": 1802.0,
        "max": 1910.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 552.0,
        "median": 754.0,
        "p90": 1985.0,
        "p95": 1985.0,
        "max": 2102.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 5.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 25.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 62.0
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
        "max": 208.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 329.0,
        "median": 359.0,
        "p90": 412.0,
        "p95": 412.0,
        "max": 417.0
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
        "min": 330.0,
        "median": 405.0,
        "p90": 1338.0,
        "p95": 1338.0,
        "max": 1344.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 25.0,
        "p90": 210.0,
        "p95": 210.0,
        "max": 297.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 204.0,
        "median": 235.5,
        "p90": 249.0,
        "p95": 256.0,
        "max": 256.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 129.0,
        "p95": 129.0,
        "max": 135.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 409.0,
        "median": 506.0,
        "p90": 1432.0,
        "p95": 1432.0,
        "max": 1432.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 62.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 61.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 564.0,
        "median": 772.0,
        "p90": 2018.0,
        "p95": 2018.0,
        "max": 2118.0
      }
    }
  },
  {
    "scenario": "mixed-15",
    "count": 15,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 10.609,
    "throughput_per_second": 1.414,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 2.156,
      "median": 6.953,
      "p90": 9.422,
      "p95": 9.422,
      "max": 10.609
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.359,
      "median": 0.625,
      "p90": 0.922,
      "p95": 0.922,
      "max": 0.969
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.438,
      "median": 0.438,
      "p90": 0.438,
      "p95": 0.438,
      "max": 0.438
    },
    "workers": {
      "worker-1": 7,
      "worker-2": 8
    },
    "cold_starts": 3,
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
        "max": 248.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 31.0,
        "max": 33.0
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
        "min": 497.0,
        "median": 629.0,
        "p90": 1665.0,
        "p95": 1665.0,
        "max": 1824.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 557.0,
        "median": 698.0,
        "p90": 1728.0,
        "p95": 1728.0,
        "max": 2005.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 20.0
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
        "p90": 173.0,
        "p95": 173.0,
        "max": 198.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 332.0,
        "median": 351.0,
        "p90": 396.0,
        "p95": 396.0,
        "max": 404.0
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
        "median": 396.0,
        "p90": 1362.0,
        "p95": 1362.0,
        "max": 1364.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 35.0,
        "p90": 101.0,
        "p95": 101.0,
        "max": 348.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 230.0,
        "median": 231.0,
        "p90": 245.0,
        "p95": 245.0,
        "max": 245.0
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
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 127.0,
        "p95": 127.0,
        "max": 137.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 416.0,
        "median": 495.0,
        "p90": 1467.0,
        "p95": 1467.0,
        "max": 1489.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 62.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 63.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 571.0,
        "median": 713.0,
        "p90": 1748.0,
        "p95": 1748.0,
        "max": 2022.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 30.86,
    "throughput_per_second": 0.972,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.438,
      "median": 1.539,
      "p90": 2.813,
      "p95": 2.937,
      "max": 3.141
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.219,
      "p95": 0.296,
      "max": 0.312
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.157,
      "median": 0.157,
      "p90": 0.313,
      "p95": 0.313,
      "max": 0.313
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 6,
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
        "p95": 229.0,
        "max": 281.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 33.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 8.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 496.0,
        "median": 593.0,
        "p90": 1595.0,
        "p95": 1795.0,
        "max": 1811.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 551.0,
        "median": 659.0,
        "p90": 1653.0,
        "p95": 1981.0,
        "max": 2012.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 50.0
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
        "p95": 183.0,
        "max": 190.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 332.0,
        "median": 350.0,
        "p90": 401.0,
        "p95": 404.0,
        "max": 412.0
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
        "median": 391.0,
        "p90": 1365.0,
        "p95": 1389.0,
        "max": 1406.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 26.0,
        "p90": 48.0,
        "p95": 51.0,
        "max": 55.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 222.0,
        "median": 234.0,
        "p90": 244.0,
        "p95": 245.0,
        "max": 245.0
      },
      "warm_container_reused": {
        "count": 24,
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
        "p90": 122.0,
        "p95": 128.0,
        "max": 144.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 412.0,
        "median": 483.0,
        "p90": 1460.0,
        "p95": 1494.0,
        "max": 1518.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 59.0,
        "p90": 64.0,
        "p95": 73.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 60.5,
        "p90": 69.0,
        "p95": 71.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 561.0,
        "median": 671.5,
        "p90": 1666.0,
        "p95": 1997.0,
        "max": 2025.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 32.734,
    "throughput_per_second": 0.916,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.438,
      "median": 1.554,
      "p90": 2.687,
      "p95": 3.813,
      "max": 3.813
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.219,
      "p95": 0.641,
      "max": 0.828
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
      "worker-1": 16,
      "worker-2": 14
    },
    "cold_starts": 7,
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
        "p95": 251.0,
        "max": 266.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 34.0,
        "max": 38.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 505.0,
        "median": 601.0,
        "p90": 1574.0,
        "p95": 1777.0,
        "max": 1801.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 568.0,
        "median": 668.5,
        "p90": 1635.0,
        "p95": 1958.0,
        "max": 2003.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 7.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 10.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 34.0,
        "max": 45.0
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
        "p95": 172.0,
        "max": 180.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 349.5,
        "p90": 414.0,
        "p95": 428.0,
        "max": 453.0
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
        "median": 401.0,
        "p90": 1349.0,
        "p95": 1388.0,
        "max": 1455.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 22.0,
        "median": 28.0,
        "p90": 42.0,
        "p95": 49.0,
        "max": 53.0
      },
      "warm_container_create_ms": {
        "count": 7,
        "min": 220.0,
        "median": 242.0,
        "p90": 245.0,
        "p95": 249.0,
        "max": 249.0
      },
      "warm_container_reused": {
        "count": 23,
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
        "p90": 126.0,
        "p95": 133.0,
        "max": 136.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 415.0,
        "median": 500.5,
        "p90": 1439.0,
        "p95": 1485.0,
        "max": 1547.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 60.0,
        "p90": 69.0,
        "p95": 71.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.5,
        "p90": 66.0,
        "p95": 71.0,
        "max": 87.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 579.0,
        "median": 679.5,
        "p90": 1647.0,
        "p95": 1972.0,
        "max": 2015.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 32.469,
    "throughput_per_second": 0.924,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.469,
      "median": 1.82,
      "p90": 2.719,
      "p95": 3.468,
      "max": 3.579
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.203,
      "p95": 0.5,
      "max": 0.547
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.141,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 14,
      "worker-2": 16
    },
    "cold_starts": 8,
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
        "p95": 263.0,
        "max": 266.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 28.0,
        "p95": 32.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 503.0,
        "median": 593.0,
        "p90": 1554.0,
        "p95": 1804.0,
        "max": 1838.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 558.0,
        "median": 665.5,
        "p90": 1616.0,
        "p95": 1979.0,
        "max": 2043.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 9.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 41.0,
        "max": 52.0
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
        "p95": 168.0,
        "max": 169.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 346.0,
        "p90": 404.0,
        "p95": 413.0,
        "max": 465.0
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
        "median": 395.0,
        "p90": 1346.0,
        "p95": 1349.0,
        "max": 1373.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 27.0,
        "p90": 48.0,
        "p95": 52.0,
        "max": 59.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 212.0,
        "median": 242.0,
        "p90": 264.0,
        "p95": 264.0,
        "max": 264.0
      },
      "warm_container_reused": {
        "count": 22,
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
        "p90": 121.0,
        "p95": 131.0,
        "max": 144.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 415.0,
        "median": 497.5,
        "p90": 1435.0,
        "p95": 1440.0,
        "max": 1472.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 70.0,
        "max": 83.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 60.5,
        "p90": 66.0,
        "p95": 76.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 571.0,
        "median": 678.0,
        "p90": 1630.0,
        "p95": 1992.0,
        "max": 2060.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 23.437,
    "throughput_per_second": 1.28,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.469,
      "median": 2.664,
      "p90": 3.891,
      "p95": 4.953,
      "max": 4.969
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.406,
      "p95": 0.468,
      "max": 0.516
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.157,
      "median": 0.375,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.406
    },
    "workers": {
      "worker-1": 14,
      "worker-2": 16
    },
    "cold_starts": 9,
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
        "p95": 250.0,
        "max": 251.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 32.0,
        "p95": 35.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 12.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 498.0,
        "median": 589.0,
        "p90": 1610.0,
        "p95": 1834.0,
        "max": 1858.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 553.0,
        "median": 664.5,
        "p90": 1682.0,
        "p95": 2032.0,
        "max": 2077.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 17.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 39.0,
        "max": 95.0
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
        "p95": 171.0,
        "max": 217.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 331.0,
        "median": 361.5,
        "p90": 410.0,
        "p95": 420.0,
        "max": 432.0
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
        "median": 392.5,
        "p90": 1385.0,
        "p95": 1394.0,
        "max": 1412.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 22.0,
        "median": 28.5,
        "p90": 39.0,
        "p95": 50.0,
        "max": 51.0
      },
      "warm_container_create_ms": {
        "count": 9,
        "min": 215.0,
        "median": 238.0,
        "p90": 263.0,
        "p95": 283.0,
        "max": 283.0
      },
      "warm_container_reused": {
        "count": 21,
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
        "p90": 137.0,
        "p95": 144.0,
        "max": 151.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 414.0,
        "median": 485.0,
        "p90": 1479.0,
        "p95": 1489.0,
        "max": 1511.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 59.5,
        "p90": 68.0,
        "p95": 70.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 67.0,
        "max": 99.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 568.0,
        "median": 683.0,
        "p90": 1698.0,
        "p95": 2045.0,
        "max": 2088.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 20.079,
    "throughput_per_second": 1.494,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.484,
      "median": 2.656,
      "p90": 3.796,
      "p95": 3.843,
      "max": 5.0
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.344,
      "p95": 0.422,
      "max": 0.906
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.188,
      "p90": 1.265,
      "p95": 1.265,
      "max": 1.265
    },
    "workers": {
      "worker-1": 14,
      "worker-2": 16
    },
    "cold_starts": 7,
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
        "p95": 226.0,
        "max": 259.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 35.0,
        "max": 44.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 508.0,
        "median": 594.5,
        "p90": 1550.0,
        "p95": 1783.0,
        "max": 1785.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 564.0,
        "median": 667.5,
        "p90": 1613.0,
        "p95": 1974.0,
        "max": 1977.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 38.0,
        "max": 40.0
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
        "p95": 173.0,
        "max": 175.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 332.0,
        "median": 345.0,
        "p90": 414.0,
        "p95": 418.0,
        "max": 437.0
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
        "median": 397.0,
        "p90": 1341.0,
        "p95": 1351.0,
        "max": 1351.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 27.0,
        "p90": 44.0,
        "p95": 58.0,
        "max": 63.0
      },
      "warm_container_create_ms": {
        "count": 7,
        "min": 213.0,
        "median": 228.0,
        "p90": 237.0,
        "p95": 266.0,
        "max": 266.0
      },
      "warm_container_reused": {
        "count": 23,
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
        "p90": 133.0,
        "p95": 137.0,
        "max": 138.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 419.0,
        "median": 492.0,
        "p90": 1429.0,
        "p95": 1447.0,
        "max": 1453.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.0,
        "p90": 70.0,
        "p95": 79.0,
        "max": 88.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 75.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 577.0,
        "median": 680.0,
        "p90": 1629.0,
        "p95": 1988.0,
        "max": 1993.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 21.406,
    "throughput_per_second": 1.401,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.422,
      "median": 2.523,
      "p90": 3.86,
      "p95": 4.828,
      "max": 5.688
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.187,
      "p90": 0.437,
      "p95": 0.484,
      "max": 0.718
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.157,
      "median": 0.172,
      "p90": 0.234,
      "p95": 0.234,
      "max": 0.234
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 8,
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
        "p95": 234.0,
        "max": 250.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 33.0,
        "max": 38.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 510.0,
        "median": 616.0,
        "p90": 1762.0,
        "p95": 1765.0,
        "max": 1817.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 569.0,
        "median": 692.5,
        "p90": 1944.0,
        "p95": 1951.0,
        "max": 2005.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 13.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
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
        "p95": 175.0,
        "max": 185.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 332.0,
        "median": 355.5,
        "p90": 416.0,
        "p95": 435.0,
        "max": 441.0
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
        "median": 406.5,
        "p90": 1343.0,
        "p95": 1369.0,
        "max": 1395.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 28.5,
        "p90": 61.0,
        "p95": 71.0,
        "max": 107.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 214.0,
        "median": 229.0,
        "p90": 263.0,
        "p95": 355.0,
        "max": 355.0
      },
      "warm_container_reused": {
        "count": 22,
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
        "p90": 128.0,
        "p95": 129.0,
        "max": 130.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 422.0,
        "median": 508.5,
        "p90": 1432.0,
        "p95": 1491.0,
        "max": 1497.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 62.5,
        "p90": 72.0,
        "p95": 75.0,
        "max": 89.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 61.5,
        "p90": 80.0,
        "p95": 82.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 584.0,
        "median": 707.0,
        "p90": 1956.0,
        "p95": 1968.0,
        "max": 2022.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 19.391,
    "throughput_per_second": 1.547,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.672,
      "median": 4.156,
      "p90": 6.203,
      "p95": 6.344,
      "max": 6.359
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.407,
      "p95": 0.407,
      "max": 0.531
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.187,
      "median": 0.187,
      "p90": 0.204,
      "p95": 0.204,
      "max": 0.204
    },
    "workers": {
      "worker-1": 14,
      "worker-2": 16
    },
    "cold_starts": 7,
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
        "p95": 225.0,
        "max": 260.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 39.0,
        "max": 41.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 15.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 506.0,
        "median": 605.5,
        "p90": 1643.0,
        "p95": 1776.0,
        "max": 1837.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 562.0,
        "median": 687.5,
        "p90": 1701.0,
        "p95": 1973.0,
        "max": 2017.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 42.0,
        "max": 77.0
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
        "p95": 207.0,
        "max": 231.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 335.0,
        "median": 354.0,
        "p90": 415.0,
        "p95": 422.0,
        "max": 440.0
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
        "median": 391.5,
        "p90": 1343.0,
        "p95": 1411.0,
        "max": 1423.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 22.0,
        "median": 28.5,
        "p90": 59.0,
        "p95": 64.0,
        "max": 116.0
      },
      "warm_container_create_ms": {
        "count": 7,
        "min": 228.0,
        "median": 255.0,
        "p90": 260.0,
        "p95": 263.0,
        "max": 263.0
      },
      "warm_container_reused": {
        "count": 23,
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
        "p90": 129.0,
        "p95": 136.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 420.0,
        "median": 488.5,
        "p90": 1437.0,
        "p95": 1507.0,
        "max": 1522.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 55.0,
        "median": 63.0,
        "p90": 68.0,
        "p95": 78.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 70.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 582.0,
        "median": 705.0,
        "p90": 1719.0,
        "p95": 1986.0,
        "max": 2030.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 19.453,
    "throughput_per_second": 1.542,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.469,
      "median": 4.25,
      "p90": 7.375,
      "p95": 8.578,
      "max": 8.734
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.406,
      "p95": 0.422,
      "max": 0.484
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.187,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.219
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 6,
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
        "p95": 231.0,
        "max": 244.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 35.0
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
        "min": 510.0,
        "median": 614.0,
        "p90": 1607.0,
        "p95": 1652.0,
        "max": 1769.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 567.0,
        "median": 762.0,
        "p90": 1669.0,
        "p95": 1726.0,
        "max": 1824.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 13.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 42.0,
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
        "p95": 180.0,
        "max": 216.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 334.0,
        "median": 351.5,
        "p90": 411.0,
        "p95": 418.0,
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
        "min": 335.0,
        "median": 368.5,
        "p90": 1365.0,
        "p95": 1412.0,
        "max": 1418.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 31.5,
        "p90": 62.0,
        "p95": 79.0,
        "max": 107.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 222.0,
        "median": 235.0,
        "p90": 243.0,
        "p95": 251.0,
        "max": 251.0
      },
      "warm_container_reused": {
        "count": 24,
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
        "p90": 134.0,
        "p95": 144.0,
        "max": 144.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 417.0,
        "median": 463.5,
        "p90": 1460.0,
        "p95": 1518.0,
        "max": 1528.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 60.5,
        "p90": 69.0,
        "p95": 73.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 62.0,
        "p90": 68.0,
        "p95": 77.0,
        "max": 84.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 579.0,
        "median": 776.5,
        "p90": 1685.0,
        "p95": 1740.0,
        "max": 1841.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 8,
    "saturation_concurrency": 8,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 17.765,
    "throughput_per_second": 1.689,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.328,
      "median": 3.914,
      "p90": 6.141,
      "p95": 6.281,
      "max": 7.297
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.734,
      "p95": 0.937,
      "max": 1.031
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.188,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.406
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 7,
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
        "p95": 270.0,
        "max": 274.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 33.0,
        "p95": 39.0,
        "max": 41.0
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
        "min": 501.0,
        "median": 615.0,
        "p90": 1637.0,
        "p95": 1777.0,
        "max": 1806.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 559.0,
        "median": 681.0,
        "p90": 1699.0,
        "p95": 1964.0,
        "max": 1995.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 12.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 42.0,
        "max": 51.0
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
        "p95": 167.0,
        "max": 189.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 331.0,
        "median": 352.5,
        "p90": 420.0,
        "p95": 429.0,
        "max": 441.0
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
        "median": 413.5,
        "p90": 1345.0,
        "p95": 1352.0,
        "max": 1430.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 30.0,
        "p90": 47.0,
        "p95": 50.0,
        "max": 66.0
      },
      "warm_container_create_ms": {
        "count": 7,
        "min": 218.0,
        "median": 242.0,
        "p90": 252.0,
        "p95": 253.0,
        "max": 253.0
      },
      "warm_container_reused": {
        "count": 23,
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
        "p90": 132.0,
        "p95": 142.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 416.0,
        "median": 510.0,
        "p90": 1437.0,
        "p95": 1447.0,
        "max": 1536.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 61.0,
        "p90": 70.0,
        "p95": 78.0,
        "max": 82.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 60.0,
        "p90": 67.0,
        "p95": 79.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 571.0,
        "median": 694.5,
        "p90": 1712.0,
        "p95": 1986.0,
        "max": 2010.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 18.078,
    "throughput_per_second": 1.659,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.125,
      "median": 8.242,
      "p90": 9.718,
      "p95": 10.515,
      "max": 11.547
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.187,
      "median": 0.484,
      "p90": 0.719,
      "p95": 0.75,
      "max": 0.797
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.312,
      "p90": 0.563,
      "p95": 0.563,
      "max": 0.563
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 8,
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
        "p95": 232.0,
        "max": 271.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 34.0,
        "p95": 39.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 7.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 511.0,
        "median": 634.0,
        "p90": 1616.0,
        "p95": 1804.0,
        "max": 1841.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 567.0,
        "median": 705.5,
        "p90": 1676.0,
        "p95": 2001.0,
        "max": 2031.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 15.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 154.0,
        "max": 219.0
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
        "p95": 202.0,
        "max": 212.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 335.0,
        "median": 355.0,
        "p90": 412.0,
        "p95": 420.0,
        "max": 421.0
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
        "median": 384.5,
        "p90": 1366.0,
        "p95": 1378.0,
        "max": 1409.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 22.0,
        "median": 35.5,
        "p90": 75.0,
        "p95": 209.0,
        "max": 361.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 226.0,
        "median": 245.5,
        "p90": 250.0,
        "p95": 251.0,
        "max": 251.0
      },
      "warm_container_reused": {
        "count": 22,
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
        "p90": 131.0,
        "p95": 135.0,
        "max": 144.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 421.0,
        "median": 482.5,
        "p90": 1451.0,
        "p95": 1468.0,
        "max": 1512.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 60.0,
        "p90": 68.0,
        "p95": 73.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 55.0,
        "median": 63.0,
        "p90": 77.0,
        "p95": 87.0,
        "max": 90.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 577.0,
        "median": 721.0,
        "p90": 1690.0,
        "p95": 2013.0,
        "max": 2044.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 17.265,
    "throughput_per_second": 1.738,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 3.14,
      "median": 7.648,
      "p90": 9.719,
      "p95": 9.938,
      "max": 10.172
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.156,
      "median": 0.406,
      "p90": 0.937,
      "p95": 1.234,
      "max": 1.234
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.157,
      "median": 0.172,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.375
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 7,
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
        "p95": 246.0,
        "max": 253.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 33.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 508.0,
        "median": 663.5,
        "p90": 1749.0,
        "p95": 1783.0,
        "max": 1824.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 564.0,
        "median": 729.0,
        "p90": 1813.0,
        "p95": 1986.0,
        "max": 2018.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 197.0,
        "max": 210.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 386.5,
        "p90": 414.0,
        "p95": 419.0,
        "max": 446.0
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
        "min": 330.0,
        "median": 401.0,
        "p90": 1365.0,
        "p95": 1403.0,
        "max": 1417.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 44.5,
        "p90": 91.0,
        "p95": 133.0,
        "max": 188.0
      },
      "warm_container_create_ms": {
        "count": 7,
        "min": 223.0,
        "median": 241.0,
        "p90": 249.0,
        "p95": 256.0,
        "max": 256.0
      },
      "warm_container_reused": {
        "count": 23,
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
        "p90": 135.0,
        "p95": 140.0,
        "max": 143.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 410.0,
        "median": 503.5,
        "p90": 1450.0,
        "p95": 1501.0,
        "max": 1520.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 62.0,
        "p90": 66.0,
        "p95": 73.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 55.0,
        "median": 61.0,
        "p90": 69.0,
        "p95": 70.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 574.0,
        "median": 746.5,
        "p90": 1830.0,
        "p95": 2003.0,
        "max": 2031.0
      }
    }
  },
  {
    "scenario": "mixed-30",
    "count": 30,
    "concurrency": 16,
    "saturation_concurrency": 16,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 3,
    "wall_seconds": 18.468,
    "throughput_per_second": 1.624,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.968,
      "median": 8.563,
      "p90": 10.672,
      "p95": 11.031,
      "max": 11.125
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.156,
      "median": 0.328,
      "p90": 0.672,
      "p95": 0.688,
      "max": 0.688
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.203,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.375
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 9,
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
        "p95": 238.0,
        "max": 283.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 36.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 491.0,
        "median": 638.0,
        "p90": 1764.0,
        "p95": 1795.0,
        "max": 1834.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 546.0,
        "median": 709.0,
        "p90": 1937.0,
        "p95": 1976.0,
        "max": 2013.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 11.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 13.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 51.0,
        "max": 104.0
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
        "p95": 180.0,
        "max": 213.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 349.0,
        "p90": 425.0,
        "p95": 430.0,
        "max": 452.0
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
        "min": 330.0,
        "median": 414.0,
        "p90": 1343.0,
        "p95": 1355.0,
        "max": 1405.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 22.0,
        "median": 35.5,
        "p90": 55.0,
        "p95": 128.0,
        "max": 226.0
      },
      "warm_container_create_ms": {
        "count": 9,
        "min": 210.0,
        "median": 236.0,
        "p90": 275.0,
        "p95": 275.0,
        "max": 275.0
      },
      "warm_container_reused": {
        "count": 21,
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
        "p90": 140.0,
        "p95": 146.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 411.0,
        "median": 519.5,
        "p90": 1434.0,
        "p95": 1453.0,
        "max": 1509.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 68.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 62.0,
        "p90": 68.0,
        "p95": 72.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 559.0,
        "median": 721.0,
        "p90": 1953.0,
        "p95": 1991.0,
        "max": 2027.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 91.14,
    "throughput_per_second": 0.878,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.453,
      "median": 1.688,
      "p90": 3.406,
      "p95": 3.828,
      "max": 5.187
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.25,
      "p95": 0.312,
      "max": 1.343
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.171,
      "p90": 0.219,
      "p95": 1.125,
      "max": 1.125
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 41
    },
    "cold_starts": 22,
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
        "p95": 234.0,
        "max": 295.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 32.0,
        "p95": 33.0,
        "max": 41.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 499.0,
        "median": 648.0,
        "p90": 1634.0,
        "p95": 1778.0,
        "max": 1867.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 556.0,
        "median": 717.5,
        "p90": 1697.0,
        "p95": 1971.0,
        "max": 2060.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 36.0,
        "max": 61.0
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
        "p95": 170.0,
        "max": 217.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 331.0,
        "median": 355.0,
        "p90": 441.0,
        "p95": 444.0,
        "max": 484.0
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
        "median": 404.5,
        "p90": 1361.0,
        "p95": 1371.0,
        "max": 1442.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 22.0,
        "median": 26.0,
        "p90": 44.0,
        "p95": 48.0,
        "max": 58.0
      },
      "warm_container_create_ms": {
        "count": 22,
        "min": 208.0,
        "median": 241.5,
        "p90": 265.0,
        "p95": 267.0,
        "max": 285.0
      },
      "warm_container_reused": {
        "count": 58,
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
        "p90": 136.0,
        "p95": 139.0,
        "max": 156.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 414.0,
        "median": 507.5,
        "p90": 1451.0,
        "p95": 1475.0,
        "max": 1548.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 60.0,
        "p90": 69.0,
        "p95": 73.0,
        "max": 82.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 60.0,
        "p90": 70.0,
        "p95": 74.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 571.0,
        "median": 733.5,
        "p90": 1709.0,
        "p95": 1984.0,
        "max": 2074.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 2,
    "saturation_concurrency": 2,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 2,
    "wall_seconds": 86.891,
    "throughput_per_second": 0.921,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.453,
      "median": 1.835,
      "p90": 2.843,
      "p95": 2.953,
      "max": 3.985
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.296,
      "p95": 0.328,
      "max": 1.188
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.141,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
    },
    "workers": {
      "worker-1": 38,
      "worker-2": 42
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
        "p95": 258.0,
        "max": 296.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 34.0,
        "max": 44.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 499.0,
        "median": 624.0,
        "p90": 1578.0,
        "p95": 1638.0,
        "max": 1790.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 555.0,
        "median": 692.0,
        "p90": 1659.0,
        "p95": 1703.0,
        "max": 1966.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 52.0
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
        "p95": 171.0,
        "max": 231.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 332.0,
        "median": 349.5,
        "p90": 423.0,
        "p95": 440.0,
        "max": 467.0
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
        "median": 410.0,
        "p90": 1351.0,
        "p95": 1363.0,
        "max": 1425.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 26.0,
        "p90": 43.0,
        "p95": 50.0,
        "max": 165.0
      },
      "warm_container_create_ms": {
        "count": 20,
        "min": 205.0,
        "median": 229.0,
        "p90": 248.0,
        "p95": 249.0,
        "max": 292.0
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
        "p90": 134.0,
        "p95": 139.0,
        "max": 154.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 413.0,
        "median": 508.5,
        "p90": 1450.0,
        "p95": 1469.0,
        "max": 1541.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.0,
        "p90": 71.0,
        "p95": 74.0,
        "max": 85.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.5,
        "p90": 72.0,
        "p95": 76.0,
        "max": 89.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 566.0,
        "median": 706.0,
        "p90": 1670.0,
        "p95": 1715.0,
        "max": 1980.0
      }
    }
  }
]
```
