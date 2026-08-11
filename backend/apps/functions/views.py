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
from apps.invocations.models import InvocationAuthType
from apps.invocations.serializers import InvocationSerializer
from apps.invocations.services import (
    enqueue_invocation,
    store_invocation_files,
    validate_invocation_files,
)
from apps.invocations.sync import (
    SyncInvocationResponseTooLarge,
    wait_for_sync_invocation,
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
    FunctionInvokeTokenCreateSerializer,
    FunctionInvokeTokenRotateSerializer,
    FunctionInvokeTokenSerializer,
    FunctionInvokeTokenUpdateSerializer,
    FunctionSerializer,
    FunctionSourceReplacementSerializer,
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
    next_replacement_version_name,
    release_build_lease,
    schedule_function_images_for_deletion,
    select_active_version,
    sync_version_from_attempt,
)
from apps.invocations.models import InvocationInputFile
from apps.invocations.serializers import InvocationInputFileSerializer
from apps.invocations.management.commands.cleanup_expired_invocations import (
    _delete_invocation_artifact_files,
)


class QueueUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Job queue is unavailable."
    default_code = "queue_unavailable"


class SyncInvocationResponseTooLargeError(APIException):
    status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    default_detail = "Synchronous invocation response is too large."
    default_code = "sync_invocation_response_too_large"


