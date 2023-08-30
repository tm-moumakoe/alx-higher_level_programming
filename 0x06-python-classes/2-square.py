#!/usr/bin/python3
# 2-square.py by TM Moumakoe
"""Defines a class Square"""


class Square:
    """Represents a Square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
