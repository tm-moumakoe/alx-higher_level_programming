#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ A Square with private instance attribute size """
     def __init__(self, size=0):
        """ Initializes a Sqaure instance
        Args:
            size (int): size of the square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = size
