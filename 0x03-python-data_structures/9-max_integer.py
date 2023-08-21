#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    m = -1
    for i in my_list:
        if i > m:
            m = i
        else:
            continue
    return m
