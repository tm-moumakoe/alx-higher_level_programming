#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ A square with private instance attribute size """
    def __init__(self, size):
        """ Initializes Square class
        Args:
            size (int): size of defined Square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('soze must be >= 0')
        self.__size = size
