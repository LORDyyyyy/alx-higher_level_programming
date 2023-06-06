#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    nstr = ''
    while i < len(str):
        if i != n:
            nstr += str[i]
        i += 1
    return nstr
