#!/usr/bin/python3
"""Here goes everything"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
        inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        self.valid_attr("width", value)
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
        self.valid_attr("height", value)
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
        self.valid_attr("x", value)
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
        self.valid_attr("y", value)
        self.__y = value

    @staticmethod
    def valid_attr(attr_name, value):
        """Check the type and the value for every setter method
        Args:
            attr_name (str): name of the attribute
            value (int): attribute value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr_name))

        if attr_name in ['width', 'height']:
            if value <= 0:
                raise ValueError("{} must be > 0".format(attr_name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr_name))

    def area(self):
        """Returns the area of the rectangle"""

        return (self.height * self.width)

    def display(self):
        """prints in stdout the Rectangle"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
            overriding the __str__ method
            return:
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """updates the values"""

        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """save as dict"""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
