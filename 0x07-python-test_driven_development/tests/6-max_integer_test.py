#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_module_max_integer(self):
        """Test"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 1024, 25]), 1024)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1000, 2, 3, 485]), 1000)
        self.assertEqual(max_integer([1, 2, 300, 4, 89, 99]), 300)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -2, -300, -4, -89, 99]), 99)
        self.assertEqual(max_integer([-1, -2, -300, -4, -89, -99]), -1)
        self.assertEqual(max_integer([15]), 15)
        self.assertRaises(TypeError, max_integer([[]]))
