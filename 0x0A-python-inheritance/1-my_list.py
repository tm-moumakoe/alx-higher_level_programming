#!/usr/bin/python3
"""Defines a class ``MyList`` that will inherit from ``list``"""


class MyList():
    """Prints a sorted list in ascending order for the ``list`` class"""
    def print_sorted(self):
        """Prints a sorted list (in ascending order)"""
        print(sorted(self))
