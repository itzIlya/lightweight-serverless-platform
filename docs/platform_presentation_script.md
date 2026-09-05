# Fleeting Circus Presentation Script

Target duration: 8 to 10 minutes  
Audience: bachelor project presentation, technical but not code-review level  
Goal: explain what the platform does, how it works, what was built, what was learned, and what remains

## Slide 1

### Contents

Title:

```text
Fleeting Circus
A lightweight serverless platform for Python functions
```

Visuals:

- Large homepage mascot image on the right or as a soft background.
- Small subtitle under the title:

```text
Upload code. Build once. Invoke through an API.
```

Optional footer:

```text
Bachelor Project Prototype
```

### Script to read from

Good morning. This project is called Fleeting Circus. It is a lightweight serverless platform for Python functions.

The idea is simple: a user writes a Python handler, uploads it to the platform, builds it once, and then calls it through an API. The platform handles the build, execution, input files, output files, logs, status tracking, and worker coordination.

This is a prototype, but it already has the full basic serverless path working. In this presentation I will first show what users can do with it, then I will explain the architecture and the execution flow under the hood, and finally I will cover the current deployment, benchmark results, and the next improvements.

## Slide 2

### Contents

Title:

```text
What the platform can do
```

Main points:

```text
Create Python functions
Declare dependencies
Build Docker images
Invoke synchronously or asynchronously
Attach input files
Publish declared output files
Download invocation packages
Manage invocation tokens
Track status through APIs and the frontend
```

Visual:

- Simple user journey line:

```text
Create function -> Build image -> Invoke -> Read result -> Download artifacts
```

### Script to read from

From the user side, the platform supports the main operations expected from a small serverless product.

A user can create a function, paste Python code, provide a `requirements.txt`, choose whether the function is private, public, or token-protected, and define what input and output files are allowed.

After that, the user builds the function. The build creates a Docker image and stores it in the registry. Once the build succeeds, the function can be invoked.

There are two invocation modes. Synchronous invocation is for simple JSON-only calls where the user wants a direct result quickly. Asynchronous invocation is the durable path. It returns an invocation id and read token, then the user polls for status and downloads the result package when it is ready.

The platform also stores stdout, stderr, exit status, result JSON, declared output files, and invocation ZIP downloads.

## Slide 3

### Contents

Title:

```text
User workflow
```

Graphic:

```text
Frontend
  |
  v
Create function
  |
  v
Paste code and requirements
  |
  v
Set access and file contract
  |
  v
Build
  |
  v
Invoke and inspect results
```

Show one small code example:

```python
def main(event, context):
    name = event.get("name", "world")
    print(f"hello {name}")
    return {"message": f"Hello, {name}!"}
```

### Script to read from

The frontend guides the user through the workflow step by step.

First, the user creates a function and writes the handler. The platform expects a Python function, usually named something like `main`, inside `handler.py`. The function receives an event and context, then returns JSON-serializable data.

Second, the user specifies dependencies in `requirements.txt`. For example, a function can require `numpy`, `requests`, or another Python package. The build process installs those dependencies inside the function image.

Third, the user defines the contract. This includes access mode, allowed input file types, maximum input size, expected output filenames, output size limits, memory, and function timeout.

Finally, the user builds and invokes the function. The frontend shows build status, invocation status, simple and advanced responses, token management, and download links for artifacts.

## Slide 4

### Contents

Title:

```text
Architecture
```

Diagram:

```text
Browser / API client
        |
        v
      Nginx
        |
        +---- userservice ---- userservice Postgres
        |
        +---- backend -------- platform Postgres
                 | \
                 |  \ object storage
                 |
              Redis Streams
                 |
             orchestrator
                 |
        +--------+--------+
        |                 |
     worker-1          worker-2
        |                 |
   Docker Engine     Docker Engine
        |
 local registry on control plane
```

Callouts:

```text
userservice signs JWTs
backend owns product APIs and artifacts
orchestrator owns active job state
workers run builds and invocations
Redis carries coordination events
PostgreSQL stores persistent metadata
```

### Script to read from

The current deployment has one control-plane machine and two worker machines.

The control plane runs Nginx, the frontend, the userservice, the backend, Postgres, Redis, the local Docker registry, the orchestrator, the projector, finalizer, cleanup services, Prometheus, Grafana, Loki, and exporters.

