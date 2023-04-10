#!/usr/bin/python3
"""Square Module

This module contains the class Square used to create and manipulate a square

"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """
        return self.__size * self.__size
