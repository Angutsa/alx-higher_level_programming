#!/usr/bin/python3
"""Square Module

This module contains the class Square used to create and manipulate a square

"""


class Square:
    """Defines a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size: size of one side of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """position: position in the square"""

        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or value[1] < 0 or value[2] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """

        return self.__size * self.__size

    def my_print(self):
        """Prints the square using #"""

        if (self.__size == 0):
            print("")
            return

        for y in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for z in range(self.__position[0]):
                print(" ", end="")

            for j in range(self.__size):
                print("#", end="")

            print("")
