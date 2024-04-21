from factories.abstract_furntiture_factory import AbstractFactory
from furnitures.chair import Chair
from furnitures.sofa import Sofa
from furnitures.table import Table


class ModerFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa("Modern")

    def create_chair(self):
        return Chair("Modern")

    def create_table(self):
        return Table("Modern")
