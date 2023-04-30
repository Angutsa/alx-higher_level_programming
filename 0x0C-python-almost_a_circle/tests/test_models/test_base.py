#!/usr/bin/python3

"""Contains unit tests for the base class
"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests the Base Class
    """

    def test_initialisation(self):
        """tests the instantiation of Base Class Objects
        """

        my_base = Base()
        self.assertEqual(my_base.id, 1)

        my_base = Base(52)
        self.assertEqual(my_base.id, 52)
