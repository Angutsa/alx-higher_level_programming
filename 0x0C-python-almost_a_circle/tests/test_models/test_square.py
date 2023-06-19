#!/usr/bin/python3

"""Contains unit tests for the Square class
"""


import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareClass(unittest.TestCase):
    """Tests the Square Class
    """

    def test_initialisation(self):
        """tests the instantiation of Square Class Objects
        """

        my_square = Square(8)

        self.assertEqual(my_square.id, 1)
        self.assertEqual(my_square.height, 8)
        self.assertEqual(my_square.width, 8)
        self.assertEqual(my_square.x, 0)
        self.assertEqual(my_square.y, 0)

        with self.assertRaises(TypeError):
            my_square = Square()

    def test_input_validation(self):
        """tests that all inputs are validated
        """

        with self.assertRaises(TypeError):
            my_square = Square("me")
            my_square = Square(2, "me", 2)
            my_square = Square(2, 2, "me")

        with self.assertRaises(ValueError):
            my_square = Square(-1)
            my_square = Square(1, -1, 1)
            my_square = Square(1, 1, -1)

    def test_encapsulation(self):
        """tests that the correct variables are private and public
        """

        with self.assertRaises(AttributeError):
            my_square = Square(2)

            self.assertRaises(AttributeError, my_square.__width)
            self.assertRaises(AttributeError, my_square.__height)
            self.assertRaises(AttributeError, my_square.__x)
            self.assertRaises(AttributeError, my_square.__y)
            self.assertRaises(AttributeError, my_square.__id)

    def test_inheritance(self):
        """tests that Square inherits from Rectangle
        """

        self.assertIs(issubclass(Square, Rectangle), True)

    def test_area_method(self):
        """Tests that the area method works correctly
        """

        my_square = Square(2, 1, 1)

        self.assertEqual(my_square.area(), 4)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method(self, stdout):
        """Tests that the square is correctly positioned with x and y values
        """

        expected = "\n\n\n  ###\n  ###\n  ###\n"
        my_square = Square(3, 2, 3)
        my_square.display()
        self.assertEqual(stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method_no_xy(self, stdout):
        """Tests that the correct square is displayed without x and y
        """

        expected = "###\n###\n###\n"
        my_square = Square(3)
        my_square.display()
        self.assertEqual(stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_output(self, stdout):
        """Tests that the correct output is produced by __str__
        """

        expected = "[Square] (12) 2/1 - 2\n"

        my_square = Square(2, 2, 1, 12)
        print(my_square)
        self.assertEqual(stdout.getvalue(), expected)

        str(my_square)
        self.assertEqual(stdout.getvalue(), expected)

    def test_update_method(self):
        """Tests that update correctly assigns the arguments passed
        """

        my_square = Square(3, 1, 2, 3)
        my_square.update(89)
        self.assertEqual(my_square.id, 89)

        my_square.update(89, 2)
        self.assertEqual(my_square.width, 2)
        self.assertEqual(my_square.height, 2)

        my_square.update(89, 2, 3)
        self.assertEqual(my_square.x, 3)

        my_square.update(89, 2, 3, 4)
        self.assertEqual(my_square.y, 4)

        my_square.update(75, 10, 5, 7)
        self.assertEqual(my_square.__str__(), "[Square] (75) 5/7 - 10")

        my_square.update(height=1)
        self.assertEqual(my_square.height, 1)

        my_square.update(x=1, height=3, y=2)
        self.assertEqual(my_square.x, 1)
        self.assertEqual(my_square.height, 3)
        self.assertEqual(my_square.y, 2)
        self.assertEqual(my_square.width, 10)

        args = (10, 10, 10, 10)
        kwargs = {"height": 16, "x": 20}
        my_square.update(*args, kwargs)
        self.assertEqual(my_square.__str__(), "[Square] (10) 10/10 - 10")
