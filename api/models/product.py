from django.db import models

from core.models import DefaultBaseModel


class Category(DefaultBaseModel):
    name = models.CharField(max_length=150)


class SubCategory(DefaultBaseModel):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Product(DefaultBaseModel):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return self.name
