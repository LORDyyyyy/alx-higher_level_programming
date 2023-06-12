#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if idx >= size or idx < 0:
        return my_list
    nlist = []
    i = 0
    flag = False
    while i < size:
        if i != idx:
            flag = True
            nlist.append(my_list[i])
        else:
            my_list[i] = None
        i += 1
    my_list.remove(None)
    return nlist
