#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    for elem in my_list:
        if elem not in new_list:
            new_list.append(elem)
    return sum(new_list)
