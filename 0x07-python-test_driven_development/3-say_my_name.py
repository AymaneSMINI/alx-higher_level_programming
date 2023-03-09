#!/usr/bin/python3

"""Defines say_my_name  function"""


def say_my_name(first_name, last_name=""):
    """ print first name and last name"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("Aymane")
    say_my_name("Aymane", "Smini")
    say_my_name(12, "White")
