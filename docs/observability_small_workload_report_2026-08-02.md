# Observability Small Workload Benchmark - 2026-08-02

## Goal

Run a small real invocation workload while Grafana, Prometheus, Loki, Alloy,
cAdvisor, Redis exporter, and Postgres exporters are active.

## Setup

- Function: existing built function `69`, version `80`
- Function type: Python sleep handler
- Access: private, invoked with owner JWT
- Worker count: 1 online worker
- Invocation count: 6
- User sleep time: 2 seconds per invocation
- Worker max invocation concurrency: 4
- Output file export: skipped because the function declares no outputs

The first attempt to use `scripts/concurrent_invocation_workload.py` failed
while uploading a new source bundle because object storage DNS resolution failed
for `c966302.parspack.net`. To avoid changing storage configuration, the actual
observability workload reused an already-built function.

## Result

Raw output:

```text
scenario: observability_small_private_existing_function
function_id: 69
count: 6
sleep_seconds: 2
wall_ms: 64453
throughput_per_second: 0.093
statuses: succeeded, failed, succeeded, succeeded, succeeded, succeeded
submit_median_ms: 227
poll_median_ms: 61101.5
invocation_ids: 677, 678, 679, 681, 680, 682
```

Raw JSON:

```text
docs/observability_small_workload_2026-08-02.json
```

## What Grafana/Prometheus Showed

Prometheus target health stayed green:

- backend: up
- userservice: up
- orchestrator: up
- worker: up
- Redis exporter: up
- both Postgres exporters: up
- cAdvisor: up

The new queue panels captured the worker-side V2 stream load:

```text
max worker invocation outstanding: 6
max worker invocation lag:         2
max worker invocation pending:     4
max worker build outstanding:      0
max worker active jobs:            4
max worker active invocations:     4
online workers:                    1
```

This matches the expected shape: 6 invocations were submitted, the worker ran up
to 4 concurrently, and 2 waited in the worker invocation stream.

The orchestrator ready queue stayed at zero in Prometheus:

```text
max orchestrator ready jobs total:     0
max orchestrator ready jobs available: 0
```

That means jobs moved through the orchestrator ready queue faster than the
10-second Prometheus scrape interval could catch. This is not necessarily bad;
it means the scheduler/orchestrator handoff was quick for this small workload.

## Loki Findings

Loki successfully collected platform logs. The relevant query returned worker,
backend, orchestrator, and finalizer logs.

Example worker timing for invocation `682`:

```text
worker_process_total_ms:          6669
executor_duration_ms:             6309
runner_total_ms:                  3633
runner_handler_execution_ms:      2000
runner_module_imports_ms:         1630
sandbox_prepare_ms:               1503
warm_container_reused:            1
warm_runner_exec_ms:              4016
warm_sandbox_cleanup_before_ms:    669
warm_sandbox_cleanup_after_ms:     200
docker_export_copy_ms:               0
output_upload_ms:                    0
```

So the no-output optimization worked: Docker export and output upload were zero.

## Failure Observed

One invocation failed:

```text
invocation_id: 678
status: failed
failure_kind: timeout
error_message: Function execution timed out after 10 seconds.
```

Other invocations succeeded but had long end-to-end durations:

```text
invocation 677 duration_ms: 14607
invocation 679 duration_ms: 15535
invocation 680 duration_ms: 15837
invocation 681 duration_ms: 7903
invocation 682 duration_ms: 6309
```

The failure and slow completions were not caused by output export. Loki showed
backend/finalizer errors caused by object storage DNS failures while committing
logs:

```text
Could not connect to the endpoint URL:
https://c966302.parspack.net/.../media/invocation_logs/.../stdout.txt
```

The finalizer retried and eventually committed several invocations, but this
object-storage outage added major latency and produced one timeout/failure.

## Observability Gaps Discovered

1. Immediate Prometheus samples can miss short queue spikes because scrape
   interval is 10 seconds.

2. `serverless_worker_active_jobs` is emitted by both backend and worker
   targets. Dashboard panels should filter `job="worker"` for live worker
   activity, which has now been corrected.

3. Backend worker metrics include many historical offline workers from earlier
   benchmark runs. Online-worker panels should filter `status="online"`.

4. Object storage health needs a first-class dashboard panel. Right now it is
   visible through Loki errors, but not as a metric.

5. Finalizer retry/finalization age should be watched during storage outages,
   because result publication can be delayed even after user code finishes.

## Conclusion

The observability stack works under a real workload:

- Prometheus scraped all targets.
- Grafana showed worker queue depth and worker concurrency.
- Loki captured backend, worker, orchestrator, and finalizer logs.
- cAdvisor exposed container-level metrics.

The workload itself exposed a real platform issue: when Parspack object storage
DNS is unavailable, invocation finalization and log commit can become slow or
fail. This is now visible in Loki, but we should add explicit object-storage
health and artifact-commit failure metrics before relying on the dashboard for
operations.
