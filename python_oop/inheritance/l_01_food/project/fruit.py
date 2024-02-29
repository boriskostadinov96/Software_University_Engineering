from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name


# fruit = Fruit("02.08.24", "Banana")
# print(fruit.expiration_date)
# print(fruit.name)
