#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([1, 2, -3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_different_list_types(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
