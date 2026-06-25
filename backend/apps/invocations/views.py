from django.conf import settings
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.utils.crypto import constant_time_compare
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action, api_view, parser_classes, permission_classes
from rest_framework.exceptions import NotAuthenticated, PermissionDenied, ValidationError
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.accounts.services import is_platform_admin
from apps.jobs.models import Job, JobStatus
from apps.jobs.services import mark_invocation_jobs_from_status

from .models import Invocation, InvocationOutputFile, hash_invocation_read_token
from .serializers import (
    InvocationOutputFileSerializer,
    InvocationReportSerializer,
    InvocationSerializer,
)
from .services import store_invocation_output_file


class InvocationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Invocation.objects.select_related(
        "function_version",
        "function_version__function",
    ).prefetch_related("input_files", "output_files")
    serializer_class = InvocationSerializer

    def get_permissions(self):
        if self.action in {"retrieve", "outputs", "download_output"}:
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        queryset = Invocation.objects.select_related(
            "function_version",
            "function_version__function",
        ).prefetch_related("input_files", "output_files")
        if self.action in {"retrieve", "outputs", "download_output"} and _read_token_from_request(
            self.request
        ):
            return queryset
        if is_platform_admin(self.request.user):
            return queryset
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(function_version__function__owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        invocation = self.get_object()
        _authorize_invocation_read(request, invocation)
        return Response(self.get_serializer(invocation).data)

    @action(detail=True, methods=["get"], url_path="outputs")
    def outputs(self, request, pk=None):
        invocation = self.get_object()
        _authorize_invocation_read(request, invocation)
        return Response(
            InvocationOutputFileSerializer(invocation.output_files.all(), many=True).data
        )

    @action(
        detail=True,
        methods=["get"],
        url_path=r"outputs/(?P<file_id>[^/.]+)/download",
    )
    def download_output(self, request, pk=None, file_id=None):
        invocation = self.get_object()
        _authorize_invocation_read(request, invocation)
        output_file = get_object_or_404(
            InvocationOutputFile,
            id=file_id,
            invocation=invocation,
        )
        return FileResponse(
            output_file.file.open("rb"),
            as_attachment=True,
            filename=output_file.safe_name,
        )


def _read_token_from_request(request) -> str:
    return request.headers.get("X-Invocation-Read-Token", "") or request.query_params.get(
        "read_token",
        "",
    )


def _authorize_invocation_read(request, invocation: Invocation) -> None:
    user = request.user
    if user.is_authenticated and (
        invocation.function_version.function.owner_id == user.id
        or is_platform_admin(user)
    ):
        return

    raw_token = _read_token_from_request(request)
    if not raw_token:
        raise NotAuthenticated(
            "This invocation requires the owner/admin JWT or invocation read token."
        )
    token_hash = hash_invocation_read_token(raw_token)
    if not invocation.read_token_hash or not constant_time_compare(
        invocation.read_token_hash,
        token_hash,
    ):
        raise PermissionDenied("Invalid invocation read token.")


@api_view(["PATCH"])
@permission_classes([])
def report_invocation(request, request_id):
    token = request.headers.get("X-Internal-Token", "")
    if token != settings.WORKER_SHARED_SECRET:
        return Response(
            {"detail": "Unauthorized."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    invocation = get_object_or_404(
        Invocation.objects.select_related(
            "function_version",
            "function_version__function",
        ).prefetch_related("input_files"),
        request_id=request_id,
    )

    serializer = InvocationReportSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    values = dict(serializer.validated_data)
    job_id = values.pop("job_id", None)
    dispatch_attempt = values.pop("dispatch_attempt", None)
    worker_name = values.pop("worker_name", "")
    stale_response = _reject_stale_invocation_report(
        invocation=invocation,
        job_id=job_id,
        dispatch_attempt=dispatch_attempt,
        worker_name=worker_name,
    )
    if stale_response is not None:
        return stale_response

    for field, value in values.items():
        setattr(invocation, field, value)
    invocation.save()
    mark_invocation_jobs_from_status(invocation, invocation.status)

    return Response(InvocationSerializer(invocation).data)


@api_view(["POST"])
@permission_classes([])
@parser_classes([MultiPartParser, FormParser])
def upload_invocation_output(request, request_id):
    token = request.headers.get("X-Internal-Token", "")
    if token != settings.WORKER_SHARED_SECRET:
        return Response(
            {"detail": "Unauthorized."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    invocation = get_object_or_404(
        Invocation.objects.select_related(
            "function_version",
            "function_version__function",
        ).prefetch_related("output_files"),
        request_id=request_id,
    )
    uploaded_file = request.FILES.get("file")
    if uploaded_file is None:
        raise ValidationError({"file": "This field is required."})

    try:
        position = int(request.data.get("position", 0) or 0)
    except (TypeError, ValueError) as exc:
        raise ValidationError({"position": "Must be an integer."}) from exc
    try:
        output_file = store_invocation_output_file(
            invocation=invocation,
            uploaded_file=uploaded_file,
            original_path=request.data.get("original_path", ""),
            position=position,
        )
    except ValueError as exc:
        raise ValidationError({"output": str(exc)}) from exc

    return Response(
        InvocationOutputFileSerializer(output_file).data,
        status=status.HTTP_201_CREATED,
    )


def _reject_stale_invocation_report(
    *,
    invocation,
    job_id,
    dispatch_attempt,
    worker_name,
):
    if not job_id:
        return None

    job = Job.objects.filter(job_id=job_id, invocation=invocation).first()
    if job is None:
        return Response(
            {
                "accepted": False,
                "stale": True,
                "detail": "Job report does not match this invocation.",
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
