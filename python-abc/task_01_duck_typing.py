#!/usr/bin/env python3
"""Create a abstract class"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
"""create a class Circle"""
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

"""create a class Rectangle"""
class Rectangle(Shape):
    def __init__(self, width, height):
        """ init width and height"""
        self.width = width
        self.height = height
""" Area method"""
    def area(self):
        return self.width * self.height
    """perimeter method"""
    def perimeter(self):
        return 2 * (self.width + self.height)
    """func shape info"""
def shape_info(shape):
    print(f"Area : {shape.area()}")
    print(f"Perimeter : {shape.perimeter()}")
