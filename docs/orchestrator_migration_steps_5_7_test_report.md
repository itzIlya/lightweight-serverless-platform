# Orchestrator Migration Steps 5-7 Test Report

Date: 2026-06-30

## Scope

- Step 5: transactional outbox and idempotent Redis Stream relay
- Step 6: no-authority V2 shadow orchestrator
- Step 7: Redis-owned worker heartbeat/capacity state with Django projection

## Step 5 Results

- Job and outbox creation commit or roll back together.
- Build and invocation enqueue each create exactly one `job.created` event.
- Redis publication failures leave events unpublished and retryable.
- Published events record their Stream ID and are not selected again.
- Real crash-window replay passed: Redis received the event, PostgreSQL was
  deliberately left unpublished, and retry still left exactly one Stream entry.

## Step 6 Comparison Gate

The dedicated `test_v1_v2_comparison.py` suite passed all five scenarios:

1. Invocation chooses the least-loaded worker.
2. Invocation avoids a worker with an active build.
3. Build chooses an idle worker.
4. Invocation returns no placement when every worker is building.
5. Build returns no placement when every worker is busy.

A live synthetic event also verified:

- Shadow selected a valid worker.
- Every production worker queue length remained unchanged.
- No production `Job` row existed for the synthetic shadow event.

## Step 7 Results

- Atomic heartbeat stores capacity, active counts, queue names, and lease expiry.
- Repeated heartbeat refreshes one worker record rather than duplicating it.
- Atomic stale expiry cannot mark a worker offline after a newer heartbeat.
- Three live workers appeared in Redis and in the Django compatibility
  projection with matching concurrency and activity values.
- Shadow placement selected one of the workers in the live Redis lease set.
- Redis heartbeat failure did not suppress Django projection.
- Raw backend connection reset did not terminate the heartbeat loop.

## Final Regression Gate

- Backend: 64 tests passed
- Scheduler: 42 tests passed
- Worker: 53 tests passed
- Migration drift: `No changes detected`
- Outbox migration applied successfully: `jobs.0004_outboxevent`

The only warning was the known development JWT secret length warning. It does
not affect these migration tests, but production must use a dedicated secret of
at least 32 bytes.

## Remaining Before Production V2

- Reclaim abandoned Redis Stream pending entries.
- Add V2 dispatch, claim, lease, recovery, and completion interfaces.
- Project V2 state to PostgreSQL for user-facing reads.
- Test canary routing and rollback with mixed V1/V2 jobs.
