#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    copy = []
    for row in matrix:
        copy.append(list(map(lambda x: x*2, row)))
    return copy
