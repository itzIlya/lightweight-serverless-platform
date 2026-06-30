from django.conf import settings
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.accounts.permissions import IsPlatformAdmin

from .models import WorkerNode, WorkerStatus
from .serializers import WorkerNodeSerializer


class WorkerNodeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = WorkerNode.objects.all()
    serializer_class = WorkerNodeSerializer
    permission_classes = [IsPlatformAdmin]


@api_view(["POST"])
@permission_classes([])
def register_worker(request):
    token = request.headers.get("X-Internal-Token", "")
    if token != settings.WORKER_SHARED_SECRET:
        return Response(
            {"detail": "Unauthorized."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    name = request.data.get("name", "").strip()
    if not name:
        return Response(
            {"detail": "name is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    worker, _ = WorkerNode.objects.update_or_create(
        name=name,
        defaults={
            "hostname": request.data.get("hostname", name),
            "status": WorkerStatus.ONLINE,
            "max_concurrency": int(request.data.get("max_concurrency") or 1),
            "max_build_concurrency": int(
                request.data.get("max_build_concurrency") or 1
            ),
            "metadata": request.data.get("metadata", {}) or {},
            "last_seen_at": timezone.now(),
        },
    )
    return Response(WorkerNodeSerializer(worker).data)


@api_view(["PATCH"])
@permission_classes([])
def heartbeat_worker(request):
    token = request.headers.get("X-Internal-Token", "")
    if token != settings.WORKER_SHARED_SECRET:
        return Response(
            {"detail": "Unauthorized."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    name = request.data.get("name", "").strip()
    if not name:
        return Response(
            {"detail": "name is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    worker = WorkerNode.objects.filter(name=name).first()
    if worker is None:
        return Response(
            {"detail": "Worker is not registered."},
            status=status.HTTP_404_NOT_FOUND,
        )

    metadata = dict(worker.metadata or {})
    metadata.update(request.data.get("metadata", {}) or {})
    for key in ("active_jobs", "active_builds", "active_invocations"):
        if key in request.data:
            metadata[key] = int(request.data.get(key) or 0)

    worker.status = WorkerStatus.ONLINE
    worker.last_seen_at = timezone.now()
    worker.metadata = metadata
    worker.save(update_fields=["status", "last_seen_at", "metadata", "updated_at"])
    return Response(WorkerNodeSerializer(worker).data)
