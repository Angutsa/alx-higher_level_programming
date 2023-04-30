#!/usr/bin/python3

"""Contains function to create data stricture for JSON serialisation
"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization of an object

    Args:
        obj (object): object to create the dict description
    """

    attributes = obj.__dict__
    return attributes
