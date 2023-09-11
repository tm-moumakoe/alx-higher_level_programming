#!/usr/bin/python3
"""Checks if an object is an instance of a subclass of the specified class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass
    (directly or indirectly) of the specified class; otherwise False
    """
    return  (type(obj) != a_class) and (issubclass(type(obj), a_class))
