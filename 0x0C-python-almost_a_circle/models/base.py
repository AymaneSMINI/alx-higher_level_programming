#!/usr/bin/python3

"""Create a class Base"""


class Base():
    """
    create attributes and methods
    Args:
    __nb_objects (int) private attribute
    id (int) public attribute
    Methods:
    __init__: initialize the id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
