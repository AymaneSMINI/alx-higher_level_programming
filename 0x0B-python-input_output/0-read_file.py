#!/usr/bin/python3
"""Function that read file"""


def read_file(filename=""):
    """ print content of the file """
    with open(filename) as f:
        print(f.read())
