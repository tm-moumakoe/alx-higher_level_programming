#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
