# User Journey Smoke Test

This smoke test shows the current average user experience of the platform:

1. Register a user and receive JWT tokens.
2. Create a function.
3. Upload a Python function version as a zip bundle.
4. Queue an asynchronous image build.
5. Poll until the version is built.
6. Invoke the function.
7. Poll until the invocation succeeds.
8. List and download a declared output file.
9. Read the JSON result, stdout/stderr metadata, timing, and status.

The current platform is asynchronous for build and invocation work. The create,
build, and invoke API calls return quickly; the user then polls resource APIs for
status and results.

## Run the Automated Smoke Test

From the project root:

```powershell
python scripts\user_journey_smoke.py --base-url http://localhost:8000
```

Expected ending:

```text
SMOKE TEST PASSED
{
  "function_id": ...,
  "version_id": ...,
  "invocation_id": ...,
  "invocation_status": "succeeded"
}
```

Verified locally on 2026-06-24:

```text
1. Register user and receive JWT
   user=smoke_4457ca4a role=user
2. Create function
   function_id=12 slug=smoke-echo-4457ca4a
3. Upload function version
   version_id=19 build_status=pending
4. Queue build
   build: queued
   build: building
   build: built
   image_ref=localhost:5000/functions/smoke-echo-4457ca4a:v19-v1
5. Invoke function
   invocation_id=22 request_id=c75876f8-c35d-43c9-8906-4342213ba267
   invocation: queued
   invocation: running
   invocation: succeeded
6. List and download invocation output file
   output_id=4 report.txt='Processed Ilya with total=6'
SMOKE TEST PASSED
```

The test creates a temporary zip bundle containing:

```python
import os


def main(event, context):
    name = event.get("name", "friend")
    numbers = event.get("numbers", [])
    output_dir = os.environ.get("FUNCTION_OUTPUT_DIR")
    if output_dir:
        with open(os.path.join(output_dir, "report.txt"), "w", encoding="utf-8") as output:
            output.write(f"Processed {name} with total={sum(numbers)}")
    return {
        "message": f"Hello, {name}!",
        "echo": event,
        "sum": sum(numbers),
        "request_id": context.get("request_id"),
    }
```

The expected result is:

```json
{
  "message": "Hello, Ilya!",
  "echo": {
    "name": "Ilya",
    "numbers": [1, 2, 3]
  },
  "sum": 6,
  "request_id": "<invocation request id>"
}
```

The expected output file is:

```text
report.txt -> Processed Ilya with total=6
```

## Reproduce Manually in PowerShell

Set a base URL:

```powershell
$base = "http://localhost:8000"
```

Create a temporary function bundle:

```powershell
$suffix = [guid]::NewGuid().ToString("N").Substring(0, 8)
$testDir = Join-Path $PWD "work\manual-smoke-$suffix"
New-Item -ItemType Directory -Force $testDir | Out-Null

@'
import os


def main(event, context):
    name = event.get("name", "friend")
    numbers = event.get("numbers", [])
    output_dir = os.environ.get("FUNCTION_OUTPUT_DIR")
    if output_dir:
        with open(os.path.join(output_dir, "report.txt"), "w", encoding="utf-8") as output:
            output.write(f"Processed {name} with total={sum(numbers)}")
    return {
        "message": f"Hello, {name}!",
        "echo": event,
        "sum": sum(numbers),
        "request_id": context.get("request_id"),
    }
'@ | Set-Content -Encoding UTF8 (Join-Path $testDir "handler.py")

"" | Set-Content -Encoding UTF8 (Join-Path $testDir "requirements.txt")
"{}" | Set-Content -Encoding UTF8 (Join-Path $testDir "config.json")

Compress-Archive -Path "$testDir\handler.py","$testDir\requirements.txt","$testDir\config.json" `
  -DestinationPath "$testDir\function.zip" -Force
```

Register a user:

```powershell
$registerBody = @{
  username = "manual_$suffix"
  email = "manual_$suffix@example.com"
  password = "StrongerPass123!"
} | ConvertTo-Json

