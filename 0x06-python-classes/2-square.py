#!/usr/bin/python3
# 2-square.py by TM Moumakoe
""" Defines a Square """


class Square:
    """ Represents a Square """
     def __init__(self, size=0):
        """ Initializes the Sqaure class
        Args:
            size (int): size of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = size