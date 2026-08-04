from django.contrib import admin
from django.urls import include, path

from apps.health.views import health_check
from apps.health.metrics import metrics
from .openapi import openapi_schema, swagger_docs


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),
    path("metrics/", metrics),
    path("api/schema/", openapi_schema, name="userservice-openapi-schema"),
    path("api/docs/", swagger_docs, name="userservice-swagger-docs"),
    path("api/auth/", include("apps.accounts.urls")),
]
