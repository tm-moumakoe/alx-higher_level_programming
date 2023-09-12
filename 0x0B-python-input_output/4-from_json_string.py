#!/usr/bin/python3
"""Defines a function that converts a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
