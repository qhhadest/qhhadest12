class Human:
    def __init__(self, name="Human", gladness):
        self.gladness = gladness
        self.name = name
        self.gladness = 50

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passanger = []

    def add_passanger(self,human):
        self.passanger.append(human)

    def print_passanger(self):
        if self.passanger == []:
           print(f"Names of {self.brand} passanger:")
           for passanger in self.passanger:
               print(passanger.name)
        else:
            print(f"No passanger in {self.brand}")

class Pet(Human):
    def __init__(self, pet, type, age, gladness):
        self.age = age
        self.pet = pet
        self.type = type
        self.gladness = gladness

    def fun(self):
        self.gladness += 10




james = Human("James")
amelia = Human("Amelia")

car = Auto("BMW")
car.add_passanger(james)
car.add_passanger(amelia)
car.print_passanger()