#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """A class that represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Creates a new rectangle with the given width and height.


        Args:
            - width (int): The width of the rectangle. Defaults to 0.
            - height (int): The height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.


        Args:
            - value (int): The new width of the rrectangle.

        Raises:
            - TypeError: If 'value' is not integer.
            - ValueError: If 'value' is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the heigth of the rectangle.

        Args:
            - value (int): The new height of the rectangle.

        Raises:
            - TypeError: If 'value' is not integer.
            - ValueError: If 'value' is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """
        Area of rectangle (int) : height * width
        """

        return self.width * self.height

    def perimeter(self):
        """
        Perimeter (int): (width + height) * 2
        """
        
        if height == 0 or width == 0:
            return 0
        return (self.width + self.height) * 2
