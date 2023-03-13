#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints list in reverse

    my_list: list to be reversed
    """

    my_list.reverse()
    for x in my_list:
        print("{:d}".format(x))
