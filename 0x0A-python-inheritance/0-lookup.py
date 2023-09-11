#!/usr/bin/python3
"""Function that returns a list of available attributes and methods"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return (dir(obj))
