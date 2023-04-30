#!/usr/bin/python3

"""Contains the Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """Defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: width of the rectangle
        """

        return self.__width

    @property
    def height(self):
        """int: height of the rectangle
        """

        return self.__height

    @property
    def x(self):
        """int: TODO
        """

        return self.__x

    @property
    def y(self):
        """int: TODO
        """

        return self.__y

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width should be an integer")

        if width <= 0:
            raise ValueError("width should be greater than 0")

        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height should be an integer")

        if height <= 0:
            raise ValueError("height should be greater than 0")

        self.__height = height

    @x.setter
    def x(self, x):
        # TODO
        self.__x = x

    @y.setter
    def y(self, y):
        # TODO
        self.__y = y

    def __del__(self):
        super().__del__()
