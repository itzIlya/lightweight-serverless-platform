# Orchestrator Migration Steps 12-13 Test Report

Date: 2026-07-01

## Implemented

Step 12 adds bounded reconciliation without placing database or network work on
the execution path:

- Finalizing and terminal transitions atomically register unfinished work in
  Redis sorted sets.
- Successful Stream publication atomically removes the corresponding marker.
- Startup reclaims abandoned creation events, recovers expired leases, resumes
  finalizations, and republishes terminal projections in batches of 20.
- Steady-state repair runs every five seconds and performs no keyspace scan.
- Finalizer and projector failures remain pending in their consumer groups.
- A PostgreSQL auditor runs every 300 seconds with a batch size of 100 and one
  pipelined Redis read. It makes HTTP calls only for mismatches.
- Existing staged-artifact cleanup continues deleting expired uncommitted data.

Step 13 adds gradual creation-time routing:

- Separate build and invocation rollout percentages.
- Separate build and invocation function-ID canary lists.
- Deterministic SHA-256 bucketing, stable across retries.
- Existing pilot booleans act as immediate kill switches.
- Stored `coordination_version` permanently pins every created job.

## Overhead Bound

The empty safety audit performs exactly two bounded PostgreSQL queries, no
Redis roundtrip, and no HTTP request. With candidates, Redis states are loaded
through one non-transactional pipeline. The orchestrator performs two small
sorted-set reads every five seconds and processes no more than 20 repair items
per pass. Job creation adds only an in-process hash calculation.

## Automated Verification

- Backend: 82 tests passed.
- Scheduler/orchestrator: 61 tests passed.
- Worker: 58 tests passed.
- Migration drift: no changes detected.

Covered failure cases include crashes before finalization-event publication,
crashes before terminal-projection publication, projector database failure,
finalizer backend/orchestrator failure, pending-entry reclaim, committed
artifacts with missing or finalizing Redis state, stale attempts, deterministic
rollout, canary-only rollout, and kill-switch rollback.

## Live Restart Verification

1. The finalizer was stopped before V2 invocation 297 completed.
2. Redis reached `finalizing`; PostgreSQL stayed `running`; the public result
   stayed empty.
3. The orchestrator was restarted while the finalizer remained unavailable.
4. Restarting the finalizer committed the completion and both stores converged
   to `succeeded` without re-execution.
5. Redis, backend, orchestrator, projector, finalizer, and all three workers
   were restarted. Redis AOF preserved terminal state and the artifact commit.
6. With general rollout at 0%, function 28 was explicitly canaried to V2 while
   function 27 remained a V1 control. Both invocations succeeded.

Temporary connection and `BUSYLOADING` errors appeared while Redis was
deliberately restarting. All retry loops recovered automatically and the final
bounded audit reported no unresolved mismatch.

## Remaining Dependency

Step 11 is still pending. User-facing V2 status reads currently use the
PostgreSQL projection rather than Redis-first active status. Steps 12 and 13 are
safe to keep deployed with pilot flags disabled while that read-path change is
implemented and tested.
