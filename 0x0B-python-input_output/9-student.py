#!/usr/bin/python3
"""A class Student."""


class Student:
    """Represents a Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student."""
        return self.__dict__
