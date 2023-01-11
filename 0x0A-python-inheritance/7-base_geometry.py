#!/usr/bin/python3

"""a class BaseGeometry"""


class BaseGeometry():
    """
    methods:
    area(): print a message
    """
    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        args:
        name (string)
        value (int)

        Raises:
        TypeError : <name> must be an integer
        ValueError : <name> must be greater than 0
        """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
