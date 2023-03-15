#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""

    c = set(my_list)
    sum = 0
    for x in c:
        sum = sum + x

    return (sum)
