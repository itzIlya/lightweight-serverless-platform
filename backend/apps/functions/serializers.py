from __future__ import annotations

import json
from pathlib import PurePosixPath

from django.utils.text import slugify
from rest_framework import serializers

from .models import BuildAttempt, BuildPolicy, BuildStatus, Function, FunctionVersion
from .services import validate_function_bundle


class FlexibleJSONField(serializers.Field):
    def to_internal_value(self, data):
        if data in (None, ""):
            return {}
        if isinstance(data, (dict, list, int, float, bool)):
            return data
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError as exc:
                raise serializers.ValidationError("Config must be valid JSON.") from exc
        raise serializers.ValidationError("Config must be valid JSON.")

    def to_representation(self, value):
        return value


class FunctionVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionVersion
        fields = [
            "id",
            "function",
            "version",
            "runtime",
            "handler",
            "source_bundle",
            "config",
            "invocation_input_mime_types",
            "invocation_input_max_files",
            "invocation_input_max_size_mb",
            "invocation_input_max_total_size_mb",
            "declared_output_files",
            "invocation_output_max_files",
            "invocation_output_max_file_size_mb",
            "invocation_output_max_total_size_mb",
            "image_ref",
            "build_status",
            "build_request_id",
            "build_log",
            "build_queued_at",
            "build_started_at",
            "build_finished_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "image_ref",
            "build_status",
            "build_request_id",
            "build_log",
            "build_queued_at",
            "build_started_at",
            "build_finished_at",
            "created_at",
            "updated_at",
        ]


