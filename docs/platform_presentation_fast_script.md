# Fleeting Circus Fast Presentation Script

Target duration: 7 to 9 minutes  
Pacing rule: do not stay on one slide for more than 20 seconds  
Recommended slide count: 28 slides, around 15 to 18 seconds each  
Audience: bachelor project presentation

## Slide 1

### Contents

Title:

```text
Fleeting Circus
```

Subtitle:

```text
A lightweight serverless platform for Python functions
```

Visual:

- Full-screen mascot or homepage image.
- Small footer: `Bachelor Project Prototype`

### Script to read from

This project is called Fleeting Circus. It is a lightweight serverless platform where users upload Python functions, build them, and invoke them through APIs.

## Slide 2

### Contents

Title:

```text
The basic idea
```

Large center text:

```text
Write a function
Build it once
Call it whenever needed
```

Visual:

- Three-step horizontal flow.

### Script to read from

The main idea is simple. A user writes a Python function, the platform builds it into an executable image, and callers invoke it later without managing servers.

## Slide 3

### Contents

Title:

```text
Why serverless
```

Main text:

```text
Users care about code and results.
The platform handles execution.
```

Supporting points:

```text
No manual server setup
Repeatable builds
API-based invocation
Automatic result tracking
```

### Script to read from

Serverless moves infrastructure work away from the user. The user focuses on the function logic, and the platform handles building, scheduling, running, and storing results.

## Slide 4

### Contents

Title:

```text
What users can build
```

Examples:

```text
JSON processors
Image or PDF processors
Small data tasks
Webhook handlers
Python automation jobs
```

Visual:

- Five simple icons or labels.

### Script to read from

The prototype supports small Python workloads: JSON processing, file processing, automation, webhook-style handlers, and functions that create output files.

## Slide 5

### Contents

Title:

```text
Function code
```

Code block:

```python
def main(event, context):
    name = event.get("name", "world")
    print(f"hello {name}")
    return {"message": f"Hello, {name}!"}
```

Side note:

```text
Input: event
Output: JSON result
```

### Script to read from

A function is just a Python handler. It receives an event object, can print output, and returns a JSON result.

## Slide 6

### Contents

Title:

```text
Dependencies
```

Text:

```text
Users can provide requirements.txt
```

Example:

```text
numpy
requests==2.32.3
pillow
```

Visual:

- `requirements.txt` file card.

### Script to read from

Users can also declare Python dependencies. During the build, the platform installs these packages into the function image.

## Slide 7

### Contents

Title:

```text
Function contract
```

Main points:

```text
Access mode
Input file rules
Expected output files
Memory
Timeout
```

Visual:

- Checklist layout.

### Script to read from

Each function also has a contract. The contract tells the platform who can call it, what files it can receive, what outputs it may publish, and how long it may run.

## Slide 8

### Contents

Title:

```text
Access modes
```

Table:

```text
Private   Owner only
Token     Anyone with a function token
Public    Anyone can invoke
```

Visual:

- Three lock states.

### Script to read from

The platform supports three access modes. Private functions require owner authentication. Token functions require an invocation token. Public functions can be called without authentication.

## Slide 9

### Contents

Title:

```text
Synchronous invocation
```

Text:

```text
For simple JSON-only calls
Returns directly if the function finishes quickly
No input files
No output files
```

Example response:

```json
{"message": "Hello, Ada!"}
```

### Script to read from

Synchronous invocation is the convenience path. It is for simple JSON-only functions where the caller wants the result directly in the HTTP response.

## Slide 10

### Contents

Title:

```text
Asynchronous invocation
```

Text:

```text
For durable execution
Supports polling
Supports files
Supports ZIP downloads
```

Example:

```json
{
  "invocation_id": 9274,
  "status": "queued",
  "read_token": "inv_..."
}
```

### Script to read from

Asynchronous invocation is the main serverless path. The call returns quickly with an invocation id, and the user checks status until the result is ready.

## Slide 11

### Contents

Title:

```text
User result view
```

Visible result fields:

```text
Returned JSON
stdout
stderr
exit status
output file paths
ZIP download link
```

### Script to read from

When a function finishes, users can see the returned JSON, printed output, error output, exit status, output file paths, and a ZIP download for the full invocation package.

## Slide 12

### Contents

Title:

```text
Frontend workflow
```

Flow:

```text
Login
Function list
Function editor
Build status
Invocation panel
Result history
```

Visual:

- Small screenshots or wireframe blocks.

### Script to read from

The frontend is designed around this workflow: log in, see functions, create or edit a function, build it, invoke it, and inspect the history.

## Slide 13

### Contents

Title:

```text
Main services
```

Diagram:

```text
userservice
backend
orchestrator
worker
Redis
PostgreSQL
registry
object storage
```

### Script to read from

The platform is split into services. The userservice handles accounts. The backend handles product APIs. The orchestrator coordinates jobs. Workers run builds and invocations.

## Slide 14

### Contents

Title:

```text
Current deployment
```

Diagram:

```text
Control plane VM
  frontend, backend, userservice
  Redis, Postgres, registry
  orchestrator, observability

Worker VM 1
  worker + Docker

Worker VM 2
  worker + Docker
```

### Script to read from

The deployed prototype uses one control-plane VM and two worker VMs. The control plane runs the APIs and coordination services. Each worker has its own Docker Engine.

