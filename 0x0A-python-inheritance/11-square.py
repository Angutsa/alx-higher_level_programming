#!/usr/bin/python3

"""Contains the Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines the class Square"""

    def __init__(self, size):
        """Initialises an instance of the class

        Attributes:
            size (int): size of the square
        """

        super().__init__(size, size)
        self.__size = size

    def integer_validator(self, name, value):
        """Ensures that size is an integer"""

        super().integer_validator('size', value)

    def __str__(self):
        """provides an output for print() and str()"""

        return "[Square] {}/{}".format(self.__size, self.__size)
