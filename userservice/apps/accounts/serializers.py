from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Account, AccountRole
from .tokens import decode_token, issue_token_pair


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="pk", read_only=True)
    subject = serializers.SerializerMethodField()
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    role = serializers.SerializerMethodField()

    def get_subject(self, user):
        account, _ = Account.objects.get_or_create(user=user)
        return str(account.subject)

    def get_role(self, user):
        account, _ = Account.objects.get_or_create(user=user)
        if user.is_staff or user.is_superuser:
            return AccountRole.ADMIN
        return account.role


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_username(self, value):
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )
        Account.objects.create(user=user, role=AccountRole.USER)
        return user


class TokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")
        self.user = user
        return attrs

    def save(self):
        return issue_token_pair(self.user)


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        try:
            claims = decode_token(attrs["refresh"], expected_type="refresh")
        except Exception as exc:
            raise serializers.ValidationError("Invalid refresh token.") from exc
        account = Account.objects.select_related("user").filter(
            subject=claims.get("sub")
        ).first()
        if account is None:
            raise serializers.ValidationError("User no longer exists.")
        self.user = account.user
        return attrs

    def save(self):
        return issue_token_pair(self.user)
