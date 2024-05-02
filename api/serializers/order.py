from rest_framework import exceptions, serializers

from api.models import Order, OrderProducts, Product
from api.utils import choices
from core.models import User


class OrderProductsSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )

    class Meta:
        model = OrderProducts
        fields = ["id", "products"]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
    products = OrderProductsSerializer(required=False)
    number = serializers.SerializerMethodField("get_order_number")
    consumption = serializers.ChoiceField(choices=choices.OrderConsumptionChoices)

    class Meta:
        model = Order
        fields = ["user", "products", "number", "consumption"]

    def get_order_number(self, obj: Order):
        return obj.number

    def create(self, validated_data: dict) -> Order:
        order_products = OrderProducts.objects.create()

        validated_data["session"] = self.context.get("session", None)

        try:
            order = Order.objects.create(products=order_products, **validated_data)
        except TypeError as error:
            order_products.delete()
            raise exceptions.ValidationError(str(error))

        return order
