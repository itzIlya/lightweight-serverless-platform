from rest_framework import serializers

from .models import (
    Invocation,
    InvocationInputFile,
    InvocationOutputFile,
    StagedCompletionStatus,
    InvocationStatus,
)


class InvocationSerializer(serializers.ModelSerializer):
    input_files = serializers.SerializerMethodField()
    output_files = serializers.SerializerMethodField()

    class Meta:
        model = Invocation
        exclude = ["read_token_hash", "read_token_prefix"]

    def get_input_files(self, obj):
        return InvocationInputFileSerializer(obj.input_files.all(), many=True).data

    def get_output_files(self, obj):
        if obj.status not in {
            InvocationStatus.SUCCEEDED,
            InvocationStatus.FAILED,
            InvocationStatus.TIMEOUT,
            InvocationStatus.CANCELLED,
        }:
            return []
        return InvocationOutputFileSerializer(
            obj.output_files.filter(status=StagedCompletionStatus.COMMITTED),
            many=True,
        ).data


class InvocationInputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvocationInputFile
        fields = [
            "id",
            "position",
            "field_name",
            "original_name",
            "content_type",
            "size_bytes",
            "created_at",
        ]


class InvocationOutputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvocationOutputFile
        fields = [
            "id",
            "original_path",
            "safe_name",
            "content_type",
            "size_bytes",
            "checksum_sha256",
            "position",
            "created_at",
        ]


class InvocationReportSerializer(serializers.Serializer):
    job_id = serializers.UUIDField(required=False)
    dispatch_attempt = serializers.IntegerField(required=False, min_value=1)
    worker_name = serializers.CharField(required=False, allow_blank=True)
    status = serializers.ChoiceField(choices=InvocationStatus.choices)
    result = serializers.JSONField(required=False, default=dict)
    stdout = serializers.CharField(required=False, allow_blank=True, default="")
    stderr = serializers.CharField(required=False, allow_blank=True, default="")
    exit_code = serializers.IntegerField(required=False, allow_null=True)
    cold_start = serializers.BooleanField(required=False)
    error_message = serializers.CharField(required=False, allow_blank=True, default="")
    started_at = serializers.DateTimeField(required=False, allow_null=True)
    finished_at = serializers.DateTimeField(required=False, allow_null=True)
    duration_ms = serializers.IntegerField(required=False, allow_null=True)
