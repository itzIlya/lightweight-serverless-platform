# Real World Integrity Suite Report

Date: 2026-07-30

## Purpose

This run tested the newest product-policy changes under realistic platform
activity:

- active build/image replacement
- concurrent invocations while a source replacement is queued and built
- declared output visibility
- invocation read-token isolation
- invocation-time input file delivery
- per-function invocation history
- registry image cleanup after replacement
- registry image cleanup after function deletion
- a heavier concurrent invocation burst

## Environment Notes

The first run against `http://localhost:8000` failed because Windows resolved
`localhost` to IPv6 `::1`, and that connection was reset. `127.0.0.1` worked.

The first real API run with object storage enabled failed during source upload:

```text
Could not connect to the endpoint URL:
https://c966302.parspack.net/c966302/media/function_bundles/v1.zip
Temporary failure in name resolution
```

That is an environment/DNS outage for Parspack from inside the backend
container, not an application assertion failure.

The normal Parspack stack was restored with:

```powershell
docker compose up -d backend outbox-relay orchestrator-projector orchestrator-reconciler staged-artifact-cleaner
```

The backend then reported `OBJECT_STORAGE_ENABLED=True`, and a direct Django
storage smoke test against Parspack passed:

- save: passed
- exists after save: passed
- read body: passed
- delete: passed
- exists after delete: false

## Test 1: Source Replacement Under Concurrent Traffic

Command:

```powershell
python .\scripts\real_world_integrity_suite.py --base-url http://127.0.0.1:8000 --output-json .\docs\real_world_integrity_suite_parspack_latest.json --skip-docker-inspection
```

Result: passed.

What happened:

1. Registered a real JWT user.
2. Created a private function.
3. Uploaded and built `v1`.
4. Submitted 4 concurrent `v1` invocations that each slept for 2 seconds.
5. Submitted a source replacement while those invocations were still running.
6. Verified function detail still pointed at the old active version and exposed
   `pending_build`.
7. Submitted one more default invocation during the candidate build.
8. Waited for replacement build `r2` to complete.
9. Verified all pre-promotion and during-build invocations returned marker
   `v1`.
10. Submitted 3 post-promotion invocations, including one multipart input-file
    invocation.
11. Verified all post-promotion invocations returned marker `v2`.
12. Verified the uploaded input file reached the function.
13. Verified only declared output `report.txt` was downloadable; the function
    also wrote an undeclared `extra.txt`, but it was not exposed.
14. Verified a wrong invocation read token was rejected with HTTP `403`.
15. Verified `GET /api/functions/{id}/invocations/` returned the function
    invocation history.

Summary from latest run:

```json
{
  "storage_backend": "parspack_s3",
  "completed_v1_invocations": 5,
  "completed_v2_invocations": 3,
  "function_invocation_history_count": 8,
  "downloaded_output": "v2 report for file-call",
  "wrong_read_token_status": 403,
  "wall_seconds": 49.578
}
```

## Test 2: Registry Cleanup After Replacement

Command:

```powershell
docker compose run --rm backend python manage.py cleanup_function_images --registry-base-url http://registry:5000
```

Result: passed.

The cleanup command reported:

```text
function_image_cleanup={'checked': 10, 'deleted': 10, 'failed': 0, 'skipped_active': 0}
```

External registry verification:

- old replaced image manifest after cleanup: HTTP `404`
- new active image manifest before function delete: HTTP `200`
- post-cleanup invocation on the new image: `succeeded`

This proves the old image was removed while the active image remained usable.

## Test 3: Registry Cleanup After Function Deletion

The throwaway function was deleted through the public API. Then image cleanup was
run again. External registry verification showed:

- new image manifest after function-delete cleanup: HTTP `404`

This proves function deletion schedules the active image for removal, and the
cleanup path can remove it after the function is gone.

## Test 4: Heavier Concurrent Invocation Burst

Command:

```powershell
python .\scripts\concurrent_invocation_workload.py --base-url http://127.0.0.1:8000 --count 8 --sleep-seconds 1 --output-json .\docs\real_world_concurrent_workload_parspack_after_milestone_7.json
```

Result: passed.

Summary:

```json
{
  "invocation_count": 8,
  "sleep_seconds": 1.0,
  "sequential_sleep_seconds": 8.0,
  "client_submit_elapsed_seconds": 0.359,
  "client_poll_elapsed_seconds": 15.609,
  "client_wall_elapsed_seconds": 15.968,
  "statuses": ["succeeded"],
  "duration_ms_min": 4552,
  "duration_ms_max": 6234,
  "duration_ms_median": 5925,
  "read_token_returned": true
}
```

This verifies integrity under parallel load. Performance is still not ideal:
one-second user work had median platform-side duration around 4.7 seconds in
this local Docker setup.

## Findings

Passed:

- Source replacement does not break in-flight invocations.
- Active version does not switch before candidate build completion.
- Default invocation uses old active image during replacement build.
- Default invocation uses new active image after successful replacement build.
- Declared output filtering works in a real container.
- Invocation read-token isolation works.
- Multipart input bytes reach the function.
- Per-function invocation history works.
- Old registry image can be deleted after replacement.
- Active image remains invokable after cleanup.
- Active image can be deleted after the function is deleted.
- 8 concurrent invocations all reached `succeeded`.

Important environment findings:

- Use `127.0.0.1` instead of `localhost` on this Windows setup for host-side
  tests.
- Object storage is currently unavailable from the backend container because
  DNS resolution for `c966302.parspack.net` temporarily failed during the first
  run, then recovered. The final run used Parspack successfully.

Contract note:

- Backend input-file metadata uses `original_name`.
- Sandbox metadata currently exposes the filename as `name`.
- The test now accepts the sandbox contract, but we should document or align
  this before frontend/user docs.

## Artifacts

- Raw integrity summary:
  `docs/real_world_integrity_suite_parspack_latest.json`
- Raw concurrent workload summary:
  `docs/real_world_concurrent_workload_parspack_after_milestone_7.json`
- Test script:
  `scripts/real_world_integrity_suite.py`
