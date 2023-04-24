#!/usr/bin/python3

"""Contains a the class MyList"""


class MyList(list):
    """MyList class that inherits from builtin list type"""

    def __init__(self):
        """Initialiser for MyList"""
        list.__init__(self)

    def print_sorted(self):
        """Prints the list in sorted order"""

        lst = []
        for item in self:
            lst.append(item)

        lst.sort()
        print(lst)
