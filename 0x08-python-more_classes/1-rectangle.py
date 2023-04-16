#!/usr/bin/python3
"""Rectangle shape module

This module creates and modifies a rectangle
"""


class Rectangle:
    """Deifnes a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor for the rectangle"""
        self.height = height
        self.width = width

    # Height Instance Attribute
    @property
    def height(self):
        """int: height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value

    # Width Instance Attribute
    @property
    def width(self):
        """int: widht of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
