import math
from protocols.shape import Shape


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return 0.5 * self.a * self.h


def print_area(shape: Shape):
    print(shape.area())