from django.contrib.auth.models import AnonymousUser
from rest_framework import filters


class IsOwnerOrAdminFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if (
            not isinstance(request.user, AnonymousUser)
            and not request.user.is_superuser
        ):
            return queryset.filter(user=request.user)

        if isinstance(request.user, AnonymousUser):
            session_key = request.session.session_key
            return queryset.filter(user__isnull=True, session=session_key)
        return queryset
