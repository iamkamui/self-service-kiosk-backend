from django.db import models
from core.models import DefaultBaseModel
from .product import Product
from .cart import Cart


class Order(DefaultBaseModel):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(DefaultBaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
