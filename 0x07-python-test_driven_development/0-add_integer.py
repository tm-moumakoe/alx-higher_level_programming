#!/usr/bin/python3
"""Defines a function that adds two integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers

    Floating point arguments are cast to
    integers before addition is performed

    Raises:
        a TypeError if either argument is neither a float nor a int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
