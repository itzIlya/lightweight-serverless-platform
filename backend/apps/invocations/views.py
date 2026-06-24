from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.accounts.services import is_platform_admin
from apps.jobs.models import Job, JobStatus
from apps.jobs.services import mark_invocation_jobs_from_status

from .models import Invocation
from .serializers import InvocationReportSerializer, InvocationSerializer


class InvocationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Invocation.objects.select_related(
        "function_version",
        "function_version__function",
    ).prefetch_related("input_files")
    serializer_class = InvocationSerializer

    def get_queryset(self):
        queryset = Invocation.objects.select_related(
            "function_version",
            "function_version__function",
        ).prefetch_related("input_files")
        if is_platform_admin(self.request.user):
            return queryset
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(function_version__function__owner=self.request.user)


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
