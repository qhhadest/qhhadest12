import random


def first_function():
    pass


class Human:
    pass


rand = random
first_f = first_function
nick = Human

# 1) help()
print(help(random))
#  2) __name__
print(random.__name__)
print(rand.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)
# 3) type()
print(type(rand))
print(type(first_f))
print(type(nick))
# 4) hasattr()
data = "string"
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))
# 5) getattr()
print(getattr(data, "startswith"))
# print(getattr(data, "reverse"))

# 6) callable()
print(callable(data))
print(callable(first_f))


# 7) isinstance()  issubclass()
class Student(Human):
    pass


st = Student()
print(isinstance(st, Human))
print(issubclass(Student, Human))
print(issubclass(Human, Student))

import inspect

print(inspect.ismodule(inspect))
print(inspect.isclass(inspect))
print(inspect.isfunction(first_f))

print(inspect.getmodule(rand))

import sys

print(sys.version)
print(sys.platform)
print(sys.executable)

# requests

import requests

print(inspect.ismodule(requests))
print(callable(requests))

print(sys.version(requests))
print(hasattr.__name__(requests))
