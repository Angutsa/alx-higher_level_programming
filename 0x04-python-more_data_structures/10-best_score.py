#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with the biggest integer value"""

    if (a_dictionary is None or len(a_dictionary) == 0):
        return

    names = list(a_dictionary)
    highest = names[0]

    for name in names:
        if (a_dictionary[name] > a_dictionary[highest]):
            highest = name

    return (highest)
