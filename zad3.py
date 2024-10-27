class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

class Zoo:
    def __init__(self, types):
        self.types = types
        self.brandzoo = []

    def add_animals_to_zoo(self, animal, animals=None):
        for animal in animals:
            self.brandzoo.append(animal)

    def print_animals_in_zoo(self):
        if self.brandzoo != []:
            print (f"In the zoo is {self.brandzoo}")
            for brandzoo in self.brandzoo:
                print(animal.name)
        else:
            print(f"No animals in {self.brandzoo}" )


monkey = Animal("Monkey")
leopard = Animal("Leopard")
zoo.add_animals_to_zoo(Monkey)
zoo.add_animals_to_zoo(Leopard)
zoo.print_animals_in_zoo




