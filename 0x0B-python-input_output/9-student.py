#!/usr/bin/python3
"""here goes the class"""


class Student:
    """ a student class"""

    def __init__(self, first_name, last_name, age):
        """inti """

        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """retrieves a dictionary representation"""

        return (self.__dict__)
