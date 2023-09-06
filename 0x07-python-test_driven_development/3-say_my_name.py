#!/usr/bin/python3
"""Defines a function that prints first and last names."""


def say_my_name(first_name, last_name=""):
    """Prints first name and last name.

    Args:
        first_name (str): first name.
        last_name (str): last name.

    Raises:
            TypeError: first_name must be a string or
                    last_name must be a string.
    """
    if not first_name or not last_name:
        raise ValueError("first_name OR last_name cannot be empty.")
    if (type(first_name) is not str) or (type(last_name) is not str)):
        raise TypeError(
            "first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
