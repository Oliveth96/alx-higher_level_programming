#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    a_list = list(my_list)
    for i in a_list:
        if i % 2 == 0:
            a_list[i] = True
        else:
            a_list[i] = False
    return a_list
