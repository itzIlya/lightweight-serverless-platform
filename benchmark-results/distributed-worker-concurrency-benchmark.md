# Distributed Worker Concurrency Benchmark

Generated: 2026-09-01T10:03:43.273991+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- This report varies worker execution concurrency and saturation concurrency.

## Built Functions

- `tiny`: function `42`, version `42`, image `10.42.1.22:5000/functions/bench-tiny-65d2ae92:v42-v1-a1-ebd361172c86-d1`
- `sleep`: function `43`, version `43`, image `10.42.1.22:5000/functions/bench-sleep-15889ba5:v43-v1-a1-16cfa331e70d-d1`
- `dependency`: function `44`, version `44`, image `10.42.1.22:5000/functions/bench-dependency-feceedfa:v44-v1-a1-dcde4dbb0bdf-d1`
- `output`: function `45`, version `45`, image `10.42.1.22:5000/functions/bench-output-39810740:v45-v1-a1-b47ff2b40d15-d1`
- `input_output`: function `46`, version `46`, image `10.42.1.22:5000/functions/bench-input_output-11f17731:v46-v1-a1-d8e19304ec37-d1`

## Run Summary

| Scenario | Count | Worker Invocation Concurrency | Cluster Invocation Capacity | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| single-tiny | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 9.016 | 1.331 | 1.477 | 1.546 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 8.875 | 1.352 | 1.485 | 1.5 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 8.985 | 1.336 | 1.485 | 1.516 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 7.016 | 1.71 | 1.539 | 2.766 | worker-1:5, worker-2:7 |
| single-tiny | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 7.094 | 1.692 | 1.531 | 2.703 | worker-1:5, worker-2:7 |
| single-tiny | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 5.765 | 2.082 | 1.508 | 2.735 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 6.75 | 1.778 | 2.945 | 4.343 | worker-1:5, worker-2:7 |
| single-tiny | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 5.453 | 2.201 | 2.719 | 4.14 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 5.641 | 2.127 | 2.828 | 4.188 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 5.531 | 2.17 | 3.539 | 5.469 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 6.265 | 1.915 | 3.679 | 5.64 | worker-1:6, worker-2:6 |
| single-tiny | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 5.782 | 2.075 | 3.805 | 5.782 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 17.438 | 0.688 | 2.61 | 3.313 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 17.531 | 0.685 | 2.633 | 3.234 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 18.359 | 0.654 | 2.649 | 3.812 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 13.422 | 0.894 | 3.836 | 5.125 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 13.875 | 0.865 | 3.813 | 5.141 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 11.796 | 1.017 | 3.797 | 5.015 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 11.157 | 1.076 | 6.633 | 8.391 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 11.36 | 1.056 | 6.852 | 7.688 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 13.688 | 0.877 | 6.485 | 8.516 | worker-1:5, worker-2:7 |
| single-sleep | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 12.235 | 0.981 | 7.086 | 11.141 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 12.515 | 0.959 | 7.125 | 11.437 | worker-1:6, worker-2:6 |
| single-sleep | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 12.687 | 0.946 | 7.124 | 11.562 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 11.672 | 1.028 | 1.531 | 2.906 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 10.094 | 1.189 | 1.485 | 1.516 | worker-1:5, worker-2:7 |
| single-dependency | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 10.157 | 1.181 | 1.492 | 1.563 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 7.312 | 1.641 | 2.265 | 3.094 | worker-1:5, worker-2:7 |
| single-dependency | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 7.234 | 1.659 | 2.117 | 2.718 | worker-1:5, worker-2:7 |
| single-dependency | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 7.0 | 1.714 | 2.094 | 2.766 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 6.641 | 1.807 | 3.929 | 5.25 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 6.688 | 1.794 | 3.898 | 4.032 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 6.844 | 1.753 | 3.797 | 5.375 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 6.813 | 1.761 | 4.211 | 6.782 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 6.625 | 1.811 | 4.149 | 6.594 | worker-1:6, worker-2:6 |
| single-dependency | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 7.484 | 1.603 | 4.304 | 7.375 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 14.109 | 0.851 | 1.492 | 2.641 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 12.656 | 0.948 | 1.515 | 2.25 | worker-1:5, worker-2:7 |
| single-output | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 13.266 | 0.905 | 1.531 | 2.672 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 7.969 | 1.506 | 2.11 | 2.704 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 8.875 | 1.352 | 2.054 | 2.719 | worker-1:5, worker-2:7 |
| single-output | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 7.797 | 1.539 | 2.078 | 2.703 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 8.281 | 1.449 | 3.914 | 5.156 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 8.187 | 1.466 | 3.945 | 5.281 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 7.313 | 1.641 | 3.789 | 4.14 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 8.016 | 1.497 | 4.727 | 7.11 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 8.484 | 1.414 | 5.164 | 7.187 | worker-1:6, worker-2:6 |
| single-output | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 8.266 | 1.452 | 4.703 | 7.672 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 2 | 1 | 12 | 0 | 15.219 | 0.788 | 2.054 | 2.704 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 2 | 2 | 12 | 0 | 13.281 | 0.904 | 1.524 | 2.672 | worker-1:5, worker-2:7 |
| single-input_output | 12 | 1 | 2 | 2 | 3 | 12 | 0 | 13.047 | 0.92 | 1.625 | 2.687 | worker-1:5, worker-2:7 |
| single-input_output | 12 | 1 | 2 | 4 | 1 | 12 | 0 | 8.735 | 1.374 | 1.789 | 2.891 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 4 | 2 | 12 | 0 | 9.25 | 1.297 | 2.203 | 2.86 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 4 | 3 | 12 | 0 | 11.141 | 1.077 | 2.188 | 3.203 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 8 | 1 | 12 | 0 | 9.735 | 1.233 | 4.266 | 5.547 | worker-1:5, worker-2:7 |
| single-input_output | 12 | 1 | 2 | 8 | 2 | 12 | 0 | 7.703 | 1.558 | 3.86 | 5.203 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 8 | 3 | 12 | 0 | 7.688 | 1.561 | 3.875 | 5.5 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 16 | 1 | 12 | 0 | 7.5 | 1.6 | 4.907 | 6.766 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 16 | 2 | 12 | 0 | 9.312 | 1.289 | 5.75 | 7.5 | worker-1:6, worker-2:6 |
| single-input_output | 12 | 1 | 2 | 16 | 3 | 12 | 0 | 8.641 | 1.389 | 5.18 | 7.188 | worker-1:6, worker-2:6 |
| mixed-15 | 15 | 1 | 2 | 2 | 1 | 15 | 0 | 17.157 | 0.874 | 2.375 | 2.828 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 1 | 2 | 2 | 2 | 15 | 0 | 16.891 | 0.888 | 1.656 | 3.953 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 2 | 3 | 15 | 0 | 18.719 | 0.801 | 1.844 | 3.953 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 4 | 1 | 15 | 0 | 10.328 | 1.452 | 2.656 | 3.782 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 4 | 2 | 15 | 0 | 11.422 | 1.313 | 2.625 | 4.937 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 4 | 3 | 15 | 0 | 12.25 | 1.224 | 2.75 | 4.61 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 8 | 1 | 15 | 0 | 9.531 | 1.574 | 4.454 | 5.688 | worker-1:8, worker-2:7 |
| mixed-15 | 15 | 1 | 2 | 8 | 2 | 15 | 0 | 9.141 | 1.641 | 3.937 | 5.39 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 8 | 3 | 15 | 0 | 10.516 | 1.426 | 4.219 | 6.453 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 16 | 1 | 15 | 0 | 9.219 | 1.627 | 6.657 | 9.125 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 16 | 2 | 15 | 0 | 9.515 | 1.576 | 5.687 | 9.437 | worker-1:7, worker-2:8 |
| mixed-15 | 15 | 1 | 2 | 16 | 3 | 15 | 0 | 10.079 | 1.488 | 6.407 | 9.985 | worker-1:7, worker-2:8 |
| mixed-30 | 30 | 1 | 2 | 2 | 1 | 30 | 0 | 32.156 | 0.933 | 1.751 | 3.219 | worker-1:16, worker-2:14 |
| mixed-30 | 30 | 1 | 2 | 2 | 2 | 30 | 0 | 34.25 | 0.876 | 1.805 | 3.86 | worker-1:13, worker-2:17 |
| mixed-30 | 30 | 1 | 2 | 2 | 3 | 30 | 0 | 30.782 | 0.975 | 1.508 | 2.828 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 4 | 1 | 30 | 0 | 20.047 | 1.496 | 2.617 | 4.171 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 4 | 2 | 30 | 0 | 20.109 | 1.492 | 2.632 | 3.812 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 4 | 3 | 30 | 0 | 21.0 | 1.429 | 2.649 | 3.875 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 8 | 1 | 30 | 0 | 18.063 | 1.661 | 4.172 | 6.078 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 8 | 2 | 30 | 0 | 19.468 | 1.541 | 4.453 | 6.313 | worker-1:14, worker-2:16 |
| mixed-30 | 30 | 1 | 2 | 8 | 3 | 30 | 0 | 18.047 | 1.662 | 3.891 | 5.234 | worker-1:16, worker-2:14 |
| mixed-30 | 30 | 1 | 2 | 16 | 1 | 30 | 0 | 18.172 | 1.651 | 6.718 | 12.25 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 16 | 2 | 30 | 0 | 18.422 | 1.628 | 8.476 | 10.344 | worker-1:15, worker-2:15 |
| mixed-30 | 30 | 1 | 2 | 16 | 3 | 30 | 0 | 18.187 | 1.65 | 8.296 | 10.75 | worker-1:15, worker-2:15 |
| mixed-80 | 80 | 1 | 2 | 2 | 1 | 80 | 0 | 85.312 | 0.938 | 1.562 | 3.329 | worker-1:40, worker-2:40 |
| mixed-80 | 80 | 1 | 2 | 2 | 2 | 80 | 0 | 87.359 | 0.916 | 2.07 | 2.937 | worker-1:38, worker-2:42 |
| mixed-80 | 80 | 1 | 2 | 2 | 3 | 80 | 0 | 82.281 | 0.972 | 1.524 | 3.094 | worker-1:39, worker-2:41 |
| mixed-80 | 80 | 1 | 2 | 4 | 1 | 79 | 1 | 57.0 | 1.386 | 2.625 | 3.875 | worker-1:39, worker-2:40 |

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
    "wall_seconds": 9.016,
    "throughput_per_second": 1.331,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.477,
      "p90": 1.546,
      "p95": 1.546,
      "max": 1.547
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
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
        "p90": 28.0,
        "p95": 28.0,
        "max": 140.0
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
        "min": 502.0,
        "median": 563.5,
        "p90": 896.0,
        "p95": 896.0,
        "max": 935.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 556.0,
        "median": 621.0,
        "p90": 961.0,
        "p95": 961.0,
        "max": 994.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
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
        "min": 336.0,
        "median": 346.5,
        "p90": 401.0,
        "p95": 401.0,
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
        "min": 337.0,
        "median": 346.5,
        "p90": 402.0,
        "p95": 402.0,
        "max": 412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 25.5,
        "p90": 37.0,
        "p95": 37.0,
        "max": 70.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 283.0,
        "median": 292.0,
        "p90": 301.0,
        "p95": 301.0,
        "max": 301.0
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
        "min": 420.0,
        "median": 437.0,
        "p90": 501.0,
        "p95": 501.0,
        "max": 507.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 567.0,
        "median": 639.0,
        "p90": 976.0,
        "p95": 976.0,
        "max": 1010.0
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
    "wall_seconds": 8.875,
    "throughput_per_second": 1.352,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.485,
      "p90": 1.5,
      "p95": 1.5,
      "max": 1.532
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.157,
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
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 529.0,
        "median": 569.0,
        "p90": 633.0,
        "p95": 633.0,
        "max": 653.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 585.0,
        "median": 633.0,
        "p90": 693.0,
        "p95": 693.0,
        "max": 720.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
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
        "min": 331.0,
        "median": 385.0,
        "p90": 424.0,
        "p95": 424.0,
        "max": 437.0
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
        "median": 385.5,
        "p90": 425.0,
        "p95": 425.0,
        "max": 438.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 26.5,
        "p90": 53.0,
        "p95": 53.0,
        "max": 53.0
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
        "median": 474.5,
        "p90": 526.0,
        "p95": 526.0,
        "max": 540.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 60.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 602.0,
        "median": 649.0,
        "p90": 706.0,
        "p95": 706.0,
        "max": 740.0
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
    "wall_seconds": 8.985,
    "throughput_per_second": 1.336,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.438,
      "median": 1.485,
      "p90": 1.516,
      "p95": 1.516,
      "max": 1.562
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.218
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
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 506.0,
        "median": 559.0,
        "p90": 598.0,
        "p95": 598.0,
        "max": 618.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 564.0,
        "median": 625.0,
        "p90": 670.0,
        "p95": 670.0,
        "max": 686.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
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
        "median": 368.0,
        "p90": 403.0,
        "p95": 403.0,
        "max": 405.0
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
        "median": 369.0,
        "p90": 404.0,
        "p95": 404.0,
        "max": 406.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 25.5,
        "p90": 33.0,
        "p95": 33.0,
        "max": 33.0
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
        "median": 463.5,
        "p90": 506.0,
        "p95": 506.0,
        "max": 509.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 63.5,
        "p90": 75.0,
        "p95": 75.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 576.0,
        "median": 635.5,
        "p90": 685.0,
        "p95": 685.0,
        "max": 700.0
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
    "wall_seconds": 7.016,
    "throughput_per_second": 1.71,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.485,
      "median": 1.539,
      "p90": 2.766,
      "p95": 2.766,
      "max": 2.797
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.18,
      "p90": 0.235,
      "p95": 0.235,
      "max": 0.25
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
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 497.0,
        "median": 543.0,
        "p90": 571.0,
        "p95": 571.0,
        "max": 617.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 554.0,
        "median": 607.0,
        "p90": 630.0,
        "p95": 630.0,
        "max": 677.0
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
        "min": 3.0,
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
        "median": 352.5,
        "p90": 386.0,
        "p95": 386.0,
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
        "min": 331.0,
        "median": 353.0,
        "p90": 386.0,
        "p95": 386.0,
        "max": 412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 26.0,
        "p90": 39.0,
        "p95": 39.0,
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
        "min": 412.0,
        "median": 452.5,
        "p90": 478.0,
        "p95": 478.0,
        "max": 507.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 566.0,
        "median": 618.5,
        "p90": 640.0,
        "p95": 640.0,
        "max": 687.0
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
    "wall_seconds": 7.094,
    "throughput_per_second": 1.692,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.531,
      "p90": 2.703,
      "p95": 2.703,
      "max": 2.703
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 496.0,
        "median": 559.5,
        "p90": 593.0,
        "p95": 593.0,
        "max": 606.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 551.0,
        "median": 619.5,
        "p90": 661.0,
        "p95": 661.0,
        "max": 668.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
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
        "min": 331.0,
        "median": 341.0,
        "p90": 387.0,
        "p95": 387.0,
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
        "median": 341.5,
        "p90": 387.0,
        "p95": 387.0,
        "max": 392.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 26.5,
        "p90": 53.0,
        "p95": 53.0,
        "max": 57.0
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
        "median": 436.5,
        "p90": 483.0,
        "p95": 483.0,
        "max": 491.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 58.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 63.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 565.0,
        "median": 634.5,
        "p90": 677.0,
        "p95": 677.0,
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
    "wall_seconds": 5.765,
    "throughput_per_second": 2.082,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.508,
      "p90": 2.735,
      "p95": 2.735,
      "max": 2.796
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.234
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
        "min": 502.0,
        "median": 570.5,
        "p90": 582.0,
        "p95": 582.0,
        "max": 671.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 562.0,
        "median": 633.5,
        "p90": 660.0,
        "p95": 660.0,
        "max": 734.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 37.0
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
        "median": 359.0,
        "p90": 396.0,
        "p95": 396.0,
        "max": 417.0
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
        "median": 359.5,
        "p90": 396.0,
        "p95": 396.0,
        "max": 417.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 25.5,
        "p90": 75.0,
        "p95": 75.0,
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
        "min": 418.0,
        "median": 455.5,
        "p90": 489.0,
        "p95": 489.0,
        "max": 519.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 574.0,
        "median": 648.0,
        "p90": 678.0,
        "p95": 678.0,
        "max": 779.0
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
    "wall_seconds": 6.75,
    "throughput_per_second": 1.778,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.593,
      "median": 2.945,
      "p90": 4.343,
      "p95": 4.343,
      "max": 4.39
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.265,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.422
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
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 518.0,
        "median": 595.5,
        "p90": 672.0,
        "p95": 672.0,
        "max": 764.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 573.0,
        "median": 656.5,
        "p90": 745.0,
        "p95": 745.0,
        "max": 827.0
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
        "p90": 15.0,
        "p95": 15.0,
        "max": 20.0
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
        "median": 351.5,
        "p90": 401.0,
        "p95": 401.0,
        "max": 405.0
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
        "median": 352.5,
        "p90": 401.0,
        "p95": 401.0,
        "max": 406.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 43.5,
        "p90": 163.0,
        "p95": 163.0,
        "max": 182.0
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
        "p90": 500.0,
        "p95": 500.0,
        "max": 507.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.5,
        "p90": 79.0,
        "p95": 79.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 584.0,
        "median": 672.0,
        "p90": 759.0,
        "p95": 759.0,
        "max": 846.0
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
    "wall_seconds": 5.453,
    "throughput_per_second": 2.201,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.609,
      "median": 2.719,
      "p90": 4.14,
      "p95": 4.14,
      "max": 4.172
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.211,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.406
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
        "min": 495.0,
        "median": 557.5,
        "p90": 738.0,
        "p95": 738.0,
        "max": 771.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 555.0,
        "median": 616.5,
        "p90": 793.0,
        "p95": 793.0,
        "max": 832.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 13.0
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 359.5,
        "p90": 395.0,
        "p95": 395.0,
        "max": 405.0
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
        "median": 360.0,
        "p90": 396.0,
        "p95": 396.0,
        "max": 406.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 33.0,
        "p90": 213.0,
        "p95": 213.0,
        "max": 221.0
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
        "min": 410.0,
        "median": 448.0,
        "p90": 491.0,
        "p95": 491.0,
        "max": 496.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 60.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 569.0,
        "median": 631.0,
        "p90": 813.0,
        "p95": 813.0,
        "max": 853.0
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
    "wall_seconds": 5.641,
    "throughput_per_second": 2.127,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.719,
      "median": 2.828,
      "p90": 4.188,
      "p95": 4.188,
      "max": 4.266
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.29,
      "p90": 0.422,
      "p95": 0.422,
      "max": 0.453
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
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 501.0,
        "median": 573.5,
        "p90": 661.0,
        "p95": 661.0,
        "max": 676.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 563.0,
        "median": 630.5,
        "p90": 730.0,
        "p95": 730.0,
        "max": 747.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 17.0,
        "p95": 17.0,
        "max": 22.0
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
        "min": 332.0,
        "median": 342.5,
        "p90": 387.0,
        "p95": 387.0,
        "max": 396.0
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
        "median": 342.5,
        "p90": 388.0,
        "p95": 388.0,
        "max": 397.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 31.5,
        "p90": 153.0,
        "p95": 153.0,
        "max": 168.0
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
        "median": 431.5,
        "p90": 481.0,
        "p95": 481.0,
        "max": 487.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 71.0,
        "p95": 71.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 573.0,
        "median": 647.0,
        "p90": 759.0,
        "p95": 759.0,
        "max": 771.0
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
    "wall_seconds": 5.531,
    "throughput_per_second": 2.17,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.657,
      "median": 3.539,
      "p90": 5.469,
      "p95": 5.469,
      "max": 5.516
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.329,
      "p90": 0.407,
      "p95": 0.407,
      "max": 0.438
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
        "min": 520.0,
        "median": 579.5,
        "p90": 670.0,
        "p95": 670.0,
        "max": 709.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 589.0,
        "median": 640.5,
        "p90": 733.0,
        "p95": 733.0,
        "max": 783.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.5,
        "p90": 12.0,
        "p95": 12.0,
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
        "min": 333.0,
        "median": 364.5,
        "p90": 397.0,
        "p95": 397.0,
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
        "min": 334.0,
        "median": 365.5,
        "p90": 397.0,
        "p95": 397.0,
        "max": 403.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 43.0,
        "p90": 144.0,
        "p95": 144.0,
        "max": 159.0
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
        "median": 464.5,
        "p90": 497.0,
        "p95": 497.0,
        "max": 498.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 50.0,
        "median": 64.0,
        "p90": 73.0,
        "p95": 73.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 62.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 605.0,
        "median": 658.0,
        "p90": 750.0,
        "p95": 750.0,
        "max": 796.0
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
    "wall_seconds": 6.265,
    "throughput_per_second": 1.915,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.734,
      "median": 3.679,
      "p90": 5.64,
      "p95": 5.64,
      "max": 6.265
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.187,
      "median": 0.351,
      "p90": 0.5,
      "p95": 0.5,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 509.0,
        "median": 566.5,
        "p90": 843.0,
        "p95": 843.0,
        "max": 870.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 566.0,
        "median": 627.5,
        "p90": 906.0,
        "p95": 906.0,
        "max": 926.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 8.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 336.0,
        "median": 350.5,
        "p90": 398.0,
        "p95": 398.0,
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
        "min": 337.0,
        "median": 351.5,
        "p90": 399.0,
        "p95": 399.0,
        "max": 412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 41.0,
        "p90": 306.0,
        "p95": 306.0,
        "max": 376.0
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
        "median": 443.5,
        "p90": 494.0,
        "p95": 494.0,
        "max": 507.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 582.0,
        "median": 647.5,
        "p90": 923.0,
        "p95": 923.0,
        "max": 945.0
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
    "wall_seconds": 5.782,
    "throughput_per_second": 2.075,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.891,
      "median": 3.805,
      "p90": 5.782,
      "p95": 5.782,
      "max": 5.782
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.375,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 503.0,
        "median": 567.5,
        "p90": 882.0,
        "p95": 882.0,
        "max": 889.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 557.0,
        "median": 632.5,
        "p90": 945.0,
        "p95": 945.0,
        "max": 955.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 15.0,
        "p95": 15.0,
        "max": 20.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 6.0,
        "p95": 6.0,
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
        "min": 333.0,
        "median": 347.5,
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
        "median": 348.0,
        "p90": 381.0,
        "p95": 381.0,
        "max": 381.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 31.0,
        "p90": 376.0,
        "p95": 376.0,
        "max": 403.0
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
        "median": 436.5,
        "p90": 473.0,
        "p95": 473.0,
        "max": 477.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 60.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 58.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 65.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 566.0,
        "median": 645.0,
        "p90": 967.0,
        "p95": 967.0,
        "max": 983.0
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
    "wall_seconds": 17.438,
    "throughput_per_second": 0.688,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.578,
      "median": 2.61,
      "p90": 3.313,
      "p95": 3.313,
      "max": 3.75
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.14,
      "p90": 0.422,
      "p95": 0.422,
      "max": 0.719
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
        "max": 143.0
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
        "min": 1516.0,
        "median": 1564.0,
        "p90": 1814.0,
        "p95": 1814.0,
        "max": 1995.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1572.0,
        "median": 1629.0,
        "p90": 1870.0,
        "p95": 1870.0,
        "max": 2065.0
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
        "median": 6.0,
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
        "min": 335.0,
        "median": 353.5,
        "p90": 392.0,
        "p95": 392.0,
        "max": 427.0
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
        "min": 1336.0,
        "median": 1354.5,
        "p90": 1393.0,
        "p95": 1393.0,
        "max": 1428.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 23.0,
        "p90": 32.0,
        "p95": 32.0,
        "max": 37.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 275.0,
        "median": 276.0,
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
        "median": 1451.0,
        "p90": 1493.0,
        "p95": 1493.0,
        "max": 1524.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 69.0,
        "p95": 69.0,
        "max": 69.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 62.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1584.0,
        "median": 1640.0,
        "p90": 1884.0,
        "p95": 1884.0,
        "max": 2081.0
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
    "wall_seconds": 17.531,
    "throughput_per_second": 0.685,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.578,
      "median": 2.633,
      "p90": 3.234,
      "p95": 3.234,
      "max": 3.813
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.672,
      "p95": 0.672,
      "max": 0.703
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
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1506.0,
        "median": 1540.0,
        "p90": 1585.0,
        "p95": 1585.0,
        "max": 1704.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1561.0,
        "median": 1606.0,
        "p90": 1662.0,
        "p95": 1662.0,
        "max": 1760.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
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
        "min": 331.0,
        "median": 349.0,
        "p90": 382.0,
        "p95": 382.0,
        "max": 388.0
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
        "median": 1350.0,
        "p90": 1383.0,
        "p95": 1383.0,
        "max": 1389.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 25.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 35.0
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
        "median": 1441.0,
        "p90": 1480.0,
        "p95": 1480.0,
        "max": 1490.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 51.0,
        "median": 59.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1579.0,
        "median": 1618.5,
        "p90": 1677.0,
        "p95": 1677.0,
        "max": 1775.0
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
    "wall_seconds": 18.359,
    "throughput_per_second": 0.654,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.578,
      "median": 2.649,
      "p90": 3.812,
      "p95": 3.812,
      "max": 5.0
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.282
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
        "min": 1499.0,
        "median": 1536.5,
        "p90": 1601.0,
        "p95": 1601.0,
        "max": 1644.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1552.0,
        "median": 1598.5,
        "p90": 1658.0,
        "p95": 1658.0,
        "max": 1717.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
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
        "min": 334.0,
        "median": 341.5,
        "p90": 384.0,
        "p95": 384.0,
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
        "min": 1335.0,
        "median": 1342.5,
        "p90": 1385.0,
        "p95": 1385.0,
        "max": 1422.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 30.0,
        "p90": 49.0,
        "p95": 49.0,
        "max": 50.0
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
        "median": 1435.0,
        "p90": 1481.0,
        "p95": 1481.0,
        "max": 1528.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 58.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 51.0,
        "median": 60.5,
        "p90": 74.0,
        "p95": 74.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1564.0,
        "median": 1617.0,
        "p90": 1671.0,
        "p95": 1671.0,
        "max": 1728.0
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
    "wall_seconds": 13.422,
    "throughput_per_second": 0.894,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.625,
      "median": 3.836,
      "p90": 5.125,
      "p95": 5.125,
      "max": 5.719
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1507.0,
        "median": 1570.5,
        "p90": 1602.0,
        "p95": 1602.0,
        "max": 1642.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1571.0,
        "median": 1632.0,
        "p90": 1667.0,
        "p95": 1667.0,
        "max": 1710.0
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
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
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
        "min": 337.0,
        "median": 373.5,
        "p90": 402.0,
        "p95": 402.0,
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
        "min": 1338.0,
        "median": 1374.5,
        "p90": 1403.0,
        "p95": 1403.0,
        "max": 1423.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 26.0,
        "p90": 40.0,
        "p95": 40.0,
        "max": 51.0
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
        "median": 1472.0,
        "p90": 1509.0,
        "p95": 1509.0,
        "max": 1523.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 61.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1582.0,
        "median": 1646.0,
        "p90": 1680.0,
        "p95": 1680.0,
        "max": 1731.0
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
    "wall_seconds": 13.875,
    "throughput_per_second": 0.865,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.609,
      "median": 3.813,
      "p90": 5.141,
      "p95": 5.141,
      "max": 6.125
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.235,
      "p95": 0.235,
      "max": 0.282
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
        "p90": 6.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1507.0,
        "median": 1580.0,
        "p90": 1597.0,
        "p95": 1597.0,
        "max": 1655.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1568.0,
        "median": 1641.0,
        "p90": 1664.0,
        "p95": 1664.0,
        "max": 1720.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 15.0
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
        "median": 359.0,
        "p90": 389.0,
        "p95": 389.0,
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
        "min": 1334.0,
        "median": 1360.0,
        "p90": 1390.0,
        "p95": 1390.0,
        "max": 1407.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 39.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 80.0
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
        "min": 1419.0,
        "median": 1457.5,
        "p90": 1488.0,
        "p95": 1488.0,
        "max": 1504.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 59.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1580.0,
        "median": 1656.5,
        "p90": 1679.0,
        "p95": 1679.0,
        "max": 1744.0
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
    "wall_seconds": 11.796,
    "throughput_per_second": 1.017,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.593,
      "median": 3.797,
      "p90": 5.015,
      "p95": 5.015,
      "max": 6.156
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.179,
      "p90": 0.25,
      "p95": 0.25,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1510.0,
        "median": 1560.5,
        "p90": 1580.0,
        "p95": 1580.0,
        "max": 1586.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1564.0,
        "median": 1618.0,
        "p90": 1647.0,
        "p95": 1647.0,
        "max": 1652.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 14.0
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
        "median": 368.0,
        "p90": 388.0,
        "p95": 388.0,
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
        "min": 1332.0,
        "median": 1370.0,
        "p90": 1389.0,
        "p95": 1389.0,
        "max": 1392.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 24.0,
        "median": 31.0,
        "p90": 36.0,
        "p95": 36.0,
        "max": 70.0
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
        "median": 1464.5,
        "p90": 1488.0,
        "p95": 1488.0,
        "max": 1490.0
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
        "min": 54.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1580.0,
        "median": 1636.0,
        "p90": 1661.0,
        "p95": 1661.0,
        "max": 1664.0
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
    "wall_seconds": 11.157,
    "throughput_per_second": 1.076,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.657,
      "median": 6.633,
      "p90": 8.391,
      "p95": 8.391,
      "max": 8.438
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.211,
      "p90": 0.297,
      "p95": 0.297,
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
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1501.0,
        "median": 1573.0,
        "p90": 1621.0,
        "p95": 1621.0,
        "max": 1675.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1559.0,
        "median": 1633.5,
        "p90": 1676.0,
        "p95": 1676.0,
        "max": 1738.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 13.0
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
        "median": 374.0,
        "p90": 389.0,
        "p95": 389.0,
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
        "min": 1335.0,
        "median": 1375.0,
        "p90": 1391.0,
        "p95": 1391.0,
        "max": 1394.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 30.5,
        "p90": 84.0,
        "p95": 84.0,
        "max": 115.0
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
        "median": 1471.5,
        "p90": 1492.0,
        "p95": 1492.0,
        "max": 1494.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 60.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1571.0,
        "median": 1647.5,
        "p90": 1690.0,
        "p95": 1690.0,
        "max": 1759.0
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
    "wall_seconds": 11.36,
    "throughput_per_second": 1.056,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.875,
      "median": 6.852,
      "p90": 7.688,
      "p95": 7.688,
      "max": 7.703
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.344
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
        "p90": 3.0,
        "p95": 3.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1509.0,
        "median": 1552.5,
        "p90": 1625.0,
        "p95": 1625.0,
        "max": 1680.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1562.0,
        "median": 1612.0,
        "p90": 1687.0,
        "p95": 1687.0,
        "max": 1739.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
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
        "min": 336.0,
        "median": 347.0,
        "p90": 386.0,
        "p95": 386.0,
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
        "min": 1337.0,
        "median": 1348.0,
        "p90": 1387.0,
        "p95": 1387.0,
        "max": 1420.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 33.0,
        "p90": 82.0,
        "p95": 82.0,
        "max": 126.0
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
        "min": 1423.0,
        "median": 1437.5,
        "p90": 1486.0,
        "p95": 1486.0,
        "max": 1517.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.0,
        "p90": 60.0,
        "p95": 60.0,
        "max": 61.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1573.0,
        "median": 1624.5,
        "p90": 1697.0,
        "p95": 1697.0,
        "max": 1755.0
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
    "wall_seconds": 13.688,
    "throughput_per_second": 0.877,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.813,
      "median": 6.485,
      "p90": 8.516,
      "p95": 8.516,
      "max": 9.578
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.227,
      "p90": 0.344,
      "p95": 0.344,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1499.0,
        "median": 1583.0,
        "p90": 1713.0,
        "p95": 1713.0,
        "max": 1748.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1557.0,
        "median": 1655.5,
        "p90": 1779.0,
        "p95": 1779.0,
        "max": 1810.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 7.5,
        "p90": 14.0,
        "p95": 14.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
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
        "min": 330.0,
        "median": 354.5,
        "p90": 400.0,
        "p95": 400.0,
        "max": 404.0
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
        "min": 1331.0,
        "median": 1356.0,
        "p90": 1401.0,
        "p95": 1401.0,
        "max": 1405.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 41.0,
        "p90": 186.0,
        "p95": 186.0,
        "max": 209.0
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
        "min": 1413.0,
        "median": 1457.0,
        "p90": 1497.0,
        "p95": 1497.0,
        "max": 1513.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 82.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.5,
        "p90": 69.0,
        "p95": 69.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1570.0,
        "median": 1674.5,
        "p90": 1793.0,
        "p95": 1793.0,
        "max": 1826.0
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
    "wall_seconds": 12.235,
    "throughput_per_second": 0.981,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 3.469,
      "median": 7.086,
      "p90": 11.141,
      "p95": 11.141,
      "max": 12.235
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.188,
      "median": 0.297,
      "p90": 0.422,
      "p95": 0.422,
      "max": 0.453
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
        "min": 1509.0,
        "median": 1573.0,
        "p90": 1625.0,
        "p95": 1625.0,
        "max": 1731.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1564.0,
        "median": 1642.0,
        "p90": 1698.0,
        "p95": 1698.0,
        "max": 1807.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
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
        "min": 333.0,
        "median": 342.5,
        "p90": 405.0,
        "p95": 405.0,
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
        "median": 1344.0,
        "p90": 1407.0,
        "p95": 1407.0,
        "max": 1412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 30.0,
        "p90": 136.0,
        "p95": 136.0,
        "max": 153.0
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
        "median": 1441.0,
        "p90": 1515.0,
        "p95": 1515.0,
        "max": 1519.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 66.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.5,
        "p90": 82.0,
        "p95": 82.0,
        "max": 88.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1576.0,
        "median": 1657.0,
        "p90": 1713.0,
        "p95": 1713.0,
        "max": 1829.0
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
    "wall_seconds": 12.515,
    "throughput_per_second": 0.959,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.797,
      "median": 7.125,
      "p90": 11.437,
      "p95": 11.437,
      "max": 12.5
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.367,
      "p90": 0.687,
      "p95": 0.687,
      "max": 0.703
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
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 1509.0,
        "median": 1585.0,
        "p90": 1721.0,
        "p95": 1721.0,
        "max": 1886.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1570.0,
        "median": 1649.0,
        "p90": 1784.0,
        "p95": 1784.0,
        "max": 1948.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 7.0,
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
        "min": 330.0,
        "median": 362.0,
        "p90": 416.0,
        "p95": 416.0,
        "max": 442.0
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
        "min": 1331.0,
        "median": 1363.0,
        "p90": 1418.0,
        "p95": 1418.0,
        "max": 1443.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 29.0,
        "p90": 232.0,
        "p95": 232.0,
        "max": 257.0
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
        "median": 1450.5,
        "p90": 1521.0,
        "p95": 1521.0,
        "max": 1556.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1585.0,
        "median": 1663.0,
        "p90": 1798.0,
        "p95": 1798.0,
        "max": 1970.0
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
      "min": 2.812,
      "median": 7.124,
      "p90": 11.562,
      "p95": 11.562,
      "max": 12.671
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.171,
      "median": 0.265,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.406
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
        "min": 1507.0,
        "median": 1585.5,
        "p90": 1869.0,
        "p95": 1869.0,
        "max": 1916.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 1565.0,
        "median": 1648.0,
        "p90": 1925.0,
        "p95": 1925.0,
        "max": 1974.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.5,
        "p90": 13.0,
        "p95": 13.0,
        "max": 26.0
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
        "min": 336.0,
        "median": 341.0,
        "p90": 394.0,
        "p95": 394.0,
        "max": 417.0
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
        "min": 1337.0,
        "median": 1342.0,
        "p90": 1396.0,
        "p95": 1396.0,
        "max": 1418.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 31.5,
        "p90": 377.0,
        "p95": 377.0,
        "max": 411.0
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
        "median": 1433.5,
        "p90": 1511.0,
        "p95": 1511.0,
        "max": 1521.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 1582.0,
        "median": 1670.5,
        "p90": 1943.0,
        "p95": 1943.0,
        "max": 1990.0
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
    "wall_seconds": 11.672,
    "throughput_per_second": 1.028,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 1.531,
      "p90": 2.906,
      "p95": 2.906,
      "max": 3.984
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.438,
      "p95": 0.438,
      "max": 1.359
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
        "p90": 38.0,
        "p95": 38.0,
        "max": 139.0
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
        "min": 691.0,
        "median": 749.5,
        "p90": 1127.0,
        "p95": 1127.0,
        "max": 1136.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 749.0,
        "median": 811.5,
        "p90": 1192.0,
        "p95": 1192.0,
        "max": 1198.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 12.0
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
        "min": 167.0,
        "median": 179.0,
        "p90": 194.0,
        "p95": 194.0,
        "max": 204.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 334.0,
        "median": 350.5,
        "p90": 395.0,
        "p95": 395.0,
        "max": 405.0
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
        "median": 528.5,
        "p90": 588.0,
        "p95": 588.0,
        "max": 610.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 26.0,
        "p90": 42.0,
        "p95": 42.0,
        "max": 46.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 272.0,
        "median": 279.0,
        "p90": 286.0,
        "p95": 286.0,
        "max": 286.0
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
        "min": 603.0,
        "median": 632.5,
        "p90": 702.0,
        "p95": 702.0,
        "max": 714.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 761.0,
        "median": 825.5,
        "p90": 1205.0,
        "p95": 1205.0,
        "max": 1212.0
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
    "wall_seconds": 10.094,
    "throughput_per_second": 1.189,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.485,
      "p90": 1.516,
      "p95": 1.516,
      "max": 2.656
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
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 680.0,
        "median": 746.5,
        "p90": 803.0,
        "p95": 803.0,
        "max": 824.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 739.0,
        "median": 807.0,
        "p90": 870.0,
        "p95": 870.0,
        "max": 889.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
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
        "min": 166.0,
        "median": 184.5,
        "p90": 203.0,
        "p95": 203.0,
        "max": 218.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 332.0,
        "median": 361.5,
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
        "min": 500.0,
        "median": 548.0,
        "p90": 592.0,
        "p95": 592.0,
        "max": 600.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 25.5,
        "p90": 45.0,
        "p95": 45.0,
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
        "min": 595.0,
        "median": 654.0,
        "p90": 701.0,
        "p95": 701.0,
        "max": 707.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 62.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 753.0,
        "median": 820.5,
        "p90": 884.0,
        "p95": 884.0,
        "max": 904.0
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
    "wall_seconds": 10.157,
    "throughput_per_second": 1.181,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 1.492,
      "p90": 1.563,
      "p95": 1.563,
      "max": 2.625
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.188,
      "p95": 0.188,
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
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 675.0,
        "median": 705.0,
        "p90": 802.0,
        "p95": 802.0,
        "max": 814.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 729.0,
        "median": 767.0,
        "p90": 873.0,
        "p95": 873.0,
        "max": 877.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
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
        "median": 172.0,
        "p90": 198.0,
        "p95": 198.0,
        "max": 205.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 332.0,
        "median": 344.0,
        "p90": 393.0,
        "p95": 393.0,
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
        "min": 500.0,
        "median": 516.0,
        "p90": 593.0,
        "p95": 593.0,
        "max": 602.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 24.5,
        "p90": 32.0,
        "p95": 32.0,
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
        "min": 594.0,
        "median": 615.0,
        "p90": 703.0,
        "p95": 703.0,
        "max": 711.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 51.0,
        "median": 58.5,
        "p90": 71.0,
        "p95": 71.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 51.0,
        "median": 60.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 740.0,
        "median": 782.5,
        "p90": 886.0,
        "p95": 886.0,
        "max": 891.0
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
    "wall_seconds": 7.312,
    "throughput_per_second": 1.641,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.468,
      "median": 2.265,
      "p90": 3.094,
      "p95": 3.094,
      "max": 3.187
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.234
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
        "min": 676.0,
        "median": 771.0,
        "p90": 866.0,
        "p95": 866.0,
        "max": 877.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 731.0,
        "median": 842.0,
        "p90": 938.0,
        "p95": 938.0,
        "max": 957.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
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
        "min": 164.0,
        "median": 188.5,
        "p90": 211.0,
        "p95": 211.0,
        "max": 227.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 362.0,
        "p90": 425.0,
        "p95": 425.0,
        "max": 438.0
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
        "median": 551.5,
        "p90": 631.0,
        "p95": 631.0,
        "max": 650.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 29.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 58.0
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
        "median": 665.0,
        "p90": 749.0,
        "p95": 749.0,
        "max": 763.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 66.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 64.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 747.0,
        "median": 856.5,
        "p90": 959.0,
        "p95": 959.0,
        "max": 974.0
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
    "wall_seconds": 7.234,
    "throughput_per_second": 1.659,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.468,
      "median": 2.117,
      "p90": 2.718,
      "p95": 2.718,
      "max": 2.812
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
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
        "min": 677.0,
        "median": 777.5,
        "p90": 846.0,
        "p95": 846.0,
        "max": 884.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 733.0,
        "median": 841.0,
        "p90": 913.0,
        "p95": 913.0,
        "max": 946.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 7.0,
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
        "median": 192.0,
        "p90": 203.0,
        "p95": 203.0,
        "max": 222.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 334.0,
        "median": 378.5,
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
        "min": 503.0,
        "median": 564.0,
        "p90": 604.0,
        "p95": 604.0,
        "max": 626.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 27.0,
        "p90": 81.0,
        "p95": 81.0,
        "max": 91.0
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
        "median": 672.0,
        "p90": 721.0,
        "p95": 721.0,
        "max": 747.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 71.0,
        "p95": 71.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 64.5,
        "p90": 67.0,
        "p95": 67.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 743.0,
        "median": 855.5,
        "p90": 927.0,
        "p95": 927.0,
        "max": 958.0
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
    "wall_seconds": 7.0,
    "throughput_per_second": 1.714,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.516,
      "median": 2.094,
      "p90": 2.766,
      "p95": 2.766,
      "max": 2.781
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
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
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 702.0,
        "median": 746.0,
        "p90": 820.0,
        "p95": 820.0,
        "max": 822.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 761.0,
        "median": 804.0,
        "p90": 877.0,
        "p95": 877.0,
        "max": 881.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
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
        "min": 166.0,
        "median": 175.0,
        "p90": 195.0,
        "p95": 195.0,
        "max": 200.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 335.0,
        "median": 350.0,
        "p90": 391.0,
        "p95": 391.0,
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
        "min": 502.0,
        "median": 524.0,
        "p90": 586.0,
        "p95": 586.0,
        "max": 592.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 43.0,
        "p90": 68.0,
        "p95": 68.0,
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
        "min": 599.0,
        "median": 632.0,
        "p90": 695.0,
        "p95": 695.0,
        "max": 700.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 773.0,
        "median": 820.0,
        "p90": 892.0,
        "p95": 892.0,
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
    "repeat": 1,
    "wall_seconds": 6.641,
    "throughput_per_second": 1.807,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.516,
      "median": 3.929,
      "p90": 5.25,
      "p95": 5.25,
      "max": 5.328
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.211,
      "p90": 0.297,
      "p95": 0.297,
      "max": 0.609
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
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 672.0,
        "median": 727.5,
        "p90": 775.0,
        "p95": 775.0,
        "max": 861.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 729.0,
        "median": 792.5,
        "p90": 833.0,
        "p95": 833.0,
        "max": 921.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 11.0,
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
        "min": 165.0,
        "median": 170.5,
        "p90": 194.0,
        "p95": 194.0,
        "max": 207.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 341.0,
        "p90": 376.0,
        "p95": 376.0,
        "max": 428.0
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
        "median": 513.5,
        "p90": 571.0,
        "p95": 571.0,
        "max": 636.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 33.0,
        "p90": 63.0,
        "p95": 63.0,
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
        "min": 588.0,
        "median": 611.5,
        "p90": 674.0,
        "p95": 674.0,
        "max": 743.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 747.0,
        "median": 810.5,
        "p90": 848.0,
        "p95": 848.0,
        "max": 936.0
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
    "wall_seconds": 6.688,
    "throughput_per_second": 1.794,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.516,
      "median": 3.898,
      "p90": 4.032,
      "p95": 4.032,
      "max": 5.219
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.195,
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
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 676.0,
        "median": 754.5,
        "p90": 812.0,
        "p95": 812.0,
        "max": 817.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 734.0,
        "median": 814.5,
        "p90": 875.0,
        "p95": 875.0,
        "max": 876.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 15.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 4.5,
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
        "min": 162.0,
        "median": 174.0,
        "p90": 197.0,
        "p95": 197.0,
        "max": 233.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 330.0,
        "median": 356.5,
        "p90": 382.0,
        "p95": 382.0,
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
        "min": 494.0,
        "median": 531.5,
        "p90": 595.0,
        "p95": 595.0,
        "max": 617.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 30.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 116.0
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
        "median": 635.0,
        "p90": 703.0,
        "p95": 703.0,
        "max": 719.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 746.0,
        "median": 827.0,
        "p90": 888.0,
        "p95": 888.0,
        "max": 889.0
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
    "wall_seconds": 6.844,
    "throughput_per_second": 1.753,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.735,
      "median": 3.797,
      "p90": 5.375,
      "p95": 5.375,
      "max": 5.391
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.376,
      "p90": 0.485,
      "p95": 0.485,
      "max": 0.516
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
        "min": 684.0,
        "median": 763.5,
        "p90": 815.0,
        "p95": 815.0,
        "max": 844.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 743.0,
        "median": 824.5,
        "p90": 878.0,
        "p95": 878.0,
        "max": 911.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
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
        "min": 163.0,
        "median": 177.5,
        "p90": 201.0,
        "p95": 201.0,
        "max": 220.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 335.0,
        "median": 354.0,
        "p90": 383.0,
        "p95": 383.0,
        "max": 384.0
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
        "min": 506.0,
        "median": 525.0,
        "p90": 586.0,
        "p95": 586.0,
        "max": 604.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 33.0,
        "p90": 96.0,
        "p95": 96.0,
        "max": 142.0
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
        "min": 596.0,
        "median": 634.0,
        "p90": 694.0,
        "p95": 694.0,
        "max": 710.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 61.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 79.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 758.0,
        "median": 834.5,
        "p90": 901.0,
        "p95": 901.0,
        "max": 924.0
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
    "wall_seconds": 6.813,
    "throughput_per_second": 1.761,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.578,
      "median": 4.211,
      "p90": 6.782,
      "p95": 6.782,
      "max": 6.813
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.274,
      "p90": 0.344,
      "p95": 0.344,
      "max": 0.407
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
        "min": 674.0,
        "median": 755.0,
        "p90": 975.0,
        "p95": 975.0,
        "max": 995.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 729.0,
        "median": 813.5,
        "p90": 1034.0,
        "p95": 1034.0,
        "max": 1056.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 16.0,
        "p95": 16.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.5,
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
        "median": 172.0,
        "p90": 193.0,
        "p95": 193.0,
        "max": 195.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 343.0,
        "p90": 394.0,
        "p95": 394.0,
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
        "min": 497.0,
        "median": 515.5,
        "p90": 586.0,
        "p95": 586.0,
        "max": 588.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 19.0,
        "median": 30.0,
        "p90": 215.0,
        "p95": 215.0,
        "max": 270.0
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
        "min": 592.0,
        "median": 621.5,
        "p90": 692.0,
        "p95": 692.0,
        "max": 695.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 57.5,
        "p90": 61.0,
        "p95": 61.0,
        "max": 62.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 742.0,
        "median": 829.0,
        "p90": 1054.0,
        "p95": 1054.0,
        "max": 1084.0
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
    "wall_seconds": 6.625,
    "throughput_per_second": 1.811,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.641,
      "median": 4.149,
      "p90": 6.594,
      "p95": 6.594,
      "max": 6.625
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.258,
      "p90": 0.438,
      "p95": 0.438,
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
        "p90": 5.0,
        "p95": 5.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 682.0,
        "median": 745.5,
        "p90": 842.0,
        "p95": 842.0,
        "max": 902.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 738.0,
        "median": 803.0,
        "p90": 901.0,
        "p95": 901.0,
        "max": 966.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 11.0,
        "p95": 11.0,
        "max": 14.0
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
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_import_ms": {
        "count": 12,
        "min": 166.0,
        "median": 173.0,
        "p90": 195.0,
        "p95": 195.0,
        "max": 200.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 331.0,
        "median": 347.0,
        "p90": 388.0,
        "p95": 388.0,
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
        "min": 501.0,
        "median": 518.0,
        "p90": 584.0,
        "p95": 584.0,
        "max": 592.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 37.5,
        "p90": 177.0,
        "p95": 177.0,
        "max": 209.0
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
        "median": 618.5,
        "p90": 684.0,
        "p95": 684.0,
        "max": 711.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 749.0,
        "median": 817.0,
        "p90": 915.0,
        "p95": 915.0,
        "max": 989.0
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
    "wall_seconds": 7.484,
    "throughput_per_second": 1.603,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.765,
      "median": 4.304,
      "p90": 7.375,
      "p95": 7.375,
      "max": 7.468
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.328,
      "p90": 0.531,
      "p95": 0.531,
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
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 689.0,
        "median": 748.5,
        "p90": 999.0,
        "p95": 999.0,
        "max": 1098.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 749.0,
        "median": 807.0,
        "p90": 1057.0,
        "p95": 1057.0,
        "max": 1161.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
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
        "min": 166.0,
        "median": 175.5,
        "p90": 209.0,
        "p95": 209.0,
        "max": 211.0
      },
      "runner_module_imports_ms": {
        "count": 12,
        "min": 333.0,
        "median": 343.0,
        "p90": 384.0,
        "p95": 384.0,
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
        "min": 499.0,
        "median": 517.5,
        "p90": 587.0,
        "p95": 587.0,
        "max": 602.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 25.5,
        "p90": 322.0,
        "p95": 322.0,
        "max": 348.0
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
        "min": 595.0,
        "median": 613.5,
        "p90": 695.0,
        "p95": 695.0,
        "max": 705.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.0,
        "p90": 75.0,
        "p95": 75.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 767.0,
        "median": 819.0,
        "p90": 1074.0,
        "p95": 1074.0,
        "max": 1180.0
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
    "wall_seconds": 14.109,
    "throughput_per_second": 0.851,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.492,
      "p90": 2.641,
      "p95": 2.641,
      "max": 2.641
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.149,
      "p90": 0.157,
      "p95": 0.157,
      "max": 0.172
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
        "min": 228.0,
        "median": 241.0,
        "p90": 264.0,
        "p95": 264.0,
        "max": 275.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 25.0,
        "p95": 25.0,
        "max": 134.0
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
        "median": 571.0,
        "p90": 841.0,
        "p95": 841.0,
        "max": 953.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 831.0,
        "median": 929.5,
        "p90": 1180.0,
        "p95": 1180.0,
        "max": 1321.0
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
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 36.5,
        "p90": 47.0,
        "p95": 47.0,
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
        "min": 339.0,
        "median": 360.0,
        "p90": 412.0,
        "p95": 412.0,
        "max": 465.0
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
        "median": 361.5,
        "p90": 413.0,
        "p95": 413.0,
        "max": 466.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 25.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 50.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 269.0,
        "median": 284.5,
        "p90": 300.0,
        "p95": 300.0,
        "max": 300.0
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
        "min": 425.0,
        "median": 455.0,
        "p90": 521.0,
        "p95": 521.0,
        "max": 563.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 842.0,
        "median": 944.0,
        "p90": 1195.0,
        "p95": 1195.0,
        "max": 1332.0
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
    "wall_seconds": 12.656,
    "throughput_per_second": 0.948,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.438,
      "median": 1.515,
      "p90": 2.25,
      "p95": 2.25,
      "max": 2.625
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.39
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.157,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.203
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
        "min": 227.0,
        "median": 248.5,
        "p90": 256.0,
        "p95": 256.0,
        "max": 270.0
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
        "median": 543.5,
        "p90": 604.0,
        "p95": 604.0,
        "max": 663.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 832.0,
        "median": 890.5,
        "p90": 972.0,
        "p95": 972.0,
        "max": 1011.0
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
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 36.5,
        "p90": 43.0,
        "p95": 43.0,
        "max": 71.0
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
        "min": 336.0,
        "median": 346.0,
        "p90": 406.0,
        "p95": 406.0,
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
        "min": 336.0,
        "median": 347.0,
        "p90": 407.0,
        "p95": 407.0,
        "max": 412.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 29.0,
        "p90": 48.0,
        "p95": 48.0,
        "max": 102.0
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
        "median": 439.5,
        "p90": 502.0,
        "p95": 502.0,
        "max": 505.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 70.0,
        "p95": 70.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 848.0,
        "median": 904.5,
        "p90": 982.0,
        "p95": 982.0,
        "max": 1026.0
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
    "wall_seconds": 13.266,
    "throughput_per_second": 0.905,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 1.531,
      "p90": 2.672,
      "p95": 2.672,
      "max": 2.688
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
      "count": 12,
      "min": 0.156,
      "median": 0.164,
      "p90": 0.172,
      "p95": 0.172,
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
        "median": 237.5,
        "p90": 262.0,
        "p95": 262.0,
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
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 503.0,
        "median": 534.5,
        "p90": 776.0,
        "p95": 776.0,
        "max": 781.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 824.0,
        "median": 867.0,
        "p90": 1126.0,
        "p95": 1126.0,
        "max": 1141.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 7.0
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
        "min": 30.0,
        "median": 35.0,
        "p90": 63.0,
        "p95": 63.0,
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
        "min": 334.0,
        "median": 350.0,
        "p90": 414.0,
        "p95": 414.0,
        "max": 418.0
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
        "median": 351.0,
        "p90": 415.0,
        "p95": 415.0,
        "max": 419.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 22.0,
        "p90": 28.0,
        "p95": 28.0,
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
        "min": 416.0,
        "median": 441.5,
        "p90": 511.0,
        "p95": 511.0,
        "max": 523.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 59.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 836.0,
        "median": 879.5,
        "p90": 1141.0,
        "p95": 1141.0,
        "max": 1155.0
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
    "wall_seconds": 7.969,
    "throughput_per_second": 1.506,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.469,
      "median": 2.11,
      "p90": 2.704,
      "p95": 2.704,
      "max": 2.766
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.234,
      "p95": 0.234,
      "max": 0.266
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.149,
      "p90": 0.156,
      "p95": 0.156,
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
        "median": 236.5,
        "p90": 262.0,
        "p95": 262.0,
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
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 498.0,
        "median": 535.5,
        "p90": 592.0,
        "p95": 592.0,
        "max": 631.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 822.0,
        "median": 894.0,
        "p90": 932.0,
        "p95": 932.0,
        "max": 981.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 43.0,
        "p90": 85.0,
        "p95": 85.0,
        "max": 100.0
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
        "median": 343.0,
        "p90": 402.0,
        "p95": 402.0,
        "max": 404.0
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
        "median": 343.5,
        "p90": 403.0,
        "p95": 403.0,
        "max": 405.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 29.5,
        "p90": 56.0,
        "p95": 56.0,
        "max": 62.0
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
        "median": 434.0,
        "p90": 496.0,
        "p95": 496.0,
        "max": 498.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 836.0,
        "median": 907.0,
        "p90": 945.0,
        "p95": 945.0,
        "max": 999.0
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
    "wall_seconds": 8.875,
    "throughput_per_second": 1.352,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.437,
      "median": 2.054,
      "p90": 2.719,
      "p95": 2.719,
      "max": 3.765
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.234
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.141,
      "p90": 0.156,
      "p95": 0.156,
      "max": 0.172
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
        "median": 249.0,
        "p90": 272.0,
        "p95": 272.0,
        "max": 273.0
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
        "min": 503.0,
        "median": 529.5,
        "p90": 561.0,
        "p95": 561.0,
        "max": 570.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 835.0,
        "median": 875.0,
        "p90": 948.0,
        "p95": 948.0,
        "max": 970.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 8.0
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
        "min": 32.0,
        "median": 35.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 90.0
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
        "median": 343.5,
        "p90": 362.0,
        "p95": 362.0,
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
        "min": 335.0,
        "median": 344.5,
        "p90": 363.0,
        "p95": 363.0,
        "max": 377.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 28.0,
        "p90": 46.0,
        "p95": 46.0,
        "max": 59.0
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
        "median": 434.0,
        "p90": 465.0,
        "p95": 465.0,
        "max": 473.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 73.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 847.0,
        "median": 890.0,
        "p90": 961.0,
        "p95": 961.0,
        "max": 985.0
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
    "wall_seconds": 7.797,
    "throughput_per_second": 1.539,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.453,
      "median": 2.078,
      "p90": 2.703,
      "p95": 2.703,
      "max": 2.734
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.218
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.157,
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
        "median": 233.5,
        "p90": 252.0,
        "p95": 252.0,
        "max": 270.0
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
        "min": 501.0,
        "median": 520.0,
        "p90": 590.0,
        "p95": 590.0,
        "max": 617.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 824.0,
        "median": 858.5,
        "p90": 1027.0,
        "p95": 1027.0,
        "max": 1091.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 10.0
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
        "min": 34.0,
        "median": 36.0,
        "p90": 78.0,
        "p95": 78.0,
        "max": 302.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
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
        "median": 339.0,
        "p90": 389.0,
        "p95": 389.0,
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
        "min": 333.0,
        "median": 340.0,
        "p90": 390.0,
        "p95": 390.0,
        "max": 425.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 24.5,
        "p90": 33.0,
        "p95": 33.0,
        "max": 43.0
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
        "median": 430.0,
        "p90": 484.0,
        "p95": 484.0,
        "max": 525.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 65.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 836.0,
        "median": 870.0,
        "p90": 1044.0,
        "p95": 1044.0,
        "max": 1106.0
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
    "wall_seconds": 8.281,
    "throughput_per_second": 1.449,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.5,
      "median": 3.914,
      "p90": 5.156,
      "p95": 5.156,
      "max": 5.25
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.211,
      "p90": 0.281,
      "p95": 0.281,
      "max": 0.281
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.141,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.219
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
        "median": 232.0,
        "p90": 264.0,
        "p95": 264.0,
        "max": 275.0
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
        "min": 499.0,
        "median": 568.0,
        "p90": 666.0,
        "p95": 666.0,
        "max": 680.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 832.0,
        "median": 891.0,
        "p90": 1015.0,
        "p95": 1015.0,
        "max": 1037.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
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
        "min": 32.0,
        "median": 36.0,
        "p90": 41.0,
        "p95": 41.0,
        "max": 43.0
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
        "median": 337.5,
        "p90": 406.0,
        "p95": 406.0,
        "max": 415.0
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
        "median": 338.5,
        "p90": 407.0,
        "p95": 407.0,
        "max": 416.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 51.5,
        "p90": 89.0,
        "p95": 89.0,
        "max": 104.0
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
        "median": 425.5,
        "p90": 515.0,
        "p95": 515.0,
        "max": 516.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 78.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 60.5,
        "p90": 76.0,
        "p95": 76.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 850.0,
        "median": 905.0,
        "p90": 1028.0,
        "p95": 1028.0,
        "max": 1054.0
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
    "wall_seconds": 8.187,
    "throughput_per_second": 1.466,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.656,
      "median": 3.945,
      "p90": 5.281,
      "p95": 5.281,
      "max": 5.328
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.211,
      "p90": 0.375,
      "p95": 0.375,
      "max": 0.422
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.39,
      "p95": 0.39,
      "max": 0.422
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
        "median": 233.5,
        "p90": 259.0,
        "p95": 259.0,
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
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 498.0,
        "median": 532.0,
        "p90": 662.0,
        "p95": 662.0,
        "max": 761.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 818.0,
        "median": 889.0,
        "p90": 990.0,
        "p95": 990.0,
        "max": 1134.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 13.0,
        "p95": 13.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 20.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 39.0,
        "p90": 60.0,
        "p95": 60.0,
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
        "median": 340.5,
        "p90": 352.0,
        "p95": 352.0,
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
        "min": 331.0,
        "median": 341.5,
        "p90": 352.0,
        "p95": 352.0,
        "max": 387.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 21.0,
        "median": 29.0,
        "p90": 174.0,
        "p95": 174.0,
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
        "min": 413.0,
        "median": 427.5,
        "p90": 468.0,
        "p95": 468.0,
        "max": 476.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 57.0,
        "p90": 62.0,
        "p95": 62.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.5,
        "p90": 75.0,
        "p95": 75.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 828.0,
        "median": 905.0,
        "p90": 1011.0,
        "p95": 1011.0,
        "max": 1173.0
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
    "wall_seconds": 7.313,
    "throughput_per_second": 1.641,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.578,
      "median": 3.789,
      "p90": 4.14,
      "p95": 4.14,
      "max": 5.187
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.235,
      "p90": 0.343,
      "p95": 0.343,
      "max": 0.343
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.149,
      "p90": 0.157,
      "p95": 0.157,
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
        "min": 227.0,
        "median": 233.5,
        "p90": 264.0,
        "p95": 264.0,
        "max": 286.0
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
        "min": 507.0,
        "median": 535.0,
        "p90": 548.0,
        "p95": 548.0,
        "max": 572.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 841.0,
        "median": 884.0,
        "p90": 914.0,
        "p95": 914.0,
        "max": 961.0
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
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 41.0,
        "p90": 103.0,
        "p95": 103.0,
        "max": 117.0
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
        "median": 340.0,
        "p90": 345.0,
        "p95": 345.0,
        "max": 358.0
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
        "median": 341.0,
        "p90": 345.0,
        "p95": 345.0,
        "max": 359.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 28.5,
        "p90": 55.0,
        "p95": 55.0,
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
        "min": 424.0,
        "median": 430.0,
        "p90": 437.0,
        "p95": 437.0,
        "max": 452.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 52.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 73.0,
        "p95": 73.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 859.0,
        "median": 903.0,
        "p90": 927.0,
        "p95": 927.0,
        "max": 981.0
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
    "wall_seconds": 8.016,
    "throughput_per_second": 1.497,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.672,
      "median": 4.727,
      "p90": 7.11,
      "p95": 7.11,
      "max": 7.688
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.305,
      "p90": 0.438,
      "p95": 0.438,
      "max": 0.485
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.157,
      "p90": 0.422,
      "p95": 0.422,
      "max": 0.671
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
        "median": 230.5,
        "p90": 244.0,
        "p95": 244.0,
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
        "median": 3.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 510.0,
        "median": 532.5,
        "p90": 715.0,
        "p95": 715.0,
        "max": 774.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 827.0,
        "median": 867.5,
        "p90": 1062.0,
        "p95": 1062.0,
        "max": 1121.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 7.0,
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
        "min": 33.0,
        "median": 37.0,
        "p90": 59.0,
        "p95": 59.0,
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
        "min": 329.0,
        "median": 342.0,
        "p90": 376.0,
        "p95": 376.0,
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
        "min": 330.0,
        "median": 342.0,
        "p90": 377.0,
        "p95": 377.0,
        "max": 383.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 20.0,
        "median": 35.5,
        "p90": 229.0,
        "p95": 229.0,
        "max": 241.0
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
        "median": 429.0,
        "p90": 481.0,
        "p95": 481.0,
        "max": 483.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 841.0,
        "median": 881.5,
        "p90": 1080.0,
        "p95": 1080.0,
        "max": 1136.0
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
    "wall_seconds": 8.484,
    "throughput_per_second": 1.414,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.75,
      "median": 5.164,
      "p90": 7.187,
      "p95": 7.187,
      "max": 8.187
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.265,
      "median": 0.445,
      "p90": 0.562,
      "p95": 0.562,
      "max": 0.671
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
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
        "min": 224.0,
        "median": 233.0,
        "p90": 247.0,
        "p95": 247.0,
        "max": 257.0
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
        "min": 502.0,
        "median": 528.5,
        "p90": 796.0,
        "p95": 796.0,
        "max": 867.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 835.0,
        "median": 900.0,
        "p90": 1121.0,
        "p95": 1121.0,
        "max": 1201.0
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
        "min": 3.0,
        "median": 6.0,
        "p90": 13.0,
        "p95": 13.0,
        "max": 14.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 35.5,
        "p90": 115.0,
        "p95": 115.0,
        "max": 153.0
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
        "median": 342.5,
        "p90": 354.0,
        "p95": 354.0,
        "max": 384.0
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
        "median": 343.5,
        "p90": 355.0,
        "p95": 355.0,
        "max": 385.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 22.0,
        "median": 26.0,
        "p90": 308.0,
        "p95": 308.0,
        "max": 359.0
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
        "median": 435.5,
        "p90": 445.0,
        "p95": 445.0,
        "max": 475.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 51.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 66.0,
        "max": 67.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 847.0,
        "median": 917.5,
        "p90": 1138.0,
        "p95": 1138.0,
        "max": 1216.0
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
    "wall_seconds": 8.266,
    "throughput_per_second": 1.452,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.579,
      "median": 4.703,
      "p90": 7.672,
      "p95": 7.672,
      "max": 7.938
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.157,
      "median": 0.282,
      "p90": 0.36,
      "p95": 0.36,
      "max": 0.438
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.196,
      "p90": 0.219,
      "p95": 0.219,
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
        "min": 224.0,
        "median": 235.0,
        "p90": 258.0,
        "p95": 258.0,
        "max": 261.0
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
        "min": 512.0,
        "median": 542.0,
        "p90": 666.0,
        "p95": 666.0,
        "max": 762.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 840.0,
        "median": 924.5,
        "p90": 992.0,
        "p95": 992.0,
        "max": 1094.0
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
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 36.0,
        "p90": 115.0,
        "p95": 115.0,
        "max": 139.0
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
        "median": 349.0,
        "p90": 398.0,
        "p95": 398.0,
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
        "min": 332.0,
        "median": 350.0,
        "p90": 399.0,
        "p95": 399.0,
        "max": 408.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 23.0,
        "median": 33.0,
        "p90": 163.0,
        "p95": 163.0,
        "max": 191.0
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
        "median": 437.5,
        "p90": 490.0,
        "p95": 490.0,
        "max": 500.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 66.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 65.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 853.0,
        "median": 940.0,
        "p90": 1003.0,
        "p95": 1003.0,
        "max": 1109.0
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
    "wall_seconds": 15.219,
    "throughput_per_second": 0.788,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 2.054,
      "p90": 2.704,
      "p95": 2.704,
      "max": 2.828
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.187,
      "median": 0.188,
      "p90": 0.437,
      "p95": 0.437,
      "max": 0.5
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.313,
      "p95": 0.313,
      "max": 0.344
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
        "min": 222.0,
        "median": 233.5,
        "p90": 262.0,
        "p95": 262.0,
        "max": 267.0
      },
      "docker_image_pull_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 38.0,
        "p95": 38.0,
        "max": 143.0
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
        "min": 525.0,
        "median": 560.5,
        "p90": 912.0,
        "p95": 912.0,
        "max": 941.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 853.0,
        "median": 909.0,
        "p90": 1236.0,
        "p95": 1236.0,
        "max": 1283.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 2.0,
        "median": 4.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 36.0,
        "p90": 44.0,
        "p95": 44.0,
        "max": 44.0
      },
      "output_validation_ms": {
        "count": 12,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 1.0
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
        "median": 340.5,
        "p90": 383.0,
        "p95": 383.0,
        "max": 389.0
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
        "median": 341.5,
        "p90": 384.0,
        "p95": 384.0,
        "max": 390.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 38.0,
        "median": 46.0,
        "p90": 57.0,
        "p95": 57.0,
        "max": 70.0
      },
      "warm_container_create_ms": {
        "count": 2,
        "min": 254.0,
        "median": 279.0,
        "p90": 304.0,
        "p95": 304.0,
        "max": 304.0
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
        "median": 430.5,
        "p90": 487.0,
        "p95": 487.0,
        "max": 494.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 53.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 59.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 865.0,
        "median": 922.5,
        "p90": 1251.0,
        "p95": 1251.0,
        "max": 1307.0
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
    "wall_seconds": 13.281,
    "throughput_per_second": 0.904,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.484,
      "median": 1.524,
      "p90": 2.672,
      "p95": 2.672,
      "max": 2.687
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.179,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.218
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.149,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
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
        "median": 250.5,
        "p90": 272.0,
        "p95": 272.0,
        "max": 303.0
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
        "min": 528.0,
        "median": 585.0,
        "p90": 634.0,
        "p95": 634.0,
        "max": 737.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 863.0,
        "median": 948.0,
        "p90": 1014.0,
        "p95": 1014.0,
        "max": 1082.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 4.5,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 36.0,
        "p90": 40.0,
        "p95": 40.0,
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
        "min": 334.0,
        "median": 351.0,
        "p90": 383.0,
        "p95": 383.0,
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
        "min": 334.0,
        "median": 352.0,
        "p90": 384.0,
        "p95": 384.0,
        "max": 408.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 40.0,
        "median": 48.5,
        "p90": 117.0,
        "p95": 117.0,
        "max": 155.0
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
        "median": 445.0,
        "p90": 493.0,
        "p95": 493.0,
        "max": 516.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 62.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 61.0,
        "p90": 72.0,
        "p95": 72.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 875.0,
        "median": 963.5,
        "p90": 1028.0,
        "p95": 1028.0,
        "max": 1095.0
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
    "wall_seconds": 13.047,
    "throughput_per_second": 0.92,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.515,
      "median": 1.625,
      "p90": 2.687,
      "p95": 2.687,
      "max": 2.735
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.188,
      "p90": 0.36,
      "p95": 0.36,
      "max": 0.375
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.141,
      "median": 0.164,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "min": 228.0,
        "median": 232.5,
        "p90": 254.0,
        "p95": 254.0,
        "max": 286.0
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
        "median": 4.5,
        "p90": 5.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 525.0,
        "median": 553.5,
        "p90": 630.0,
        "p95": 630.0,
        "max": 685.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 856.0,
        "median": 907.0,
        "p90": 972.0,
        "p95": 972.0,
        "max": 1016.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 25.0,
        "p95": 25.0,
        "max": 26.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 37.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 85.0
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
        "median": 342.5,
        "p90": 389.0,
        "p95": 389.0,
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
        "min": 336.0,
        "median": 343.5,
        "p90": 390.0,
        "p95": 390.0,
        "max": 395.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 45.0,
        "p90": 63.0,
        "p95": 63.0,
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
        "max": 0.0
      },
      "warm_runner_exec_ms": {
        "count": 12,
        "min": 420.0,
        "median": 434.5,
        "p90": 490.0,
        "p95": 490.0,
        "max": 497.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.0,
        "p90": 67.0,
        "p95": 67.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 865.0,
        "median": 932.0,
        "p90": 983.0,
        "p95": 983.0,
        "max": 1053.0
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
    "wall_seconds": 8.735,
    "throughput_per_second": 1.374,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.656,
      "median": 1.789,
      "p90": 2.891,
      "p95": 2.891,
      "max": 3.063
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.258,
      "p90": 0.329,
      "p95": 0.329,
      "max": 0.344
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.187,
      "p90": 0.281,
      "p95": 0.281,
      "max": 0.282
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
        "median": 240.0,
        "p90": 249.0,
        "p95": 249.0,
        "max": 254.0
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
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 530.0,
        "median": 550.5,
        "p90": 589.0,
        "p95": 589.0,
        "max": 607.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 863.0,
        "median": 899.0,
        "p90": 953.0,
        "p95": 953.0,
        "max": 965.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.5,
        "p90": 14.0,
        "p95": 14.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 7.0,
        "p95": 7.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 30.0,
        "median": 36.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 103.0
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
        "median": 339.0,
        "p90": 348.0,
        "p95": 348.0,
        "max": 379.0
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
        "median": 340.0,
        "p90": 349.0,
        "p95": 349.0,
        "max": 380.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 59.5,
        "p90": 92.0,
        "p95": 92.0,
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
        "min": 417.0,
        "median": 427.0,
        "p90": 442.0,
        "p95": 442.0,
        "max": 461.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 58.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 57.0,
        "p90": 59.0,
        "p95": 59.0,
        "max": 63.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 875.0,
        "median": 913.0,
        "p90": 966.0,
        "p95": 966.0,
        "max": 981.0
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
    "wall_seconds": 9.25,
    "throughput_per_second": 1.297,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.516,
      "median": 2.203,
      "p90": 2.86,
      "p95": 2.86,
      "max": 2.906
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.203,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.313
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
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
        "min": 222.0,
        "median": 230.5,
        "p90": 258.0,
        "p95": 258.0,
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
        "min": 522.0,
        "median": 577.5,
        "p90": 713.0,
        "p95": 713.0,
        "max": 729.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 836.0,
        "median": 930.5,
        "p90": 1038.0,
        "p95": 1038.0,
        "max": 1088.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 12.0,
        "p95": 12.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 39.0,
        "p90": 83.0,
        "p95": 83.0,
        "max": 129.0
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
        "median": 341.5,
        "p90": 377.0,
        "p95": 377.0,
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
        "min": 330.0,
        "median": 342.5,
        "p90": 378.0,
        "p95": 378.0,
        "max": 381.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 40.0,
        "median": 81.5,
        "p90": 182.0,
        "p95": 182.0,
        "max": 228.0
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
        "min": 411.0,
        "median": 429.0,
        "p90": 473.0,
        "p95": 473.0,
        "max": 476.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 58.5,
        "p90": 62.0,
        "p95": 62.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 52.0,
        "median": 57.5,
        "p90": 63.0,
        "p95": 63.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 850.0,
        "median": 944.5,
        "p90": 1067.0,
        "p95": 1067.0,
        "max": 1110.0
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
    "wall_seconds": 11.141,
    "throughput_per_second": 1.077,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.547,
      "median": 2.188,
      "p90": 3.203,
      "p95": 3.203,
      "max": 3.984
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.281,
      "p90": 0.953,
      "p95": 0.953,
      "max": 1.203
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.125,
      "median": 0.266,
      "p90": 0.375,
      "p95": 0.375,
      "max": 1.188
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
        "median": 240.0,
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
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 533.0,
        "median": 574.0,
        "p90": 642.0,
        "p95": 642.0,
        "max": 649.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 857.0,
        "median": 917.5,
        "p90": 986.0,
        "p95": 986.0,
        "max": 998.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 31.0,
        "median": 35.5,
        "p90": 77.0,
        "p95": 77.0,
        "max": 82.0
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
        "median": 342.5,
        "p90": 373.0,
        "p95": 373.0,
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
        "min": 338.0,
        "median": 343.5,
        "p90": 374.0,
        "p95": 374.0,
        "max": 425.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 48.5,
        "p90": 92.0,
        "p95": 92.0,
        "max": 161.0
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
        "median": 433.5,
        "p90": 465.0,
        "p95": 465.0,
        "max": 521.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 60.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.5,
        "p90": 65.0,
        "p95": 65.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 870.0,
        "median": 931.5,
        "p90": 1003.0,
        "p95": 1003.0,
        "max": 1012.0
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
    "wall_seconds": 9.735,
    "throughput_per_second": 1.233,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.735,
      "median": 4.266,
      "p90": 5.547,
      "p95": 5.547,
      "max": 6.25
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.243,
      "p90": 0.438,
      "p95": 0.438,
      "max": 0.438
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.281
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
        "min": 228.0,
        "median": 232.0,
        "p90": 255.0,
        "p95": 255.0,
        "max": 257.0
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
        "max": 13.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 529.0,
        "median": 593.5,
        "p90": 666.0,
        "p95": 666.0,
        "max": 880.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 854.0,
        "median": 953.5,
        "p90": 993.0,
        "p95": 993.0,
        "max": 1216.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 5.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 14.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 36.5,
        "p90": 80.0,
        "p95": 80.0,
        "max": 100.0
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
        "p90": 396.0,
        "p95": 396.0,
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
        "min": 333.0,
        "median": 356.5,
        "p90": 397.0,
        "p95": 397.0,
        "max": 400.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 54.5,
        "p90": 96.0,
        "p95": 96.0,
        "max": 310.0
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
        "median": 457.0,
        "p90": 499.0,
        "p95": 499.0,
        "max": 504.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 56.0,
        "median": 61.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 64.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 82.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 867.0,
        "median": 968.0,
        "p90": 1009.0,
        "p95": 1009.0,
        "max": 1235.0
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
    "wall_seconds": 7.703,
    "throughput_per_second": 1.558,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.703,
      "median": 3.86,
      "p90": 5.203,
      "p95": 5.203,
      "max": 5.484
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.203,
      "median": 0.594,
      "p90": 0.703,
      "p95": 0.703,
      "max": 1.547
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.234,
      "p95": 0.234,
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
        "min": 225.0,
        "median": 233.0,
        "p90": 259.0,
        "p95": 259.0,
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
        "min": 4.0,
        "median": 4.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 9.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 543.0,
        "median": 575.0,
        "p90": 639.0,
        "p95": 639.0,
        "max": 706.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 868.0,
        "median": 912.0,
        "p90": 1046.0,
        "p95": 1046.0,
        "max": 1071.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 8.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.5,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 32.0,
        "median": 40.0,
        "p90": 66.0,
        "p95": 66.0,
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
        "min": 335.0,
        "median": 344.0,
        "p90": 378.0,
        "p95": 378.0,
        "max": 398.0
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
        "median": 344.5,
        "p90": 379.0,
        "p95": 379.0,
        "max": 399.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 43.0,
        "median": 62.0,
        "p90": 112.0,
        "p95": 112.0,
        "max": 221.0
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
        "median": 437.5,
        "p90": 490.0,
        "p95": 490.0,
        "max": 498.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 68.0,
        "p95": 68.0,
        "max": 80.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 56.0,
        "median": 58.5,
        "p90": 64.0,
        "p95": 64.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 881.0,
        "median": 927.0,
        "p90": 1060.0,
        "p95": 1060.0,
        "max": 1085.0
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
    "wall_seconds": 7.688,
    "throughput_per_second": 1.561,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.625,
      "median": 3.875,
      "p90": 5.5,
      "p95": 5.5,
      "max": 5.656
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.289,
      "p90": 0.406,
      "p95": 0.406,
      "max": 0.672
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.219,
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
        "min": 223.0,
        "median": 237.5,
        "p90": 251.0,
        "p95": 251.0,
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
        "min": 4.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 6.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 546.0,
        "median": 588.0,
        "p90": 707.0,
        "p95": 707.0,
        "max": 740.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 868.0,
        "median": 938.5,
        "p90": 1041.0,
        "p95": 1041.0,
        "max": 1076.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 7.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 34.0,
        "median": 37.5,
        "p90": 49.0,
        "p95": 49.0,
        "max": 82.0
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
        "median": 350.5,
        "p90": 391.0,
        "p95": 391.0,
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
        "min": 332.0,
        "median": 351.5,
        "p90": 392.0,
        "p95": 392.0,
        "max": 395.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 40.0,
        "median": 69.5,
        "p90": 172.0,
        "p95": 172.0,
        "max": 176.0
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
        "median": 445.0,
        "p90": 493.0,
        "p95": 493.0,
        "max": 502.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 58.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.5,
        "p90": 61.0,
        "p95": 61.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 888.0,
        "median": 956.5,
        "p90": 1051.0,
        "p95": 1051.0,
        "max": 1092.0
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
    "wall_seconds": 7.5,
    "throughput_per_second": 1.6,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.734,
      "median": 4.907,
      "p90": 6.766,
      "p95": 6.766,
      "max": 7.172
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.266,
      "median": 0.329,
      "p90": 0.859,
      "p95": 0.859,
      "max": 0.906
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.281,
      "p95": 0.281,
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
        "min": 220.0,
        "median": 233.5,
        "p90": 250.0,
        "p95": 250.0,
        "max": 252.0
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
        "max": 8.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 533.0,
        "median": 568.5,
        "p90": 610.0,
        "p95": 610.0,
        "max": 736.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 854.0,
        "median": 917.0,
        "p90": 961.0,
        "p95": 961.0,
        "max": 1069.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 11.0
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
        "min": 32.0,
        "median": 35.5,
        "p90": 44.0,
        "p95": 44.0,
        "max": 65.0
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
        "median": 339.5,
        "p90": 367.0,
        "p95": 367.0,
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
        "median": 340.5,
        "p90": 368.0,
        "p95": 368.0,
        "max": 407.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 40.0,
        "median": 55.0,
        "p90": 126.0,
        "p95": 126.0,
        "max": 246.0
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
        "median": 431.5,
        "p90": 463.0,
        "p95": 463.0,
        "max": 503.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.5,
        "p90": 61.0,
        "p95": 61.0,
        "max": 61.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 66.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 868.0,
        "median": 934.0,
        "p90": 975.0,
        "p95": 975.0,
        "max": 1084.0
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
    "wall_seconds": 9.312,
    "throughput_per_second": 1.289,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 2.89,
      "median": 5.75,
      "p90": 7.5,
      "p95": 7.5,
      "max": 8.703
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.39,
      "p90": 0.547,
      "p95": 0.547,
      "max": 0.641
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.172,
      "median": 0.328,
      "p90": 1.312,
      "p95": 1.312,
      "max": 1.313
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
        "median": 230.0,
        "p90": 260.0,
        "p95": 260.0,
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
        "min": 4.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 530.0,
        "median": 600.0,
        "p90": 1060.0,
        "p95": 1060.0,
        "max": 1084.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 847.0,
        "median": 951.0,
        "p90": 1378.0,
        "p95": 1378.0,
        "max": 1451.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 2.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 18.0
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
        "min": 31.0,
        "median": 34.5,
        "p90": 56.0,
        "p95": 56.0,
        "max": 143.0
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
        "median": 370.0,
        "p90": 409.0,
        "p95": 409.0,
        "max": 423.0
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
        "median": 371.0,
        "p90": 410.0,
        "p95": 410.0,
        "max": 424.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 42.0,
        "median": 49.0,
        "p90": 506.0,
        "p95": 506.0,
        "max": 579.0
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
        "median": 465.0,
        "p90": 518.0,
        "p95": 518.0,
        "max": 522.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 55.0,
        "median": 59.5,
        "p90": 72.0,
        "p95": 72.0,
        "max": 74.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 859.0,
        "median": 965.5,
        "p90": 1405.0,
        "p95": 1405.0,
        "max": 1467.0
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
    "wall_seconds": 8.641,
    "throughput_per_second": 1.389,
    "successes": 12,
    "failures": 0,
    "terminal_seconds": {
      "count": 12,
      "min": 1.75,
      "median": 5.18,
      "p90": 7.188,
      "p95": 7.188,
      "max": 8.328
    },
    "accept_seconds": {
      "count": 12,
      "min": 0.188,
      "median": 0.36,
      "p90": 0.531,
      "p95": 0.531,
      "max": 0.547
    },
    "output_download_seconds": {
      "count": 12,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.313
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
        "median": 229.0,
        "p90": 258.0,
        "p95": 258.0,
        "max": 271.0
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
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 12,
        "min": 525.0,
        "median": 586.0,
        "p90": 825.0,
        "p95": 825.0,
        "max": 878.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 12,
        "min": 847.0,
        "median": 949.5,
        "p90": 1145.0,
        "p95": 1145.0,
        "max": 1261.0
      },
      "orchestrator_claim_ms": {
        "count": 12,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 12,
        "min": 4.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 15.0
      },
      "output_upload_ms": {
        "count": 12,
        "min": 33.0,
        "median": 37.0,
        "p90": 83.0,
        "p95": 83.0,
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
        "min": 332.0,
        "median": 344.0,
        "p90": 384.0,
        "p95": 384.0,
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
        "min": 333.0,
        "median": 345.0,
        "p90": 385.0,
        "p95": 385.0,
        "max": 396.0
      },
      "sandbox_prepare_ms": {
        "count": 12,
        "min": 39.0,
        "median": 56.5,
        "p90": 336.0,
        "p95": 336.0,
        "max": 353.0
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
        "median": 430.0,
        "p90": 488.0,
        "p95": 488.0,
        "max": 500.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 12,
        "min": 54.0,
        "median": 57.5,
        "p90": 61.0,
        "p95": 61.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 12,
        "min": 53.0,
        "median": 58.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 12,
        "min": 860.0,
        "median": 964.5,
        "p90": 1163.0,
        "p95": 1163.0,
        "max": 1282.0
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
    "wall_seconds": 17.157,
    "throughput_per_second": 0.874,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.391,
      "median": 2.375,
      "p90": 2.828,
      "p95": 2.828,
      "max": 3.219
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.531,
      "p95": 0.531,
      "max": 1.172
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.218,
      "median": 0.218,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.218
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
        "median": 27.0,
        "p90": 32.0,
        "p95": 32.0,
        "max": 34.0
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
        "min": 515.0,
        "median": 801.0,
        "p90": 1806.0,
        "p95": 1806.0,
        "max": 1814.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 573.0,
        "median": 888.0,
        "p90": 1993.0,
        "p95": 1993.0,
        "max": 2010.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 17.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
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
        "p90": 173.0,
        "p95": 173.0,
        "max": 179.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 333.0,
        "median": 342.0,
        "p90": 385.0,
        "p95": 385.0,
        "max": 388.0
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
        "median": 376.0,
        "p90": 1340.0,
        "p95": 1340.0,
        "max": 1357.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 18.0,
        "median": 24.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 50.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 232.0,
        "median": 260.0,
        "p90": 274.0,
        "p95": 282.0,
        "max": 282.0
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
        "p90": 141.0,
        "p95": 141.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 420.0,
        "median": 466.0,
        "p90": 1429.0,
        "p95": 1429.0,
        "max": 1448.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 59.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 71.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 584.0,
        "median": 904.0,
        "p90": 2009.0,
        "p95": 2009.0,
        "max": 2030.0
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
    "wall_seconds": 16.891,
    "throughput_per_second": 0.888,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.454,
      "median": 1.656,
      "p90": 3.953,
      "p95": 3.953,
      "max": 4.062
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.187,
      "p90": 1.172,
      "p95": 1.172,
      "max": 1.188
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
        "max": 240.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 30.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 505.0,
        "median": 597.0,
        "p90": 1827.0,
        "p95": 1827.0,
        "max": 1838.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 559.0,
        "median": 661.0,
        "p90": 2037.0,
        "p95": 2037.0,
        "max": 2054.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 15.0
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
        "p90": 172.0,
        "p95": 172.0,
        "max": 189.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 330.0,
        "median": 349.0,
        "p90": 393.0,
        "p95": 393.0,
        "max": 420.0
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
        "median": 387.0,
        "p90": 1350.0,
        "p95": 1350.0,
        "max": 1361.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 20.0,
        "median": 24.0,
        "p90": 36.0,
        "p95": 36.0,
        "max": 53.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 208.0,
        "median": 216.0,
        "p90": 257.0,
        "p95": 257.0,
        "max": 257.0
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
        "p90": 144.0,
        "p95": 144.0,
        "max": 152.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 416.0,
        "median": 479.0,
        "p90": 1445.0,
        "p95": 1445.0,
        "max": 1457.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 52.0,
        "median": 58.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 53.0,
        "median": 61.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 571.0,
        "median": 680.0,
        "p90": 2049.0,
        "p95": 2049.0,
        "max": 2066.0
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
    "wall_seconds": 18.719,
    "throughput_per_second": 0.801,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.422,
      "median": 1.844,
      "p90": 3.953,
      "p95": 3.953,
      "max": 4.781
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.203,
      "p90": 0.516,
      "p95": 0.516,
      "max": 1.14
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.25,
      "median": 0.25,
      "p90": 0.25,
      "p95": 0.25,
      "max": 0.25
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
        "max": 253.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 33.0,
        "p95": 33.0,
        "max": 38.0
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
        "min": 510.0,
        "median": 593.0,
        "p90": 1755.0,
        "p95": 1755.0,
        "max": 1837.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 566.0,
        "median": 675.0,
        "p90": 1948.0,
        "p95": 1948.0,
        "max": 2076.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
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
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 166.0,
        "p95": 166.0,
        "max": 177.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 333.0,
        "median": 359.0,
        "p90": 396.0,
        "p95": 396.0,
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
        "min": 334.0,
        "median": 378.0,
        "p90": 1338.0,
        "p95": 1338.0,
        "max": 1366.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 24.0,
        "p90": 57.0,
        "p95": 57.0,
        "max": 89.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 212.0,
        "median": 235.5,
        "p90": 257.0,
        "p95": 257.0,
        "max": 257.0
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
        "p90": 128.0,
        "p95": 128.0,
        "max": 170.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 417.0,
        "median": 469.0,
        "p90": 1430.0,
        "p95": 1430.0,
        "max": 1465.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 60.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 74.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 60.0,
        "p90": 70.0,
        "p95": 70.0,
        "max": 77.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 577.0,
        "median": 693.0,
        "p90": 1960.0,
        "p95": 1960.0,
        "max": 2090.0
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
    "wall_seconds": 10.328,
    "throughput_per_second": 1.452,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.484,
      "median": 2.656,
      "p90": 3.782,
      "p95": 3.782,
      "max": 3.906
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.281,
      "p95": 0.281,
      "max": 0.297
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
        "max": 241.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 37.0,
        "p95": 37.0,
        "max": 45.0
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
        "min": 511.0,
        "median": 577.0,
        "p90": 1521.0,
        "p95": 1521.0,
        "max": 1842.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 565.0,
        "median": 642.0,
        "p90": 1577.0,
        "p95": 1577.0,
        "max": 2059.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
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
        "p90": 201.0,
        "p95": 201.0,
        "max": 205.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 355.0,
        "p90": 399.0,
        "p95": 399.0,
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
        "min": 337.0,
        "median": 382.0,
        "p90": 1343.0,
        "p95": 1343.0,
        "max": 1390.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 19.0,
        "median": 26.0,
        "p90": 45.0,
        "p95": 45.0,
        "max": 55.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 230.0,
        "median": 236.0,
        "p90": 239.0,
        "p95": 239.0,
        "max": 239.0
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
        "p90": 137.0,
        "p95": 137.0,
        "max": 156.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 419.0,
        "median": 476.0,
        "p90": 1431.0,
        "p95": 1431.0,
        "max": 1483.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 56.0,
        "median": 59.0,
        "p90": 69.0,
        "p95": 69.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 576.0,
        "median": 652.0,
        "p90": 1589.0,
        "p95": 1589.0,
        "max": 2072.0
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
    "wall_seconds": 11.422,
    "throughput_per_second": 1.313,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.453,
      "median": 2.625,
      "p90": 4.937,
      "p95": 4.937,
      "max": 5.0
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.141,
      "median": 0.157,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.188
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
        "max": 237.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 38.0
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
        "min": 514.0,
        "median": 554.0,
        "p90": 1812.0,
        "p95": 1812.0,
        "max": 1880.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 568.0,
        "median": 619.0,
        "p90": 2022.0,
        "p95": 2022.0,
        "max": 2085.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
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
        "max": 1.0
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
        "min": 330.0,
        "median": 343.0,
        "p90": 381.0,
        "p95": 381.0,
        "max": 387.0
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
        "median": 351.0,
        "p90": 1360.0,
        "p95": 1360.0,
        "max": 1382.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 28.0,
        "p90": 34.0,
        "p95": 34.0,
        "max": 41.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 239.0,
        "median": 242.0,
        "p90": 265.0,
        "p95": 265.0,
        "max": 265.0
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
        "p90": 144.0,
        "p95": 144.0,
        "max": 144.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 428.0,
        "median": 443.0,
        "p90": 1449.0,
        "p95": 1449.0,
        "max": 1483.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 51.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 58.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 581.0,
        "median": 630.0,
        "p90": 2035.0,
        "p95": 2035.0,
        "max": 2100.0
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
    "wall_seconds": 12.25,
    "throughput_per_second": 1.224,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.438,
      "median": 2.75,
      "p90": 4.61,
      "p95": 4.61,
      "max": 5.031
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.14,
      "median": 0.203,
      "p90": 1.187,
      "p95": 1.187,
      "max": 1.343
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.188,
      "median": 0.188,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.188
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
        "max": 229.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 32.0,
        "p95": 32.0,
        "max": 33.0
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
        "min": 516.0,
        "median": 595.0,
        "p90": 1835.0,
        "p95": 1835.0,
        "max": 1847.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 571.0,
        "median": 655.0,
        "p90": 2047.0,
        "p95": 2047.0,
        "max": 2067.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
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
        "p90": 174.0,
        "p95": 174.0,
        "max": 213.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 329.0,
        "median": 355.0,
        "p90": 386.0,
        "p95": 386.0,
        "max": 392.0
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
        "min": 341.0,
        "median": 377.0,
        "p90": 1350.0,
        "p95": 1350.0,
        "max": 1387.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 19.0,
        "median": 30.0,
        "p90": 52.0,
        "p95": 52.0,
        "max": 57.0
      },
      "warm_container_create_ms": {
        "count": 5,
        "min": 229.0,
        "median": 234.0,
        "p90": 258.0,
        "p95": 258.0,
        "max": 258.0
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
        "p90": 148.0,
        "p95": 148.0,
        "max": 159.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 428.0,
        "median": 469.0,
        "p90": 1453.0,
        "p95": 1453.0,
        "max": 1484.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 54.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 60.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 80.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 581.0,
        "median": 671.0,
        "p90": 2057.0,
        "p95": 2057.0,
        "max": 2080.0
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
    "wall_seconds": 9.531,
    "throughput_per_second": 1.574,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.938,
      "median": 4.454,
      "p90": 5.688,
      "p95": 5.688,
      "max": 6.829
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.156,
      "median": 0.219,
      "p90": 0.719,
      "p95": 0.719,
      "max": 0.719
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.188,
      "median": 0.188,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.188
    },
    "workers": {
      "worker-1": 8,
      "worker-2": 7
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
        "max": 232.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 40.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 509.0,
        "median": 646.0,
        "p90": 1577.0,
        "p95": 1577.0,
        "max": 1961.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 566.0,
        "median": 708.0,
        "p90": 1631.0,
        "p95": 1631.0,
        "max": 2186.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 4.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
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
        "p90": 182.0,
        "p95": 182.0,
        "max": 196.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 333.0,
        "median": 344.0,
        "p90": 410.0,
        "p95": 410.0,
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
        "min": 334.0,
        "median": 379.0,
        "p90": 1361.0,
        "p95": 1361.0,
        "max": 1392.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 18.0,
        "median": 25.0,
        "p90": 120.0,
        "p95": 120.0,
        "max": 335.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 235.0,
        "median": 256.0,
        "p90": 290.0,
        "p95": 290.0,
        "max": 290.0
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
        "p90": 142.0,
        "p95": 142.0,
        "max": 156.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 417.0,
        "median": 472.0,
        "p90": 1456.0,
        "p95": 1456.0,
        "max": 1488.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 67.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 55.0,
        "median": 61.0,
        "p90": 79.0,
        "p95": 79.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 581.0,
        "median": 722.0,
        "p90": 1639.0,
        "p95": 1639.0,
        "max": 2199.0
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
    "wall_seconds": 9.141,
    "throughput_per_second": 1.641,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.656,
      "median": 3.937,
      "p90": 5.39,
      "p95": 5.39,
      "max": 6.609
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.156,
      "median": 0.218,
      "p90": 0.328,
      "p95": 0.328,
      "max": 0.344
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
        "max": 234.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 27.0,
        "max": 30.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 4.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 504.0,
        "median": 590.0,
        "p90": 1539.0,
        "p95": 1539.0,
        "max": 1871.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 557.0,
        "median": 664.0,
        "p90": 1606.0,
        "p95": 1606.0,
        "max": 1949.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 11.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 77.0
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
        "max": 194.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 346.0,
        "p90": 387.0,
        "p95": 387.0,
        "max": 394.0
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
        "median": 351.0,
        "p90": 1347.0,
        "p95": 1347.0,
        "max": 1350.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 21.0,
        "median": 31.0,
        "p90": 61.0,
        "p95": 61.0,
        "max": 62.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 231.0,
        "median": 256.0,
        "p90": 264.0,
        "p95": 264.0,
        "max": 264.0
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
        "p90": 119.0,
        "p95": 119.0,
        "max": 137.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 418.0,
        "median": 458.0,
        "p90": 1440.0,
        "p95": 1440.0,
        "max": 1443.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 52.0,
        "median": 59.0,
        "p90": 77.0,
        "p95": 77.0,
        "max": 79.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 52.0,
        "median": 60.0,
        "p90": 74.0,
        "p95": 74.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 570.0,
        "median": 680.0,
        "p90": 1630.0,
        "p95": 1630.0,
        "max": 1960.0
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
    "wall_seconds": 10.516,
    "throughput_per_second": 1.426,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.469,
      "median": 4.219,
      "p90": 6.453,
      "p95": 6.453,
      "max": 6.468
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.312,
      "p95": 0.312,
      "max": 0.516
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.265,
      "median": 0.265,
      "p90": 0.265,
      "p95": 0.265,
      "max": 0.265
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
        "max": 226.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 27.0,
        "max": 28.0
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
        "min": 497.0,
        "median": 568.0,
        "p90": 1818.0,
        "p95": 1818.0,
        "max": 1847.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 553.0,
        "median": 628.0,
        "p90": 2015.0,
        "p95": 2015.0,
        "max": 2048.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
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
        "p90": 193.0,
        "p95": 193.0,
        "max": 202.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 331.0,
        "median": 357.0,
        "p90": 383.0,
        "p95": 383.0,
        "max": 385.0
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
        "median": 376.0,
        "p90": 1359.0,
        "p95": 1359.0,
        "max": 1386.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 20.0,
        "median": 25.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 87.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 222.0,
        "median": 238.0,
        "p90": 241.0,
        "p95": 241.0,
        "max": 241.0
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
        "p90": 131.0,
        "p95": 131.0,
        "max": 139.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 415.0,
        "median": 471.0,
        "p90": 1462.0,
        "p95": 1462.0,
        "max": 1481.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 56.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 72.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 55.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 568.0,
        "median": 645.0,
        "p90": 2031.0,
        "p95": 2031.0,
        "max": 2066.0
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
    "wall_seconds": 9.219,
    "throughput_per_second": 1.627,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.875,
      "median": 6.657,
      "p90": 9.125,
      "p95": 9.125,
      "max": 9.204
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.281,
      "median": 0.422,
      "p90": 0.61,
      "p95": 0.61,
      "max": 0.625
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
        "max": 225.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 27.0,
        "max": 35.0
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
        "min": 502.0,
        "median": 612.0,
        "p90": 1749.0,
        "p95": 1749.0,
        "max": 1873.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 555.0,
        "median": 672.0,
        "p90": 1815.0,
        "p95": 1815.0,
        "max": 2084.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
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
        "max": 57.0
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
        "max": 190.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 328.0,
        "median": 363.0,
        "p90": 387.0,
        "p95": 387.0,
        "max": 391.0
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
        "min": 329.0,
        "median": 380.0,
        "p90": 1363.0,
        "p95": 1363.0,
        "max": 1385.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 18.0,
        "median": 38.0,
        "p90": 227.0,
        "p95": 227.0,
        "max": 266.0
      },
      "warm_container_create_ms": {
        "count": 3,
        "min": 223.0,
        "median": 249.0,
        "p90": 265.0,
        "p95": 265.0,
        "max": 265.0
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
        "p90": 137.0,
        "p95": 137.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 412.0,
        "median": 472.0,
        "p90": 1457.0,
        "p95": 1457.0,
        "max": 1481.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 59.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 55.0,
        "median": 60.0,
        "p90": 68.0,
        "p95": 68.0,
        "max": 70.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 564.0,
        "median": 706.0,
        "p90": 1828.0,
        "p95": 1828.0,
        "max": 2098.0
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
    "wall_seconds": 9.515,
    "throughput_per_second": 1.576,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 1.969,
      "median": 5.687,
      "p90": 9.437,
      "p95": 9.437,
      "max": 9.5
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.187,
      "median": 0.312,
      "p90": 0.594,
      "p95": 0.594,
      "max": 0.609
    },
    "output_download_seconds": {
      "count": 1,
      "min": 0.125,
      "median": 0.125,
      "p90": 0.125,
      "p95": 0.125,
      "max": 0.125
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
        "max": 251.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 29.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 15,
        "min": 3.0,
        "median": 3.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 15,
        "min": 508.0,
        "median": 604.0,
        "p90": 1856.0,
        "p95": 1856.0,
        "max": 1877.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 569.0,
        "median": 662.0,
        "p90": 1942.0,
        "p95": 1942.0,
        "max": 2097.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 3.0,
        "median": 5.0,
        "p90": 22.0,
        "p95": 22.0,
        "max": 23.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 6.0,
        "p90": 12.0,
        "p95": 12.0,
        "max": 14.0
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
        "p90": 167.0,
        "p95": 167.0,
        "max": 170.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 330.0,
        "median": 367.0,
        "p90": 402.0,
        "p95": 402.0,
        "max": 403.0
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
        "min": 334.0,
        "median": 393.0,
        "p90": 1356.0,
        "p95": 1356.0,
        "max": 1363.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 20.0,
        "median": 39.0,
        "p90": 359.0,
        "p95": 359.0,
        "max": 379.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 238.0,
        "median": 243.5,
        "p90": 266.0,
        "p95": 266.0,
        "max": 266.0
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
        "p90": 149.0,
        "p95": 149.0,
        "max": 175.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 414.0,
        "median": 484.0,
        "p90": 1452.0,
        "p95": 1452.0,
        "max": 1459.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 53.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 54.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 66.0,
        "max": 69.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 588.0,
        "median": 685.0,
        "p90": 1971.0,
        "p95": 1971.0,
        "max": 2114.0
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
    "wall_seconds": 10.079,
    "throughput_per_second": 1.488,
    "successes": 15,
    "failures": 0,
    "terminal_seconds": {
      "count": 15,
      "min": 2.079,
      "median": 6.407,
      "p90": 9.985,
      "p95": 9.985,
      "max": 10.079
    },
    "accept_seconds": {
      "count": 15,
      "min": 0.297,
      "median": 0.547,
      "p90": 0.704,
      "p95": 0.704,
      "max": 0.719
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
        "max": 227.0
      },
      "docker_image_pull_ms": {
        "count": 15,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 30.0,
        "max": 34.0
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
        "min": 504.0,
        "median": 599.0,
        "p90": 1807.0,
        "p95": 1807.0,
        "max": 1907.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 15,
        "min": 561.0,
        "median": 657.0,
        "p90": 2018.0,
        "p95": 2018.0,
        "max": 2130.0
      },
      "orchestrator_claim_ms": {
        "count": 15,
        "min": 2.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 15,
        "min": 4.0,
        "median": 5.0,
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
        "max": 66.0
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
        "max": 196.0
      },
      "runner_module_imports_ms": {
        "count": 15,
        "min": 332.0,
        "median": 355.0,
        "p90": 386.0,
        "p95": 386.0,
        "max": 394.0
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
        "median": 376.0,
        "p90": 1357.0,
        "p95": 1357.0,
        "max": 1395.0
      },
      "sandbox_prepare_ms": {
        "count": 15,
        "min": 22.0,
        "median": 32.0,
        "p90": 113.0,
        "p95": 113.0,
        "max": 176.0
      },
      "warm_container_create_ms": {
        "count": 4,
        "min": 210.0,
        "median": 230.5,
        "p90": 256.0,
        "p95": 256.0,
        "max": 256.0
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
        "p90": 149.0,
        "p95": 149.0,
        "max": 151.0
      },
      "warm_runner_exec_ms": {
        "count": 15,
        "min": 420.0,
        "median": 471.0,
        "p90": 1456.0,
        "p95": 1456.0,
        "max": 1495.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 15,
        "min": 55.0,
        "median": 61.0,
        "p90": 71.0,
        "p95": 71.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 15,
        "min": 52.0,
        "median": 61.0,
        "p90": 64.0,
        "p95": 64.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 15,
        "min": 572.0,
        "median": 666.0,
        "p90": 2031.0,
        "p95": 2031.0,
        "max": 2144.0
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
    "wall_seconds": 32.156,
    "throughput_per_second": 0.933,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.453,
      "median": 1.751,
      "p90": 2.828,
      "p95": 3.219,
      "max": 3.312
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.235,
      "p95": 0.391,
      "max": 0.469
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
        "p95": 242.0,
        "max": 269.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 32.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 502.0,
        "median": 577.5,
        "p90": 1506.0,
        "p95": 1857.0,
        "max": 1871.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 556.0,
        "median": 641.5,
        "p90": 1576.0,
        "p95": 2069.0,
        "max": 2072.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 11.0,
        "p95": 16.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 6.0,
        "p95": 9.0,
        "max": 10.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 40.0,
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
        "p95": 169.0,
        "max": 170.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 327.0,
        "median": 344.0,
        "p90": 393.0,
        "p95": 397.0,
        "max": 425.0
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
        "median": 388.0,
        "p90": 1335.0,
        "p95": 1375.0,
        "max": 1398.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 19.0,
        "median": 23.5,
        "p90": 41.0,
        "p95": 46.0,
        "max": 70.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 211.0,
        "median": 243.5,
        "p90": 260.0,
        "p95": 292.0,
        "max": 292.0
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
        "p90": 129.0,
        "p95": 145.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 417.0,
        "median": 484.5,
        "p90": 1420.0,
        "p95": 1467.0,
        "max": 1492.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.0,
        "p90": 68.0,
        "p95": 70.0,
        "max": 78.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 57.0,
        "p90": 65.0,
        "p95": 65.0,
        "max": 68.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 574.0,
        "median": 654.0,
        "p90": 1588.0,
        "p95": 2079.0,
        "max": 2086.0
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
    "wall_seconds": 34.25,
    "throughput_per_second": 0.876,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.437,
      "median": 1.805,
      "p90": 3.281,
      "p95": 3.86,
      "max": 3.921
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.171,
      "p90": 0.593,
      "p95": 0.688,
      "max": 0.844
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.156,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
    },
    "workers": {
      "worker-1": 13,
      "worker-2": 17
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
        "p95": 229.0,
        "max": 260.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 36.0,
        "max": 39.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 504.0,
        "median": 598.5,
        "p90": 1562.0,
        "p95": 1847.0,
        "max": 1854.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 561.0,
        "median": 658.5,
        "p90": 1620.0,
        "p95": 2058.0,
        "max": 2061.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 2.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 12.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 41.0,
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
        "p95": 180.0,
        "max": 187.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 328.0,
        "median": 363.0,
        "p90": 391.0,
        "p95": 409.0,
        "max": 417.0
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
        "min": 339.0,
        "median": 388.0,
        "p90": 1340.0,
        "p95": 1373.0,
        "max": 1378.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 26.0,
        "p90": 46.0,
        "p95": 62.0,
        "max": 63.0
      },
      "warm_container_create_ms": {
        "count": 8,
        "min": 219.0,
        "median": 248.0,
        "p90": 252.0,
        "p95": 274.0,
        "max": 274.0
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
        "p90": 132.0,
        "p95": 139.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 424.0,
        "median": 487.0,
        "p90": 1435.0,
        "p95": 1464.0,
        "max": 1480.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.0,
        "p90": 65.0,
        "p95": 67.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 60.5,
        "p90": 68.0,
        "p95": 72.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 572.0,
        "median": 671.5,
        "p90": 1631.0,
        "p95": 2077.0,
        "max": 2078.0
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
    "wall_seconds": 30.782,
    "throughput_per_second": 0.975,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.438,
      "median": 1.508,
      "p90": 2.672,
      "p95": 2.828,
      "max": 2.891
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.188,
      "p95": 0.188,
      "max": 0.391
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
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
        "p95": 243.0,
        "max": 256.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 36.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 497.0,
        "median": 580.5,
        "p90": 1571.0,
        "p95": 1580.0,
        "max": 1609.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 550.0,
        "median": 641.5,
        "p90": 1635.0,
        "p95": 1643.0,
        "max": 1673.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 12.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 10.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 39.0,
        "max": 44.0
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
        "p95": 179.0,
        "max": 180.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 329.0,
        "median": 341.5,
        "p90": 394.0,
        "p95": 406.0,
        "max": 411.0
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
        "median": 361.5,
        "p90": 1366.0,
        "p95": 1383.0,
        "max": 1399.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 25.0,
        "p90": 41.0,
        "p95": 49.0,
        "max": 55.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 219.0,
        "median": 249.5,
        "p90": 254.0,
        "p95": 290.0,
        "max": 290.0
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
        "p95": 129.0,
        "max": 142.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 413.0,
        "median": 456.5,
        "p90": 1472.0,
        "p95": 1484.0,
        "max": 1505.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 59.0,
        "p90": 63.0,
        "p95": 63.0,
        "max": 64.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 72.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 562.0,
        "median": 657.0,
        "p90": 1646.0,
        "p95": 1658.0,
        "max": 1691.0
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
    "wall_seconds": 20.047,
    "throughput_per_second": 1.496,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.453,
      "median": 2.617,
      "p90": 3.813,
      "p95": 4.171,
      "max": 5.0
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.203,
      "p95": 0.25,
      "max": 0.5
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.188,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.218
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
        "p95": 249.0,
        "max": 251.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 35.0,
        "max": 40.0
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
        "min": 499.0,
        "median": 576.0,
        "p90": 1541.0,
        "p95": 1604.0,
        "max": 1612.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 556.0,
        "median": 637.0,
        "p90": 1606.0,
        "p95": 1666.0,
        "max": 1673.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 13.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
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
        "p95": 82.0,
        "max": 87.0
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
        "p95": 177.0,
        "max": 190.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 328.0,
        "median": 348.5,
        "p90": 395.0,
        "p95": 406.0,
        "max": 410.0
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
        "min": 329.0,
        "median": 363.0,
        "p90": 1347.0,
        "p95": 1402.0,
        "max": 1407.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 30.5,
        "p90": 59.0,
        "p95": 70.0,
        "max": 72.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 231.0,
        "median": 237.0,
        "p90": 265.0,
        "p95": 266.0,
        "max": 266.0
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
        "p90": 128.0,
        "p95": 133.0,
        "max": 138.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 415.0,
        "median": 461.0,
        "p90": 1440.0,
        "p95": 1499.0,
        "max": 1504.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 59.5,
        "p90": 66.0,
        "p95": 72.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 59.5,
        "p90": 68.0,
        "p95": 74.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 569.0,
        "median": 656.0,
        "p90": 1620.0,
        "p95": 1683.0,
        "max": 1688.0
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
    "wall_seconds": 20.109,
    "throughput_per_second": 1.492,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.438,
      "median": 2.632,
      "p90": 3.765,
      "p95": 3.812,
      "max": 4.922
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.188,
      "p95": 0.203,
      "max": 0.203
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.14,
      "median": 0.188,
      "p90": 0.218,
      "p95": 0.218,
      "max": 0.218
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
        "p95": 234.0,
        "max": 252.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 28.0,
        "p95": 31.0,
        "max": 35.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 491.0,
        "median": 572.0,
        "p90": 1566.0,
        "p95": 1583.0,
        "max": 1644.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 548.0,
        "median": 632.5,
        "p90": 1624.0,
        "p95": 1652.0,
        "max": 1711.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 9.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 32.0,
        "max": 33.0
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
        "max": 188.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 328.0,
        "median": 350.0,
        "p90": 390.0,
        "p95": 403.0,
        "max": 416.0
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
        "min": 329.0,
        "median": 366.5,
        "p90": 1384.0,
        "p95": 1392.0,
        "max": 1418.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 19.0,
        "median": 24.5,
        "p90": 47.0,
        "p95": 58.0,
        "max": 73.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 228.0,
        "median": 241.5,
        "p90": 256.0,
        "p95": 277.0,
        "max": 277.0
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
        "p90": 123.0,
        "p95": 131.0,
        "max": 140.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 414.0,
        "median": 458.5,
        "p90": 1479.0,
        "p95": 1491.0,
        "max": 1519.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 52.0,
        "median": 57.5,
        "p90": 64.0,
        "p95": 72.0,
        "max": 78.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 71.0,
        "max": 72.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 558.0,
        "median": 645.5,
        "p90": 1636.0,
        "p95": 1666.0,
        "max": 1723.0
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
    "wall_seconds": 21.0,
    "throughput_per_second": 1.429,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.453,
      "median": 2.649,
      "p90": 3.563,
      "p95": 3.875,
      "max": 3.906
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.125,
      "median": 0.157,
      "p90": 0.782,
      "p95": 0.813,
      "max": 0.829
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.172,
      "p90": 0.187,
      "p95": 0.187,
      "max": 0.187
    },
    "workers": {
      "worker-1": 15,
      "worker-2": 15
    },
    "cold_starts": 10,
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
        "p95": 241.0,
        "max": 247.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 30.0,
        "max": 31.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 501.0,
        "median": 765.0,
        "p90": 1570.0,
        "p95": 1604.0,
        "max": 1620.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 557.0,
        "median": 868.0,
        "p90": 1631.0,
        "p95": 1672.0,
        "max": 1680.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.5,
        "p90": 7.0,
        "p95": 12.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 11.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
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
        "p95": 168.0,
        "max": 178.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 331.0,
        "median": 357.5,
        "p90": 394.0,
        "p95": 405.0,
        "max": 450.0
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
        "median": 377.0,
        "p90": 1378.0,
        "p95": 1398.0,
        "max": 1406.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 29.0,
        "p90": 41.0,
        "p95": 88.0,
        "max": 167.0
      },
      "warm_container_create_ms": {
        "count": 10,
        "min": 216.0,
        "median": 229.5,
        "p90": 260.0,
        "p95": 269.0,
        "max": 269.0
      },
      "warm_container_reused": {
        "count": 20,
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
        "p95": 141.0,
        "max": 147.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 411.0,
        "median": 472.0,
        "p90": 1471.0,
        "p95": 1505.0,
        "max": 1513.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 52.0,
        "median": 59.0,
        "p90": 70.0,
        "p95": 71.0,
        "max": 76.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 52.0,
        "median": 60.0,
        "p90": 67.0,
        "p95": 71.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 572.0,
        "median": 885.5,
        "p90": 1644.0,
        "p95": 1689.0,
        "max": 1698.0
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
    "wall_seconds": 18.063,
    "throughput_per_second": 1.661,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 2.125,
      "median": 4.172,
      "p90": 5.172,
      "p95": 6.078,
      "max": 6.25
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.14,
      "median": 0.211,
      "p90": 0.422,
      "p95": 0.453,
      "max": 0.453
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.141,
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
        "p95": 226.0,
        "max": 229.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 26.0,
        "p95": 32.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 501.0,
        "median": 613.5,
        "p90": 1524.0,
        "p95": 1602.0,
        "max": 1614.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 555.0,
        "median": 673.5,
        "p90": 1579.0,
        "p95": 1661.0,
        "max": 1683.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 7.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 34.0,
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
        "p95": 179.0,
        "max": 184.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 344.0,
        "p90": 376.0,
        "p95": 385.0,
        "max": 392.0
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
        "median": 370.0,
        "p90": 1334.0,
        "p95": 1362.0,
        "max": 1363.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 40.5,
        "p90": 97.0,
        "p95": 126.0,
        "max": 182.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 210.0,
        "median": 228.5,
        "p90": 237.0,
        "p95": 241.0,
        "max": 241.0
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
        "p90": 131.0,
        "p95": 133.0,
        "max": 142.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 417.0,
        "median": 464.5,
        "p90": 1419.0,
        "p95": 1454.0,
        "max": 1457.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 58.0,
        "p90": 64.0,
        "p95": 68.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 58.5,
        "p90": 66.0,
        "p95": 69.0,
        "max": 90.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 568.0,
        "median": 689.5,
        "p90": 1598.0,
        "p95": 1684.0,
        "max": 1702.0
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
    "wall_seconds": 19.468,
    "throughput_per_second": 1.541,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.5,
      "median": 4.453,
      "p90": 6.203,
      "p95": 6.313,
      "max": 6.343
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.125,
      "median": 0.172,
      "p90": 0.218,
      "p95": 0.265,
      "max": 0.281
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.156,
      "p90": 0.172,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 14,
      "worker-2": 16
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
        "p95": 255.0,
        "max": 259.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 34.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 500.0,
        "median": 583.5,
        "p90": 1524.0,
        "p95": 1642.0,
        "max": 1670.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 556.0,
        "median": 647.5,
        "p90": 1580.0,
        "p95": 1709.0,
        "max": 1734.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 2.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 7.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.5,
        "p90": 10.0,
        "p95": 12.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 34.0,
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
        "p95": 177.0,
        "max": 191.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 357.0,
        "p90": 393.0,
        "p95": 402.0,
        "max": 434.0
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
        "median": 373.5,
        "p90": 1347.0,
        "p95": 1396.0,
        "max": 1435.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 18.0,
        "median": 26.5,
        "p90": 51.0,
        "p95": 90.0,
        "max": 93.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 225.0,
        "median": 228.5,
        "p90": 243.0,
        "p95": 262.0,
        "max": 262.0
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
        "min": 415.0,
        "median": 467.5,
        "p90": 1434.0,
        "p95": 1509.0,
        "max": 1541.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 54.0,
        "median": 59.5,
        "p90": 70.0,
        "p95": 73.0,
        "max": 73.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 59.0,
        "p90": 68.0,
        "p95": 72.0,
        "max": 78.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 567.0,
        "median": 659.5,
        "p90": 1595.0,
        "p95": 1718.0,
        "max": 1747.0
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
    "wall_seconds": 18.047,
    "throughput_per_second": 1.662,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.578,
      "median": 3.891,
      "p90": 5.11,
      "p95": 5.234,
      "max": 5.281
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.297,
      "p95": 0.375,
      "max": 0.391
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.141,
      "median": 0.203,
      "p90": 0.219,
      "p95": 0.219,
      "max": 0.219
    },
    "workers": {
      "worker-1": 16,
      "worker-2": 14
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
        "p95": 235.0,
        "max": 256.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 27.0,
        "p95": 29.0,
        "max": 36.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 3.0,
        "p90": 4.0,
        "p95": 5.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 507.0,
        "median": 566.0,
        "p90": 1526.0,
        "p95": 1556.0,
        "max": 1560.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 563.0,
        "median": 625.0,
        "p90": 1580.0,
        "p95": 1617.0,
        "max": 1620.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 10.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 12.0,
        "max": 12.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 40.0,
        "max": 92.0
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
        "p95": 169.0,
        "max": 179.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 332.0,
        "median": 343.0,
        "p90": 374.0,
        "p95": 387.0,
        "max": 388.0
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
        "median": 371.5,
        "p90": 1336.0,
        "p95": 1370.0,
        "max": 1373.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 30.5,
        "p90": 69.0,
        "p95": 92.0,
        "max": 162.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 214.0,
        "median": 237.5,
        "p90": 272.0,
        "p95": 272.0,
        "max": 272.0
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
        "p90": 128.0,
        "p95": 140.0,
        "max": 156.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 416.0,
        "median": 463.0,
        "p90": 1425.0,
        "p95": 1460.0,
        "max": 1464.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 52.0,
        "median": 57.5,
        "p90": 61.0,
        "p95": 63.0,
        "max": 65.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 53.0,
        "median": 58.5,
        "p90": 65.0,
        "p95": 72.0,
        "max": 81.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 573.0,
        "median": 643.0,
        "p90": 1594.0,
        "p95": 1629.0,
        "max": 1634.0
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
    "wall_seconds": 18.172,
    "throughput_per_second": 1.651,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.765,
      "median": 6.718,
      "p90": 11.953,
      "p95": 12.25,
      "max": 12.516
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.156,
      "median": 0.265,
      "p90": 0.5,
      "p95": 0.547,
      "max": 0.578
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.188,
      "median": 0.25,
      "p90": 0.266,
      "p95": 0.266,
      "max": 0.266
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
        "max": 264.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 26.0,
        "p95": 33.0,
        "max": 42.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 4.0,
        "p95": 4.0,
        "max": 5.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 515.0,
        "median": 701.0,
        "p90": 1562.0,
        "p95": 1616.0,
        "max": 1619.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 575.0,
        "median": 758.5,
        "p90": 1624.0,
        "p95": 1678.0,
        "max": 1706.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 12.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 7.0,
        "p90": 12.0,
        "p95": 13.0,
        "max": 17.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 37.0,
        "max": 55.0
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
        "max": 188.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 334.0,
        "median": 348.5,
        "p90": 381.0,
        "p95": 401.0,
        "max": 420.0
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
        "median": 358.0,
        "p90": 1356.0,
        "p95": 1402.0,
        "max": 1422.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 21.0,
        "median": 38.5,
        "p90": 165.0,
        "p95": 260.0,
        "max": 263.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 216.0,
        "median": 238.0,
        "p90": 254.0,
        "p95": 255.0,
        "max": 255.0
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
        "p95": 142.0,
        "max": 153.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 421.0,
        "median": 451.5,
        "p90": 1452.0,
        "p95": 1510.0,
        "max": 1521.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 52.0,
        "median": 58.5,
        "p90": 67.0,
        "p95": 72.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 55.0,
        "median": 60.0,
        "p90": 66.0,
        "p95": 74.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 593.0,
        "median": 777.0,
        "p90": 1646.0,
        "p95": 1697.0,
        "max": 1725.0
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
    "wall_seconds": 18.422,
    "throughput_per_second": 1.628,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.969,
      "median": 8.476,
      "p90": 9.844,
      "p95": 10.344,
      "max": 11.063
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.141,
      "median": 0.312,
      "p90": 0.688,
      "p95": 0.734,
      "max": 0.781
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.156,
      "median": 0.188,
      "p90": 0.203,
      "p95": 0.203,
      "max": 0.203
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
        "p95": 240.0,
        "max": 251.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 29.0,
        "p95": 32.0,
        "max": 34.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 7.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 509.0,
        "median": 662.0,
        "p90": 1539.0,
        "p95": 1601.0,
        "max": 1648.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 563.0,
        "median": 721.0,
        "p90": 1594.0,
        "p95": 1666.0,
        "max": 1723.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 5.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 13.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 6.0,
        "p90": 11.0,
        "p95": 12.0,
        "max": 18.0
      },
      "output_upload_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 64.0,
        "max": 160.0
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
        "p95": 189.0,
        "max": 192.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 335.0,
        "median": 347.5,
        "p90": 381.0,
        "p95": 409.0,
        "max": 427.0
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
        "median": 369.0,
        "p90": 1349.0,
        "p95": 1368.0,
        "max": 1428.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 32.5,
        "p90": 177.0,
        "p95": 369.0,
        "max": 374.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 203.0,
        "median": 237.0,
        "p90": 260.0,
        "p95": 288.0,
        "max": 288.0
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
        "p90": 129.0,
        "p95": 141.0,
        "max": 149.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 419.0,
        "median": 463.5,
        "p90": 1443.0,
        "p95": 1466.0,
        "max": 1547.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 58.5,
        "p90": 65.0,
        "p95": 66.0,
        "max": 75.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 60.0,
        "p90": 67.0,
        "p95": 71.0,
        "max": 75.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 580.0,
        "median": 734.5,
        "p90": 1607.0,
        "p95": 1684.0,
        "max": 1736.0
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
    "wall_seconds": 18.187,
    "throughput_per_second": 1.65,
    "successes": 30,
    "failures": 0,
    "terminal_seconds": {
      "count": 30,
      "min": 1.906,
      "median": 8.296,
      "p90": 10.0,
      "p95": 10.75,
      "max": 11.032
    },
    "accept_seconds": {
      "count": 30,
      "min": 0.141,
      "median": 0.243,
      "p90": 0.5,
      "p95": 0.609,
      "max": 0.703
    },
    "output_download_seconds": {
      "count": 3,
      "min": 0.172,
      "median": 0.187,
      "p90": 0.235,
      "p95": 0.235,
      "max": 0.235
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
        "p95": 257.0,
        "max": 262.0
      },
      "docker_image_pull_ms": {
        "count": 30,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 34.0,
        "max": 37.0
      },
      "docker_input_copy_ms": {
        "count": 30,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 6.0,
        "max": 6.0
      },
      "executor_duration_ms": {
        "count": 30,
        "min": 499.0,
        "median": 738.0,
        "p90": 1548.0,
        "p95": 1594.0,
        "max": 1622.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 30,
        "min": 558.0,
        "median": 796.0,
        "p90": 1603.0,
        "p95": 1655.0,
        "max": 1686.0
      },
      "orchestrator_claim_ms": {
        "count": 30,
        "min": 3.0,
        "median": 6.0,
        "p90": 10.0,
        "p95": 11.0,
        "max": 11.0
      },
      "orchestrator_completion_ms": {
        "count": 30,
        "min": 4.0,
        "median": 7.0,
        "p90": 10.0,
        "p95": 10.0,
        "max": 13.0
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
        "p95": 177.0,
        "max": 186.0
      },
      "runner_module_imports_ms": {
        "count": 30,
        "min": 330.0,
        "median": 344.5,
        "p90": 389.0,
        "p95": 395.0,
        "max": 414.0
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
        "median": 374.0,
        "p90": 1339.0,
        "p95": 1344.0,
        "max": 1397.0
      },
      "sandbox_prepare_ms": {
        "count": 30,
        "min": 20.0,
        "median": 33.0,
        "p90": 180.0,
        "p95": 331.0,
        "max": 353.0
      },
      "warm_container_create_ms": {
        "count": 6,
        "min": 214.0,
        "median": 228.5,
        "p90": 241.0,
        "p95": 242.0,
        "max": 242.0
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
        "p90": 130.0,
        "p95": 136.0,
        "max": 158.0
      },
      "warm_runner_exec_ms": {
        "count": 30,
        "min": 418.0,
        "median": 465.5,
        "p90": 1432.0,
        "p95": 1455.0,
        "max": 1497.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 30,
        "min": 53.0,
        "median": 59.5,
        "p90": 63.0,
        "p95": 66.0,
        "max": 68.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 30,
        "min": 54.0,
        "median": 59.0,
        "p90": 66.0,
        "p95": 67.0,
        "max": 71.0
      },
      "worker_process_total_ms": {
        "count": 30,
        "min": 570.0,
        "median": 813.5,
        "p90": 1619.0,
        "p95": 1667.0,
        "max": 1706.0
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
    "wall_seconds": 85.312,
    "throughput_per_second": 0.938,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.437,
      "median": 1.562,
      "p90": 2.687,
      "p95": 3.329,
      "max": 3.75
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.164,
      "p90": 0.188,
      "p95": 0.219,
      "max": 0.579
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.156,
      "median": 0.172,
      "p90": 0.187,
      "p95": 0.578,
      "max": 0.578
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
        "p95": 230.0,
        "max": 277.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 34.0,
        "max": 43.0
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
        "min": 502.0,
        "median": 598.0,
        "p90": 1543.0,
        "p95": 1578.0,
        "max": 1660.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 555.0,
        "median": 671.0,
        "p90": 1606.0,
        "p95": 1645.0,
        "max": 1736.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 9.0,
        "max": 12.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 19.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 76.0
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
        "p95": 180.0,
        "max": 215.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 331.0,
        "median": 349.5,
        "p90": 407.0,
        "p95": 418.0,
        "max": 450.0
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
        "median": 389.0,
        "p90": 1351.0,
        "p95": 1391.0,
        "max": 1411.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 20.0,
        "median": 25.5,
        "p90": 45.0,
        "p95": 57.0,
        "max": 79.0
      },
      "warm_container_create_ms": {
        "count": 16,
        "min": 213.0,
        "median": 243.0,
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
        "p95": 135.0,
        "max": 148.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 415.0,
        "median": 483.5,
        "p90": 1446.0,
        "p95": 1488.0,
        "max": 1521.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 51.0,
        "median": 60.0,
        "p90": 71.0,
        "p95": 74.0,
        "max": 86.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.0,
        "p90": 71.0,
        "p95": 72.0,
        "max": 86.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 572.0,
        "median": 683.0,
        "p90": 1618.0,
        "p95": 1657.0,
        "max": 1751.0
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
    "wall_seconds": 87.359,
    "throughput_per_second": 0.916,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.422,
      "median": 2.07,
      "p90": 2.734,
      "p95": 2.937,
      "max": 3.782
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.172,
      "p90": 0.235,
      "p95": 0.422,
      "max": 0.906
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.149,
      "p90": 0.171,
      "p95": 0.25,
      "max": 0.25
    },
    "workers": {
      "worker-1": 38,
      "worker-2": 42
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
        "p95": 245.0,
        "max": 275.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 32.0,
        "p95": 34.0,
        "max": 37.0
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
        "min": 510.0,
        "median": 590.0,
        "p90": 1551.0,
        "p95": 1564.0,
        "max": 1767.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 570.0,
        "median": 656.5,
        "p90": 1609.0,
        "p95": 1633.0,
        "max": 1934.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 5.0,
        "p90": 7.0,
        "p95": 8.0,
        "max": 10.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 3.0,
        "median": 6.0,
        "p90": 8.0,
        "p95": 9.0,
        "max": 23.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 34.0,
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
        "p90": 1.0,
        "p95": 177.0,
        "max": 195.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 333.0,
        "median": 348.5,
        "p90": 392.0,
        "p95": 405.0,
        "max": 466.0
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
        "min": 334.0,
        "median": 383.5,
        "p90": 1348.0,
        "p95": 1372.0,
        "max": 1390.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 19.0,
        "median": 25.0,
        "p90": 51.0,
        "p95": 59.0,
        "max": 101.0
      },
      "warm_container_create_ms": {
        "count": 19,
        "min": 214.0,
        "median": 242.0,
        "p90": 260.0,
        "p95": 267.0,
        "max": 280.0
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
        "p90": 137.0,
        "p95": 144.0,
        "max": 175.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 420.0,
        "median": 479.0,
        "p90": 1441.0,
        "p95": 1469.0,
        "max": 1482.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 53.0,
        "median": 61.0,
        "p90": 66.0,
        "p95": 68.0,
        "max": 70.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 53.0,
        "median": 59.0,
        "p90": 67.0,
        "p95": 69.0,
        "max": 87.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 583.0,
        "median": 670.5,
        "p90": 1622.0,
        "p95": 1647.0,
        "max": 1947.0
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
    "repeat": 3,
    "wall_seconds": 82.281,
    "throughput_per_second": 0.972,
    "successes": 80,
    "failures": 0,
    "terminal_seconds": {
      "count": 80,
      "min": 1.422,
      "median": 1.524,
      "p90": 2.735,
      "p95": 3.094,
      "max": 4.125
    },
    "accept_seconds": {
      "count": 80,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.203,
      "p95": 0.25,
      "max": 0.797
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.187,
      "p95": 0.609,
      "max": 0.609
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
        "p95": 237.0,
        "max": 282.0
      },
      "docker_image_pull_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 31.0,
        "p95": 35.0,
        "max": 50.0
      },
      "docker_input_copy_ms": {
        "count": 80,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 10.0
      },
      "executor_duration_ms": {
        "count": 80,
        "min": 497.0,
        "median": 583.0,
        "p90": 1572.0,
        "p95": 1753.0,
        "max": 1789.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 80,
        "min": 550.0,
        "median": 651.5,
        "p90": 1634.0,
        "p95": 1951.0,
        "max": 1992.0
      },
      "orchestrator_claim_ms": {
        "count": 80,
        "min": 2.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 11.0,
        "max": 16.0
      },
      "orchestrator_completion_ms": {
        "count": 80,
        "min": 4.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 8.0,
        "max": 26.0
      },
      "output_upload_ms": {
        "count": 80,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 49.0
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
        "p95": 172.0,
        "max": 233.0
      },
      "runner_module_imports_ms": {
        "count": 80,
        "min": 330.0,
        "median": 350.0,
        "p90": 393.0,
        "p95": 401.0,
        "max": 424.0
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
        "median": 385.0,
        "p90": 1354.0,
        "p95": 1380.0,
        "max": 1399.0
      },
      "sandbox_prepare_ms": {
        "count": 80,
        "min": 19.0,
        "median": 26.0,
        "p90": 45.0,
        "p95": 47.0,
        "max": 69.0
      },
      "warm_container_create_ms": {
        "count": 20,
        "min": 208.0,
        "median": 229.0,
        "p90": 250.0,
        "p95": 289.0,
        "max": 319.0
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
        "p90": 129.0,
        "p95": 140.0,
        "max": 154.0
      },
      "warm_runner_exec_ms": {
        "count": 80,
        "min": 414.0,
        "median": 480.0,
        "p90": 1448.0,
        "p95": 1475.0,
        "max": 1499.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 80,
        "min": 52.0,
        "median": 60.0,
        "p90": 64.0,
        "p95": 68.0,
        "max": 77.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 80,
        "min": 52.0,
        "median": 61.0,
        "p90": 68.0,
        "p95": 72.0,
        "max": 76.0
      },
      "worker_process_total_ms": {
        "count": 80,
        "min": 565.0,
        "median": 665.0,
        "p90": 1647.0,
        "p95": 1963.0,
        "max": 2009.0
      }
    }
  },
  {
    "scenario": "mixed-80",
    "count": 80,
    "concurrency": 4,
    "saturation_concurrency": 4,
    "worker_invocation_concurrency": 1,
    "cluster_invocation_capacity": 2,
    "repeat": 1,
    "wall_seconds": 57.0,
    "throughput_per_second": 1.386,
    "successes": 79,
    "failures": 1,
    "terminal_seconds": {
      "count": 79,
      "min": 1.453,
      "median": 2.625,
      "p90": 3.75,
      "p95": 3.875,
      "max": 4.438
    },
    "accept_seconds": {
      "count": 79,
      "min": 0.125,
      "median": 0.157,
      "p90": 0.234,
      "p95": 0.5,
      "max": 0.797
    },
    "output_download_seconds": {
      "count": 8,
      "min": 0.14,
      "median": 0.157,
      "p90": 0.157,
      "p95": 0.172,
      "max": 0.172
    },
    "workers": {
      "worker-1": 39,
      "worker-2": 40
    },
    "cold_starts": 18,
    "worker_timing_ms": {
      "backend_final_report_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "backend_running_report_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "docker_export_copy_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 248.0,
        "max": 274.0
      },
      "docker_image_pull_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 30.0,
        "p95": 32.0,
        "max": 39.0
      },
      "docker_input_copy_ms": {
        "count": 79,
        "min": 3.0,
        "median": 4.0,
        "p90": 5.0,
        "p95": 5.0,
        "max": 11.0
      },
      "executor_duration_ms": {
        "count": 79,
        "min": 492.0,
        "median": 600.0,
        "p90": 1613.0,
        "p95": 1766.0,
        "max": 1800.0
      },
      "executor_wall_with_cleanup_ms": {
        "count": 79,
        "min": 547.0,
        "median": 677.0,
        "p90": 1681.0,
        "p95": 1945.0,
        "max": 1976.0
      },
      "orchestrator_claim_ms": {
        "count": 79,
        "min": 2.0,
        "median": 5.0,
        "p90": 9.0,
        "p95": 11.0,
        "max": 18.0
      },
      "orchestrator_completion_ms": {
        "count": 79,
        "min": 3.0,
        "median": 5.0,
        "p90": 8.0,
        "p95": 10.0,
        "max": 16.0
      },
      "output_upload_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 35.0,
        "max": 95.0
      },
      "output_validation_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "result_read_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_environment_read_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_event_load_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_handler_execution_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 1000.0,
        "p95": 1000.0,
        "max": 1000.0
      },
      "runner_handler_import_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 196.0,
        "max": 228.0
      },
      "runner_module_imports_ms": {
        "count": 79,
        "min": 331.0,
        "median": 353.0,
        "p90": 412.0,
        "p95": 421.0,
        "max": 430.0
      },
      "runner_result_serialize_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_result_write_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_setup_ms": {
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 0.0,
        "p95": 0.0,
        "max": 0.0
      },
      "runner_total_ms": {
        "count": 79,
        "min": 331.0,
        "median": 392.0,
        "p90": 1353.0,
        "p95": 1400.0,
        "max": 1416.0
      },
      "sandbox_prepare_ms": {
        "count": 79,
        "min": 19.0,
        "median": 27.0,
        "p90": 68.0,
        "p95": 78.0,
        "max": 111.0
      },
      "warm_container_create_ms": {
        "count": 18,
        "min": 206.0,
        "median": 236.5,
        "p90": 260.0,
        "p95": 263.0,
        "max": 280.0
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
        "count": 79,
        "min": 0.0,
        "median": 0.0,
        "p90": 129.0,
        "p95": 140.0,
        "max": 176.0
      },
      "warm_runner_exec_ms": {
        "count": 79,
        "min": 410.0,
        "median": 490.0,
        "p90": 1461.0,
        "p95": 1503.0,
        "max": 1518.0
      },
      "warm_sandbox_cleanup_after_ms": {
        "count": 79,
        "min": 52.0,
        "median": 60.0,
        "p90": 70.0,
        "p95": 73.0,
        "max": 81.0
      },
      "warm_sandbox_cleanup_before_ms": {
        "count": 79,
        "min": 53.0,
        "median": 60.0,
        "p90": 68.0,
        "p95": 69.0,
        "max": 83.0
      },
      "worker_process_total_ms": {
        "count": 79,
        "min": 559.0,
        "median": 686.0,
        "p90": 1692.0,
        "p95": 1958.0,
        "max": 1987.0
      }
    }
  }
]
```
