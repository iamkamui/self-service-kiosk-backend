from random import choice
from typing import Dict

from faker.providers import BaseProvider


class DrinkProvider(BaseProvider):
    drinks = [
        {"category": "Refrigerante", "brand": "Coca-Cola Company", "name": "Coca-Cola"},
        {"category": "Refrigerante", "brand": "PepsiCo", "name": "Pepsi"},
        {"category": "Refrigerante", "brand": "Coca-Cola Company", "name": "Fanta"},
        {"category": "Refrigerante", "brand": "Coca-Cola Company", "name": "Sprite"},
        {"category": "Refrigerante", "brand": "AMBEV", "name": "Guaraná Antarctica"},
        {"category": "Refrigerante", "brand": "AMBEV", "name": "Sukita"},
        {"category": "Suco", "brand": "Coca-Cola Company", "name": "Del Valle"},
    ]

    brands = ["Coca-Cola Company", "PepsiCo", "AMBEV"]

    categories = ["Refrigerante", "Suco"]

    sizes = ["350ml", "500ml", "750ml", "1000ml"]

    def drink_object(self) -> Dict:
        drk = choice(self.drinks)
        drk["size"] = self.size()
        return drk

    def size(self) -> str:
        size = choice(self.sizes)
        return size

    def drink_category(self) -> str:
        category = choice(self.categories)
        return category
