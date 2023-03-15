#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""

    if key not in a_dictionary:
        return (a_dictionary)

    new_dict = a_dictionary
    del new_dict[key]
    return (new_dict)
