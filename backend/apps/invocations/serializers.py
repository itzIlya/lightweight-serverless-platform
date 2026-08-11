from rest_framework import serializers

from .models import (
    Invocation,
    InvocationAttempt,
    InvocationAuthType,
    InvocationInputFile,
    InvocationLogArtifact,
    InvocationOutputFile,
    StagedCompletionStatus,
    InvocationStatus,
)


class InvocationSerializer(serializers.ModelSerializer):
    resource = serializers.SerializerMethodField()
    input_files = serializers.SerializerMethodField()
    output_files = serializers.SerializerMethodField()
    frontend_state = serializers.SerializerMethodField()
    is_terminal = serializers.SerializerMethodField()
    poll_after_seconds = serializers.SerializerMethodField()
    result_available = serializers.SerializerMethodField()
    outputs_available = serializers.SerializerMethodField()
    can_read_outputs = serializers.SerializerMethodField()
    can_download = serializers.SerializerMethodField()
    outputs_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()
    log_delivery = serializers.SerializerMethodField()
    attempts = serializers.SerializerMethodField()
    invocation_token_name = serializers.SerializerMethodField()
    invocation_token_prefix = serializers.SerializerMethodField()

    class Meta:
        model = Invocation
        exclude = ["read_token_hash", "read_token_prefix"]

    def get_resource(self, obj):
        return "invocation"

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

    def get_frontend_state(self, obj):
        return obj.status

    def get_is_terminal(self, obj):
        return obj.status in terminal_invocation_statuses()

    def get_poll_after_seconds(self, obj):
        return None if self.get_is_terminal(obj) else 1

    def get_result_available(self, obj):
        return self.get_is_terminal(obj)

    def get_outputs_available(self, obj):
        if not self.get_is_terminal(obj):
            return False
        return obj.output_files.filter(status=StagedCompletionStatus.COMMITTED).exists()

    def get_can_read_outputs(self, obj):
        return self.get_is_terminal(obj)

    def get_can_download(self, obj):
        return self.get_is_terminal(obj)

    def get_outputs_url(self, obj):
        return f"/api/invocations/{obj.id}/outputs/"

    def get_download_url(self, obj):
        return f"/api/invocations/{obj.id}/download/"

    def get_links(self, obj):
        return {
            "self": f"/api/invocations/{obj.id}/",
            "outputs": self.get_outputs_url(obj),
            "download": self.get_download_url(obj),
        }

    def get_log_delivery(self, obj):
        return "zip_only"

    def get_attempts(self, obj):
        return InvocationAttemptSerializer(obj.attempts.all(), many=True).data

    def get_invocation_token_name(self, obj):
        if obj.invocation_auth_type != InvocationAuthType.FUNCTION_TOKEN:
            return ""
        return obj.invocation_token.name if obj.invocation_token_id else ""

    def get_invocation_token_prefix(self, obj):
        if obj.invocation_auth_type != InvocationAuthType.FUNCTION_TOKEN:
            return ""
        return obj.invocation_token.prefix if obj.invocation_token_id else ""


class InvocationAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvocationAttempt
        fields = [
            "id",
            "attempt_number",
            "dispatch_attempt",
            "worker_name",
            "status",
            "failure_kind",
            "error_message",
            "queued_at",
            "started_at",
            "finished_at",
            "duration_ms",
        ]


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


class InvocationLogArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvocationLogArtifact
        fields = [
            "id",
            "stream",
            "safe_name",
            "content_type",
            "size_bytes",
            "preview",
            "status",
            "created_at",
        ]


def terminal_invocation_statuses():
    return {
        InvocationStatus.SUCCEEDED,
        InvocationStatus.FAILED,
        InvocationStatus.TIMEOUT,
        InvocationStatus.CANCELLED,
    }


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
