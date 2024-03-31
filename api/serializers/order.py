from rest_framework import serializers

from api.models import Order, OrderProducts, Product
from api.utils import choices


class OrderProductsSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )

    class Meta:
        model = OrderProducts
        fields = ["products"]


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductsSerializer()
    consumption = serializers.ChoiceField(choices=choices.OrderConsumptionChoices)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data: dict) -> Order:
        products_data = validated_data.pop("products")
        order_products = OrderProducts.objects.create(**products_data)
        return Order.objects.create(products=order_products, **validated_data)
