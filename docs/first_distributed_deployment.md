# First Distributed Deployment

This document describes the first distributed version of the platform.

The existing local workflow remains available through `docker-compose.yml`. Use
the new files only when testing remote workers:

- `docker-compose.control-plane.yml`
- `docker-compose.worker.yml`
- `.env.control-plane.example`
- `.env.worker.example`
- `scripts/serverless-deploy.sh`

## Target Topology

```text
Machine A: control plane
  frontend
  userservice
  backend
  postgres
  userservice-postgres
  redis
  registry
  orchestrator
  outbox relay
  projector
  invocation finalizer
  cleaners

Machine B: worker-1
  worker
  local Docker Engine

Machine C: worker-2
  worker
  local Docker Engine
```

For this first version, Redis remains on the control-plane machine and workers
still connect to Redis directly. That is a known prototype dependency.

For runtime add/remove operations, see:

```text
docs/worker_scaling_operations.md
```

## Local Mode Stays The Same

Use the current local compose file for previous tests and benchmarks:

```powershell
docker --context desktop-linux compose up -d
docker --context desktop-linux compose exec backend python manage.py test apps.functions
docker --context desktop-linux compose exec worker python -m unittest discover -s worker -p "test_*.py" -v
```

Local mode keeps local image refs such as:

```text
localhost:5000/functions/name:tag
```

## Distributed Mode Setup

### Recommended Interactive Setup

On a Linux server, use the interactive bootstrap script:

```bash
bash scripts/serverless-deploy.sh
```

It asks what this machine should run:

```text
1) control-plane
2) worker
3) status
4) stop worker gracefully
```

Choose `control-plane` on the main server. The script creates
`.env.control-plane`, generates local secrets, starts the control-plane Compose
stack, and runs migrations for both the userservice and backend databases.

Choose `worker` on each worker server. The script creates `.env.worker`, asks
for the control-plane host/IP, asks for the shared worker secret, and starts the
worker-only Compose stack.

The generated `.env.control-plane` and `.env.worker` files are intentionally
ignored by git.

### Manual Setup

On the control-plane machine:

```powershell
Copy-Item .env.control-plane.example .env.control-plane
```

Edit `.env.control-plane` and replace every example secret and IP address.

Important values:

```env
CONTROL_PLANE_HOST=192.168.1.10
LOCAL_REGISTRY=192.168.1.10:5000
REGISTRY_IMAGE_REF_HOST=192.168.1.10:5000
WORKER_SHARED_SECRET=replace-me
```

`REGISTRY_IMAGE_REF_HOST` is the host written into function image refs. Remote
workers pull this exact image ref, so it must be reachable from worker machines.

Start the control plane:

```powershell
docker --context desktop-linux compose --env-file .env.control-plane -f docker-compose.control-plane.yml up -d
docker --context desktop-linux compose --env-file .env.control-plane -f docker-compose.control-plane.yml exec userservice python manage.py migrate
docker --context desktop-linux compose --env-file .env.control-plane -f docker-compose.control-plane.yml exec backend python manage.py migrate
```

On each worker machine:

```powershell
Copy-Item .env.worker.example .env.worker
```

Edit `.env.worker`:

```env
WORKER_NAME=worker-1
REDIS_URL=redis://192.168.1.10:6379/0
BACKEND_BASE_URL=http://192.168.1.10:8000
ORCHESTRATOR_BASE_URL=http://192.168.1.10:8010
LOCAL_REGISTRY=192.168.1.10:5000
WORKER_SHARED_SECRET=replace-me
FUNCTION_CONTAINER_NETWORK=
```

Start the worker:

```powershell
docker --context desktop-linux compose --env-file .env.worker -f docker-compose.worker.yml up -d
```

Use a different `WORKER_NAME` on every worker machine.

## Required Network Ports

Control-plane ports that workers need:

```text
6379  Redis
5000  Docker registry
8000  backend internal API
8010  orchestrator internal API
```

Browser/client ports:

```text
5173  frontend
8000  backend API
8100  userservice API
```

Do not expose Postgres publicly. Restrict Redis, registry, and orchestrator to
worker IPs/private network rules.

## Worker Docker Registry Setup

For this first distributed version, the registry is plain HTTP. Each worker's
Docker daemon must trust the control-plane registry as an insecure registry.

Linux worker example:

```json
{
  "insecure-registries": ["192.168.1.10:5000"]
}
```

Put that in:

```text
/etc/docker/daemon.json
```

Then restart Docker on the worker.

Windows Docker Desktop worker:

```text
Docker Desktop -> Settings -> Docker Engine -> insecure-registries
```

Add the control-plane registry address and restart Docker Desktop.

## Validation Checklist

Control plane:

```powershell
docker --context desktop-linux compose --env-file .env.control-plane -f docker-compose.control-plane.yml ps
```

Expected:

```text
backend healthy
userservice healthy
redis healthy
orchestrator healthy
registry running
```

Worker:

```powershell
docker --context desktop-linux compose --env-file .env.worker -f docker-compose.worker.yml ps
```

Expected:

```text
worker running
```

Platform test:

```text
1. Open frontend.
2. Build a simple no-dependency function.
3. Confirm the image ref starts with CONTROL_PLANE_HOST:5000.
4. Invoke async.
5. Invoke sync for a JSON-only function.
6. Create a second worker with a different WORKER_NAME.
7. Confirm both workers heartbeat and receive work.
```

## Known Limitations

This first distributed version intentionally keeps:

```text
single control plane
single Redis
single Postgres
single registry
single orchestrator
manual worker provisioning
plain HTTP registry
worker direct Redis access
```

The purpose of this milestone is to prove remote workers, not production-grade
high availability.

## Why Not Docker Swarm Yet?

Docker Swarm could run services across multiple machines, provide overlay
networking, and help with service restarts. It is not the best first move for
this prototype because our worker still needs direct access to its local Docker
Engine to create function containers. Running that inside Swarm would still
require mounting `/var/run/docker.sock`, trusting the central registry, and
preserving our own orchestrator's job fencing and completion protocol.

For now, SSH plus Compose is simpler and maps cleanly to the architecture:

```text
one control-plane machine
many worker machines
one worker Compose stack per worker machine
```

Swarm, Kubernetes, or Nomad become more useful later when we want declarative
cluster membership, rolling updates, service discovery, secrets management, and
multi-node lifecycle control.
