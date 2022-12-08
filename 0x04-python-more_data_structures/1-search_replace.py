#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if search < 0 or search > len(my_list):
        return my_list
    new_list = my_list.copy()
    for i in range(len(my_list)):
            if my_list[i] == search:
                my_list[i] = replace
    return new_list
