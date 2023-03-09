#!/usr/bin/python3
import hidden_4 as module


def printnames():
    """Prints names from the hidden_4 module

    Function will not print names beginning with __
    """
    for name in dir(module):
        if (name[0:2] == '__'):
            continue

        print(f"{name}")


if (__name__ == '__main__'):
    printnames()
