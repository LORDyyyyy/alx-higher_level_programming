#!/usr/bin/python3
"""

A  Rectangle

"""


class Rectangle:
    """An empty Rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1

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

    def print_rect(self):
        """ prints the rectangle"""

        w = self.__width
        h = self.__height
        rect = ""

        if w == 0 or h == 0:
            return rect

        for i in range(h):
            for j in range(w):
                rect += str(self.print_symbol)
            if i != h - 1:
                rect += '\n'

        return rect

    def __str__(self):
        """returns a string, the rectangle itself"""

        return self.print_rect()

    def __repr__(self):
        """ returns the representation of the rectangle"""

        w = self.__width
        h = self.__height

        return "Rectangle({}, {})".format(w, h)

    def __del__(self):
        """deletes the instance and sends a message"""

        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        """Compares between two rectangles

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        """

        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        r1_a = rect_1.area()
        r2_a = rect_2.area()

        if r1_a >= r2_a:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """makes a square"""

        return cls(size, size)