## Slide 15

### Contents

Title:

```text
Build flow
```

Flow:

```text
Upload source
Store ZIP
Create build job
Dispatch to worker
Build image
Push registry
Promote image
```

### Script to read from

The build flow starts with source upload. The backend stores the source, creates a job, the orchestrator dispatches it, and the worker builds and pushes the image.

## Slide 16

### Contents

Title:

```text
Safe rebuilds
```

Text:

```text
Old image stays active
New image becomes candidate
Only successful builds are promoted
Failed builds do not break the function
```

### Script to read from

Rebuilds are safe. A new build is treated as a candidate. The platform only replaces the active function image after the new build succeeds.

## Slide 17

### Contents

Title:

```text
Invocation flow
```

Flow:

```text
API request
Validate access
Create job
Dispatch
Claim
Run container
Stage result
Commit artifacts
Read result
```

### Script to read from

For invocation, the backend validates the request, creates a job, the orchestrator dispatches it, the worker claims it, runs the function, and the platform commits the result.

## Slide 18

### Contents

Title:

```text
Input and output files
```

Text:

```text
Input files are validated before execution
Output files must be declared by name
Unexpected outputs are rejected
Artifacts expire with the invocation
```

### Script to read from

Files are controlled by the function contract. Inputs are validated before execution, and outputs are only accepted if the function declared them during setup.

## Slide 19

### Contents

Title:

```text
Why staging exists
```

Problem:

```text
A file may upload before the job is finalized.
```

Solution:

```text
Staged artifacts are hidden until committed.
```

### Script to read from

Staging prevents inconsistent results. A file can physically exist before completion, but users cannot see it until the platform commits the invocation.

## Slide 20

### Contents

Title:

```text
Orchestrator role
```

Text:

```text
Reads job events
Chooses workers
Issues dispatch attempts
Validates claims
Tracks active state
Handles recovery
```

### Script to read from

The orchestrator is the active coordination component. It chooses workers, validates claims, tracks attempts, and recovers jobs when workers stop responding.

## Slide 21

### Contents

Title:

```text
Worker role
```

Text:

```text
Consumes assigned stream
Claims job
Downloads source or inputs
Runs Docker work
Reports completion
Maintains warm containers
```

### Script to read from

Workers are execution machines. They consume assigned jobs, claim them, run Docker builds or function containers, and report the result back to the platform.

## Slide 22

### Contents

Title:

```text
Reliability features
```

Main points:

```text
Redis Streams
Attempt fencing
Heartbeats
Lease recovery
Dead-letter jobs
Idempotent completion
```

### Script to read from

The reliability model uses Redis Streams, worker heartbeats, attempt fencing, recovery, and dead-letter jobs. These prevent most duplicate and lost-job cases in the prototype.

## Slide 23

### Contents

Title:

```text
Warm containers
```

Text:

```text
Cold path: create and start container
Warm path: reuse an idle container
Resident runner: avoid repeated Python startup
```

Benchmark callout:

```text
No-op median: 3918 ms to 88 ms
```

### Script to read from

Warm containers were the biggest latency improvement. With the resident warm runner, a no-op function dropped from about 3918 milliseconds to about 88 milliseconds in our benchmark.

## Slide 24

### Contents

Title:

```text
Performance bottlenecks
```

Text:

```text
Docker create/start
Python imports
File copying
Output artifact handling
Concurrent Docker contention
```

### Script to read from

The largest bottlenecks are still in the execution layer: Docker create and start time, Python imports, file operations, output artifact handling, and Docker contention under load.

## Slide 25

### Contents

Title:

```text
Observability
```

Text:

```text
Grafana dashboard
Prometheus metrics
Loki logs
Redis exporter
Postgres exporter
cAdvisor container metrics
```

### Script to read from

The observability stack uses Grafana for dashboards, Prometheus for metrics, Loki for logs, and exporters for Redis, Postgres, and container-level metrics.

## Slide 26

### Contents

Title:

```text
What did not work well
```

Text:

```text
Backend-centered coordination became too heavy
Docker copy/export paths were expensive
Vite dev serving is weak for production
Worker health missed consume-loop failure
Old private registry refs broke after network changes
```

### Script to read from

Several decisions changed along the way. Backend-centered coordination became too heavy, Docker copy/export was expensive, and the recent deployment showed that worker health must check the consume loop, not only the container state.

## Slide 27

### Contents

Title:

```text
Current state
```

Text:

```text
Working prototype
Separate userservice
V2 orchestrator
Two distributed workers
Function editor frontend
Token-based invocation
Artifacts and ZIP downloads
OpenAPI docs
```

### Script to read from

At this point, the project is a working prototype. It has authentication, function creation, builds, invocation, tokens, distributed workers, artifacts, frontend flows, and API documentation.

## Slide 28

### Contents

Title:

```text
Next steps
```

Text:

```text
Recover worker consume-loop failures
Harden distributed networking
Add stronger build resource limits
Improve dependency handling
Serve frontend as a production static build
Run longer failure and load tests
```

Closing line:

```text
The prototype proves the full serverless path.
```

### Script to read from

The next work is mostly reliability and production hardening. The prototype already proves the full serverless path, and it exposes the real tradeoffs in coordination, isolation, artifacts, and performance.

