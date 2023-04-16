#!/usr/bin/python3
"""Rectangle shape module

This module creates and modifies a rectangle.
"""


class Rectangle:
    """Defines a rectangle shape

    Attributes:
        number_of_instances (int): number of rectangle instances created
        print_symbol (optional): synbol to use in printing the rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor for the rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    # Height Instance Attribute
    @property
    def height(self):
        """int: height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    # Width Instance Attribute
    @property
    def width(self):
        """int: width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    # Methods
    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        output = ""
        if self.__width == 0 or self.__height == 0:
            return output

        for row in range(self.__height):
            for item in range(self.__width):
                output = "{}{}".format(output, self.print_symbol)

            if row != (self.__height - 1):
                output = output + "\n"

        return output

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
