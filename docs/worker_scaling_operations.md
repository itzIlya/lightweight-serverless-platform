# Worker Scaling Operations

This document describes how to add and remove workers while the platform stays
online. It covers the current architecture:

```text
users -> frontend/backend -> orchestrator/Redis -> distributed workers
```

Users do not call workers directly. Workers are private execution capacity.

## Current Support Level

The platform supports runtime worker membership:

1. A worker starts with a unique `WORKER_NAME`.
2. The worker registers with the backend compatibility projection.
3. The worker heartbeats into Redis/orchestrator state.
4. The orchestrator sees the worker as `online`.
5. New jobs can be dispatched to that worker.
6. On shutdown, the worker reports `draining`, stops accepting new jobs, waits
   for active jobs to finish, then reports `offline`.

The current first distributed version still uses one central Redis, one central
orchestrator, one central backend, and one central registry.

## Add A Remote Worker

On the new worker machine, the recommended path is:

```bash
bash scripts/serverless-deploy.sh
```

Choose `worker`, then enter:

```text
control-plane host/IP
unique worker name
same shared worker secret used by the control plane
worker concurrency settings
```

The script writes `.env.worker` and starts:

```bash
docker compose --env-file .env.worker -f docker-compose.worker.yml up -d --build
```

Manual setup is still available:

```powershell
Copy-Item .env.worker.example .env.worker
```

Edit `.env.worker`:

```env
WORKER_NAME=worker-2
REDIS_URL=redis://<control-plane-ip>:6379/0
BACKEND_BASE_URL=http://<control-plane-ip>:8000
ORCHESTRATOR_BASE_URL=http://<control-plane-ip>:8010
LOCAL_REGISTRY=<control-plane-ip>:5000
WORKER_SHARED_SECRET=<same-secret-as-control-plane>
FUNCTION_CONTAINER_NETWORK=
```

Then start the worker:

```powershell
docker compose --env-file .env.worker -f docker-compose.worker.yml up -d
```

Use a unique `WORKER_NAME` for every worker. Good names include:

```text
worker-tehran-1
worker-tehran-2
worker-frankfurt-1
```

## Remove A Worker Gracefully

SSH to the worker machine and stop only the worker service:

```bash
bash scripts/serverless-deploy.sh
```

Choose `stop worker gracefully`.

Manual command:

```powershell
docker compose --env-file .env.worker -f docker-compose.worker.yml stop worker
```

What happens:

1. Docker sends `SIGTERM`.
2. The worker immediately reports `draining`.
3. The orchestrator stops choosing it for new jobs.
4. The worker stops polling its queues.
5. Active invocations/builds continue until they finish.
6. The worker reports `offline`.

The worker Compose files set:

```yaml
stop_grace_period: 6m
```

This is intentionally longer than the current frontend timeout limit of 300
seconds, so a normal function can finish during drain.

## Force Remove A Stuck Worker

If a worker is stuck and cannot drain:

```powershell
docker compose --env-file .env.worker -f docker-compose.worker.yml kill worker
```

The orchestrator will eventually mark the worker stale after missed heartbeats.
Jobs that were dispatched but not completed are recovered according to the
existing recovery/backoff/dead-letter policy.

Use force removal only when graceful stop fails.

## Scale Workers On One Machine

For local testing:

```powershell
docker compose up -d --scale worker=3
```

For remote machines, prefer one `docker-compose.worker.yml` worker per machine.
If multiple workers run on the same remote machine, each worker needs:

```text
unique WORKER_NAME
unique WORKER_METRICS_PORT
separate Compose project name or separate working directory
```

Otherwise the metrics port or Compose service name can collide.

## Required Control-Plane Ports

Workers need access to these control-plane ports:

```text
6379  Redis
5000  registry
8000  backend internal API
8010  orchestrator API
```

Postgres should not be exposed to workers.

Restrict Redis, registry, backend internal endpoints, and orchestrator to the
worker network or worker IP allow-list.

## Registry Requirement

Distributed workers must pull built function images from the control-plane
registry. In distributed mode, image refs must not use `localhost:5000`.

Control-plane `.env.control-plane` should contain:

```env
LOCAL_REGISTRY=<control-plane-ip>:5000
REGISTRY_IMAGE_REF_HOST=<control-plane-ip>:5000
```

Each worker Docker daemon must trust the registry if it is plain HTTP:

```json
{
  "insecure-registries": ["<control-plane-ip>:5000"]
}
```

Restart Docker after changing daemon registry settings.

## Observability Checks

Use Grafana/Prometheus for visibility, not direct control.

Useful signals:

```text
number of online workers
worker status: online/draining/offline
active jobs per worker
active invocations per worker
active builds per worker
worker queue depths
orchestrator pending invocation/build queue depth
dead-letter count
recovery count
```

Operationally:

```text
before adding a worker:
  confirm backend, Redis, registry, and orchestrator are healthy

after adding a worker:
  confirm the worker becomes online
  confirm its queues appear
  confirm it receives at least one test invocation

before removing a worker:
  check active jobs
  prefer graceful stop

after removing a worker:
  confirm status becomes offline
  confirm no new jobs are routed to it
```

Adding and removing workers is runtime-safe because workers announce their
state through heartbeat. A new worker becomes eligible after it heartbeats as
`online`. A gracefully stopped worker first heartbeats as `draining`, which
causes the orchestrator to stop assigning new jobs to it while active jobs
finish.

## Known Limitations

- Worker control is currently SSH/Docker based, not a dashboard button.
- Observability can show worker state but cannot safely stop a worker by itself.
- Redis is still the central queue/state transport.
- The registry is still single-region and central.
- Worker capabilities are still basic; routing does not yet consider CPU class,
  GPU, runtime variants, cached images without warm containers, or memory class.
