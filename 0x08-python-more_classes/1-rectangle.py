#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.
        args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle """
        return self._height

    @height.setter
    def height(self, value):
        """ Set the heigth of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
