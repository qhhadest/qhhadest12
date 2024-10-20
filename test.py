import random


class Pet:
    pass
    def __init__(self, name, age, type):
        # public prop
        self.name = name
        self.age = age
        self.type = type
        self.gladness = 50
        self.need = 20
        self.alive = True

    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.type)

    def take_a_walk(self):
        print("Time to a take a walking!")
        self.gladness += 5
        self.need -= 10

    def to_sleep(self):
        print("I want to sleep")
        self.gladness += 2
        self.need += 5

    def is_alive(self):
        if self.gladness == 0
            print("Depression")
            self.alive = False

    def to_chill(self):
        print("rest time")
        self.gladness += 5

    def to_eat(self):
        print("time for eating")
        self.gladness += 3
        self.need += 8

    def end_of_day(self):
        print(f"name{self.name}")
        print(f"gladness{self.gladness}")
        print(f"need{self.need}")
        print(f"alive"{self.alive})


    def live(self,day):
        day = "Day" +str(day) + "of" + self.name + "life"
        print(day)
        live_cube = random.randint(1,3)
        if live_cube == 1:
           self.take_a_walk()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_eat()
            self.to_sleep()
            self.end_of_day()
            self.is_alive()



nick = Pet("Cat",3)
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)



st1 = Pet("Cat", 3)
st1.show_info()

st2 = Pet("Dog", 5)
st2.show_info()