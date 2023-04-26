#!/usr/bin/python3

"""Contains the BaseGeometry class"""


class BaseGeometry:
    """Defines the class BaseGeometry"""

    def area(self):
        """Calculates the area of the shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value

        Args:
            name (str): name
            value (integer): value to validate
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
