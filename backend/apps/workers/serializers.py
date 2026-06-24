from rest_framework import serializers

from .models import WorkerNode


class WorkerNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerNode
        fields = "__all__"
