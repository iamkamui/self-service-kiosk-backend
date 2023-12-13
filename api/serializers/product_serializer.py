from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    subcategory = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=50)
    price = serializers.FloatField()

    class Meta:
        ordering = ["subcategory", "-price"]
