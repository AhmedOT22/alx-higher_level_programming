#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    pos = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            pos.append(True)
        else:
            pos.append(False)
    return pos
