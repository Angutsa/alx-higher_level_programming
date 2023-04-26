#!/usr/bin/python3

"""Defines the MyInt class"""


class MyInt(int):
    """Class inverts the == and != operators"""

    def __eq__(self, num):
        """Inverts the function of == to !="""

        return int(self) != num

    def __ne__(self, num2):
        """Inverts the function of != to =="""

        return int(self) == num2
