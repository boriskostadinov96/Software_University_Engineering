class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        new_catalogue = []

        for letter in self.products:
            if letter.startswith(first_letter):
                new_catalogue.append(letter)

        return new_catalogue

    def __repr__(self):
        sorted_products = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(sorted_products)

        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
