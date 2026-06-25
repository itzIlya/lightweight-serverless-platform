# Output File Validation Test Plan

Date: 2026-06-25

This document describes the output-file validation checks currently covered by
the backend and worker tests.

The goal is to make sure a function can only persist declared output files and
that invalid output conditions fail before the worker uploads anything to the
backend.

## Runtime Behavior Under Test

The worker now follows this order during and after execution:

1. Mount `/sandbox/output` as tmpfs, sized from the version total output limit.
2. Run the function runner.
3. Copy `/sandbox/output/.` into `/sandbox/export/output/` before the
   container exits.
4. Let the container exit normally with the runner exit code.
5. Copy `/sandbox/export` from the stopped container through Docker archive.
6. Read `result.json` or stdout for the function return value.
7. Validate declared output files against the invocation job contract.
8. If validation fails, return invocation status `failed`.
9. If validation fails, upload no output files.
10. If validation passes, upload only declared root-level output files.

The backend still validates uploads too. So the system has two layers:

- Worker-side validation: avoids unnecessary uploads and gives a fast invocation
  failure.
- Backend-side validation: protects persisted artifact storage and remains the
  final enforcement point.

## Worker-Side Conditions

Run:

```powershell
docker compose exec worker python -m unittest discover -s worker -p test_*.py -v
```

Covered cases:

| Test | Purpose | Expected behavior |
| --- | --- | --- |
| `test_collect_declared_output_files_ignores_extra_files` | Function writes declared and undeclared files. | Worker collects only declared files. |
| `test_upload_output_files_sends_declared_files_to_backend` | Valid declared output exists. | Worker uploads it with original path, position, and content type. |
| `test_executor_mounts_output_as_size_limited_tmpfs` | Worker creates the function container. | `/sandbox/output` is mounted as tmpfs with the version output size. |
| `test_wait_for_exit_returns_container_exit_code` | Function container has exited. | Worker uses the normal container exit code. |
| `test_copy_directory_from_container_uses_docker_archive` | Worker copies exported output from a stopped container. | Worker uses Docker archive, not an exec/live-tar stream. |
| `test_executor_fails_invocation_when_output_export_fails` | The wrapper cannot copy tmpfs output into `/sandbox/export`. | Invocation fails and no output upload is attempted. |
| `test_worker_output_validation_rejects_non_list_declaration` | Job payload has invalid `declared_output_files` type. | Validation fails. |
| `test_worker_output_validation_rejects_unsafe_declared_name` | Declaration contains `../secret.txt`. | Validation fails. |
| `test_worker_output_validation_rejects_result_json_declaration` | Declaration contains reserved `result.json`. | Validation fails. |
| `test_worker_output_validation_rejects_directory_output` | Declared output path exists but is a directory. | Validation fails. |
| `test_worker_output_validation_enforces_file_count_limit` | More declared files are produced than allowed. | Validation fails. |
| `test_worker_output_validation_enforces_per_file_size_limit` | One declared file exceeds per-file size limit. | Validation fails. |
| `test_worker_output_validation_enforces_total_size_limit` | Combined declared output size exceeds total limit. | Validation fails. |
| `test_worker_output_validation_missing_declared_output_is_allowed` | A declared output file is not produced. | Validation passes with no uploaded file. |
| `test_worker_output_validation_skips_upload_when_invalid` | Container exits successfully but output is too large. | Invocation result becomes failed and no upload is attempted. |

Important current rule:

```text
declared_output_files = ["report.txt"]
```

means:

```text
/sandbox/output/report.txt
```

It does not mean:

```text
/sandbox/output/nested/report.txt
```

Only root-level output files are collected.

## Backend-Side Conditions

Run:

```powershell
docker compose exec backend python manage.py test apps.jobs apps.invocations
```

Covered cases:

| Test | Purpose | Expected behavior |
| --- | --- | --- |
| `test_invocation_enqueue_creates_durable_job_record` | Invocation job payload includes output contract. | Worker receives declared files and limits. |
| `test_internal_worker_upload_stores_declared_output` | Worker uploads a valid declared file. | Backend stores metadata and file. |
| `test_internal_worker_upload_requires_shared_secret` | Upload lacks internal token. | Backend returns `401`. |
| `test_internal_worker_upload_rejects_undeclared_output` | Worker uploads `extra.txt` when only `report.txt` is declared. | Backend returns `400`, stores nothing. |
| `test_internal_worker_upload_rejects_unsafe_output_path` | Worker uploads `../report.txt`. | Backend returns `400`, stores nothing. |
| `test_internal_worker_upload_enforces_file_size_limit` | Worker uploads a file over the version limit. | Backend returns `400`, stores nothing. |
| `test_owner_can_list_and_download_outputs` | Owner requests output metadata/download. | Backend allows access. |
| `test_other_user_cannot_list_outputs` | Different user requests output metadata. | Backend denies access. |
| `test_invocation_read_token_can_read_result_and_outputs` | Token/public caller uses invocation read token. | Backend allows access to only that invocation. |
| `test_wrong_invocation_read_token_is_rejected` | Caller uses wrong invocation read token. | Backend returns `403`. |

## Full Verification

Recommended full check:

```powershell
python -m py_compile worker\executor.py worker\test_worker.py
docker compose exec worker python -m unittest discover -s worker -p test_*.py -v
docker compose exec backend python manage.py test apps.accounts apps.functions apps.invocations apps.jobs apps.workers
docker compose exec backend python manage.py makemigrations --check --dry-run
python scripts\user_journey_smoke.py --base-url http://localhost:8000
```

Verified on 2026-06-25:

```text
Worker suite: 38 tests, OK
Backend suite: 56 tests, OK
Migration drift check: No changes detected
Smoke test: SMOKE TEST PASSED
Smoke IDs: function_id=13, version_id=20, invocation_id=23
Downloaded output: report.txt -> Processed Ilya with total=6
```

## What This Does Not Solve Yet

The tmpfs quota protects worker disk by keeping `/sandbox/output` memory-backed
and size-limited. It does mean output files compete with memory, so this design
is best for small artifacts. Larger outputs should eventually use a different
artifact strategy, such as direct object-storage upload.
