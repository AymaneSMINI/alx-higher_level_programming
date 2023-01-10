#!/usr/bin/python3

"""Defines a function that write in file"""


def append_write(filename="", text=""):
    """write a text in file"""

    with open(filename, 'a') as f:
        f.write(text)
