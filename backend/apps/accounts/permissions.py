from rest_framework.permissions import BasePermission

from .services import is_platform_admin


class IsPlatformAdmin(BasePermission):
    def has_permission(self, request, view):
        return is_platform_admin(request.user)

