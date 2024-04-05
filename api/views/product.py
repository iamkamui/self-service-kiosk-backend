from rest_framework import viewsets

from api.models import Product
from api.permissions import IsAdminOrReadOnly
from api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]

    class CustomMeta:
        base_url = "products"
