#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = 'arguments:'
    if (len(sys.argv) - 1) == 1:
        arg = 'argument:'
    elif (len(sys.argv) - 1) == 0:
        arg = 'arguments.'
    print('{} {}'.format(len(sys.argv) - 1, arg))
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
