from __future__ import annotations

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def _schema_url(request) -> str:
    return request.build_absolute_uri(reverse("openapi-schema"))


@api_view(["GET"])
@permission_classes([AllowAny])
def openapi_schema(request):
    return JsonResponse(_serverless_backend_schema(request))


@api_view(["GET"])
@permission_classes([AllowAny])
def swagger_docs(request):
    schema_url = _schema_url(request)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Serverless Platform API Docs</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
  <style>
    body {{ margin: 0; background: #f8fafc; }}
    .offline-note {{
      padding: 12px 16px;
      font-family: system-ui, sans-serif;
      background: #fff7ed;
      border-bottom: 1px solid #fed7aa;
      color: #7c2d12;
    }}
  </style>
</head>
<body>
  <div class="offline-note">
    Machine-readable schema: <a href="{schema_url}">{schema_url}</a>.
    Swagger UI assets load from a CDN, so the JSON schema remains usable if the
    internet is unavailable.
  </div>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.ui = SwaggerUIBundle({{
      url: "{schema_url}",
      dom_id: "#swagger-ui",
      deepLinking: true,
      presets: [SwaggerUIBundle.presets.apis],
      layout: "BaseLayout"
    }});
  </script>
</body>
</html>"""
    return HttpResponse(html)


def _serverless_backend_schema(request) -> dict:
    server_url = request.build_absolute_uri("/").rstrip("/")
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "Serverless Platform Backend API",
            "version": "0.1.0",
            "description": (
                "Frontend-facing API for function management, builds, "
                "invocations, result reads, output downloads, and worker/admin "
                "inspection. Authentication is normally issued by the separate "
                "userservice."
            ),
        },
        "servers": [{"url": server_url}],
        "tags": [
            {"name": "Functions"},
            {"name": "Builds"},
            {"name": "Invocations"},
            {"name": "Invocation Tokens"},
            {"name": "Workers"},
            {"name": "Compatibility Auth"},
        ],
        "paths": {
            "/health/": {
                "get": {
                    "tags": ["Functions"],
                    "summary": "Health check",
                    "security": [],
                    "responses": {"200": {"description": "Service is healthy"}},
                }
            },
            "/api/functions/": {
                "get": {
                    "tags": ["Functions"],
                    "summary": "List functions owned by the current user",
                    "responses": _json_response("200", "Function list", "FunctionList"),
                },
                "post": {
                    "tags": ["Functions"],
                    "summary": "Create a function shell",
                    "requestBody": _json_body("FunctionCreate"),
                    "responses": _json_response("201", "Created function", "Function"),
                },
            },
            "/api/functions/{function_id}/": {
                "get": {
                    "tags": ["Functions"],
                    "summary": "Get a function summary",
                    "parameters": [_path_int("function_id")],
                    "responses": _json_response("200", "Function", "Function"),
                },
                "patch": {
                    "tags": ["Functions"],
                    "summary": "Update function metadata",
                    "parameters": [_path_int("function_id")],
                    "requestBody": _json_body("FunctionCreate"),
                    "responses": _json_response("200", "Updated function", "Function"),
                },
                "delete": {
                    "tags": ["Functions"],
                    "summary": "Delete a function, artifacts, and scheduled images",
                    "parameters": [_path_int("function_id")],
                    "responses": {"204": {"description": "Deleted"}},
                },
            },
            "/api/functions/{function_id}/source/": {
                "get": {
                    "tags": ["Builds"],
                    "summary": "Read the current browser-editable source",
                    "description": (
                        "Returns the active version's handler.py and requirements.txt "
                        "for the function editor. If no active version exists, the "
                        "latest stored version is used. Large or non-UTF-8 editor "
                        "files return 400; full source bundles remain stored separately."
                    ),
                    "parameters": [_path_int("function_id")],
                    "responses": _json_response("200", "Editable source", "FunctionSourceRead"),
                },
                "post": {
                    "tags": ["Builds"],
                    "summary": "Upload replacement source and queue a build",
                    "parameters": [_path_int("function_id")],
                    "requestBody": _multipart_body(
                        {
                            "source_bundle": {"type": "string", "format": "binary"},
                            "runtime": {"type": "string", "example": "python3.13"},
                            "handler": {"type": "string", "example": "handler.main"},
                            "config": {"type": "string", "example": "{\"memory_mb\":128}"},
                            "declared_output_files": {
                                "type": "string",
                                "example": "[\"report.txt\"]",
                            },
                            "invocation_input_mime_types": {
                                "type": "string",
                                "example": "[\"image/png\",\"application/pdf\"]",
                            },
                            "invocation_input_max_files": {"type": "integer", "example": 1},
                            "invocation_input_max_size_mb": {"type": "integer", "example": 10},
                            "invocation_input_max_total_size_mb": {"type": "integer", "example": 10},
                            "invocation_output_max_files": {"type": "integer", "example": 5},
                            "invocation_output_max_file_size_mb": {"type": "integer", "example": 10},
                            "invocation_output_max_total_size_mb": {"type": "integer", "example": 10},
                        },
                        required=["source_bundle"],
                    ),
                    "responses": _json_response("202", "Build queued", "SourceReplacementResponse"),
                }
            },
            "/api/functions/{function_id}/build-status/": {
                "get": {
                    "tags": ["Builds"],
                    "summary": "Read frontend-friendly build state",
                    "parameters": [_path_int("function_id")],
                    "responses": _json_response("200", "Build status", "BuildStatusResponse"),
                }
            },
            "/api/functions/{function_id}/invocations/": {
                "get": {
                    "tags": ["Invocations"],
                    "summary": "List invocation history for one function",
                    "parameters": [
                        _path_int("function_id"),
                        _query_string("status"),
                        _query_int("limit", default=50),
                    ],
                    "responses": _json_response("200", "Invocation list", "InvocationList"),
                }
            },
            "/api/functions/{function_id}/invoke/": {
                "post": {
                    "tags": ["Invocations"],
                    "summary": "Invoke a function",
                    "description": (
                        "Private functions require owner/admin JWT. Token functions "
                        "accept X-Function-Token. Public functions accept no auth. "
                        "The response includes a one-invocation read_token. "
                        "response_mode defaults to simple; use advanced for the full "
                        "dashboard/status payload."
                    ),
                    "parameters": [
                        _path_int("function_id"),
                        _response_mode_query(),
                        {
                            "name": "X-Function-Token",
                            "in": "header",
                            "required": False,
                            "schema": {"type": "string"},
                        },
                    ],
                    "requestBody": {
                        "required": False,
                        "content": {
                            "application/json": {"schema": {"$ref": "#/components/schemas/InvokeRequest"}},
                            "multipart/form-data": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "event": {"type": "string", "example": "{\"name\":\"Ilya\"}"},
                                        "files": {
                                            "type": "array",
                                            "items": {"type": "string", "format": "binary"},
                                        },
                                    },
                                }
                            },
                        },
                    },
                    "responses": _json_response("202", "Invocation queued", "InvokeResponse"),
                }
            },
            "/api/functions/{function_id}/invoke-sync/": {
                "post": {
                    "tags": ["Invocations"],
                    "summary": "Synchronously invoke a function",
                    "description": (
                        "Runs through the V2 invocation path and waits briefly for a "
                        "terminal result. Only functions without declared output files "
                        "and requests without input files are eligible. If execution is "
                        "still running when the sync wait expires, the API returns 202 "
                        "with polling links. response_mode defaults to simple."
                    ),
                    "parameters": [
                        _path_int("function_id"),
                        _response_mode_query(),
                        {
                            "name": "X-Function-Token",
                            "in": "header",
                            "required": False,
                            "schema": {"type": "string"},
                        },
                    ],
                    "requestBody": _json_body("InvokeRequest"),
                    "responses": {
                        **_json_response("200", "Invocation completed", "InvokeResponse"),
                        **_json_response("202", "Invocation still running", "InvokeResponse"),
                        "400": {
                            "description": "Sync invocation is not eligible for this request"
                        },
                        "413": {
                            "description": "Sync response exceeded configured response limits"
                        },
                    },
                }
            },
            "/api/functions/{function_id}/tokens/": {
                "get": {
                    "tags": ["Invocation Tokens"],
                    "summary": "List function invocation tokens",
                    "parameters": [_path_int("function_id")],
                    "responses": _json_response("200", "Token list", "FunctionInvokeTokenList"),
                },
                "post": {
                    "tags": ["Invocation Tokens"],
                    "summary": "Create a function invocation token",
                    "parameters": [_path_int("function_id")],
                    "requestBody": _json_body("FunctionInvokeTokenCreate"),
                    "responses": _json_response("201", "Created token; raw token shown once", "FunctionInvokeTokenSecret"),
                },
            },
            "/api/functions/{function_id}/tokens/{token_id}/": {
                "get": {
                    "tags": ["Invocation Tokens"],
                    "summary": "Get invocation token metadata",
                    "parameters": [_path_int("function_id"), _path_int("token_id")],
                    "responses": _json_response("200", "Token", "FunctionInvokeToken"),
                },
                "patch": {
                    "tags": ["Invocation Tokens"],
                    "summary": "Update invocation token metadata",
                    "parameters": [_path_int("function_id"), _path_int("token_id")],
                    "requestBody": _json_body("FunctionInvokeTokenUpdate"),
                    "responses": _json_response("200", "Updated token", "FunctionInvokeToken"),
                },
                "delete": {
                    "tags": ["Invocation Tokens"],
                    "summary": "Revoke an invocation token",
                    "parameters": [_path_int("function_id"), _path_int("token_id")],
                    "responses": {"204": {"description": "Revoked"}},
                },
            },
            "/api/functions/{function_id}/tokens/{token_id}/rotate/": {
                "post": {
                    "tags": ["Invocation Tokens"],
                    "summary": "Rotate an invocation token secret",
                    "parameters": [_path_int("function_id"), _path_int("token_id")],
                    "requestBody": _json_body("FunctionInvokeTokenRotate"),
                    "responses": _json_response("200", "Rotated token; raw token shown once", "FunctionInvokeTokenSecret"),
                }
            },
            "/api/versions/{version_id}/build/": {
                "post": {
                    "tags": ["Builds"],
                    "summary": "Queue a build for a function version",
                    "parameters": [_path_int("version_id")],
                    "responses": _json_response("202", "Build queued", "FunctionVersion"),
                }
            },
            "/api/versions/{version_id}/builds/": {
                "get": {
                    "tags": ["Builds"],
                    "summary": "List build attempts for a version",
                    "parameters": [_path_int("version_id")],
                    "responses": _json_response("200", "Build attempts", "BuildAttemptList"),
                }
            },
            "/api/build-attempts/{attempt_id}/cancel/": {
                "post": {
                    "tags": ["Builds"],
                    "summary": "Cancel a queued/running build attempt",
                    "parameters": [_path_int("attempt_id")],
                    "responses": _json_response("200", "Cancelled/cancelling attempt", "BuildAttempt"),
                }
            },
            "/api/invocations/": {
                "get": {
                    "tags": ["Invocations"],
                    "summary": "List invocations owned by the current user",
                    "responses": _json_response("200", "Invocation list", "InvocationList"),
                }
            },
            "/api/invocations/{invocation_id}/": {
                "get": {
                    "tags": ["Invocations"],
                    "summary": "Read invocation status/result",
                    "parameters": [
                        _path_int("invocation_id"),
                        _read_token_header(),
                        _response_mode_query(),
                    ],
                    "responses": _json_response("200", "Invocation", "InvocationReadResponse"),
                }
            },
            "/api/invocations/{invocation_id}/outputs/": {
                "get": {
                    "tags": ["Invocations"],
                    "summary": "List committed output files",
                    "parameters": [_path_int("invocation_id"), _read_token_header()],
                    "responses": _json_response("200", "Output files", "InvocationOutputFileList"),
                }
            },
            "/api/invocations/{invocation_id}/outputs/{file_id}/download/": {
                "get": {
                    "tags": ["Invocations"],
                    "summary": "Download one committed output file",
                    "parameters": [_path_int("invocation_id"), _path_int("file_id"), _read_token_header()],
                    "responses": {"200": {"description": "File download"}},
                }
            },
            "/api/invocations/{invocation_id}/download/": {
                "get": {
                    "tags": ["Invocations"],
                    "summary": "Download invocation ZIP bundle",
                    "parameters": [_path_int("invocation_id"), _read_token_header()],
                    "responses": {
                        "200": {
                            "description": "ZIP containing manifest, inputs, outputs, stdout, and stderr"
                        },
                        "409": {
                            "description": "Invocation artifacts are not ready yet",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/ArtifactsNotReady"
                                    }
                                }
                            },
                        },
                    },
                }
            },
            "/api/workers/": {
                "get": {
                    "tags": ["Workers"],
                    "summary": "List workers; admin only",
                    "responses": _json_response("200", "Workers", "WorkerList"),
                }
            },
            "/api/auth/register/": {
                "post": {
                    "tags": ["Compatibility Auth"],
                    "summary": "Legacy backend-local registration; prefer userservice",
                    "security": [],
                    "requestBody": _json_body("LegacyRegisterRequest"),
                    "responses": _json_response("201", "Legacy token pair", "LegacyTokenResponse"),
                }
            },
            "/api/auth/token/": {
                "post": {
                    "tags": ["Compatibility Auth"],
                    "summary": "Legacy backend-local login; prefer userservice",
                    "security": [],
                    "requestBody": _json_body("LegacyLoginRequest"),
                    "responses": _json_response("200", "Legacy token pair", "LegacyTokenResponse"),
                }
            },
        },
        "components": {
            "securitySchemes": {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "Userservice-issued RS256 JWT access token.",
                },
                "InvocationReadToken": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-Invocation-Read-Token",
                },
                "FunctionInvokeToken": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-Function-Token",
                },
            },
            "schemas": _schemas(),
        },
        "security": [{"BearerAuth": []}],
    }


def _schemas() -> dict:
    return {
        "FunctionCreate": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "invoke_access": {"type": "string", "enum": ["private", "token", "public"], "default": "private"},
            },
        },
        "Function": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "resource": {"type": "string", "example": "function"},
                "name": {"type": "string"},
                "slug": {"type": "string"},
                "description": {"type": "string"},
                "invoke_access": {"type": "string"},
                "active_version": {"nullable": True, "$ref": "#/components/schemas/FunctionVersion"},
                "active_image_ref": {"type": "string"},
                "build_status": {"type": "string"},
                "pending_build": {"nullable": True, "type": "object"},
                "links": {"$ref": "#/components/schemas/Links"},
            },
        },
        "FunctionList": {"type": "array", "items": {"$ref": "#/components/schemas/Function"}},
        "FunctionVersion": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "function": {"type": "integer"},
                "version": {"type": "string"},
                "runtime": {"type": "string"},
                "handler": {"type": "string"},
                "config": {"type": "object"},
                "declared_output_files": {"type": "array", "items": {"type": "string"}},
                "invocation_input_mime_types": {"type": "array", "items": {"type": "string"}},
                "invocation_input_max_files": {"type": "integer"},
                "invocation_input_max_size_mb": {"type": "integer"},
                "invocation_input_max_total_size_mb": {"type": "integer"},
                "invocation_output_max_files": {"type": "integer"},
                "invocation_output_max_file_size_mb": {"type": "integer"},
                "invocation_output_max_total_size_mb": {"type": "integer"},
                "build_status": {"type": "string", "enum": ["pending", "queued", "building", "cancelling", "built", "failed", "cancelled"]},
                "image_ref": {"type": "string"},
            },
        },
        "FunctionSourceRead": {
            "type": "object",
            "properties": {
                "version_id": {"type": "integer"},
                "version": {"type": "string"},
                "runtime": {"type": "string", "example": "python3.13"},
                "handler": {"type": "string", "example": "handler.main"},
                "config": {"type": "object", "example": {"memory_mb": 128}},
                "code": {
                    "type": "string",
                    "description": "UTF-8 text from handler.py, capped for browser editing.",
                    "example": "def main(event, context):\n    return {\"echo\": event}\n",
                },
                "requirements": {
                    "type": "string",
                    "description": "UTF-8 text from requirements.txt.",
                    "example": "requests==2.32.3\n",
                },
            },
        },
        "SourceReplacementResponse": {
            "type": "object",
            "properties": {
                "resource": {"type": "string", "example": "source_replacement"},
                "state": {"type": "string", "example": "queued"},
                "frontend_state": {"type": "string", "example": "queued"},
                "is_terminal": {"type": "boolean", "example": False},
                "poll_after_seconds": {"type": "integer", "nullable": True, "example": 1},
                "can_cancel": {"type": "boolean"},
                "can_invoke": {"type": "boolean"},
                "links": {"$ref": "#/components/schemas/Links"},
                "candidate_version": {"$ref": "#/components/schemas/FunctionVersion"},
                "build_attempt": {"$ref": "#/components/schemas/BuildAttempt"},
                "active_version": {"nullable": True, "$ref": "#/components/schemas/FunctionVersion"},
            },
        },
        "BuildStatusResponse": {
            "type": "object",
            "properties": {
                "resource": {"type": "string", "example": "build"},
                "function_id": {"type": "integer"},
                "state": {"type": "string"},
                "frontend_state": {"type": "string"},
                "is_terminal": {"type": "boolean"},
                "poll_after_seconds": {"type": "integer", "nullable": True},
                "can_cancel": {"type": "boolean"},
                "can_invoke": {"type": "boolean"},
                "links": {"$ref": "#/components/schemas/Links"},
                "active_version": {"nullable": True, "$ref": "#/components/schemas/FunctionVersion"},
                "pending_version": {"nullable": True, "$ref": "#/components/schemas/FunctionVersion"},
                "latest_attempt": {"nullable": True, "$ref": "#/components/schemas/BuildAttempt"},
            },
        },
        "BuildAttempt": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "request_id": {"type": "string", "format": "uuid"},
                "attempt_number": {"type": "integer"},
                "status": {"type": "string"},
                "image_ref": {"type": "string"},
                "log": {"type": "string"},
                "retries_remaining": {"type": "integer"},
            },
        },
        "BuildAttemptList": {"type": "array", "items": {"$ref": "#/components/schemas/BuildAttempt"}},
        "InvokeRequest": {
            "type": "object",
            "properties": {
                "event": {"type": "object", "default": {}},
                "version_id": {"type": "integer"},
                "version": {"type": "string"},
                "response_mode": {
                    "type": "string",
                    "enum": ["simple", "advanced"],
                    "default": "simple",
                    "description": "Also accepted as ?response_mode=. Query parameter is preferred.",
                },
            },
        },
        "InvokeResponse": {
            "oneOf": [
                {
                    "allOf": [
                        {"$ref": "#/components/schemas/SimpleInvocationResponse"},
                        {"$ref": "#/components/schemas/InvocationReadToken"},
                    ]
                },
                {
                    "allOf": [
                        {"$ref": "#/components/schemas/Invocation"},
                        {"$ref": "#/components/schemas/InvocationReadToken"},
                    ]
                },
            ]
        },
        "InvocationReadResponse": {
            "oneOf": [
                {"$ref": "#/components/schemas/SimpleInvocationResponse"},
                {"$ref": "#/components/schemas/Invocation"},
            ],
        },
        "InvocationReadToken": {
            "type": "object",
            "properties": {
                "read_token": {
                    "type": "string",
                    "description": "Shown once. Use as X-Invocation-Read-Token for this invocation.",
                }
            },
        },
        "SimpleInvocationResponse": {
            "type": "object",
            "description": (
                "Default response mode. Pending invocations return polling "
                "information. Terminal successes return only the function result "
                "and committed output file download paths. stdout/stderr are "
                "available only in the invocation ZIP or advanced response mode."
            ),
            "properties": {
                "id": {"type": "integer", "description": "Present while pending."},
                "request_id": {
                    "type": "string",
                    "format": "uuid",
                    "description": "Present while pending.",
                },
                "status": {
                    "type": "string",
                    "description": "Present while pending, or inside error for terminal failures.",
                    "example": "running",
                },
                "poll_after_seconds": {"type": "integer", "example": 1},
                "links": {"$ref": "#/components/schemas/Links"},
                "result": {"type": "object"},
                "output_files": {
                    "type": "array",
                    "items": {"$ref": "#/components/schemas/SimpleOutputFile"},
                },
                "error": {"type": "object"},
            },
        },
        "SimpleOutputFile": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "example": "report.txt"},
                "size_bytes": {"type": "integer", "example": 128},
                "content_type": {"type": "string", "example": "text/plain"},
                "download_url": {
                    "type": "string",
                    "example": "/api/invocations/123/outputs/456/download/",
                },
            },
        },
        "Invocation": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "resource": {"type": "string", "example": "invocation"},
                "request_id": {"type": "string", "format": "uuid"},
                "function_version": {"type": "integer"},
                "status": {"type": "string", "enum": ["queued", "running", "succeeded", "failed", "timeout", "cancelled"]},
                "frontend_state": {"type": "string"},
                "is_terminal": {"type": "boolean"},
                "poll_after_seconds": {"type": "integer", "nullable": True},
                "result_available": {"type": "boolean"},
                "outputs_available": {"type": "boolean"},
                "can_read_outputs": {"type": "boolean"},
                "can_download": {"type": "boolean"},
                "event": {"type": "object"},
                "result": {"type": "object"},
                "stdout": {"type": "string"},
                "stderr": {"type": "string"},
                "exit_code": {"type": "integer", "nullable": True},
                "cold_start": {"type": "boolean"},
                "error_message": {"type": "string"},
                "duration_ms": {"type": "integer", "nullable": True},
                "invocation_auth_type": {
                    "type": "string",
                    "enum": ["owner_jwt", "function_token", "public"],
                },
                "invocation_token": {"type": "integer", "nullable": True},
                "invocation_token_name": {"type": "string"},
                "invocation_token_prefix": {"type": "string"},
                "input_files": {"type": "array", "items": {"$ref": "#/components/schemas/InvocationInputFile"}},
                "output_files": {"type": "array", "items": {"$ref": "#/components/schemas/InvocationOutputFile"}},
                "outputs_url": {"type": "string"},
                "download_url": {"type": "string"},
                "links": {"$ref": "#/components/schemas/Links"},
                "log_delivery": {"type": "string", "example": "zip_only"},
            },
        },
        "InvocationList": {"type": "array", "items": {"$ref": "#/components/schemas/Invocation"}},
        "InvocationInputFile": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "position": {"type": "integer"},
                "original_name": {"type": "string"},
                "content_type": {"type": "string"},
                "size_bytes": {"type": "integer"},
            },
        },
        "InvocationOutputFile": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "original_path": {"type": "string"},
                "safe_name": {"type": "string"},
                "content_type": {"type": "string"},
                "size_bytes": {"type": "integer"},
                "checksum_sha256": {"type": "string"},
                "position": {"type": "integer"},
            },
        },
        "InvocationOutputFileList": {"type": "array", "items": {"$ref": "#/components/schemas/InvocationOutputFile"}},
        "ArtifactsNotReady": {
            "type": "object",
            "properties": {
                "detail": {"type": "string"},
                "frontend_state": {"type": "string", "example": "running"},
                "poll_after_seconds": {"type": "integer", "example": 1},
            },
        },
        "FunctionInvokeToken": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "prefix": {"type": "string"},
                "is_active": {"type": "boolean"},
                "expires_at": {"type": "string", "format": "date-time", "nullable": True},
                "revoked_at": {"type": "string", "format": "date-time", "nullable": True},
                "last_used_at": {"type": "string", "format": "date-time", "nullable": True},
            },
        },
        "FunctionInvokeTokenList": {"type": "array", "items": {"$ref": "#/components/schemas/FunctionInvokeToken"}},
        "FunctionInvokeTokenCreate": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"},
                "expires_at": {"type": "string", "format": "date-time", "nullable": True},
            },
        },
        "FunctionInvokeTokenUpdate": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "expires_at": {"type": "string", "format": "date-time", "nullable": True},
                "is_active": {"type": "boolean"},
            },
        },
        "FunctionInvokeTokenRotate": {
            "type": "object",
            "properties": {"expires_at": {"type": "string", "format": "date-time", "nullable": True}},
        },
        "FunctionInvokeTokenSecret": {
            "type": "object",
            "properties": {
                "token": {"$ref": "#/components/schemas/FunctionInvokeToken"},
                "raw_token": {"type": "string", "description": "Shown once only."},
            },
        },
        "WorkerList": {"type": "array", "items": {"type": "object"}},
        "LegacyRegisterRequest": {
            "type": "object",
            "required": ["username", "password"],
            "properties": {
                "username": {"type": "string"},
                "email": {"type": "string"},
                "password": {"type": "string", "format": "password"},
            },
        },
        "LegacyLoginRequest": {
            "type": "object",
            "required": ["username", "password"],
            "properties": {
                "username": {"type": "string"},
                "password": {"type": "string", "format": "password"},
            },
        },
        "LegacyTokenResponse": {
            "type": "object",
            "properties": {
                "user": {"type": "object"},
                "refresh": {"type": "string"},
                "access": {"type": "string"},
            },
        },
        "Links": {
            "type": "object",
            "additionalProperties": {"type": "string"},
        },
    }


def _json_response(status_code: str, description: str, schema_name: str) -> dict:
    return {
        status_code: {
            "description": description,
            "content": {
                "application/json": {
                    "schema": {"$ref": f"#/components/schemas/{schema_name}"}
                }
            },
        }
    }


def _json_body(schema_name: str) -> dict:
    return {
        "required": True,
        "content": {
            "application/json": {
                "schema": {"$ref": f"#/components/schemas/{schema_name}"}
            }
        },
    }


def _multipart_body(properties: dict, *, required: list[str] | None = None) -> dict:
    return {
        "required": bool(required),
        "content": {
            "multipart/form-data": {
                "schema": {
                    "type": "object",
                    "required": required or [],
                    "properties": properties,
                }
            }
        },
    }


def _path_int(name: str) -> dict:
    return {
        "name": name,
        "in": "path",
        "required": True,
        "schema": {"type": "integer"},
    }


def _query_string(name: str) -> dict:
    return {
        "name": name,
        "in": "query",
        "required": False,
        "schema": {"type": "string"},
    }


def _query_int(name: str, *, default: int) -> dict:
    return {
        "name": name,
        "in": "query",
        "required": False,
        "schema": {"type": "integer", "default": default},
    }


def _response_mode_query() -> dict:
    return {
        "name": "response_mode",
        "in": "query",
        "required": False,
        "schema": {
            "type": "string",
            "enum": ["simple", "advanced"],
            "default": "simple",
        },
        "description": "simple is the default caller response; advanced returns dashboard metadata.",
    }


def _read_token_header() -> dict:
    return {
        "name": "X-Invocation-Read-Token",
        "in": "header",
        "required": False,
        "schema": {"type": "string"},
        "description": "Required for non-owner public/token callers.",
    }
