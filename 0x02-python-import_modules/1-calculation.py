#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    #print the sum of a and b
    print("{} + {} = {}".format(a, b, add(a, b)))
    #print the subtraction of a and b
    print("{} - {} = {}".format(a, b, sub(a, b)))
    #print the multiplicationn of a and b
    print("{} * {} = {}".format(a, b, mul(a, b)))
    #print the division of a and b
    print("{} / {} = {}".format(a, b, div(a, b)))
