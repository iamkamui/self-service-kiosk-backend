from django.contrib import admin  # noqa

from api.models import Category, Product, SubCategory

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
