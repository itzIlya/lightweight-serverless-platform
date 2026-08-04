from django.urls import path

from .views import (
    JWKSView,
    MeView,
    PublicKeyView,
    RegisterView,
    TokenObtainView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="userservice-register"),
    path("token/", TokenObtainView.as_view(), name="userservice-token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="userservice-token-refresh"),
    path("me/", MeView.as_view(), name="userservice-me"),
    path("public-key/", PublicKeyView.as_view(), name="userservice-public-key"),
    path("jwks/", JWKSView.as_view(), name="userservice-jwks"),
]