class BuildAttemptSerializer(serializers.ModelSerializer):
    retries_remaining = serializers.SerializerMethodField()

    class Meta:
        model = BuildAttempt
        fields = [
            "id",
            "request_id",
            "build_id",
            "function_version",
            "attempt_number",
            "status",
            "image_ref",
            "log",
            "queued_at",
            "started_at",
            "finished_at",
            "cancel_requested_at",
            "retries_remaining",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields

    def get_retries_remaining(self, obj):
        policy = BuildPolicy.objects.filter(pk=1).first()
        max_retries = policy.max_retries if policy else 2
        return max(0, max_retries - (obj.attempt_number - 1))


class FunctionVersionCreateSerializer(serializers.ModelSerializer):
    config = FlexibleJSONField(required=False, default=dict)
    invocation_input_mime_types = FlexibleJSONField(required=False, default=list)
    declared_output_files = FlexibleJSONField(required=False, default=list)

    class Meta:
        model = FunctionVersion
        fields = [
            "id",
            "version",
            "runtime",
            "handler",
            "source_bundle",
            "config",
            "invocation_input_mime_types",
            "invocation_input_max_files",
            "invocation_input_max_size_mb",
            "invocation_input_max_total_size_mb",
            "declared_output_files",
            "invocation_output_max_files",
            "invocation_output_max_file_size_mb",
            "invocation_output_max_total_size_mb",
        ]
        read_only_fields = ["id"]

    def validate_invocation_input_mime_types(self, value):
        if value in (None, ""):
            return []
        if not isinstance(value, list):
            raise serializers.ValidationError("Must be a JSON array of MIME types.")
        normalized = []
        for item in value:
            if not isinstance(item, str) or not item.strip():
                raise serializers.ValidationError(
                    "Each MIME type must be a non-empty string."
                )
            normalized.append(item.strip().lower())
        return normalized

    def validate_declared_output_files(self, value):
        if value in (None, ""):
            return []
        if not isinstance(value, list):
            raise serializers.ValidationError("Must be a JSON array of filenames.")

        normalized = []
        seen = set()
        for item in value:
            if not isinstance(item, str) or not item.strip():
                raise serializers.ValidationError(
                    "Each output file must be a non-empty string."
                )
            name = item.strip().replace("\\", "/")
            path = PurePosixPath(name)
            if (
                path.is_absolute()
                or path.name != name
                or name in {".", ".."}
                or any(part == ".." for part in path.parts)
            ):
                raise serializers.ValidationError(
                    "Output files must be simple filenames, not paths."
                )
            if name == "result.json":
                raise serializers.ValidationError(
                    "result.json is reserved for the function return value."
                )
            lowered = name.lower()
            if lowered in seen:
                raise serializers.ValidationError(
                    f"Duplicate output file declaration: {name}"
                )
            seen.add(lowered)
            normalized.append(name)
        return normalized

    def validate(self, attrs):
        attrs = super().validate(attrs)
        max_files = attrs.get("invocation_input_max_files", 1)
        max_size = attrs.get("invocation_input_max_size_mb", 10)
        max_total_size = attrs.get("invocation_input_max_total_size_mb", 10)
        max_output_files = attrs.get("invocation_output_max_files", 5)
        max_output_file_size = attrs.get("invocation_output_max_file_size_mb", 10)
        max_output_total_size = attrs.get("invocation_output_max_total_size_mb", 10)
        declared_outputs = attrs.get("declared_output_files", [])
        if max_files < 0:
            raise serializers.ValidationError(
                {"invocation_input_max_files": "Must be zero or greater."}
            )
        if max_size <= 0:
            raise serializers.ValidationError(
                {"invocation_input_max_size_mb": "Must be greater than zero."}
            )
        if max_total_size <= 0:
            raise serializers.ValidationError(
                {"invocation_input_max_total_size_mb": "Must be greater than zero."}
            )
        if max_size > max_total_size:
            raise serializers.ValidationError(
                {
                    "invocation_input_max_size_mb": (
                        "Must be less than or equal to the total input size limit."
                    )
                }
            )
        if max_output_files < 0:
            raise serializers.ValidationError(
                {"invocation_output_max_files": "Must be zero or greater."}
            )
        if max_output_file_size <= 0:
            raise serializers.ValidationError(
                {"invocation_output_max_file_size_mb": "Must be greater than zero."}
            )
        if max_output_total_size <= 0:
            raise serializers.ValidationError(
                {"invocation_output_max_total_size_mb": "Must be greater than zero."}
            )
        if len(declared_outputs) > max_output_files:
            raise serializers.ValidationError(
                {
                    "declared_output_files": (
                        f"Declare at most {max_output_files} output file(s)."
                    )
                }
            )
        if max_output_file_size > max_output_total_size:
            raise serializers.ValidationError(
                {
                    "invocation_output_max_file_size_mb": (
                        "Must be less than or equal to the total output size limit."
                    )
                }
            )
        return attrs

    def validate_source_bundle(self, value):
        try:
            validate_function_bundle(value)
        except ValueError as exc:
            raise serializers.ValidationError(str(exc)) from exc
        return value


class FunctionSerializer(serializers.ModelSerializer):
    versions = FunctionVersionSerializer(many=True, read_only=True)

    class Meta:
        model = Function
        fields = [
            "id",
            "owner",
            "name",
            "slug",
            "description",
            "invoke_access",
            "created_at",
            "updated_at",
            "versions",
        ]
        read_only_fields = ["owner", "slug", "created_at", "updated_at", "versions"]


class FunctionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ["id", "name", "slug", "description", "invoke_access"]
        read_only_fields = ["id", "slug"]

    def create(self, validated_data):
        owner = validated_data.pop("owner")
        base_slug = slugify(validated_data["name"])
        slug = base_slug or "function"
        suffix = 1
        while Function.objects.filter(slug=slug).exists():
            suffix += 1
            slug = f"{base_slug}-{suffix}" if base_slug else f"function-{suffix}"
        return Function.objects.create(owner=owner, slug=slug, **validated_data)


class FunctionInvokeSerializer(serializers.Serializer):
    event = serializers.JSONField(required=False, default=dict)
    version_id = serializers.IntegerField(required=False)
    version = serializers.CharField(required=False)

    def validate(self, attrs):
        if "version_id" in attrs and "version" in attrs:
            raise serializers.ValidationError(
                "Use either version_id or version, not both."
            )
        return attrs


class BuildReportSerializer(serializers.Serializer):
    job_id = serializers.UUIDField(required=False)
    dispatch_attempt = serializers.IntegerField(required=False, min_value=1)
    worker_name = serializers.CharField(required=False, allow_blank=True)
    status = serializers.ChoiceField(
        choices=[
            BuildStatus.BUILDING,
            BuildStatus.BUILT,
            BuildStatus.FAILED,
            BuildStatus.CANCELLED,
        ]
    )
    image_ref = serializers.CharField(required=False, allow_blank=True)
    build_log = serializers.CharField(required=False, allow_blank=True, default="")
    build_started_at = serializers.DateTimeField(required=False, allow_null=True)
    build_finished_at = serializers.DateTimeField(required=False, allow_null=True)

    def validate(self, attrs):
        if attrs.get("status") == BuildStatus.BUILT and not attrs.get("image_ref"):
            raise serializers.ValidationError(
                {"image_ref": "A completed build must include an image reference."}
            )
        return attrs
