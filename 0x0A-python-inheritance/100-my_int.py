#!/usr/bin/python3
"""Defines a subclass of int called MyInt that inverts == & !="""


class MyInt(int):
    """Represents MyInt"""
    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
