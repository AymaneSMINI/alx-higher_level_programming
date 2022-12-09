#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    copy = my_list.copy()
    for i in range(len(my_list)):
        copy[i] *= number
    return copy
