from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name: str):
        super().__init__(name, 25)

    def details(self):
        return f"{self.__class__.name}: {self.name}, {self.energy}"
