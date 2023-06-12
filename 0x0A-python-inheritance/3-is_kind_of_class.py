#!/usr/bin/python3

"""Contains function that checks if an object inherits"""


def is_kind_of_class(obj, a_class):
    """Checks if an object inherits from a class

    Args:
        obj (object): object to check
        a_class (class): class to compare with

    Return:
        True if the object inherits from the specified class
        False if the object inherits from the specified class
    """

    return isinstance(obj, a_class)
