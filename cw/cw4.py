class Parent:
    def info(self):
        print("parent")


class Child(Parent):
    pass


child = Child()
child.info()

class Human:
    __id = 0
    company = "apple"
    def __init__(self, name, age):
        self.name = "human"
        self.age = 0
        self.__id += 1

    def show_info(self):
        print(f"name:{self.name}\nage:{self.age}")

    def get_id(self):
        return self.__id

class Worker(Human):
    def __init__(self, name, age, salery):
        super().__init__(name, age)
        self.salery = salery


class Student(Human):
    def __init__(self, name, age, mark):
        super().__init__(name, age)
        self.mark = mark

    def show_info(self):
        super().show_info()
        print(f"mark:{self.mark}")



worker = Worker("James", 24, 300)
worker.show_info()

st = Student("Misha", 19, 10)
st.show_info()


humans = [worker, st]
for human in humans:
    print(human.name)


class Computer:
    def calculator(self):
        print("calculator")

class Display:
    def display(self):
        print("display the image")

class SmartPhone(Display, Computer):
    pass

ipone = SmartPhone()
ipone.display()
ipone.calculator()
ipone.show()
