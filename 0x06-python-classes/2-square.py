#!/usr/bin/python3
# 2-square.py by TM Moumakoe
""" Defines a Square """


class Square:
    """ A class representing a Square

    Attributes:
        __size (int): size of a Square
    """
    def __init__(self, size):
        """ Initializes Square class

        Args:
            size (int): size of defined Square

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('soze must be >= 0')
        else:
            self.__size = size
