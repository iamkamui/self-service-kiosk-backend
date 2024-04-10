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
