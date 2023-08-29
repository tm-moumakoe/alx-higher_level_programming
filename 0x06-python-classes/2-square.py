#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ A Square with private instance attribute size """
     def __init__(self, size=0):
        """ Initialzes a Sqaure instance
        Args:
            size (int): size of the square.
        """
        self.__size = size
