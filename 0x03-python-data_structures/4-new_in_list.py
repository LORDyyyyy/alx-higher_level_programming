#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nlist = my_list.copy()
    
    if idx >= len(my_list) or idx < 0:
        return nlist

    nlist[idx] = element
    return nlist
