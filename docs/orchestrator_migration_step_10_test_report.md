# Orchestrator Migration Step 10 Test Report

Date: 2026-07-01

## Scope

Step 10 adds staged V2 invocation results and outputs. Physical artifacts may
exist before terminal completion, but user APIs publish neither result metadata
nor files until finalization succeeds.

## Protocol Verified

1. The worker uploads declared outputs with `job_id`, `dispatch_attempt`,
   `completion_id`, size, and SHA-256 checksum.
2. The backend stores files as `staged`; list and download APIs hide them.
3. The worker reports the result and output manifest to the orchestrator.
4. Redis atomically changes `running -> finalizing`, stores the completion, ACKs
   the worker delivery, and emits one finalization event.
5. The finalizer verifies the exact backend manifest and commits the staged
   completion idempotently.
6. The orchestrator verifies the completion and artifact commit IDs, changes
   `finalizing -> succeeded|failed`, and emits one terminal projection.
7. PostgreSQL publishes result metadata and committed output files.

## Automated Tests

- Backend: 71 tests passed.
- Scheduler/orchestrator: 57 tests passed.
- Worker: 58 tests passed.
- Migration drift check: no changes detected.

The focused safety cases verify:

- A worker can upload a file and die before completion; the invocation remains
  running/recoverable, its result is empty, and list/download APIs reveal no
  output.
- Invalid checksums and manifests cannot commit.
- Commit retries return the same artifact commit ID.
- Completion retries emit only one finalization event.
- Finalization retries emit only one terminal event.
- Old dispatch attempts cannot enter finalization.
- Backend or orchestrator failure leaves the finalization Stream entry pending.
- Expired uncommitted stages delete their physical files.
- A staged-output transport failure withholds worker completion so lease
  recovery can retry execution.

## Live Verification

A real V2 invocation used three running workers and existing built version 35.

```text
invocation_id: 296
job_id: 7ed96f4b-7faa-4132-9619-254ef580ea67
coordination_version: 2
final invocation status: succeeded
projected job status: succeeded
staged completion status: committed
artifact_commit_id: de8ba964-ea2d-41ec-bf1e-511b8354321a
```

Service logs showed the expected order: claim, lease renewal, completion
acceptance, and finalization. The committed result became visible only after
the finalizer supplied the artifact commit ID and the terminal projector ran.

## Remaining Risk

The failure boundaries are covered by deterministic integration tests, but a
larger process-kill and network-partition campaign remains future work. Both V2
pilot flags still default to `false`, so normal API-created jobs remain V1 until
an explicit canary rollout.
