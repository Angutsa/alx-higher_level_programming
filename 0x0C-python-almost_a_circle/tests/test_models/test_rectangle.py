#!/usr/bin/python3

"""Contains unit tests for the Rectangle class
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Tests the Rectangle Class
    """

    def test_initialisation(self):
        """tests the instantiation of Rectangle Class Objects
        """

        my_rect = Rectangle(8, 5)

        self.assertEqual(my_rect.id, 1)
        self.assertEqual(my_rect.height, 5)
        self.assertEqual(my_rect.width, 8)
        self.assertEqual(my_rect.x, 0)
        self.assertEqual(my_rect.y, 0)

        with self.assertRaises(TypeError):
            my_rect = Rectangle()
            my_rect = Rectangle(2)

    def test_input_validation(self):
        """tests that all inputs are validated
        """

        with self.assertRaises(TypeError):
            my_rect = Rectangle("me", 2)
            my_rect = Rectangle(2, "me")
            my_rect = Rectangle(2, 2, "me", 2)
            my_rect = Rectangle(2, 2, 2, "me")

        with self.assertRaises(ValueError):
            my_rect = Rectangle(-1, 2)
            my_rect = Rectangle(1, -2)
            my_rect = Rectangle(1, 2, -1, 1)
            my_rect = Rectangle(1, 2, 1, -1)

    def test_encapsulation(self):
        """tests that the correct variables are private and public
        """

        with self.assertRaises(AttributeError):
            my_rect = Rectangle(2, 3)

            self.assertRaises(AttributeError, my_rect.__width)
            self.assertRaises(AttributeError, my_rect.__height)
            self.assertRaises(AttributeError, my_rect.__x)
            self.assertRaises(AttributeError, my_rect.__y)
            self.assertRaises(AttributeError, my_rect.__id)

    def test_inheritance(self):
        """tests that Rectangle inherits from Base
        """

        self.assertIs(issubclass(Rectangle, Base), True)
