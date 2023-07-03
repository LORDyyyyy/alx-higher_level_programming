#!/usr/bin/python3
"""

A  Rectangle

"""


class Rectangle:
    """An empty Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle

        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    @property
    def width(self):
        """ returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width's value

        Args:
            value (int): width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height's value

        Args:
            value (int): height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Gets the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """ Gets the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * self.__height + 2 * self.__width
