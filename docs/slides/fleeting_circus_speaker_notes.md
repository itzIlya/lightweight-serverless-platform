# Fleeting Circus Speaker Notes

Target duration: 7 to 9 minutes  
Pacing: around 15 to 18 seconds per slide

## Slide 1: Fleeting Circus

This project is called Fleeting Circus. It is a lightweight serverless platform where users upload Python functions, build them, and invoke them through APIs.

## Slide 2: The basic idea

The main idea is simple. A user writes a Python function, the platform builds it into an executable image, and callers invoke it later without managing servers.

## Slide 3: Why this project

Serverless moves infrastructure work away from the user. The user focuses on function logic, and the platform handles building, scheduling, running, and storing results.

## Slide 4: Workloads

The prototype supports small Python workloads: JSON processing, file processing, automation, webhook-style handlers, and functions that create output files.

## Slide 5: Function code

A function is just a Python handler. It receives an event object, can print output, and returns a JSON result.

## Slide 6: Dependencies

Users can declare Python dependencies in `requirements.txt`. During the build, the platform installs those packages into the function image.

## Slide 7: Function contract

Each function has a contract. The contract says who can call it, what files it may receive, what outputs it may publish, and how long it may run.

## Slide 8: Access modes

The platform supports three access modes. Private functions require owner authentication. Token functions require an invocation token. Public functions can be called without authentication.

## Slide 9: Synchronous invocation

Synchronous invocation is the convenience path. It is for simple JSON-only functions where the caller wants the result directly in the HTTP response.

## Slide 10: Asynchronous invocation

Asynchronous invocation is the main serverless path. The call returns quickly with an invocation id, and the user checks status until the result is ready.

## Slide 11: Result view

When a function finishes, users can see returned JSON, printed output, error output, exit status, output file paths, and a ZIP download for the full invocation package.

## Slide 12: Frontend workflow

The frontend workflow is: log in, view functions, create or edit a function, build it, invoke it, and inspect the invocation history.

## Slide 13: Main services

The platform is split into services. The userservice handles accounts. The backend handles product APIs. The orchestrator coordinates jobs. Workers run builds and invocations.

## Slide 14: Current deployment

The deployed prototype uses one control-plane VM and two worker VMs. The control plane runs the APIs and coordination services. Each worker has its own Docker Engine.

## Slide 15: Build flow

The build flow starts with source upload. The backend stores the source, creates a job, the orchestrator dispatches it, and the worker builds and pushes the image.

## Slide 16: Safe rebuilds

Rebuilds are safe. A new build is treated as a candidate. The platform only replaces the active function image after the new build succeeds.

## Slide 17: Invocation flow

For invocation, the backend validates the request, creates a job, the orchestrator dispatches it, the worker claims it, runs the function, and the platform commits the result.

## Slide 18: Files

Files are controlled by the function contract. Inputs are validated before execution, and outputs are only accepted if the function declared them during setup.

## Slide 19: Staged artifacts

Staging prevents inconsistent results. A file can physically exist before completion, but users cannot see it until the platform commits the invocation.

## Slide 20: Orchestrator role

The orchestrator owns active coordination state. It reads job events, chooses workers, validates claims, tracks attempts, and recovers jobs when workers stop responding.

## Slide 21: Worker role

Workers are execution machines. They consume assigned jobs, claim them, run Docker builds or function containers, and report results back to the platform.

## Slide 22: Reliability model

The reliability model uses Redis Streams, worker heartbeats, attempt fencing, recovery, and dead-letter jobs. These reduce duplicate and lost-job cases in the prototype.

## Slide 23: Warm containers

Warm containers were the biggest latency improvement. With the resident warm runner, a no-op function dropped from about 3918 milliseconds to about 88 milliseconds in our benchmark.

## Slide 24: Performance bottlenecks

The largest bottlenecks are still in the execution layer: Docker create and start time, Python imports, file operations, output artifact handling, and Docker contention under load.

## Slide 25: Observability

The observability stack uses Grafana for dashboards, Prometheus for metrics, Loki for logs, and exporters for Redis, Postgres, and container metrics.

## Slide 26: Lessons from failures

Several decisions changed along the way. Backend-centered coordination became too heavy, Docker copy and export were expensive, and worker health missed consume-loop failure.

## Slide 27: Current state

At this point, the project is a working prototype. It has authentication, function creation, builds, invocation, tokens, distributed workers, artifacts, frontend flows, and API documentation.

## Slide 28: Next work

The next work is mostly reliability and production hardening. The prototype proves the full serverless path and exposes the real tradeoffs in coordination, isolation, artifacts, and performance.

