#!/usr/bin/python3

"""Defines a function to set an attribute"""


def add_attribute(obj, name, value):
    """Creates a new attribute if possible

    Args:
        obj (object): object to add attribute to
        name (str): attribute name
        value (obj): attribute value
    """

    if '__dict__' in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
