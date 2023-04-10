#!/usr/bin/python3
class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        
        if size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """
        return self.__size * self.__size
