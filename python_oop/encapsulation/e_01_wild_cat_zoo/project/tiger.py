from project.animal import Animal


class Tiger(Animal):
    COST = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Tiger.COST)
