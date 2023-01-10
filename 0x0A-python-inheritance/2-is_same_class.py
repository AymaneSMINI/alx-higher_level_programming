#!/usr/bin/python3

"""Checking function"""


def is_same_class(obj, a_class):
    """ check if a class is an instance"""

    return type(obj).__name__ == a_class
