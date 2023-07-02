#!/usr/bin/python3
"""Module add-integer

Adds two integer together

"""


def add_integer(a, b=98):
    """Returns a + b

    Calculates the addition of two numbers.
    
    Args:
        a (int): first number.
        b (int): second number.
    
    Returns:
        int: The result of the addition.
    
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
