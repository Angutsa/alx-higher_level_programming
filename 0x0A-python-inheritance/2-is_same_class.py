#!/usr/bin/python3

"""Contains function that checks if an object is an instance"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class

    Args:
        obj (object): object to check
        a_class (class): class to compare with

    Return:
        True if the object is exactly an instance of the specified class
        False if the object is not exactly an instance of the specified
        class
    """

    if (a_class == object):
        return False

    return isinstance(obj, a_class)
