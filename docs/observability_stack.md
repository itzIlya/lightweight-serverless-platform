# Observability Stack

The local observability stack is opt-in through the `observability` Compose profile.

It includes:

- Grafana for dashboards.
- Prometheus for metrics scraping and metric storage.
- Loki for container log storage and querying.
- Grafana Alloy for Docker log collection into Loki.
- cAdvisor for Docker container CPU, memory, network and filesystem metrics.
- Redis exporter for Redis metrics.
- Postgres exporter for the platform database.
- A second Postgres exporter for the userservice database.

## Start With Docker Hub Images

```powershell
docker compose --profile observability up -d prometheus grafana loki alloy cadvisor redis-exporter postgres-exporter userservice-postgres-exporter
```

## Start With Runflare Mirror Images

Use this when Docker Hub is unavailable:

```powershell
docker compose -f docker-compose.yml -f docker-compose.mirrors-runflare.yml --profile observability up -d prometheus grafana loki alloy cadvisor redis-exporter postgres-exporter userservice-postgres-exporter
```

Runflare worked for all required observability images, including cAdvisor from the `gcr.io` namespace.

## Arvan Mirror Notes

Arvan can be used as `docker.arvancloud.ir/<ImageName>` for Docker Hub images.

It did not work for cAdvisor with `docker.arvancloud.ir/gcr.io/cadvisor/cadvisor:v0.49.1`, because cAdvisor is not a Docker Hub image. For this stack, Runflare is the cleaner single mirror override.

## URLs

- Grafana: `http://localhost:3000`
- Prometheus: `http://localhost:9090`
- Loki: `http://localhost:3100`
- Alloy UI: `http://localhost:12345`
- cAdvisor: `http://localhost:8081`
- Redis exporter: `http://localhost:9121/metrics`
- Platform Postgres exporter: `http://localhost:9187/metrics`
- Userservice Postgres exporter: `http://localhost:9188/metrics`

The bare Loki root URL, `http://localhost:3100`, returns `404`. That is expected:
Loki does not provide a normal browser UI at `/`. Use Grafana for log browsing,
or use Loki API endpoints such as `http://localhost:3100/ready`,
`http://localhost:3100/metrics`, and `http://localhost:3100/loki/api/v1/labels`.

Default Grafana credentials:

```text
username: admin
password: admin
```

The dashboard is provisioned automatically under:

```text
Serverless Platform / Serverless Platform Overview
```

## Metrics Endpoints

Application services expose Prometheus text metrics:

- Backend: `http://localhost:8000/metrics/`
- Userservice: `http://localhost:8100/metrics/`
- Orchestrator: `http://orchestrator:8010/metrics/`
- Worker: `http://worker:9102/metrics/`

The orchestrator metrics endpoint uses the internal token. Prometheus currently expects the default token value `change-me`. If `WORKER_SHARED_SECRET` changes, update `observability/prometheus/prometheus.yml`.

## Queue Metrics

The dashboard includes:

- Online worker count from `serverless_worker_up`.
- Orchestrator queued jobs from `serverless_orchestrator_ready_jobs_total`.
- Immediately dispatchable orchestrator jobs from
  `serverless_orchestrator_ready_jobs_available_total`.
- Per-worker V2 invocation/build stream backlog from
  `serverless_worker_queue_lag`.
- Per-worker V2 invocation/build delivered-but-unacked work from
  `serverless_worker_queue_pending`.
- Per-worker outstanding work from `serverless_worker_queue_outstanding`.

For Redis Streams, raw stream length is intentionally not used as the queue
depth, because acknowledged stream entries can remain in the stream until
trimming. The useful operational values are:

- `lag`: jobs not yet delivered to a worker consumer.
- `pending`: jobs delivered to a worker but not ACKed yet.
- `outstanding`: `lag + pending`.

## Log Collection

Alloy collects Docker logs from platform application services only:

- backend
- userservice
- worker
- scheduler
- orchestrator
- invocation-finalizer
- orchestrator-projector
- orchestrator-reconciler
- orchestrator-shadow
- outbox-relay
- staged-artifact-cleaner
- orphan-image-cleaner

It intentionally skips Redis, Postgres, registry and observability service logs for now to reduce startup backlog and avoid monitoring noise.

## Validation Commands

```powershell
docker compose -f docker-compose.yml -f docker-compose.mirrors-runflare.yml --profile observability ps
Invoke-WebRequest http://localhost:9090/-/ready -UseBasicParsing
Invoke-WebRequest http://localhost:3000/api/health -UseBasicParsing
Invoke-WebRequest http://localhost:3100/ready -UseBasicParsing
Invoke-RestMethod http://localhost:9090/api/v1/targets
```
