from rest_framework import serializers

from api.models import Product, SubCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True, queryset=SubCategory.objects.all(), slug_field="name"
    )

    class Meta:
        model = Product
        fields = ["id", "name", "brand", "category", "price"]
