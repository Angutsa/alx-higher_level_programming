#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces the element at requested index
    my_list: list to be indexed
    idx: index
    element: replacement value
    """

    if ((idx > 0) and (idx < len(my_list))):
        my_list[idx] = element
        return (my_list)

    return (my_list)
