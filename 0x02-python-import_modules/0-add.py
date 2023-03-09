#!/usr/bin/python3
from add_0 import add

a = 1
b = 2


def addition():
    """Adds 1 and 2

    Prints the result
    """
    print("{} + {} = {}".format(a, b, add(a, b)))


if (__name__ == "__main__"):
    addition()
