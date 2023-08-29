#!/usr/bin/python3
# 2-square.py by TM Moumakoe
""" A module that defines a Square """


class Square:
    """ Represents a Square

    Attributes:
        __size (int): size of a Square
    """
    def __init__(self, size=0):
        """ Initializes the Sqaure class
        Args:
            size (int): size of a Square
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = size
