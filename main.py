# int float str bool
import random


class Student:
        def __init__(self, name, age):
            # public prop
            self.name = name
            self.age = age
            self.gladness = 50
            self.alive = True
            self.progress = 0
            # private
            self.__money = 100

        def show_info(self):
            print(self.name)
            print(self.age)
            print(self.__money, "$")

        def to_study(self):
            print("time to study")
            self.gladness -= 3
            self.progress += 3

        def to_sleep(self):
            print("i need to sleep")
            self.gladness += 5

        def to_chill(self):
            print("rest time")
            self.progress -= 0.1
            self.gladness += 5

        def is_alive(self):
            if self.progress < -0.5:
                print("cast out")
                self.alive = False
            elif self.gladness <= 0:
                print("depression")
                self.alive = False

        def work(self):
            if self.__money >= 90:
                self.gladness -= 10
                self.__money += 20


        def end_of_day(self):
            print(f"name {self.name}")
            print(f"gladness {self.gladness}")
            print(f"progress {self.progress}")

        def live(self,day):
            day = "Day" +str(day) + "of" + self.name + "life"
            print(day)
            live_cube = random.randint(1,3)
            if live_cube == 1:
               self.to_study()
            elif live_cube == 2:
                self.to_chill()
            elif live_cube == 3:
                self.to_sleep()
                self.end_of_day()
                self.is_alive()






nick = Student("Nick",20)
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)



st1 = Student("mark", 15)
st1.show_info()

st2 = Student("Ilon", 45)
st2.show_info()
