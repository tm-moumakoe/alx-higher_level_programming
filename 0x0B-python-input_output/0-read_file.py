#!/usr/bin/python3
"""Defines a function that reads a text file."""


def read_file(filename=""):
    """Prints the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
