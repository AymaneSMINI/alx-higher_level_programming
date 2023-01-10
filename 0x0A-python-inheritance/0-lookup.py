#!/usr/bin/python3

"""Define a function that returns the list of attributes"""


def lookup(obj):
    """returns the list of available attributes"""

    return dir(obj)
