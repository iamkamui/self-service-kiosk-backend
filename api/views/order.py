from django.contrib.auth.models import AnonymousUser
from rest_framework import response, status, viewsets
from rest_framework.decorators import action

from api.models import Order
from api.serializers import OrderSerializer


class OrderViewSet(viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    class CustomMeta:
        base_url = "order"

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
