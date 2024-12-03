from project.animal import Animal


class Lion(Animal):
    COST = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Lion.COST)