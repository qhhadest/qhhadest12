class Human:
    def __init__(self, name, age):
        self.name = "Human"
        self.age = age

    def show_info(self):
        print(f"name:{self.name}\nage:{self.age}")


class Brain(Human):
    def __init__(self, age, iq):
        super().__init__(age)
        self.iq = iq

    def show_info(self):
        super().show_info()
        print(f"iq:{self.iq}")

class Heart(Human):
    def __init__(self, age, bpm):
        super().__init__(age)
        self.bpm = bpm

    def show_info(self):
        super().show_info()
        print(f"bpm:{self.bpm}")

    def run(self):
        pass
class Legs(Human):
    def __init__(self, age, speed):
        super().__init__(age)
        self.speed = speed


brain = Brain(15, 126)
brain.show_info()

heart = Heart(17, 94)
heart.show_info()


