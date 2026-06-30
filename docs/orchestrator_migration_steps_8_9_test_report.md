# Orchestrator Migration Steps 8-9 Test Report

Date: 2026-06-30

## Step 8: V2 Build Pilot

Implemented flow:

`outbox -> orchestrator event Stream -> atomic dispatch -> worker build Stream ->`
`claim/lease -> build/push -> idempotent completion -> PostgreSQL projector`

Build safeguards:

- Image tags contain the build-attempt UUID prefix and dispatch attempt.
- Dispatch state and worker Stream publication are one Redis Lua operation.
- Successful completion requires a nonempty artifact commit ID.
- `FunctionVersion.image_ref` is projected only after Redis finalizes success.
- Lease recovery fences the old attempt and emits orphan-image cleanup.
- Registry deletion resolves a tag to its digest and is idempotent on 404.
- Repeated crashes eventually dead-letter instead of retrying forever.

Gate results:

- Duplicate completion: passed; one terminal projection was emitted.
- Lost completion response: passed; retry returned idempotent success.
- Worker crash while running: passed; attempt 1 was fenced and attempt 2 used a
  different immutable image tag.
- Orphan cleanup: detection, digest resolution, delete request, and missing-image
  idempotency passed.
- Real V2 builds: two succeeded through the complete live pipeline.
- Image visibility: 11 nonterminal samples all hid the new image; the finalized
  image became visible afterward.

## Step 9: V2 Invocation Dispatch and Claims

Implemented flow:

- Orchestrator selects a live Redis-owned worker.
- Atomic dispatch appends to `worker:<name>:v2:invocations`.
- Worker claims through the protected orchestrator API.
- Matching worker and dispatch attempt receive a renewable lease.
- Running state is authoritative in Redis and projected asynchronously.
- Inputs and output uploads continue through protected backend APIs.
- Durable backend result persistence occurs before orchestrator completion.

Crash-transition gates:

- Dispatch: state and Stream message cannot split.
- Delivery before claim: dispatch lease expiry requeues; old delivery is fenced.
- Claim response loss: duplicate matching claim is idempotent.
- Running worker crash: lease recovery requeues and old completion is rejected.
- Repeated crashes: job dead-letters at its configured recovery limit.

One real V2 invocation succeeded with a one-second user function. Redis running
and asynchronously projected PostgreSQL running state were both observed before
Redis, PostgreSQL Job, and Invocation all reached `succeeded` at attempt 1.

## Final Verification

- Backend: 67 tests passed
- Scheduler/orchestrator: 52 tests passed
- Worker: 56 tests passed
- Migration drift: `No changes detected`
- Live V2 jobs: 2 builds and 1 invocation, all succeeded
- Ready jobs: 0
- Active V2 job leases: 0
- Production event pending entries: 0
- Projection pending entries: 0
- Worker Stream pending entries: 0
- Live workers: 3

Both pilot flags remain disabled by default. Set one or both in `.env` only for
controlled canary traffic:

```text
V2_BUILD_PILOT_ENABLED=true
V2_INVOCATION_PILOT_ENABLED=true
```
