#!/usr/bin/python3
from models.base import Base
"""Create a class Rectangle that inherits from Base"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class
        Args:
            height (int) : the height of the rectangle
            width (int) : the width of the recrangle
            x (int) : the x coordinate of the rectangle
            y (int): the y coordinate of the rectangle
            id : attribute from super class Base
        Methods:
            def __init__ : constructor
            def width :setter and getter of height
            def setter an getter of the width
            def setter and getter of x
            def setter and getter of the y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of the rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y of the rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
