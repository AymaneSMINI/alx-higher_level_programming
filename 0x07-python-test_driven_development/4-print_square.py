#!/usr/bin/python3

def print_square(size):
    """Defines print_square function that print a square"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()


if __name__ == "__main__":
    print_square(2)
