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
        self.integer_validator('size', size)
