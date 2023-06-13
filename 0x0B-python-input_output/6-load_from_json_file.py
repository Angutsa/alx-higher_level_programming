#!/usr/bin/python3

"""Contains a function to create and Object from a JSOn file
"""


import json


def load_from_json_file(filename):
    """Create an object from a JSON file

    Args:
        filename (str): file containing JSON representation
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        jsonObject = f.read()
        return json.loads(jsonObject)
