#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        m = 0
        for i in my_list:
            if i > m:
                m = i
        return m
    return 'None'
