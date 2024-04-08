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
            return queryset.filter(user__isnull=True)
            # TODO: Implement the logic for identify order from anonymous user
        return queryset
