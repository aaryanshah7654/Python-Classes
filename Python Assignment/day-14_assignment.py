from abc import ABC , abstractmethod
import math

class shape(ABC):

    def perimeter(self):
        pass

    def area(self):
        pass

class Rectangle(shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width
    
class Triangle(shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return 0.5 * self.b * self.height
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

r = Rectangle(4, 5)
print("Rectangle → Area:", r.area(), "Perimeter:", r.perimeter())

t = Triangle(3, 4, 5, 2.5)
print("Triangle → Area:", t.area(), "Perimeter:", t.perimeter())

c = Circle(3)
print("Circle → Area:", round(c.area(), 2), "Perimeter:", round(c.perimeter(), 2))
