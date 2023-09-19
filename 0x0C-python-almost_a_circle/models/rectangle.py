#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Overrides the __str__ method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
            + f" - {self.width}/{self.height}"

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """Get/set the x value"""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Get/set the y value"""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns the area value of a Rectangle"""
        return self.height * self.width

    def display(self):
        """Prints the Rectangle on stdout using #s"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for height in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the Rectangle"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
