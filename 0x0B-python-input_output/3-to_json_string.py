#!/usr/bin/python3

"""Contains a function that returns a JSON representation
"""


import json


def to_json_string(my_obj):
    """Creates a JSON representation of my_obj

    Args:
        my_obj (object): object to serialise
    """

    return json.dumps(my_obj)
