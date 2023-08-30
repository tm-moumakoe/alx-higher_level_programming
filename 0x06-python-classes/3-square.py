#!/usr/bin/python3
# 3-square.py by TM Moumakoe
"""Defines a class Square"""


class Square:
    """Represents a Square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the Square

        Args:
            size (int): size of a side of the Square

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

    def area(self):
        """Computes the Square's area

        Returns:
            The area of the square
        """
        return self.__size ** 2
