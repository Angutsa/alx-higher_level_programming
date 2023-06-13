#!/usr/bin/python3

"""Contains a function that converts JSON to Python object
"""


import json


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str (str): JSON string to deserialise
    """

    return json.loads(my_str)
