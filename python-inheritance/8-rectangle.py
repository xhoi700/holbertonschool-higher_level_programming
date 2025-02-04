#!/usr/bin/python3

"""Module about a rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class about a rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
