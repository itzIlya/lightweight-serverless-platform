from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.health.views import health_check
from apps.functions.views import (
    BuildAttemptViewSet,
    FunctionVersionViewSet,
    FunctionViewSet,
    acquire_build_lease_view,
    download_build_source,
    download_invocation_input,
    get_build_state,
    list_invocation_inputs,
    release_build_lease_view,
    report_build,
)
from apps.invocations.views import InvocationViewSet, report_invocation
from apps.jobs.views import (
    claim_worker_job,
    dispatch_scheduler_job,
    expire_stale_scheduler_workers,
    get_scheduler_job,
    list_scheduler_workers,
    requeue_scheduler_job,
)
from apps.workers.views import WorkerNodeViewSet, heartbeat_worker, register_worker


router = DefaultRouter()
router.register(r"functions", FunctionViewSet, basename="function")
router.register(r"versions", FunctionVersionViewSet, basename="function-version")
router.register(r"build-attempts", BuildAttemptViewSet, basename="build-attempt")
router.register(r"invocations", InvocationViewSet, basename="invocation")
router.register(r"workers", WorkerNodeViewSet, basename="worker")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),
    path(
        "api/internal/builds/<uuid:build_request_id>/source/",
        download_build_source,
        name="download-build-source",
    ),
    path(
        "api/internal/builds/<uuid:build_request_id>/state/",
        get_build_state,
        name="get-build-state",
    ),
    path(
        "api/internal/builds/<uuid:build_request_id>/lease/acquire/",
        acquire_build_lease_view,
        name="acquire-build-lease",
    ),
    path(
        "api/internal/builds/<uuid:build_request_id>/lease/release/",
        release_build_lease_view,
        name="release-build-lease",
    ),
    path(
        "api/internal/builds/<uuid:build_request_id>/report/",
        report_build,
        name="report-build",
    ),
    path(
        "api/internal/scheduler/jobs/<uuid:job_id>/",
        get_scheduler_job,
        name="get-scheduler-job",
    ),
    path(
        "api/internal/scheduler/jobs/<uuid:job_id>/dispatch/",
        dispatch_scheduler_job,
        name="dispatch-scheduler-job",
    ),
    path(
        "api/internal/scheduler/jobs/<uuid:job_id>/requeue/",
        requeue_scheduler_job,
        name="requeue-scheduler-job",
    ),
    path(
        "api/internal/jobs/<uuid:job_id>/claim/",
        claim_worker_job,
        name="claim-worker-job",
    ),
    path(
        "api/internal/scheduler/workers/",
        list_scheduler_workers,
        name="list-scheduler-workers",
    ),
    path(
        "api/internal/scheduler/workers/expire-stale/",
        expire_stale_scheduler_workers,
        name="expire-stale-scheduler-workers",
    ),
    path(
        "api/internal/workers/register/",
        register_worker,
        name="register-worker",
    ),
    path(
        "api/internal/workers/heartbeat/",
        heartbeat_worker,
        name="heartbeat-worker",
    ),
    path(
        "api/internal/invocations/<uuid:request_id>/inputs/",
        list_invocation_inputs,
        name="list-invocation-inputs",
    ),
    path(
        "api/internal/invocations/<uuid:request_id>/inputs/<int:file_id>/download/",
        download_invocation_input,
        name="download-invocation-input",
    ),
    path(
        "api/internal/invocations/<uuid:request_id>/report/",
        report_invocation,
        name="report-invocation",
    ),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/", include(router.urls)),
]
