from django.db import models, transaction
from django.utils import timezone

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
    user = models.ForeignKey(
        User, verbose_name="user id", on_delete=models.CASCADE, null=True
    )
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
    consumption = models.CharField(
        "consumption option",
        max_length=50,
        choices=choices.OrderConsumptionChoices,
        default=choices.OrderConsumptionChoices.EAT_IN,
    )

    class Meta:
        unique_together = ["number", "created_at"]
        ordering = ["-created_at"]

    @property
    def total_price(self):
        return self.products.get_total_price()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            last_daily_order = (
                Order.objects.select_for_update(nowait=True)
                .filter(created_at__date=timezone.now().date())
                .order_by("-number")
                .first()
            )

            if last_daily_order and self.number is None:
                self.number = last_daily_order + 1
            else:
                self.number = 1

            super().save(*args, **kwargs)
