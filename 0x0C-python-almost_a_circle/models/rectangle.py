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
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def __del__(self):
        """Class deconstructor
        """

        super().__del__()

    def area(self):
        """returns the area value of the Rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """prints the rectangle to stdout using #
        """

        for row in range(self.__height):
            for item in range(self.__width):
                print("#", end="")

            print()

    def __str__(self):
        """provides output for print() and str()
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
