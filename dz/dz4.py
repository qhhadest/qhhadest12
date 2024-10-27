class Sport:
    def __init__(self, name):
        self.name = name

    def Sport1(self):
        print("Go to sport")

class Run(Sport):
    def __init__(self, name, run):
        super().__init__(name)
        self.run = run

    def spurt(self):
        print("Go to spurt")

class Swim(Sport):
    def __init__(self, name, swim):
        super().__init__(name)
        self.swim = swim

    def fastswim(self):
        print("Go to fastly swimming")


sport1 = Run("spurt running", "123")
sport2 = Swim("speed swimming", "234")


print(sport1.name)
print(sport1.run)
sport1.Sport1()
sport1.spurt()

print(sport2.name)
print(sport2.swim)
sport2.Sport1()
sport2.fastswim()
