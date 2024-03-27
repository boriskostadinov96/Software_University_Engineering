from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAINING_SPEED_ADD = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + self.TRAINING_SPEED_ADD, self.MAX_SPEED)
