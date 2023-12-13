from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets

from api.models import Product
from api.serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    class CustomMeta:
        base_url = "products"
