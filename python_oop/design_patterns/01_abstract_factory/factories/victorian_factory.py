from factories.abstract_furntiture_factory import AbstractFactory
from furnitures.chair import Chair
from furnitures.sofa import Sofa
from furnitures.table import Table


class VictorianFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa("Victorian")

    def create_chair(self):
        return Chair("Victorian")

    def create_table(self):
        return Table("Victorian")