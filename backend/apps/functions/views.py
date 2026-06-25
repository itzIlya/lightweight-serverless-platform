from django.conf import settings
from django.db import transaction
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.utils.crypto import constant_time_compare
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import APIException, NotAuthenticated, PermissionDenied, ValidationError
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.accounts.services import is_platform_admin
from apps.invocations.models import Invocation
from apps.invocations.serializers import InvocationSerializer
from apps.invocations.services import (
    enqueue_invocation,
    store_invocation_files,
    validate_invocation_files,
)
from apps.jobs.services import mark_build_jobs_from_status
from apps.jobs.models import Job, JobStatus

from .models import (
    BuildAttempt,
    BuildStatus,
    Function,
    FunctionInvokeToken,
    FunctionVersion,
    InvokeAccess,
    hash_invoke_token,
)
from .serializers import (
    BuildAttemptSerializer,
    BuildReportSerializer,
    FunctionCreateSerializer,
    FunctionInvokeSerializer,
    FunctionSerializer,
    FunctionVersionCreateSerializer,
    FunctionVersionSerializer,
)
from .services import (
    BuildAdmissionError,
    acquire_build_lease,
    create_build_attempt,
    enqueue_build_attempt,
    enforce_build_submission_limits,
    get_locked_build_policy,
    get_build_policy,
    release_build_lease,
    sync_version_from_attempt,
)
from apps.invocations.models import InvocationInputFile
from apps.invocations.serializers import InvocationInputFileSerializer


class QueueUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Job queue is unavailable."
    default_code = "queue_unavailable"


class BuildLimitExceeded(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = "Build limit exceeded."
    default_code = "build_limit_exceeded"


class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.select_related("owner").prefetch_related("versions")
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = Function.objects.select_related("owner").prefetch_related("versions")
        if self.action == "invoke":
            return queryset
        if is_platform_admin(self.request.user):
            return queryset
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return FunctionCreateSerializer
        return FunctionSerializer

    def get_permissions(self):
        if self.action == "invoke":
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["get", "post"], url_path="versions")
    def versions(self, request, pk=None):
        function = self.get_object()

        if request.method.lower() == "get":
            serializer = FunctionVersionSerializer(function.versions.all(), many=True)
            return Response(serializer.data)

        serializer = FunctionVersionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        version = serializer.save(function=function)
        output = FunctionVersionSerializer(version)
        return Response(output.data, status=201)

    @action(detail=True, methods=["post"], url_path="invoke")
    def invoke(self, request, pk=None):
        function = self.get_object()
        self._authorize_invocation(request, function)
        serializer = FunctionInvokeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        version = self._select_version(function, serializer.validated_data)
        if version.build_status != BuildStatus.BUILT or not version.image_ref:
            raise ValidationError(
                {"version": "Function version must be built before invocation."}
            )

        uploaded_files = request.FILES.getlist("files") or request.FILES.getlist(
            "input_files"
        )
        try:
            validate_invocation_files(version, uploaded_files)
        except ValueError as exc:
            raise ValidationError({"files": str(exc)}) from exc

        try:
            with transaction.atomic():
                invocation = Invocation.objects.create(
                    function_version=version,
                    event=serializer.validated_data.get("event", {}),
                )
                read_token = invocation.issue_read_token()
                if uploaded_files:
                    store_invocation_files(invocation, uploaded_files)
                enqueue_invocation(invocation)
        except Exception as exc:
            raise QueueUnavailable(str(exc)) from exc

        output = dict(InvocationSerializer(invocation).data)
        output["read_token"] = read_token
        return Response(output, status=status.HTTP_202_ACCEPTED)

    def _authorize_invocation(self, request, function):
        if function.invoke_access == InvokeAccess.PUBLIC:
            return

        user = request.user
        is_owner_or_admin = (
            user.is_authenticated
            and (function.owner_id == user.id or is_platform_admin(user))
        )
        if is_owner_or_admin:
            return

        if function.invoke_access == InvokeAccess.PRIVATE:
            raise NotAuthenticated(
                "This function requires the owner or an admin JWT to invoke."
            )

        raw_token = request.headers.get("X-Function-Token", "")
        if not raw_token:
            raise NotAuthenticated("This function requires an invocation token.")

        token_hash = hash_invoke_token(raw_token)
        token = (
            FunctionInvokeToken.objects.filter(
                function=function,
                token_hash=token_hash,
            )
            .only("id", "token_hash", "is_active", "expires_at", "last_used_at")
            .first()
        )
        if token is None or not constant_time_compare(token.token_hash, token_hash):
            raise PermissionDenied("Invalid invocation token.")
        if not token.is_usable():
            raise PermissionDenied("Invocation token is inactive or expired.")

        token.last_used_at = timezone.now()
        token.save(update_fields=["last_used_at", "updated_at"])

    def _select_version(self, function, data):
        versions = function.versions.all()
        if "version_id" in data:
            try:
                return versions.get(id=data["version_id"])
            except FunctionVersion.DoesNotExist as exc:
                raise ValidationError(
                    {"version_id": "Version does not belong to this function."}
                ) from exc

        if "version" in data:
            try:
                return versions.get(version=data["version"])
            except FunctionVersion.DoesNotExist as exc:
                raise ValidationError(
                    {"version": "Version does not belong to this function."}
                ) from exc

        version = versions.order_by("-created_at").first()
        if version is None:
            raise ValidationError("Function has no versions to invoke.")
        return version


class FunctionVersionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = FunctionVersion.objects.select_related("function", "function__owner")
    serializer_class = FunctionVersionSerializer

    def get_queryset(self):
        queryset = FunctionVersion.objects.select_related("function", "function__owner")
        if is_platform_admin(self.request.user):
            return queryset
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(function__owner=self.request.user)

    @action(detail=True, methods=["post"], url_path="build")
    def build(self, request, pk=None):
        version = self.get_object()

        try:
            with transaction.atomic():
                version = FunctionVersion.objects.select_for_update().get(
                    pk=version.pk
                )
                if version.build_status == BuildStatus.BUILT and version.image_ref:
                    return Response(FunctionVersionSerializer(version).data)

                if version.build_status in {
                    BuildStatus.QUEUED,
                    BuildStatus.BUILDING,
                    BuildStatus.CANCELLING,
                }:
                    return Response(
                        FunctionVersionSerializer(version).data,
                        status=status.HTTP_202_ACCEPTED,
                    )

                policy = get_locked_build_policy()
                try:
                    enforce_build_submission_limits(
                        version=version,
                        policy=policy,
                    )
                except BuildAdmissionError as exc:
                    response = {"detail": str(exc)}
                    if exc.retry_after_seconds is not None:
                        response["retry_after_seconds"] = exc.retry_after_seconds
                    raise BuildLimitExceeded(response) from exc

                attempt = create_build_attempt(version)
                enqueue_build_attempt(attempt)
        except BuildLimitExceeded:
            raise
        except Exception as exc:
            raise QueueUnavailable(str(exc)) from exc

        version.refresh_from_db()
        return Response(
            FunctionVersionSerializer(version).data,
            status=status.HTTP_202_ACCEPTED,
        )

    @action(detail=True, methods=["get"], url_path="builds")
    def builds(self, request, pk=None):
        version = self.get_object()
        attempts = version.build_attempts.all()
        return Response(BuildAttemptSerializer(attempts, many=True).data)

    @action(detail=True, methods=["post"], url_path="cancel-build")
    def cancel_build(self, request, pk=None):
        version = self.get_object()
        attempt = version.build_attempts.filter(
            status__in=[
                BuildStatus.QUEUED,
                BuildStatus.BUILDING,
                BuildStatus.CANCELLING,
            ]
        ).first()
        if attempt is None:
            raise ValidationError({"build": "There is no active build to cancel."})
        return cancel_attempt(attempt)


class BuildAttemptViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = BuildAttempt.objects.select_related(
        "function_version",
        "function_version__function",
    )
    serializer_class = BuildAttemptSerializer

    def get_queryset(self):
        queryset = BuildAttempt.objects.select_related(
            "function_version",
            "function_version__function",
        )
        if is_platform_admin(self.request.user):
            return queryset
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(function_version__function__owner=self.request.user)

    @action(detail=True, methods=["post"], url_path="cancel")
    def cancel(self, request, pk=None):
        return cancel_attempt(self.get_object())


