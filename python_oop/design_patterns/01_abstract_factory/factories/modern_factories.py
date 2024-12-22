from factories.abstract_factory import AbstractFactory
from furnitures.chair import Chair
from furnitures.sofa import Sofa
from furnitures.table import Table


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Modern  chair')

    def create_sofa(self):
        return Sofa('Modern sofa')

    def create_table(self):
        return Table('Modern table')
