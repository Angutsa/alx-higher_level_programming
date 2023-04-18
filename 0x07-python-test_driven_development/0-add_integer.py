#!/usr/bin/python3
"""Contains a function to add two integers

"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int or float): first number to add
        b (int or float): second number to add

    Return:
        Returns the sum of a and b as an integer
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
