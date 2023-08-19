from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
