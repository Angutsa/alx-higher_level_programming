#!/usr/bin/python3
from sys import argv


def infinite():
    """Adds up all the arguments passed to it

    """

    total = 0

    for x in argv:
        if (x == argv[0]):
            continue

        total = total + int(x)

    print(f"{total}")


if (__name__ == '__main__'):
    infinite()