def cancel_attempt(attempt):
    if attempt.status in {
        BuildStatus.BUILT,
        BuildStatus.FAILED,
        BuildStatus.CANCELLED,
    }:
        raise ValidationError(
            {"build": f"Build attempt is already {attempt.status}."}
        )

    now = timezone.now()
    attempt.cancel_requested_at = attempt.cancel_requested_at or now
    if attempt.status == BuildStatus.QUEUED:
        attempt.status = BuildStatus.CANCELLED
        attempt.finished_at = now
        attempt.log = "Build cancelled before execution."
    else:
        attempt.status = BuildStatus.CANCELLING
        attempt.log = "Cancellation requested. Waiting for the worker to stop."
    attempt.save()

    version = attempt.function_version
    if version.build_request_id == attempt.request_id:
        sync_version_from_attempt(version, attempt)

    return Response(BuildAttemptSerializer(attempt).data)


def _authorize_worker(request):
    token = request.headers.get("X-Internal-Token", "")
    if token != settings.WORKER_SHARED_SECRET:
        return Response(
            {"detail": "Unauthorized."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    return None


@api_view(["GET"])
@permission_classes([])
def download_build_source(request, build_request_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    attempt = get_object_or_404(
        BuildAttempt.objects.select_related(
            "function_version",
            "function_version__function",
        ),
        request_id=build_request_id,
    )
    version = attempt.function_version
    return FileResponse(
        version.source_bundle.open("rb"),
        as_attachment=True,
        filename=f"{version.function.slug}-{version.version}.zip",
    )


@api_view(["GET"])
@permission_classes([])
def list_invocation_inputs(request, request_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    invocation = get_object_or_404(
        Invocation.objects.select_related("function_version", "function_version__function")
        .prefetch_related("input_files"),
        request_id=request_id,
    )
    return Response(InvocationInputFileSerializer(invocation.input_files.all(), many=True).data)


@api_view(["GET"])
@permission_classes([])
def download_invocation_input(request, request_id, file_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    input_file = get_object_or_404(
        InvocationInputFile.objects.select_related("invocation"),
        id=file_id,
        invocation__request_id=request_id,
    )
    return FileResponse(
        input_file.file.open("rb"),
        as_attachment=True,
        filename=input_file.original_name,
    )


@api_view(["GET"])
@permission_classes([])
def get_build_state(request, build_request_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    attempt = get_object_or_404(BuildAttempt, request_id=build_request_id)
    return Response(BuildAttemptSerializer(attempt).data)


@api_view(["POST"])
@permission_classes([])
def acquire_build_lease_view(request, build_request_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    attempt = get_object_or_404(
        BuildAttempt.objects.select_related(
            "function_version",
            "function_version__function",
        ),
        request_id=build_request_id,
    )
    max_build_concurrency = request.data.get("max_build_concurrency")
    if max_build_concurrency in ("", None):
        max_build_concurrency = None
    else:
        max_build_concurrency = int(max_build_concurrency)

    lease, reason = acquire_build_lease(
        attempt=attempt,
        worker_name=request.data.get("worker_name", ""),
        hostname=request.data.get("hostname", ""),
        max_build_concurrency=max_build_concurrency,
    )
    if lease is None:
        return Response(
            {
                "granted": False,
                "reason": reason,
            }
        )
    return Response(
        {
            "granted": True,
            "reason": reason,
            "lease_id": lease.id,
            "worker": lease.worker.name,
            "expires_at": lease.expires_at,
        }
    )


@api_view(["POST"])
@permission_classes([])
def release_build_lease_view(request, build_request_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    attempt = get_object_or_404(BuildAttempt, request_id=build_request_id)
    lease_id = request.data.get("lease_id")
    if lease_id in ("", None):
        lease_id = None
    else:
        lease_id = int(lease_id)
    released = release_build_lease(
        attempt=attempt,
        lease_id=lease_id,
        reason=request.data.get("reason", ""),
    )
    return Response({"released": released})


@api_view(["PATCH"])
@permission_classes([])
def report_build(request, build_request_id):
    unauthorized = _authorize_worker(request)
    if unauthorized:
        return unauthorized

    serializer = BuildReportSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    retry_attempt = None
    with transaction.atomic():
        attempt = get_object_or_404(
            BuildAttempt.objects.select_for_update().select_related(
                "function_version",
                "function_version__function",
            ),
            request_id=build_request_id,
        )
        version = attempt.function_version
        values = dict(serializer.validated_data)
        job_id = values.pop("job_id", None)
        dispatch_attempt = values.pop("dispatch_attempt", None)
        worker_name = values.pop("worker_name", "")
        reported_status = values.pop("status")

        stale_response = _reject_stale_build_report(
            attempt=attempt,
            job_id=job_id,
            dispatch_attempt=dispatch_attempt,
            worker_name=worker_name,
        )
        if stale_response is not None:
            return stale_response

        if attempt.cancel_requested_at and reported_status != BuildStatus.CANCELLED:
            reported_status = BuildStatus.CANCELLED
            values["build_finished_at"] = values.get(
                "build_finished_at"
            ) or timezone.now()
            values["build_log"] = "Build cancelled by user."

        attempt.status = reported_status
        if "image_ref" in values:
            attempt.image_ref = values["image_ref"]
        if "build_log" in values:
            attempt.log = values["build_log"]
        if "build_started_at" in values:
            attempt.started_at = values["build_started_at"]
        if "build_finished_at" in values:
            attempt.finished_at = values["build_finished_at"]
        attempt.save()
        mark_build_jobs_from_status(attempt, reported_status)

        if version.build_request_id == attempt.request_id:
            sync_version_from_attempt(version, attempt)

        if reported_status in {
            BuildStatus.BUILT,
            BuildStatus.FAILED,
            BuildStatus.CANCELLED,
        }:
            release_build_lease(
                attempt=attempt,
                reason=f"Build reported {reported_status}.",
            )

        if reported_status == BuildStatus.FAILED:
            policy = get_build_policy()
            if attempt.attempt_number <= policy.max_retries:
                retry_attempt = create_build_attempt(
                    version,
                    build_id=attempt.build_id,
                    attempt_number=attempt.attempt_number + 1,
                )
                try:
                    enqueue_build_attempt(retry_attempt)
                except Exception as exc:
                    retry_attempt.status = BuildStatus.FAILED
                    retry_attempt.log = f"Could not queue retry: {exc}"
                    retry_attempt.finished_at = timezone.now()
                    retry_attempt.save()
                    sync_version_from_attempt(version, retry_attempt)

    response = {
        "attempt": BuildAttemptSerializer(attempt).data,
        "retry_scheduled": retry_attempt is not None
        and retry_attempt.status == BuildStatus.QUEUED,
    }
    if retry_attempt is not None:
        response["retry_attempt"] = BuildAttemptSerializer(retry_attempt).data
    return Response(response)


def _reject_stale_build_report(
    *,
    attempt,
    job_id,
    dispatch_attempt,
    worker_name,
):
    if not job_id:
        return None

    job = Job.objects.filter(job_id=job_id, build_attempt=attempt).first()
    if job is None:
        return Response(
            {
                "accepted": False,
                "stale": True,
                "detail": "Job report does not match this build attempt.",
            }
        )

    expected_attempt = job.payload.get("dispatch_attempt")
    expected_worker = job.payload.get("assigned_worker", "")
    if (
        job.status not in {JobStatus.DISPATCHED, JobStatus.RUNNING}
        or expected_attempt != dispatch_attempt
        or expected_worker != worker_name
    ):
        return Response(
            {
                "accepted": False,
                "stale": True,
                "job_status": job.status,
                "expected_dispatch_attempt": expected_attempt,
                "reported_dispatch_attempt": dispatch_attempt,
                "expected_worker": expected_worker,
                "reported_worker": worker_name,
            }
        )
    return None
