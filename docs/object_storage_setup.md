# Object Storage Setup

The prototype can use an S3-compatible backend for Django media artifacts.

Current prototype configuration:

- Provider: Parspack S3-compatible object storage
- Bucket: `c966302`
- Status: enabled on the deployed control plane and live smoke-tested from the backend container

Environment variables:

- `OBJECT_STORAGE_ENABLED`
- `OBJECT_STORAGE_ENDPOINT_URL`
- `OBJECT_STORAGE_ACCESS_KEY_ID`
- `OBJECT_STORAGE_SECRET_ACCESS_KEY`
- `OBJECT_STORAGE_BUCKET_NAME`
- `OBJECT_STORAGE_REGION_NAME`
- `OBJECT_STORAGE_FORCE_PATH_STYLE`
- `OBJECT_STORAGE_MEDIA_LOCATION`

Notes:

- The backend keeps local storage unless object storage is explicitly enabled.
- The deployed control plane was still using local storage until 2026-09-02,
  so benchmark artifacts created before that fix stayed in the `backend-media`
  Docker volume and were not uploaded to Parspack retroactively.
- New source bundles, invocation inputs, invocation outputs, invocation logs and
  ZIP artifacts use Parspack when created after object storage is enabled.
- Invocation logs are stored as downloadable artifacts, with a short preview
  retained in PostgreSQL.
- The live smoke test saved, read, and deleted a tiny object through Django's
  default storage backend.
- A second smoke test saved, read, and deleted real invocation stdout/stderr log
  artifacts through `store_invocation_log_artifacts`.
- A public-domain user journey smoke test on 2026-09-02 created invocation
  `9273`; its `report.txt` output and stdout log both used `S3Storage` and
  returned `exists=True` through Django storage.