The workers run the worker container and use the local Docker Engine on each worker VM. They connect back to the control plane for Redis, backend APIs, orchestrator APIs, and registry pulls.

The important design decision is that authentication and account management live in a separate userservice. The userservice signs JWTs, and the backend verifies those tokens using the userservice public key.

The backend owns product resources: functions, builds, invocations, tokens, input files, output files, logs, ZIP downloads, and frontend-facing response formats.

The orchestrator owns active coordination state for V2 jobs using Redis. The workers are execution machines. They do not decide global placement policy. They claim assigned jobs, run the work, and report completion.

## Slide 5

### Contents

Title:

```text
Build flow
```

Diagram:

```text
User uploads source
        |
        v
Backend stores source bundle
        |
        v
Backend creates build job event
        |
        v
Outbox relay publishes to Redis
        |
        v
Orchestrator assigns worker
        |
        v
Worker claims build
        |
        v
Worker builds image and pushes registry tag
        |
        v
Backend promotes successful image
```

Small notes:

```text
Failed builds do not replace the active image
Successful rebuilds schedule old image cleanup
Build attempts are recorded
```

### Script to read from

The build flow starts when the user uploads source code.

The frontend creates a ZIP bundle containing files such as `handler.py` and `requirements.txt`. The backend validates and stores this source bundle. It then creates a build record and writes an outbox event.

The outbox relay publishes the event to Redis. This gives us an important safety property: the database write and the event publication are decoupled, and failed publication can be retried.

The orchestrator reads the build event and chooses a worker. The worker receives the delivery through a worker-specific Redis Stream, asks the orchestrator to claim the job, downloads the source bundle from a protected backend endpoint, builds the Docker image, and pushes it to the registry.

If the build succeeds, the backend promotes the image and marks it as the active version. If the build fails, the previous working version remains active. This means editing a function does not break the currently deployed version until the new build is actually successful.

## Slide 6

### Contents

Title:

```text
Invocation flow
```

Diagram:

```text
Client invokes function
        |
        v
Backend validates access and input files
        |
        v
Backend creates invocation job
        |
        v
Orchestrator dispatches to worker
        |
        v
Worker claims with attempt fencing
        |
        v
Worker runs function container
        |
        v
Runner writes result and uploads declared outputs
        |
        v
Worker reports completion
        |
        v
Finalizer commits artifacts
        |
        v
User reads result or downloads ZIP
```

Side box:

```text
Simple response: result and output paths
Advanced response: status, timings, stdout, stderr, exit code, links
```

### Script to read from

Invocation is the most important path in the system.

The client calls the backend. The backend checks whether the function is private, public, or token-protected. For token and public callers, the backend also returns a read token so that the caller can later view only their own invocation result.

If the request contains input files, the backend validates file count, MIME type, per-file size, and total size. The files are stored as invocation artifacts and later fetched by the worker through internal endpoints.

The backend creates an invocation job and publishes it through the outbox path. The orchestrator dispatches the job to a worker. The worker then claims it through the orchestrator. The claim includes the worker name and dispatch attempt, so an old worker cannot execute a stale delivery after recovery.

The worker prepares the sandbox, starts or reuses a function container, and runs the runner. The function receives the event JSON and optional file metadata. The function returns a JSON result and may write declared output files.

The current fast path lets the runner upload declared outputs directly to the backend using a scoped upload token. The worker still owns execution and completion reporting. The finalizer commits staged artifacts so that users never see half-published results.

After that, the frontend can show a simple response, an advanced response, output file links, and the invocation ZIP download.

## Slide 7

### Contents

Title:

```text
Coordination and reliability
```

Visual:

```text
Redis Streams
  job.created
  worker delivery
  finalization event
  projection event
```

Reliability features:

```text
Attempt fencing
Worker heartbeats
Stale lease recovery
Dead-letter jobs
Staged outputs
Idempotent completion
PostgreSQL projection
Graceful worker draining
```

Small incident note:

```text
Recent issue found: worker consume loop died after Redis connection reset
Fix direction: retry Redis reads and expose consume-loop health
```

### Script to read from

The platform moved from a simpler backend-driven queue model to a V2 orchestrator protocol.

