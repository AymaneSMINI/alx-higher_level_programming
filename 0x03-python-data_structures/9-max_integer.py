#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        Max = 0
        for integer in my_list:
            if integer > Max:
                Max = integer
        return Max
    return 'None'
