from django.db import models

from api.models.category import SubCategory
from api.models.managers import ActiveManager, InactiveManager
from core.models import BaseModel


class Product(BaseModel):
    name = models.CharField("product name", max_length=150, blank=False, null=False)
    brand = models.CharField("product brand", max_length=100)
    category = models.ManyToManyField(SubCategory, verbose_name="categories")
    price = models.DecimalField("product price", max_digits=10, decimal_places=2)
    is_active = models.BooleanField("is active", default=True)

    objects = models.Manager()
    active = ActiveManager()
    inactive = InactiveManager()

    def __str__(self) -> str:
        return f"{self.name} ({self.brand})"
