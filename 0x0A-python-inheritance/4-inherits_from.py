#!/usr/bin/python3

"""Checking function"""


def inherits_from(obj, a_class):
    """ check if an instance is inherits directly or indirectly
    from a the spicified class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
