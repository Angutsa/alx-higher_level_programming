#!/usr/bin/python3

"""Module contains function to print a square"""


def print_square(size):
    """prints out a square

    Args:
        size (int): size of the square to print
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        if type(size) == float:
            raise TypeError("size must be an integer")

        raise ValueError("size must be >= 0")

    for row in range(size):
        for item in range(size):
            print("#", end="")

        print()
