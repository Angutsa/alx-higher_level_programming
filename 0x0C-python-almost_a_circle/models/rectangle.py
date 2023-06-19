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

        for line in range(self.__y):
            print("")

        for row in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")

            for item in range(self.__width):
                print("#", end="")

            print()

    def __str__(self):
        """provides output for print() and str()
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """updates the instance attributes

        function will skip over **kwargs if *args exists and is not empty
        """

        if len(args) <= 0:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = kwargs["width"]
                elif key == "height":
                    self.height = kwargs["height"]
                elif key == "id":
                    self.id = kwargs["id"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

            return

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.height = args[2]

        if len(args) > 3:
            self.x = args[3]

        if len(args) > 4:
            self.y = args[4]
