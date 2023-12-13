from django.db import models

from . import Product
from core.models import DefaultBaseModel


class Cart(DefaultBaseModel):
    session_id = models.CharField(max_length=250, unique=True)


class CartItem(DefaultBaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