In V2, Redis Streams carry job events and worker deliveries. The orchestrator is the authority for active job state. The backend remains important for product data and artifacts, but it does not need to be the active coordinator for every running job.

The system uses attempt fencing. Every dispatch has an attempt number. When a worker claims or completes a job, the orchestrator checks that the worker and attempt match the current state. This prevents stale workers from overwriting newer attempts.

Workers send heartbeats. If a worker stops heartbeating, the orchestrator can recover jobs and dispatch them again. If recovery happens too many times, the job moves to a dead-letter state instead of looping forever.

For output correctness, the platform uses staged artifacts. A worker or runner can upload physical output files, but those files stay hidden until finalization commits them. This avoids a bad state where a file exists but the invocation has not finished correctly.

One recent operational issue taught us that worker health must include the consume loop itself. The container was running and heartbeating, but Redis stream consumption had died after a connection reset. The next reliability fix is to retry Redis stream reads and expose consume-loop health in the worker healthcheck.

## Slide 8

### Contents

Title:

```text
Performance work
```

Table:

```text
Change                         Result
V2 orchestration                Lower queue-to-start time
Warm containers                 Faster repeated invocations
Resident warm runner            Removed repeated Python startup
Output export skipping          Avoids artifact work when no outputs exist
Worker concurrency benchmarks   Found useful saturation points
```

Concrete benchmark callout:

```text
Resident warm no-op median:
old warm path: 3918 ms
new resident runner: 88 ms
```

Second callout:

```text
Output-producing calls still pay artifact overhead
Docker runtime remains the largest bottleneck
```

### Script to read from

Performance became one of the most interesting parts of the project.

The first versions paid a lot of overhead per invocation. Some of it came from queueing, some from backend coordination, and a lot from Docker lifecycle work: creating containers, starting containers, copying files, reading logs, and cleaning up.

V2 orchestration helped queue-to-start time because jobs were dispatched through Redis and claimed through the orchestrator instead of using PostgreSQL as the active running-state coordinator.

Warm containers helped repeated invocations. The biggest improvement came from the resident warm runner. In the old warm path, each warm invocation still launched Python inside the container again. In the resident runner path, the container keeps a small runner process alive and accepts local calls inside the container. For a no-op function, the measured median dropped from about 3918 milliseconds to about 88 milliseconds.

For functions that sleep for three seconds, the improvement is smaller because real user code dominates. For functions with output files, artifact handling still matters.

The current performance bottleneck is still the Docker runtime and artifact path under concurrent load. Better worker health, better concurrency tuning, and eventually stronger isolation technology or a different runtime model would be the next steps.

## Slide 9

### Contents

Title:

```text
Current state and next work
```

Current state:

```text
Working frontend and API prototype
Separate userservice with JWTs
Backend function and invocation APIs
V2 Redis orchestrator path
Two distributed workers
Warm-container execution
Object-storage-backed artifacts
Grafana observability stack
OpenAPI and Swagger docs
```

Next work:

```text
Worker consume-loop recovery
Safer distributed networking
Resource limits for builds
Dependency and image security scanning
Production static frontend deployment
More complete user account management
Longer benchmark and failure testing
```

Closing line:

```text
The prototype proves the full serverless path and exposes the real engineering tradeoffs.
```

### Script to read from

The current prototype proves the main platform path end to end.

Users can create accounts, define Python functions, build Docker images, invoke functions, manage invocation tokens, attach files, read results, download invocation ZIPs, and use the frontend as the main workspace.

Architecturally, the platform now has a separate userservice, backend, Redis-based orchestrator, distributed workers, local registry, object storage integration, and observability stack.

The next engineering work is clear. First, worker reliability needs one more layer: the consume loop must recover from Redis connection resets, and worker health must fail if consumption stops. Second, distributed networking should be tightened so Redis, registry, backend internals, and orchestrator APIs are not broadly exposed. Third, builds need stronger resource limits and dependency handling. Finally, the frontend deployment should move from Vite dev serving to a real static production build behind Nginx.

Overall, the platform works as a serverless prototype and, more importantly, it shows the real tradeoffs: coordination correctness, artifact consistency, Docker overhead, warm container reuse, distributed worker reliability, and the boundary between product APIs and internal orchestration.

That is what I set out to explore with this project.

