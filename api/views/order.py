from django.contrib.auth.models import AnonymousUser
from rest_framework import mixins, permissions, response, status, viewsets
from rest_framework.decorators import action

from api.filters import IsOwnerOrAdminFilterBackend
from api.models import Order
from api.serializers import OrderSerializer


class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [
        IsOwnerOrAdminFilterBackend,
    ]

    class CustomMeta:
        base_url = "orders"

    @classmethod
    def get_base_url(self):
        return self.CustomMeta.base_url

    @action(
        methods=["post", "get"],
        permission_classes=[
            permissions.AllowAny,
        ],
        detail=False,
        url_name="start",
        url_path="start",
    )
    def start_order(self, request, format=["JSON"]):

        if not isinstance(request.user, AnonymousUser):
            request.data["user"] = request.user.id

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)