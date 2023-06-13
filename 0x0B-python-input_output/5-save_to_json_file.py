#!/usr/bin/python3

"""Contains a function to write JSON to a textfile
"""


import json


def save_to_json_file(my_obj, filename):
    """writes and object to a text file using JSON representation

    Args:
        my_obj (object): object to write to file
        filename (str): file to write to
    """

    jsonData = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(jsonData)
