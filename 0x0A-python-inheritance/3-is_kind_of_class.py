#!/usr/bin/python3
"""Checks if an object is an instance of a class or an inherited class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class
    or a class that inherits from a_class
    """
    return (isinstance(obj, a_class))
