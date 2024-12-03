from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = sum(w.salary for w in self.workers)

        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_budget = sum(a.money_for_care for a in self.animals)

        if self.__budget >= animals_budget:
            self.__budget -= animals_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        amount_of_lions = sum(isinstance(animal, Lion) for animal in self.animals)
        amount_of_tigers = sum(isinstance(animal, Tiger) for animal in self.animals)
        amount_of_cheetahs = sum(isinstance(animal, Cheetah) for animal in self.animals)

        result = f"You have {total_animals_count} animals\n"

        # Lions
        result += f"----- {amount_of_lions} Lions:\n"
        lions = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        result += "\n".join(lions) + "\n"

        # Tigers
        result += f"----- {amount_of_tigers} Tigers:\n"
        tigers = [repr(animal) for animal in self.animals if isinstance(animal, Tiger)]
        result += "\n".join(tigers) + "\n"

        # Cheetahs
        result += f"----- {amount_of_cheetahs} Cheetahs:\n"
        cheetahs = [repr(animal) for animal in self.animals if isinstance(animal, Cheetah)]
        result += "\n".join(cheetahs)

        return result

    def workers_status(self) -> str:
        total_workers_count = len(self.workers)
        amount_of_keepers = sum(isinstance(worker, Keeper) for worker in self.workers)
        amount_of_caretakers = sum(isinstance(worker, Caretaker) for worker in self.workers)
        amount_of_vets = sum(isinstance(worker, Vet) for worker in self.workers)

        result = f"You have {total_workers_count} workers\n"

        # Keepers
        result += f"----- {amount_of_keepers} Keepers:\n"
        keepers = [repr(worker) for worker in self.workers if isinstance(worker, Keeper)]
        result += "\n".join(keepers) + "\n"

        # Caretakers
        result += f"----- {amount_of_caretakers} Caretakers:\n"
        caretakers = [repr(worker) for worker in self.workers if isinstance(worker, Caretaker)]
        result += "\n".join(caretakers) + "\n"

        # Vets
        result += f"----- {amount_of_vets} Vets:\n"
        vets = [repr(worker) for worker in self.workers if isinstance(worker, Vet)]
        result += "\n".join(vets)

        return result
