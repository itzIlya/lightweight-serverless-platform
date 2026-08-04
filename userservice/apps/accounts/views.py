from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .keys import jwk, key_id, public_key_pem
from .serializers import (
    RegisterSerializer,
    TokenObtainSerializer,
    TokenRefreshSerializer,
    UserSerializer,
)
from .tokens import issue_token_pair


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = issue_token_pair(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                **tokens,
            },
            status=status.HTTP_201_CREATED,
        )


class TokenObtainView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenObtainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.save()
        return Response(
            {
                "user": UserSerializer(serializer.user).data,
                **tokens,
            }
        )


class TokenRefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenRefreshSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class PublicKeyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "kid": key_id(),
                "alg": "RS256",
                "public_key": public_key_pem(),
            }
        )


class JWKSView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"keys": [jwk()]})
