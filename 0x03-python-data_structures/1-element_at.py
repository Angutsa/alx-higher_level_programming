#!/usr/bin/python3

def element_at(my_list, idx):
    """returns the element at requested index
    my_list: list to be indexed
    idx: index
    """

    if ((idx < 0) and (idx >= len(my_list))):
        return

    return (my_list[idx])
