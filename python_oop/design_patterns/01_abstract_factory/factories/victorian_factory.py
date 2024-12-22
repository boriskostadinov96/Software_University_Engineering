from factories.abstract_factory import AbstractFactory
from furnitures.chair import Chair
from furnitures.sofa import Sofa
from furnitures.table import Table


class VictoriaFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Victorian chair')

    def create_sofa(self):
        return Sofa('Victorian sofa')

    def create_table(self):
        return Table('Victoria table')
