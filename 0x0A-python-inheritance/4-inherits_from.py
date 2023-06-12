#!/usr/bin/python3

"""Contains function that checks if an object inherits from an instance"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a class that is an instance

    Args:
        obj (object): object to check
        a_class (class): class to compare with

    Return:
        True if the object inherits from the specified class
        False if the object inherits from the specified class
    """

    if (type(obj) == a_class):
        return False
    return issubclass(type(obj), a_class)
