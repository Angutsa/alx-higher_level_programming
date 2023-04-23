#!/usr/bin/python3

"""Module contains function to say your name"""


def say_my_name(first_name, last_name=""):
    """prints the user's full name

    Args:
        first_name (string): user's first name
        last_name (string): user's last name

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