class BuildLimitExceeded(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = "Build limit exceeded."
    default_code = "build_limit_exceeded"


class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.select_related("owner", "active_version").prefetch_related("versions")
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = Function.objects.select_related("owner", "active_version").prefetch_related("versions")
        if self.action in {"invoke", "invoke_sync"}:
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
        if self.action in {"invoke", "invoke_sync"}:
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        function = (
            Function.objects.select_related("owner", "active_version")
            .prefetch_related("versions")
            .get(pk=serializer.instance.pk)
        )
        return Response(
            FunctionSerializer(function).data,
            status=status.HTTP_201_CREATED,
        )

    def perform_destroy(self, instance):
        with transaction.atomic():
            function = (
                Function.objects.select_for_update()
                .prefetch_related("versions")
                .get(pk=instance.pk)
            )
            schedule_function_images_for_deletion(
                function,
                reason="function deleted",
            )
            for invocation in (
                Invocation.objects.select_for_update()
                .filter(function_version__function=function)
                .prefetch_related(
                    "input_files",
                    "output_files",
                    "log_artifacts",
                    "staged_completions__output_files",
                    "staged_completions__log_artifacts",
                )
            ):
                _delete_invocation_artifact_files(invocation)
            for version in function.versions.all():
                if version.source_bundle:
                    version.source_bundle.delete(save=False)
            function.delete()

    @action(detail=True, methods=["get"], url_path="invocations")
    def invocations(self, request, pk=None):
        function = self.get_object()
        queryset = (
            Invocation.objects.filter(function_version__function=function)
            .select_related("function_version", "function_version__function")
            .prefetch_related("input_files", "output_files", "log_artifacts")
        )
        status_filter = request.query_params.get("status")
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        try:
            limit = int(request.query_params.get("limit", "50"))
        except ValueError:
            limit = 50
        limit = max(1, min(limit, 100))
        queryset = queryset.order_by("-queued_at", "-id")[:limit]
        return Response(InvocationSerializer(queryset, many=True).data)

    @action(detail=True, methods=["get"], url_path="build-status")
    def build_status(self, request, pk=None):
        function = self.get_object()
        active_version = select_active_version(function)
        pending_version = (
            function.versions.filter(
                build_status__in=[
                    BuildStatus.QUEUED,
                    BuildStatus.BUILDING,
                    BuildStatus.CANCELLING,
                ]
            )
            .order_by("-created_at", "-id")
            .first()
        )
        latest_version = function.versions.order_by("-created_at", "-id").first()
        status_version = pending_version or active_version or latest_version
        latest_attempt = (
            status_version.build_attempts.order_by("-created_at", "-id").first()
            if status_version is not None
            else None
        )
        state = status_version.build_status if status_version is not None else "not_built"
        active_states = {
            BuildStatus.QUEUED,
            BuildStatus.BUILDING,
            BuildStatus.CANCELLING,
        }
        can_invoke = (
            active_version is not None
            and active_version.build_status == BuildStatus.BUILT
            and bool(active_version.image_ref)
        )
        return Response(
            {
                "resource": "build",
                "function_id": function.id,
                "state": state,
                "frontend_state": state,
                "is_terminal": state not in active_states,
                "poll_after_seconds": 1 if state in active_states else None,
                "can_cancel": state in active_states,
                "can_invoke": can_invoke,
                "links": {
                    "function": f"/api/functions/{function.id}/",
                    "build_status": f"/api/functions/{function.id}/build-status/",
                    "invoke": f"/api/functions/{function.id}/invoke/",
                    "invocations": f"/api/functions/{function.id}/invocations/",
                },
                "active_version": (
                    FunctionVersionSerializer(active_version).data
                    if active_version is not None
                    else None
                ),
                "pending_version": (
                    FunctionVersionSerializer(pending_version).data
                    if pending_version is not None
                    else None
                ),
                "latest_version": (
                    FunctionVersionSerializer(latest_version).data
                    if latest_version is not None
                    else None
                ),
                "latest_attempt": (
                    BuildAttemptSerializer(latest_attempt).data
                    if latest_attempt is not None
                    else None
                ),
            }
        )

    @action(detail=True, methods=["get", "post"], url_path="tokens")
    def tokens(self, request, pk=None):
        function = self.get_object()
        if request.method.lower() == "get":
            tokens = function.invoke_tokens.select_related("created_by").all()
            return Response(FunctionInvokeTokenSerializer(tokens, many=True).data)

        serializer = FunctionInvokeTokenCreateSerializer(
            data=request.data,
            context={"function": function},
        )
        serializer.is_valid(raise_exception=True)
        token, raw_token = FunctionInvokeToken.create_token(
            function=function,
            name=serializer.validated_data["name"],
            created_by=request.user,
            expires_at=serializer.validated_data.get("expires_at"),
        )
        return Response(
            {
                "token": FunctionInvokeTokenSerializer(token).data,
                "raw_token": raw_token,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["get", "patch", "delete"],
        url_path=r"tokens/(?P<token_id>[^/.]+)",
    )
    def token_detail(self, request, pk=None, token_id=None):
        function = self.get_object()
        token = get_object_or_404(function.invoke_tokens, pk=token_id)

        if request.method.lower() == "get":
            return Response(FunctionInvokeTokenSerializer(token).data)

        if request.method.lower() == "delete":
            token.revoke()
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = FunctionInvokeTokenUpdateSerializer(
            data=request.data,
            partial=True,
            context={"function": function, "token": token},
        )
        serializer.is_valid(raise_exception=True)
        values = serializer.validated_data
        if "name" in values:
            token.name = values["name"]
        if "expires_at" in values:
            token.expires_at = values["expires_at"]
        if "is_active" in values:
            token.is_active = values["is_active"]
            token.revoked_at = None if values["is_active"] else timezone.now()
        token.save(
            update_fields=[
                "name",
                "expires_at",
                "is_active",
                "revoked_at",
                "updated_at",
            ]
        )
        return Response(FunctionInvokeTokenSerializer(token).data)

    @action(detail=True, methods=["post"], url_path=r"tokens/(?P<token_id>[^/.]+)/revoke")
    def revoke_token(self, request, pk=None, token_id=None):
        function = self.get_object()
        token = get_object_or_404(function.invoke_tokens, pk=token_id)
        token.revoke()
        return Response(FunctionInvokeTokenSerializer(token).data)

    @action(detail=True, methods=["post"], url_path=r"tokens/(?P<token_id>[^/.]+)/rotate")
    def rotate_token(self, request, pk=None, token_id=None):
        function = self.get_object()
        token = get_object_or_404(function.invoke_tokens, pk=token_id)
        serializer = FunctionInvokeTokenRotateSerializer(
            data=request.data,
            context={"function": function, "token": token},
        )
        serializer.is_valid(raise_exception=True)
        raw_token = token.rotate(expires_at=serializer.validated_data.get("expires_at"))
        return Response(
            {
                "token": FunctionInvokeTokenSerializer(token).data,
                "raw_token": raw_token,
            }
        )

    @action(detail=True, methods=["post"], url_path="source")
    def replace_source(self, request, pk=None):
        function = self.get_object()
        active_version = select_active_version(function)
        serializer = FunctionSourceReplacementSerializer(
            data=request.data,
            context={"active_version": active_version},
        )
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                function = (
                    Function.objects.select_for_update()
                    .get(pk=function.pk)
                )
                active_build_exists = function.versions.filter(
                    build_status__in=[
                        BuildStatus.QUEUED,
                        BuildStatus.BUILDING,
                        BuildStatus.CANCELLING,
                    ]
                ).exists()
                if active_build_exists:
                    raise ValidationError(
                        {"build": "This function already has a build in progress."}
                    )

                values = dict(serializer.validated_data)
                version = FunctionVersion.objects.create(
                    function=function,
                    version=next_replacement_version_name(function),
                    runtime=values["runtime"],
                    handler=values["handler"],
                    source_bundle=values["source_bundle"],
                    config=values["config"],
                    invocation_input_mime_types=values["invocation_input_mime_types"],
                    invocation_input_max_files=values["invocation_input_max_files"],
                    invocation_input_max_size_mb=values["invocation_input_max_size_mb"],
                    invocation_input_max_total_size_mb=values[
                        "invocation_input_max_total_size_mb"
                    ],
                    declared_output_files=values["declared_output_files"],
                    invocation_output_max_files=values["invocation_output_max_files"],
                    invocation_output_max_file_size_mb=values[
                        "invocation_output_max_file_size_mb"
                    ],
                    invocation_output_max_total_size_mb=values[
                        "invocation_output_max_total_size_mb"
                    ],
                )

                policy = get_locked_build_policy()
                try:
                    enforce_build_submission_limits(version=version, policy=policy)
                except BuildAdmissionError as exc:
                    response = {"detail": str(exc)}
                    if exc.retry_after_seconds is not None:
                        response["retry_after_seconds"] = exc.retry_after_seconds
                    raise BuildLimitExceeded(response) from exc

                attempt = create_build_attempt(version)
                enqueue_build_attempt(attempt)
        except BuildLimitExceeded:
            raise
        except ValidationError:
            raise
        except Exception as exc:
            raise QueueUnavailable(str(exc)) from exc

        return Response(
            {
                "resource": "source_replacement",
                "state": version.build_status,
                "frontend_state": version.build_status,
                "is_terminal": False,
                "poll_after_seconds": 1,
                "can_cancel": True,
                "can_invoke": bool(function.active_version_id),
                "links": {
                    "function": f"/api/functions/{function.id}/",
                    "build_status": f"/api/functions/{function.id}/build-status/",
                    "invoke": f"/api/functions/{function.id}/invoke/",
                    "invocations": f"/api/functions/{function.id}/invocations/",
                    "cancel_build": f"/api/versions/{version.id}/cancel-build/",
                },
                "candidate_version": FunctionVersionSerializer(version).data,
                "build_attempt": BuildAttemptSerializer(attempt).data,
                "active_version": (
                    FunctionVersionSerializer(function.active_version).data
                    if function.active_version_id
                    else None
                ),
            },
            status=status.HTTP_202_ACCEPTED,
        )

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
        invocation, read_token, _version = self._create_invocation_from_request(
            request,
            self.get_object(),
        )
        output = dict(InvocationSerializer(invocation).data)
        output["read_token"] = read_token
        return Response(output, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=["post"], url_path="invoke-sync")
    def invoke_sync(self, request, pk=None):
        invocation, read_token, _version = self._create_invocation_from_request(
            request,
            self.get_object(),
            synchronous=True,
        )
        try:
            wait_result = wait_for_sync_invocation(invocation)
        except SyncInvocationResponseTooLarge as exc:
            raise SyncInvocationResponseTooLargeError(str(exc)) from exc

        output = dict(wait_result.data)
        output["read_token"] = read_token
        if wait_result.completed:
            return Response(output, status=status.HTTP_200_OK)
        output["detail"] = "Invocation is still running. Continue polling."
        output["poll_after_seconds"] = output.get("poll_after_seconds") or 1
        return Response(output, status=status.HTTP_202_ACCEPTED)

    def _create_invocation_from_request(self, request, function, *, synchronous=False):
        invocation_auth = self._authorize_invocation(request, function)
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
        if synchronous:
            self._validate_sync_invocation_eligibility(version, uploaded_files)
        try:
            validate_invocation_files(version, uploaded_files)
        except ValueError as exc:
            raise ValidationError({"files": str(exc)}) from exc

        try:
            with transaction.atomic():
                invocation = Invocation.objects.create(
                    function_version=version,
                    event=serializer.validated_data.get("event", {}),
                    invocation_auth_type=invocation_auth["type"],
                    invocation_token=invocation_auth.get("token"),
                )
                read_token = invocation.issue_read_token()
                if uploaded_files:
                    store_invocation_files(invocation, uploaded_files)
                enqueue_invocation(invocation)
        except Exception as exc:
            raise QueueUnavailable(str(exc)) from exc

        return invocation, read_token, version

    def _validate_sync_invocation_eligibility(self, version, uploaded_files):
        if version.declared_output_files:
            raise ValidationError(
                {
                    "detail": (
                        "Synchronous invocation is only available for functions "
                        "without declared output files."
                    )
                }
            )
        if uploaded_files:
            raise ValidationError(
                {
                    "detail": (
                        "Synchronous invocation does not accept input files. "
                        "Use async invocation for file inputs."
                    )
                }
            )

    def _authorize_invocation(self, request, function):
        if function.invoke_access == InvokeAccess.PUBLIC:
            return {"type": InvocationAuthType.PUBLIC}

        user = request.user
        is_owner_or_admin = (
            user.is_authenticated
            and (function.owner_id == user.id or is_platform_admin(user))
        )
        if is_owner_or_admin:
            return {"type": InvocationAuthType.OWNER_JWT}

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
            .only(
                "id",
                "token_hash",
                "is_active",
                "expires_at",
                "revoked_at",
                "last_used_at",
            )
            .first()
        )
        if token is None or not constant_time_compare(token.token_hash, token_hash):
            raise PermissionDenied("Invalid invocation token.")
        if not token.is_usable():
            raise PermissionDenied("Invalid invocation token.")

        token.last_used_at = timezone.now()
        token.save(update_fields=["last_used_at", "updated_at"])
        return {"type": InvocationAuthType.FUNCTION_TOKEN, "token": token}

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

        version = select_active_version(function)
        if version is None:
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
    if not settings.V1_COORDINATION_ENDPOINTS_ENABLED:
        return Response(
            {"detail": "V1 build reporting has been retired."},
            status=status.HTTP_410_GONE,
        )

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
