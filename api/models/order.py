from django.db import models

from api.models.product import Product
from api.utils import choices
from core.models import BaseModel, User


class OrderProducts(BaseModel):
    products = models.ManyToManyField(Product, verbose_name="products")

    @property
    def total_price(self):
        return self.get_total_price()

    def get_total_price(self):
        return sum(product.price for product in self.products.all())


class Order(BaseModel):
    user = models.ForeignKey(User, verbose_name="user id", on_delete=models.CASCADE)
    products = models.OneToOneField(
        OrderProducts, verbose_name="order products", on_delete=models.CASCADE
    )
    number = models.BigIntegerField("order number")
    status = models.CharField(
        "order status",
        max_length=20,
        choices=choices.OrderStatusChoices,
        default=choices.OrderStatusChoices.PREPARING,
    )

    @property
    def total_price(self):
        return self.products.get_total_price()
