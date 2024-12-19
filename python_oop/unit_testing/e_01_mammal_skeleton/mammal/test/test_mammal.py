from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Leo", "Lion", "Roar")

    def test_correct_init(self):
        self.assertEqual("Leo", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        # using name mangling in order to get the private attr.
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_animal_make_sound_correctly(self):
        self.assertEqual(f"Leo makes Roar", self.mammal.make_sound())

    def test_get_kingdom_correctly(self):
        self.assertEqual(f"animals", self.mammal.get_kingdom())

    def test_returns_correct_info(self):
        self.assertEqual(f"Leo is of type Lion", self.mammal.info())


if __name__ == "__main__":
    main()
