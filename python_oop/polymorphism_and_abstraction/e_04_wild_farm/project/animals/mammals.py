from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def food_that_eat(self):
        return [Vegetable, Fruit]

    @property
    def gain_weight(self):
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):

    @property
    def food_that_eat(self):
        return [Meat]

    @property
    def gain_weight(self):
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):

    @property
    def food_that_eat(self):
        return [Meat, Vegetable]

    @property
    def gain_weight(self):
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):

    @property
    def food_that_eat(self):
        return [Meat]

    @property
    def gain_weight(self):
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
