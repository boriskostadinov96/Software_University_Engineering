from project.cat import Cat


class Tomcat(Cat):
    TOMCAT_GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.TOMCAT_GENDER)

    @staticmethod
    def make_sound():
        return "Hiss"
