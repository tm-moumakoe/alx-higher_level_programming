#!/usr/bin/python3
"""A function that returns the description of an object's JSON serialization"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    return obj.__dict__
