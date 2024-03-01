from typing import List
from drink import Drink
from project.food import Food


class ProductRepository:
    def __init__(self):
        self.all_products: List[Food, Drink] = []

    def add(self, product: Food or Drink) -> None:
        self.all_products.append(product)

    def find(self, product_name: str) -> Food or Drink:
        for product in self.all_products:
            if product_name == product_name:
                return product

    def remove(self, product_name) -> None:
        product = self.find(product_name)

        if product:
            self.all_products.remove(product)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.all_products)
