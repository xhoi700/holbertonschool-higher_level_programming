#!/usr/bin/python3

"""Module for a class"""


class BaseGeometry:
    """Class of basegeometry"""
    def area(self):
        """Func to calculate area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