$auth = Invoke-RestMethod -Method Post -Uri "$base/api/auth/register/" `
  -ContentType "application/json" -Body $registerBody

$token = $auth.access
```

Create a function:

```powershell
$functionBody = @{
  name = "Manual Smoke $suffix"
  description = "Manual user journey smoke test."
  invoke_access = "private"
} | ConvertTo-Json

$function = Invoke-RestMethod -Method Post -Uri "$base/api/functions/" `
  -Headers @{ Authorization = "Bearer $token" } `
  -ContentType "application/json" -Body $functionBody
```

Upload a function version with `curl.exe`:

```powershell
$versionJson = curl.exe -sS -X POST "$base/api/functions/$($function.id)/versions/" `
  -H "Authorization: Bearer $token" `
  -F "version=v1" `
  -F "runtime=python3.13" `
  -F "handler=handler.main" `
  -F "config={""memory_mb"":128,""timeout_seconds"":10}" `
  -F "declared_output_files=[""report.txt""]" `
  -F "invocation_output_max_files=1" `
  -F "invocation_output_max_file_size_mb=1" `
  -F "invocation_output_max_total_size_mb=1" `
  -F "source_bundle=@$testDir\function.zip"

$version = $versionJson | ConvertFrom-Json
```

Queue a build:

```powershell
Invoke-RestMethod -Method Post -Uri "$base/api/versions/$($version.id)/build/" `
  -Headers @{ Authorization = "Bearer $token" }
```

Poll until the build is complete:

```powershell
do {
  Start-Sleep -Seconds 3
  $version = Invoke-RestMethod -Method Get -Uri "$base/api/versions/$($version.id)/" `
    -Headers @{ Authorization = "Bearer $token" }
  $version.build_status
} while ($version.build_status -in @("pending", "queued", "building", "cancelling"))

$version
```

Invoke the function:

```powershell
$invokeBody = @{
  version = "v1"
  event = @{
    name = "Ilya"
    numbers = @(1, 2, 3)
  }
} | ConvertTo-Json -Depth 4

$invocation = Invoke-RestMethod -Method Post -Uri "$base/api/functions/$($function.id)/invoke/" `
  -Headers @{ Authorization = "Bearer $token" } `
  -ContentType "application/json" -Body $invokeBody

$readToken = $invocation.read_token
```

Poll until the invocation is complete:

```powershell
do {
  Start-Sleep -Seconds 2
  $invocation = Invoke-RestMethod -Method Get -Uri "$base/api/invocations/$($invocation.id)/" `
    -Headers @{ Authorization = "Bearer $token" }
  $invocation.status
} while ($invocation.status -in @("queued", "running"))

$invocation.result | ConvertTo-Json -Depth 6
```

List and download the declared output file:

```powershell
$outputs = Invoke-RestMethod -Method Get -Uri "$base/api/invocations/$($invocation.id)/outputs/" `
  -Headers @{ "X-Invocation-Read-Token" = $readToken }

$outputs

$outputPath = Join-Path $testDir "downloaded-report.txt"
Invoke-WebRequest -Method Get `
  -Uri "$base/api/invocations/$($invocation.id)/outputs/$($outputs[0].id)/download/" `
  -Headers @{ "X-Invocation-Read-Token" = $readToken } `
  -OutFile $outputPath

Get-Content $outputPath
```

## Reproduce in Postman

Create an environment with these variables:

- `base_url`: `http://localhost:8000`
- `access_token`: empty initially
- `function_id`: empty initially
- `version_id`: empty initially
- `invocation_id`: empty initially
- `invocation_read_token`: empty initially
- `output_id`: empty initially

### 1. Register

`POST {{base_url}}/api/auth/register/`

Body, raw JSON:

```json
{
  "username": "postman_smoke_001",
  "email": "postman_smoke_001@example.com",
  "password": "StrongerPass123!"
}
```

