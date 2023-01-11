#!/usr/bin/python3

"""Define a class MyList that inherits from list"""


class MyList(list):
    """Implements a function thatprint sorted list"""

    def print_sorted(self):
        print(sorted(self))
