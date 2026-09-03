# Distributed Platform Benchmark

Generated: 2026-09-01T20:18:26.453110+00:00

## Terminology

- `Saturation Concurrency` is the number of simultaneous client-side invocation requests this benchmark keeps in flight.
- `Worker Invocation Concurrency` is the `WORKER_MAX_INVOCATION_CONCURRENCY` value configured on each worker.
- `Cluster Invocation Capacity` is worker count multiplied by worker invocation concurrency.
- Worker execution concurrency is configured on each worker with `WORKER_MAX_INVOCATION_CONCURRENCY` and was held constant during these runs.

## Built Functions

- `tiny`: function `77`, version `77`, image `10.42.1.22:5000/functions/bench-tiny-626dffd4:v77-v1-a1-c606a978e160-d1`
- `sleep`: function `78`, version `78`, image `10.42.1.22:5000/functions/bench-sleep-19ca9b1b:v78-v1-a1-b79329f124f8-d1`
- `dependency`: function `79`, version `79`, image `10.42.1.22:5000/functions/bench-dependency-a3023ada:v79-v1-a1-1fc803fbd7be-d1`
- `output`: function `80`, version `80`, image `10.42.1.22:5000/functions/bench-output-1b7fef33:v80-v1-a1-f34ca898b9f9-d1`
- `input_output`: function `81`, version `81`, image `10.42.1.22:5000/functions/bench-input_output-1a6841dd:v81-v1-a1-08dd3a49d4ae-d1`

## Run Summary

| Scenario | Count | Saturation Concurrency | Repeat | Success | Fail | Wall s | Throughput/s | Median terminal s | P95 terminal s | Workers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|

## Detailed JSON Summary

```json
[]
```
