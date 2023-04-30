#!/usr/bin/python3

"""Contains function to write to a file
"""


def write_file(filename="", text=""):
    """Writes 'text' to  the file 'filename'

    Args:
        filename (str): file to write to
        text (str):  text to write into file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
