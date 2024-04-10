from rest_framework import viewsets

from api.models import Product
from api.serializers import ProductSerializer
from core.permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]

    class CustomMeta:
        base_url = "products"

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Product.active.all()
        return super().get_queryset()
