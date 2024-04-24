import decimal
import random

from faker import Faker

from api.models import Category, Product, SubCategory
from core.tests.utils.providers import DrinkProvider


class FakeProductBuild:

    def __init__(self) -> None:
        self.fake = Faker("pt_BR")
        self.fake.add_provider(DrinkProvider)

    def _get_category(self, product_category: str):
        drink_categories = ["Refrigerante", "Suco"]
        category, _ = (
            Category.objects.get_or_create(name="Bebida")
            if product_category in drink_categories
            else Category.objects.get_or_create("Comida")
        )
        return category

    def build(self) -> Product:
        product = self.fake.drink_object()
        product_category = product.get("category")

        category = self._get_category(product_category)

        sub_category, _ = SubCategory.objects.get_or_create(
            name=product_category, category=category
        )

        product, _ = Product.objects.get_or_create(
            **{
                "name": product.get("name"),
                "brand": product.get("brand"),
                "price": decimal.Decimal(random.randrange(300, 1500)) / 100,
            }
        )
        product.category.add(sub_category)

        return product
