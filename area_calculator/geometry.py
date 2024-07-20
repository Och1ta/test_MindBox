import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Базовый класс для всех фигур"""
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    """Класс для круга"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Класс для треугольника"""
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def is_right_angle(self):
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)
