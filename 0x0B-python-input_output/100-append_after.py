#!/usr/bin/python3
""" here goes the function"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file"""

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
