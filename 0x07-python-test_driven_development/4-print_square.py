#!/usr/bin/python3
"""Defines a function that prints a square of specific size"""


def print_square(size):
    """Prints a square using the # character
    Arguments:
        size: the length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        print("#" * size)
