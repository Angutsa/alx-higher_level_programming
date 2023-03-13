#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a string without modifying it
    my_list: list to index
    idx: index
    element: replacement integer
    """

    if (idx < 0 or idx >= len(my_list)):
        return (my_list)

    newlist = []
    newlist = [x for x in my_list]
    newlist[idx] = element
    return (newlist)
