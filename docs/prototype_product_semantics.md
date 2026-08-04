# Prototype Product Semantics

Date: 2026-07-30

This document freezes the user-facing product rules for the next prototype
phase. Internal models may still use `FunctionVersion` and build attempts, but
the frontend should present a simpler model.

## Function Source

- A function owns its source bundle.
- Submitted source is retained indefinitely.
- Source is deleted only when the user deletes the function.
- Invocation downloads must not include source code.

## Build/Image Model

User-facing rule:

- A function has one active build/image.
- A different build means the same function has been rebuilt, not that the user
  selected among many public versions.
- If the source changes, the function must be rebuilt.
- The active build is represented internally by `Function.active_version`.
- A source replacement creates a candidate `FunctionVersion`; traffic keeps
  using `active_version` until the candidate build succeeds.

Safe rebuild rule:

1. Keep the old image active.
2. Store the new source.
3. Build a new attempt-specific candidate image.
4. If the build succeeds, atomically switch the function to the new image.
5. Mark the old image `pending_delete` only after the successful switch.
6. If the build fails, keep the old image active.
7. If a failed candidate build produced an image, mark that image
   `pending_delete`.

This avoids breaking a working function because a replacement build failed.

Current implementation note:

- `FunctionImage` records track active, candidate, pending-delete, deleted, and
  delete-failed image references.
- `cleanup_function_images` performs registry deletion outside the user request
  path.
- The cleanup path re-checks whether an image is still active before deleting
  it.
- Deleting a function removes source bundles and invocation artifacts, then
  schedules its image references for deletion.
- Function detail responses include `active_image_ref`, `build_status`, and
  `pending_build` so the frontend can show the current product state without
  reasoning through all internal version rows.
- `GET /api/functions/{id}/invocations/` lists invocation history for that
  function.

## Invocation Retention

- Invocations are available for 7 days.
- When an invocation expires, the whole invocation disappears:
  - invocation row
  - input files
  - output files
  - stdout/stderr logs
  - read token
  - invocation job records
- Non-terminal invocations are not removed by retention cleanup.

Current implementation note:

- Invocation logs are now written as storage-backed artifacts.
- PostgreSQL keeps short stdout/stderr previews for status reads and quick
  inspection.
- The Parspack object-storage backend is configured and live smoke-tested for
  direct Django storage writes and invocation log artifacts.

## Invocation Download

While an invocation is still available, users should eventually be able to
download a ZIP bundle:

```text
invocation-<request_id>.zip
  manifest.json
  input/
  output/
  logs/
```

`manifest.json` should include references to the function and image used, but
not source code.

## Dead Letters

- Dead-letter jobs are platform debugging records.
- They are retained separately from user invocation artifacts.
- Default retention is 60 days.
