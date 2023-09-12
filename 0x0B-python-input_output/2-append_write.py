#!/usr/bin/python3
"""Defines a function that appends to a file."""


def append_write(filename="", text=""):
    """Appends text to the end of filename."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
