from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        products_details = '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)
        return f"{products_details}"
