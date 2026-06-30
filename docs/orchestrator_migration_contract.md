# Orchestrator Migration Contract

This document freezes the current job-coordination behavior before the V2
orchestrator migration. Jobs never change coordination protocol after creation.

## Protocol Selection

- `coordination_version=1`: Django/PostgreSQL dispatch, claim, recovery, and
  terminal reporting remain authoritative.
- `coordination_version=2`: reserved for Redis-backed orchestrator state. V2 is
  not routed to production execution until a later migration phase.

Existing rows and newly created jobs default to V1. Cutover flags must select a
version only when creating a job; they must never reroute an in-flight job.

## V1 State Contract

| Operation | Required state | Result |
| --- | --- | --- |
| Dispatch | `queued` and available | `dispatched`, worker and attempt recorded |
| Claim | `dispatched`, matching worker/attempt | `running` |
| Duplicate claim | `running`, matching worker/attempt | accepted idempotently |
| Recover | any non-terminal assigned state | `queued` or `dead_lettered` |
| Build/invocation running report | active state | `running` |
| Successful final report | active matching attempt | `succeeded` |
| Failed final report | active matching attempt | `failed` |
| Cancellation | cancellable state | `cancelled` |

Terminal V1 states are `succeeded`, `failed`, `cancelled`, and
`dead_lettered`. Claims and recovery requests do not reopen terminal jobs.

## V1 Durability Boundaries

- PostgreSQL `Job` rows are the durable coordination source of truth.
- Redis Lists carry job IDs and delivery envelopes.
- Worker deliveries move atomically to a processing List before execution.
- A worker ACK removes its delivery only after terminal reporting.
- `dispatch_attempt` fences stale worker claims and reports.

## V2 Isolation Rule

The initial V2 state-machine implementation is shadow-only. Production API,
scheduler, and worker paths must continue creating and processing V1 jobs until
an explicit later cutover step is implemented and tested.

## Steps 5-7 Migration State

The following bridge infrastructure is now active:

- Each new V1 `Job` and its `job.created` outbox event are committed in one
  PostgreSQL transaction.
- The outbox relay publishes events to the `orchestrator:events` Redis Stream.
- Publication is idempotent by `event_id`; replaying the Redis-success / database-
  update-failure window returns the original Stream ID instead of adding a
  duplicate event.
- The shadow orchestrator consumes the Stream and writes only to
  `orchestrator:v2:shadow:*` keys.
- Shadow placement can model a V2 dispatch, but it cannot call the production
  dispatch endpoint or push a worker queue.
- Workers write heartbeat, capacity, activity, queue names, and a 30-second
  lease to `orchestrator:v2:worker:*`.
- V2 shadow placement reads workers from Redis. Workers continue sending the
  same heartbeat to Django as a compatibility projection for V1.

The production V1 scheduler still reads Django worker records, coordinates
jobs in PostgreSQL, and uses Redis Lists. The outbox and shadow state do not
change production execution.

## Required Before V2 Cutover

- Reclaim abandoned Redis Stream consumer-group pending entries.
- Add production orchestrator dispatch, claim, lease, recovery, and completion
  APIs with attempt fencing.
- Project authoritative V2 state back to PostgreSQL for user-facing reads.
- Preserve the staged artifact/finalization rule before terminal success.
- Run canary and rollback tests with mixed V1/V2 jobs.

## Steps 8-9 Pilot State

Production-shaped V2 authority now exists behind creation-time pilot flags:

- `V2_BUILD_PILOT_ENABLED=true` creates new build jobs as V2.
- `V2_INVOCATION_PILOT_ENABLED=true` creates new invocation jobs as V2.
- Both flags default to `false`; jobs already created never change protocol.

The V2 path is:

`transactional outbox -> Redis event Stream -> orchestrator -> worker Stream ->`
`orchestrator claim/lease -> worker execution -> orchestrator finalization ->`
`PostgreSQL projector`

Dispatch atomically updates the fenced attempt and appends the worker Stream
entry. Both dispatched and running jobs hold expiring leases. Recovery requeues
the job, increments the next dispatch attempt, ACKs the abandoned delivery, and
fences old claims and completions.

Build image tags include both the durable build attempt and orchestrator
dispatch attempt. PostgreSQL exposes the image on `FunctionVersion` only after
the orchestrator has finalized success with that image as the artifact commit.
Expired build attempts emit orphan-image events; the cleanup consumer resolves
the registry manifest digest and deletes it idempotently.

V2 invocation inputs and output uploads still use protected backend endpoints.
The orchestrator owns dispatch, claim, leases, running state, and terminal
fencing. Running state reaches PostgreSQL asynchronously through the projector.
The backend result write happens before orchestrator completion, preserving the
artifact-before-terminal invariant.
