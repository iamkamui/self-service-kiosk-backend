from django.db import models
from models.product import Product
from models.cart import Cart


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
