#!/usr/bin/python3

"""Module contains function to get all attributes"""


def lookup(obj):
    """Returns all attributes and methods in 'obj'

    Args:
        obj (object): object to loookup
    """

    return dir(obj)
