from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # admin_permission = super().has_permission(request, view)
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission
