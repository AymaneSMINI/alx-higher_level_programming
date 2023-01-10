#!/usr/bin/python3

"""Defines a function that write in file"""


def write_file(filename="", text=""):
    """write a text in file"""

    with open(filename) as f:
        f.write(text)
