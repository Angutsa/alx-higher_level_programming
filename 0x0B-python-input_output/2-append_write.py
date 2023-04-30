#!/usr/bin/python3

"""Contains function to append to a file
"""


def append_write(filename="", text=""):
    """appends 'text' to the file 'filename'

    Args:
        filename (str): file to write to
        text (str): text to append in the file
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
