from __future__ import annotations

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def _schema_url(request) -> str:
    return request.build_absolute_uri(reverse("userservice-openapi-schema"))


@api_view(["GET"])
@permission_classes([AllowAny])
def openapi_schema(request):
    return JsonResponse(_userservice_schema(request))


@api_view(["GET"])
@permission_classes([AllowAny])
def swagger_docs(request):
    schema_url = _schema_url(request)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Userservice API Docs</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
  <style>
    body {{ margin: 0; background: #f8fafc; }}
    .offline-note {{
      padding: 12px 16px;
      font-family: system-ui, sans-serif;
      background: #eff6ff;
      border-bottom: 1px solid #bfdbfe;
      color: #1e3a8a;
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


def _userservice_schema(request) -> dict:
    server_url = request.build_absolute_uri("/").rstrip("/")
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "Serverless Userservice API",
            "version": "0.1.0",
            "description": (
                "Primary account and authentication service. It issues RS256 JWTs "
                "that the serverless backend verifies through the JWKS/public-key "
                "endpoints."
            ),
        },
        "servers": [{"url": server_url}],
        "tags": [{"name": "Auth"}, {"name": "Keys"}],
        "paths": {
            "/health/": {
                "get": {
                    "tags": ["Auth"],
                    "summary": "Health check",
                    "security": [],
                    "responses": {"200": {"description": "Service is healthy"}},
                }
            },
            "/api/auth/register/": {
                "post": {
                    "tags": ["Auth"],
                    "summary": "Register an account and issue tokens",
                    "security": [],
                    "requestBody": _json_body("RegisterRequest"),
                    "responses": _json_response("201", "Created account", "TokenPairResponse"),
                }
            },
            "/api/auth/token/": {
                "post": {
                    "tags": ["Auth"],
                    "summary": "Login and issue tokens",
                    "security": [],
                    "requestBody": _json_body("TokenRequest"),
                    "responses": _json_response("200", "Token pair", "TokenPairResponse"),
                }
            },
            "/api/auth/token/refresh/": {
                "post": {
                    "tags": ["Auth"],
                    "summary": "Refresh an access token",
                    "security": [],
                    "requestBody": _json_body("RefreshRequest"),
                    "responses": _json_response("200", "Token pair", "RefreshResponse"),
                }
            },
            "/api/auth/me/": {
                "get": {
                    "tags": ["Auth"],
                    "summary": "Get current user profile",
                    "responses": _json_response("200", "Current user", "User"),
                }
            },
            "/api/auth/public-key/": {
                "get": {
                    "tags": ["Keys"],
                    "summary": "Get current RS256 public key",
                    "security": [],
                    "responses": _json_response("200", "Public key", "PublicKey"),
                }
            },
            "/api/auth/jwks/": {
                "get": {
                    "tags": ["Keys"],
                    "summary": "Get JWKS for JWT verification",
                    "security": [],
                    "responses": _json_response("200", "JWKS", "JWKS"),
                }
            },
        },
        "components": {
            "securitySchemes": {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            },
            "schemas": {
                "RegisterRequest": {
                    "type": "object",
                    "required": ["username", "password"],
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string", "format": "email"},
                        "password": {"type": "string", "format": "password", "minLength": 8},
                    },
                },
                "TokenRequest": {
                    "type": "object",
                    "required": ["username", "password"],
                    "properties": {
                        "username": {"type": "string"},
                        "password": {"type": "string", "format": "password"},
                    },
                },
                "RefreshRequest": {
                    "type": "object",
                    "required": ["refresh"],
                    "properties": {"refresh": {"type": "string"}},
                },
                "User": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "subject": {"type": "string", "format": "uuid"},
                        "username": {"type": "string"},
                        "email": {"type": "string", "format": "email"},
                        "role": {"type": "string", "enum": ["user", "admin"]},
                    },
                },
                "TokenPairResponse": {
                    "type": "object",
                    "properties": {
                        "user": {"$ref": "#/components/schemas/User"},
                        "access": {"type": "string"},
                        "refresh": {"type": "string"},
                    },
                },
                "RefreshResponse": {
                    "type": "object",
                    "properties": {
                        "access": {"type": "string"},
                        "refresh": {"type": "string"},
                    },
                },
                "PublicKey": {
                    "type": "object",
                    "properties": {
                        "kid": {"type": "string"},
                        "alg": {"type": "string", "example": "RS256"},
                        "public_key": {"type": "string"},
                    },
                },
                "JWKS": {
                    "type": "object",
                    "properties": {
                        "keys": {
                            "type": "array",
                            "items": {"type": "object"},
                        }
                    },
                },
            },
        },
        "security": [{"BearerAuth": []}],
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
