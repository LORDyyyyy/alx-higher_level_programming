#!/usr/bin/python3
"""Here goes everything"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
        inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Return private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Set private attribute
        """
        self.__width = value

    @property
    def height(self):
        """
            Return private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Set private attribute
        """
        self.__height = value

    @property
    def x(self):
        """
            Return private attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Set private attribute
        """
        self.__x = value

    @property
    def y(self):
        """
            Return private attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Set private attribute
        """
        self.__y = value
