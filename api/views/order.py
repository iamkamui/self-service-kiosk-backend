from django.contrib.auth.models import AnonymousUser
from rest_framework import response, status, viewsets
from rest_framework.decorators import action

from api.models import Order
from api.permissions import IsOwnerOrAdmin
from api.serializers import OrderSerializer


class OrderViewSet(viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    class CustomMeta:
        base_url = "orders"

    @classmethod
    def get_base_url(self):
        return self.CustomMeta.base_url

    @action(methods=["post", "get"], detail=False, url_name="start", url_path="start")
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

    def list(
        self,
        request,
        format=["JSON"],
        permission_classes=[
            IsOwnerOrAdmin,
        ],
        *args,
        **kwargs
    ):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
