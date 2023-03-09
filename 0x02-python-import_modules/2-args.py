#!/usr/bin/python3
from sys import argv


def arguments():
    """Prints its arguments

    Prints the arguments passed to it
    """

    argc = len(argv)

    if (argc > 1):
        if (argc == 2):
            print(f"1 argument:")
        else:
            print(f"{argc - 1} arguments:")

        for num in range(1, argc):
            print(f"{num}: {argv[num]}")
    else:
        print(f"0 arguments.")


if (__name__ == '__main__'):
    arguments()
