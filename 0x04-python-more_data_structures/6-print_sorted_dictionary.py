#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    for elem in sorted(keys):
        print("{}: {}".format(elem, a_dictionary[elem]))
