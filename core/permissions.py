from rest_framework.permissions import BasePermission

READ_ONLY_METHODS = ["GET", "HEAD", "OPTIONS"]


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a admin user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in READ_ONLY_METHODS
            or request.user
            and request.user.is_superuser
        )
