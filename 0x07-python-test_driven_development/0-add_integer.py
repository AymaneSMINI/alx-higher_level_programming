#!/usr/bin/python

""" Function that add two integer """

def add_integer(a, b=98):

    """in case of a or b isn't an integer or float raise an error type"""
    type_list = [int, float]
    if type(a) not in type_list:
        raise TypeError("a must be an integer")
    if type(b) not in type_list:
        raise TypeError("b must be an integer")
    return a + b
