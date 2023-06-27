#!/usr/bin/python3

"""Square Class

Class Square that defines a square

"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Initialize a squre
         Args:
            size (int): the size of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        # self.size = size

    @property
    def size(self):
        """return the size value"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size
        Args:
            value (int) : the value which will be set to the size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print('')
