#!/usr/bin/python3

"""Contains unit tests for the Rectangle class
"""


import unittest
from unittest.mock import patch
from io import StringIO
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

        my_rect2 = Rectangle(9, 6)
        self.assertEqual(my_rect2.id, 2)
        self.assertEqual(my_rect2.height, 6)
        self.assertEqual(my_rect2.width, 9)
        self.assertEqual(my_rect2.x, 0)
        self.assertEqual(my_rect2.y, 0)


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

    def test_area_method(self):
        """Tests that the area method works correctly
        """

        my_rect = Rectangle(2, 3, 1, 1)

        self.assertEqual(my_rect.area(), 6)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method(self, stdout):
        """Tests that the rectangle is correctly positioned with x and y values
        """

        expected = "\n\n\n  ###\n  ###\n  ###\n  ###\n"
        my_rect = Rectangle(3, 4, 2, 3)
        my_rect.display()
        self.assertEqual(stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method_no_xy(self, stdout):
        """Tests that the correct rectangle is displayed without x and y
        """

        expected = "###\n###\n###\n###\n"
        my_rect = Rectangle(3, 4)
        my_rect.display()
        self.assertEqual(stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_output(self, stdout):
        """Tests that the correct output is produced by __str__
        """

        expected = "[Rectangle] (12) 2/1 - 2/3\n"

        my_rect = Rectangle(2, 3, 2, 1, 12)
        print(my_rect)
        self.assertEqual(stdout.getvalue(), expected)

        str(my_rect)
        self.assertEqual(stdout.getvalue(), expected)

    def test_update_method(self):
        """Tests that update correctly assigns the arguments passed
        """

        my_rect = Rectangle(3, 4, 1, 2, 3)
        my_rect.update(89)
        self.assertEqual(my_rect.id, 89)

        my_rect.update(89, 2)
        self.assertEqual(my_rect.width, 2)

        my_rect.update(89, 2, 3)
        self.assertEqual(my_rect.height, 3)

        my_rect.update(89, 2, 3, 4)
        self.assertEqual(my_rect.x, 4)

        my_rect.update(89, 2, 3, 4, 5)
        self.assertEqual(my_rect.y, 5)

        my_rect.update(75, 10, 10, 5, 7)
        self.assertEqual(my_rect.__str__(), "[Rectangle] (75) 5/7 - 10/10")

        my_rect.update(height=1)
        self.assertEqual(my_rect.height, 1)

        my_rect.update(x=1, height=3, y=2)
        self.assertEqual(my_rect.x, 1)
        self.assertEqual(my_rect.height, 3)
        self.assertEqual(my_rect.y, 2)
        self.assertEqual(my_rect.width, 10)

        args = (10, 10, 10, 10, 10)
        kwargs = {"height": 16, "x": 20}
        my_rect.update(*args, kwargs)
        self.assertEqual(my_rect.__str__(), "[Rectangle] (10) 10/10 - 10/10")
