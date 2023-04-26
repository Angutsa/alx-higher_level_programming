#!/usr/bin/python3

"""Contains the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the class Rectangle"""

    def __init__(self, width, height):
        """Initialises an instance of the class

        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        super()
        self.__width = width
        self.integer_validator('width', width)

        self.__height = height
        self.integer_validator('height', height)
