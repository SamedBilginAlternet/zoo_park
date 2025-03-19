class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} the {self.species}, {self.age} years old"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(animal)


if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_animal(Animal("Leo", "Lion", 5))
    zoo.add_animal(Animal("Molly", "Monkey", 2))
    zoo.show_animals()