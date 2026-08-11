from __future__ import annotations

import json
from pathlib import PurePosixPath

from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from rest_framework import serializers

from .models import (
    BuildAttempt,
    BuildPolicy,
    BuildStatus,
    Function,
    FunctionInvokeToken,
    FunctionVersion,
)
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
            "invocation_max_retries",
            "invocation_retry_backoff_seconds",
            "retry_invocation_timeouts",
            "retry_invocation_function_errors",
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
    invocation_retry_backoff_seconds = FlexibleJSONField(required=False, default=list)

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
            "invocation_max_retries",
            "invocation_retry_backoff_seconds",
            "retry_invocation_timeouts",
            "retry_invocation_function_errors",
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
        invocation_max_retries = attrs.get("invocation_max_retries", 0)
        invocation_retry_backoff = attrs.get("invocation_retry_backoff_seconds", [])
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
        if invocation_max_retries < 0:
            raise serializers.ValidationError(
                {"invocation_max_retries": "Must be zero or greater."}
            )
        if not isinstance(invocation_retry_backoff, list):
            raise serializers.ValidationError(
                {"invocation_retry_backoff_seconds": "Must be a JSON array."}
            )
        for value in invocation_retry_backoff:
            if not isinstance(value, int) or value < 0:
                raise serializers.ValidationError(
                    {
                        "invocation_retry_backoff_seconds": (
                            "Each retry backoff value must be a non-negative integer."
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
    resource = serializers.SerializerMethodField()
    versions = FunctionVersionSerializer(many=True, read_only=True)
    active_version = FunctionVersionSerializer(read_only=True)
    active_image_ref = serializers.SerializerMethodField()
    build_status = serializers.SerializerMethodField()
    pending_build = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Function
        fields = [
            "id",
            "resource",
            "owner",
            "name",
            "slug",
            "description",
            "invoke_access",
            "active_version",
            "active_image_ref",
            "build_status",
            "pending_build",
            "links",
            "created_at",
            "updated_at",
            "versions",
        ]
        read_only_fields = [
            "owner",
            "resource",
            "slug",
            "active_version",
            "active_image_ref",
            "build_status",
            "pending_build",
            "links",
            "created_at",
            "updated_at",
            "versions",
        ]

    def get_resource(self, obj):
        return "function"

    def get_active_image_ref(self, obj):
        active_version = getattr(obj, "active_version", None)
        return active_version.image_ref if active_version else ""

    def get_build_status(self, obj):
        pending = self._latest_pending_version(obj)
        if pending is not None:
            return pending.build_status
        active_version = getattr(obj, "active_version", None)
        if active_version is not None:
            return active_version.build_status
        latest = obj.versions.order_by("-created_at", "-id").first()
        return latest.build_status if latest else "not_built"

    def get_pending_build(self, obj):
        pending = self._latest_pending_version(obj)
        if pending is None:
            return None
        latest_attempt = pending.build_attempts.order_by("-created_at", "-id").first()
        return {
            "version_id": pending.id,
            "version": pending.version,
            "build_status": pending.build_status,
            "build_request_id": str(pending.build_request_id),
            "attempt": (
                BuildAttemptSerializer(latest_attempt).data
                if latest_attempt is not None
                else None
            ),
        }

    def get_links(self, obj):
        return {
            "self": f"/api/functions/{obj.id}/",
            "source": f"/api/functions/{obj.id}/source/",
            "build_status": f"/api/functions/{obj.id}/build-status/",
            "invoke": f"/api/functions/{obj.id}/invoke/",
            "invoke_sync": f"/api/functions/{obj.id}/invoke-sync/",
            "invocations": f"/api/functions/{obj.id}/invocations/",
            "tokens": f"/api/functions/{obj.id}/tokens/",
        }

    def _latest_pending_version(self, obj):
        return (
            obj.versions.filter(
                build_status__in=[
                    BuildStatus.QUEUED,
                    BuildStatus.BUILDING,
                    BuildStatus.CANCELLING,
                ]
            )
            .order_by("-created_at", "-id")
            .first()
        )


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


class FunctionInvokeTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionInvokeToken
        fields = [
            "id",
            "name",
            "prefix",
            "is_active",
            "expires_at",
            "revoked_at",
            "last_used_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields


class FunctionInvokeTokenCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120, trim_whitespace=True)
    expires_at = serializers.DateTimeField(required=False, allow_null=True)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Token name is required.")
        return value.strip()

    def validate_expires_at(self, value):
        if value is not None and value <= timezone.now():
            raise serializers.ValidationError("Expiry must be in the future.")
        return value

    def validate(self, attrs):
        function = self.context["function"]
        active_count = function.invoke_tokens.filter(
            is_active=True,
            revoked_at__isnull=True,
        ).count()
        if active_count >= settings.MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION:
            raise serializers.ValidationError(
                {
                    "tokens": (
                        "This function has reached the maximum number of "
                        "active invocation tokens."
                    )
                }
            )
        if _active_token_name_exists(function, attrs["name"]):
            raise serializers.ValidationError(
                {"name": "An active invocation token with this name already exists."}
            )
        return attrs


class FunctionInvokeTokenUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120, trim_whitespace=True, required=False)
    expires_at = serializers.DateTimeField(required=False, allow_null=True)
    is_active = serializers.BooleanField(required=False)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Token name is required.")
        return value.strip()

    def validate_expires_at(self, value):
        if value is not None and value <= timezone.now():
            raise serializers.ValidationError("Expiry must be in the future.")
        return value

    def validate(self, attrs):
        token = self.context["token"]
        function = self.context["function"]
        target_name = attrs.get("name", token.name)
        target_active = attrs.get("is_active", token.is_active)
        target_expires_at = attrs.get("expires_at", token.expires_at)
        if (
            target_active
            and target_expires_at is not None
            and target_expires_at <= timezone.now()
        ):
            raise serializers.ValidationError(
                {"is_active": "Expired invocation tokens cannot be activated."}
            )
        if target_active and not token.is_active:
            active_count = function.invoke_tokens.filter(
                is_active=True,
                revoked_at__isnull=True,
            ).exclude(pk=token.pk).count()
            if active_count >= settings.MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION:
                raise serializers.ValidationError(
                    {
                        "tokens": (
                            "This function has reached the maximum number of "
                            "active invocation tokens."
                        )
                    }
                )
        if target_active and _active_token_name_exists(
            function,
            target_name,
            exclude_pk=token.pk,
        ):
            raise serializers.ValidationError(
                {"name": "An active invocation token with this name already exists."}
            )
        return attrs


class FunctionInvokeTokenRotateSerializer(serializers.Serializer):
    expires_at = serializers.DateTimeField(required=False, allow_null=True)

    def validate_expires_at(self, value):
        if value is not None and value <= timezone.now():
            raise serializers.ValidationError("Expiry must be in the future.")
        return value

    def validate(self, attrs):
        function = self.context["function"]
        token = self.context["token"]
        if not token.is_active:
            active_count = function.invoke_tokens.filter(
                is_active=True,
                revoked_at__isnull=True,
            ).exclude(pk=token.pk).count()
            if active_count >= settings.MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION:
                raise serializers.ValidationError(
                    {
                        "tokens": (
                            "This function has reached the maximum number of "
                            "active invocation tokens."
                        )
                    }
                )
        if _active_token_name_exists(function, token.name, exclude_pk=token.pk):
            raise serializers.ValidationError(
                {"name": "An active invocation token with this name already exists."}
            )
        return attrs


def _active_token_name_exists(function, name: str, *, exclude_pk=None) -> bool:
    queryset = function.invoke_tokens.filter(
        name__iexact=name,
        is_active=True,
        revoked_at__isnull=True,
    )
    if exclude_pk is not None:
        queryset = queryset.exclude(pk=exclude_pk)
    return queryset.exists()


class FunctionSourceReplacementSerializer(serializers.Serializer):
    source_bundle = serializers.FileField()
    runtime = serializers.CharField(required=False)
    handler = serializers.CharField(required=False)
    config = FlexibleJSONField(required=False)
    invocation_input_mime_types = FlexibleJSONField(required=False)
    invocation_input_max_files = serializers.IntegerField(required=False, min_value=0)
    invocation_input_max_size_mb = serializers.IntegerField(required=False, min_value=1)
    invocation_input_max_total_size_mb = serializers.IntegerField(required=False, min_value=1)
    declared_output_files = FlexibleJSONField(required=False)
    invocation_output_max_files = serializers.IntegerField(required=False, min_value=0)
    invocation_output_max_file_size_mb = serializers.IntegerField(required=False, min_value=1)
    invocation_output_max_total_size_mb = serializers.IntegerField(required=False, min_value=1)
    invocation_max_retries = serializers.IntegerField(required=False, min_value=0)
    invocation_retry_backoff_seconds = FlexibleJSONField(required=False)
    retry_invocation_timeouts = serializers.BooleanField(required=False)
    retry_invocation_function_errors = serializers.BooleanField(required=False)

    def validate_source_bundle(self, value):
        try:
            validate_function_bundle(value)
        except ValueError as exc:
            raise serializers.ValidationError(str(exc)) from exc
        return value

    def validate_invocation_input_mime_types(self, value):
        return FunctionVersionCreateSerializer().validate_invocation_input_mime_types(value)

    def validate_declared_output_files(self, value):
        return FunctionVersionCreateSerializer().validate_declared_output_files(value)

    def validate(self, attrs):
        active_version = self.context.get("active_version")
        base = {}
        if active_version is not None:
            for field in [
                "runtime",
                "handler",
                "config",
                "invocation_input_mime_types",
                "invocation_input_max_files",
                "invocation_input_max_size_mb",
                "invocation_input_max_total_size_mb",
                "declared_output_files",
                "invocation_output_max_files",
                "invocation_output_max_file_size_mb",
                "invocation_output_max_total_size_mb",
                "invocation_max_retries",
                "invocation_retry_backoff_seconds",
                "retry_invocation_timeouts",
                "retry_invocation_function_errors",
            ]:
                base[field] = getattr(active_version, field)
        else:
            base.update(
                {
                    "runtime": "python3.13",
                    "handler": "handler.main",
                    "config": {},
                    "invocation_input_mime_types": [],
                    "invocation_input_max_files": 1,
                    "invocation_input_max_size_mb": 10,
                    "invocation_input_max_total_size_mb": 10,
                    "declared_output_files": [],
                    "invocation_output_max_files": 5,
                    "invocation_output_max_file_size_mb": 10,
                    "invocation_output_max_total_size_mb": 10,
                    "invocation_max_retries": 0,
                    "invocation_retry_backoff_seconds": [],
                    "retry_invocation_timeouts": False,
                    "retry_invocation_function_errors": False,
                }
            )
        base.update(attrs)
        FunctionVersionCreateSerializer().validate(base)
        return base


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
