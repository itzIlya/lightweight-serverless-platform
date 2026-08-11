from __future__ import annotations

from django.conf import settings
from django.http import HttpResponse


class FrontendCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        origin = request.headers.get("Origin", "")
        if request.method == "OPTIONS" and self._origin_allowed(origin):
            response = HttpResponse(status=204)
        else:
            response = self.get_response(request)

        if self._origin_allowed(origin):
            response["Access-Control-Allow-Origin"] = origin
            response["Vary"] = _append_vary(response.get("Vary", ""), "Origin")
            response["Access-Control-Allow-Methods"] = ", ".join(
                settings.CORS_ALLOWED_METHODS
            )
            response["Access-Control-Allow-Headers"] = ", ".join(
                settings.CORS_ALLOWED_HEADERS
            )
            response["Access-Control-Expose-Headers"] = ", ".join(
                settings.CORS_EXPOSE_HEADERS
            )
            response["Access-Control-Max-Age"] = str(settings.CORS_PREFLIGHT_MAX_AGE)
            if settings.CORS_ALLOW_CREDENTIALS:
                response["Access-Control-Allow-Credentials"] = "true"
        return response

    def _origin_allowed(self, origin: str) -> bool:
        if not origin:
            return False
        if settings.CORS_ALLOW_ALL_ORIGINS:
            return True
        return origin in settings.CORS_ALLOWED_ORIGINS


def _append_vary(current: str, value: str) -> str:
    values = [item.strip() for item in current.split(",") if item.strip()]
    lowered = {item.lower() for item in values}
    if value.lower() not in lowered:
        values.append(value)
    return ", ".join(values)
