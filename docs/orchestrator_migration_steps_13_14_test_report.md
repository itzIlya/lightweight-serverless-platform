# Orchestrator Migration Steps 13-14 Test Report

Date: 2026-07-01

## Step 13: Ordered Cutover

New jobs are routed through these eligibility stages:

1. `internal`: only explicit function-ID canaries.
2. `builds`: build jobs.
3. `private`: private owner invocations.
4. `token`: token-protected invocations.
5. `public`: public invocations.
6. `all`: all job classes, with both percentages set to 100 for final cutover.

Canaries bypass the percentage only after the internal stage is enabled.
Non-canary eligible jobs use deterministic SHA-256 bucketing. Pilot booleans
remain immediate kill switches, and every stored Job remains pinned to its
creation-time `coordination_version`.

## Monitoring

The protected orchestrator `/metrics/` endpoint reports:

- terminal success/failure count and error rate;
- current finalizing count and oldest finalizing age;
- duplicate dispatches, claims, completions, and finalizations;
- recovery count;
- PostgreSQL projector lag/pending count;
- invocation finalizer lag/pending count.

Exceptional counters and terminal outcomes are updated inside existing Redis
Lua transitions. Finalizing age uses one sorted set. Reading metrics performs
no PostgreSQL query and no Redis job scan.

## Step 14: Retirement Controls

Actual V1 retirement was intentionally not activated because the required soak
period has not occurred. The following controls are ready:

- `V1_JOB_CREATION_ENABLED=false` prevents creation of any job that is not
  eligible for V2.
- `v1_retirement_status` verifies terminal V1 Jobs and empty known V1 Lists.
- `V1_COORDINATION_ENDPOINTS_ENABLED=false` changes V1 dispatch, claim,
  requeue, build-report, and invocation-report endpoints to HTTP 410.
- `retire_v1_queues --confirm RETIRE_V1` refuses deletion unless the drain gate
  passes, then deletes only known V1 List keys.
- Compatibility code remains present for the required release window.

The live readiness check currently reports zero active V1 jobs and zero queued
V1 items, but both compatibility switches remain enabled.

## Verification

- Backend: 89 tests passed.
- Scheduler/orchestrator: 63 tests passed.
- Worker: 58 tests passed.
- Migration drift: no changes detected.

The full reliability matrix covers duplicate dispatch/claim, stale attempts,
worker crashes before and after execution, crash after staged upload, lost
completion responses, orchestrator finalization crashes, backend commit
failure, Redis restart, projector outage, staged expiry, reconciliation, and
simultaneous V1/V2 operation.

A deployed internal-stage canary produced V2 invocation 300. Its live metrics
reported one terminal success, zero errors, zero finalizing jobs, zero
duplicates, zero recoveries, and zero projector/finalizer lag.

Redis was also restarted while V2 invocation 301 was `finalizing` and its
finalizer delivery had not been ACKed. AOF restored the same completion ID and
`finalizing` state. After the finalizer restarted, Redis and PostgreSQL both
reached `succeeded`, the result became visible, and the committed artifact UUID
matched without another function execution.

## Required Before Activation

Step 11 Redis-first status reads is still pending. After Step 11, run a sustained
full-V2 soak with alert thresholds for every metric above. Only then disable V1
creation, drain existing V1 jobs, disable its endpoints, hold compatibility for
one release, and retire the Lists.
