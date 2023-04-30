#!/usr/bin/python3

"""Contains the Square Class
"""


class Square(Rectangle):
    """Defines a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        """

        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """provides output for str() and print()
        """

        return "[Square] ({}) {]/{} - {}".format(self.__id, self.__x, self.__y,
                                                 self.__width)
