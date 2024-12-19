from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal(
            'Tiger',
            'Cats',
            'Roar',
        )

    def test_init(self):
        self.assertEqual('Tiger', self.mammal.name)
        self.assertEqual('Cats', self.mammal.type)
        self.assertEqual('Roar', self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual("Tiger makes Roar", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_get_animal_info(self):
        self.assertEqual("Tiger is of type Cats", self.mammal.info())


if __name__ == "__main__":
    main()
