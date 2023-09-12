#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing search_string in a file."""
    text = ""
    with open(filename) as fr:
        for line in fr:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fw:
        fw.write(text)