Tests tab:

```javascript
const body = pm.response.json();
pm.environment.set("access_token", body.access);
```

### 2. Create Function

`POST {{base_url}}/api/functions/`

Authorization:

```text
Bearer Token: {{access_token}}
```

Body, raw JSON:

```json
{
  "name": "Postman Smoke Function",
  "description": "Postman user journey smoke test.",
  "invoke_access": "private"
}
```

Tests tab:

```javascript
const body = pm.response.json();
pm.environment.set("function_id", body.id);
```

### 3. Upload Version

`POST {{base_url}}/api/functions/{{function_id}}/versions/`

Authorization:

```text
Bearer Token: {{access_token}}
```

Body: `form-data`

| Key | Type | Value |
| --- | --- | --- |
| `version` | Text | `v1` |
| `runtime` | Text | `python3.13` |
| `handler` | Text | `handler.main` |
| `config` | Text | `{"memory_mb":128,"timeout_seconds":10}` |
| `declared_output_files` | Text | `["report.txt"]` |
| `invocation_output_max_files` | Text | `1` |
| `invocation_output_max_file_size_mb` | Text | `1` |
| `invocation_output_max_total_size_mb` | Text | `1` |
| `source_bundle` | File | select `function.zip` |

Tests tab:

```javascript
const body = pm.response.json();
pm.environment.set("version_id", body.id);
```

### 4. Queue Build

`POST {{base_url}}/api/versions/{{version_id}}/build/`

Authorization:

```text
Bearer Token: {{access_token}}
```

Expected status: `202 Accepted`.

### 5. Poll Version

`GET {{base_url}}/api/versions/{{version_id}}/`

Authorization:

```text
Bearer Token: {{access_token}}
```

Repeat until:

```json
{
  "build_status": "built"
}
```

### 6. Invoke

`POST {{base_url}}/api/functions/{{function_id}}/invoke/`

Authorization:

```text
Bearer Token: {{access_token}}
```

Body, raw JSON:

```json
{
  "version": "v1",
  "event": {
    "name": "Ilya",
    "numbers": [1, 2, 3]
  }
}
```

Tests tab:

```javascript
const body = pm.response.json();
pm.environment.set("invocation_id", body.id);
pm.environment.set("invocation_read_token", body.read_token);
```

### 7. Poll Invocation

`GET {{base_url}}/api/invocations/{{invocation_id}}/`

Authorization:

```text
Bearer Token: {{access_token}}
```

Repeat until:

```json
{
  "status": "succeeded"
}
```

### 8. List Outputs

`GET {{base_url}}/api/invocations/{{invocation_id}}/outputs/`

Headers:

```text
X-Invocation-Read-Token: {{invocation_read_token}}
```

Tests tab:

```javascript
const body = pm.response.json();
pm.environment.set("output_id", body[0].id);
```

### 9. Download Output

`GET {{base_url}}/api/invocations/{{invocation_id}}/outputs/{{output_id}}/download/`

Headers:

```text
X-Invocation-Read-Token: {{invocation_read_token}}
```

Expected body:

```text
Processed Ilya with total=6
```

The `result` field should include:

```json
{
  "message": "Hello, Ilya!",
  "echo": {
    "name": "Ilya",
    "numbers": [1, 2, 3]
  },
  "sum": 6
}
```

## What This Shows About The Current Platform

Current strengths:

- Users can authenticate with JWT.
- Users can create functions without sending `owner_id`.
- Users can upload a version as a zip bundle.
- Builds are asynchronous.
- Scheduler assigns jobs to workers.
- Workers claim jobs before execution.
- Invocations are asynchronous.
- Users can poll status and read JSON results.
- Function versions can declare output filenames.
- Workers upload matching files from `/sandbox/output`.
- Invocation callers can read their own result and output files with an
  invocation read token.

Current gaps:

- There is no synchronous `wait=true` invocation mode yet.
- There is no UI yet.
