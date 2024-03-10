class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.personal_id = Trainer.id
        Trainer.id += 1

    def __repr__(self):
        return f"Trainer <{self.personal_id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id
