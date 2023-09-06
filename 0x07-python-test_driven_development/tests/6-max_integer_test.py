#!/usr/bin/python3
#6-max_integer_test.py by TM Moumakoe
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def ordered_list(self):
        """Test an ordered list of integers."""
        ol = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ol), 5)

    def unordered_list(self):
        """Test an unordered list of integers."""
        ul = [1, 2, 4, 3, 5]
        self.assertEqual(max_integer(ul), 5)

    def max_at_begginning(self):
        """Test a list with a beginning max value."""
        mab = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(mab), 5)

    def empty_list(self):
        """Test an empty list."""
        el = []
        self.assertEqual(max_integer(el), None)

    def one_lmnt(self):
        """Test a list with one element."""
        lmnt = [5]
        self.assertEqual(max_integer(lmnt), 5)

    def floats(self):
        """Test a list of floats."""
        fl = [8.30, 6.64, -5.38, 18.52, 9.0]
        self.assertEqual(max_integer(fl), 18.52)

    def ints_floats(self):
        """Test a list of integers and floats."""
        ifl = [18.03, 16, -8.94, 5, 16]
        self.assertEqual(max_integer(ifl), 18.03)

    def string(self):
        """Test a string."""
        s = "Brennan"
        self.assertEqual(max_integer(s), 'r')

    def list_of_strings(self):
        """Test a list of strings."""
        sl = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(sl), "name")

    def empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
