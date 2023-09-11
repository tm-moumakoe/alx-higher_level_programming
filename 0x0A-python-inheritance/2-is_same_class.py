#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of the a_class, otherwise false"""
    return (type(obj) == a_class)
