#!/usr/bin/python3

"""Contains the Base class
"""


class Base:
    """This is the base claass for all classes for this project

    Attributes:
        __nb_objects (int): number of instances of the class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): TODO
        """

        if id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            id = Base.__nb_objects

        self.id = id

    def __del__(self):
        """Class destructor
        """

        Base.__nb_objects -= 1
