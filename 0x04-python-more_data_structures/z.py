#!/usr/bin/python3

search_replace = __import__('1-search_replace').search_replace



my_list = [1, 2, 3, 1, 1, 3, 6]

search = 1

replace = 0

new_list = search_replace(my_list, search, replace)



print(new_list)

print(my_list)
