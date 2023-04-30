#!/usr/bin/python3

"""Contains unit tests for the base class
"""


import unittest
import sys
sys.path.append("/home/angutsa/alx-higher_level_programming/0x0C-python-almost_a_circle/models")
from base import Base

class TestBaseClass(unittest.TestCase):
    def test_initialisation(self):
        """tests the instantiation of Base Class Objects
        """

        my_base = Base()
        self.assertEqual(my_base.id, 1)

        my_base = Base(52)
        self.assertEqual(my_base.id, 52)
