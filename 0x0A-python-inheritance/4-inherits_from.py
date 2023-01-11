#!/usr/bin/python3

"""Checking function"""


def inherits_from(obj, a_class):
    """ check if an instance is inherits directly or indirectly from a the spicified class"""

    return issubclass(obj, a_class)
