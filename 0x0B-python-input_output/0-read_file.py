#!/usr/bin/python3

"""Contains a function to read from a file
"""


def read_file(filename=""):
    """Reads a textfile and prints it out to stdout

    Args:
        filename (str): file to be read
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
