#!/usr/bin/python3
from models.base import Base
"""Create a class Rectangle that inherits from Base"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class
        Args:
        height (int)
        width (int)
        x
        y
        Methods:
        __init__ : constructor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        self.__width = value
    
    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height
