from project.cat import Cat


class Kitten(Cat):
    KITTEN_GENDER = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.KITTEN_GENDER)

    @staticmethod
    def make_sound():
        return "Meow"
