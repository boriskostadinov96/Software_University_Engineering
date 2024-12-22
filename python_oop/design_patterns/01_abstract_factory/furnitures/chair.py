from factories.abstract_factory import AbstractFactory


class Chair(AbstractFactory):
    def __init__(self, _type):
        self.type = _type

    def create_chair(self):
        pass

    def create_sofa(self):
        pass

    def create_table(self):
        pass
