class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)

        elif species == 'bird':
            self.birds.append(name)

        else:
            self.fishes.append(name)

        Zoo._Zoo__animals += 1

    def get_info(self, species):
        result = ""

        if species == 'mammal':
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}"

        elif species == 'fish':
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}"

        else:
            result = f"Birds in {self.name}: {', '.join(self.birds)}"

        return f"{result}\n Total animals: {Zoo._Zoo__animals}"


zoo_name = input()
animals_count = int(input())
zoo = Zoo(zoo_name)

for _ in range(animals_count):
    species, animal_name = input().split()
    zoo.add_animal(species, animal_name)

kind = input()
print(zoo.get_info(kind))
