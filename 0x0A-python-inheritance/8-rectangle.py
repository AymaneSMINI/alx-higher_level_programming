#!/usr/bin/python3

"""Define a class inherits from basegeometry"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """implementation of the class
    Args:
    height (int): the height of the rectangle
    width (int): the width of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
