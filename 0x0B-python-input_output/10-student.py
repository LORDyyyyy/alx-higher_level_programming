#!/usr/bin/python3
"""here goes the class"""


class Student:
    """ a student class"""

    def __init__(self, first_name, last_name, age):
        """inti """

        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attr is None:
            return (self.__dict__)
        else:
            dict = {}
            for i in attrs:
                if hasattr(self, i):
                    dict[i] = getattr(self, i)
            return dict
