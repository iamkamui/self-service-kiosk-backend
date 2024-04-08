from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField("category", max_length=150)

    def __str__(self) -> str:
        return self.name.capitalize()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class SubCategory(BaseModel):
    name = models.CharField("product category", max_length=150)
    category_id = models.ForeignKey(
        Category, verbose_name="category", on_delete=models.DO_NOTHING, null=True
    )

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name = "sub category"
        verbose_name_plural = "sub categories"
