#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    a_list = list(my_list)
    for index in a_list:
        if index % 2 == 0:
            a_list[index] = True
        else:
            a_list[index] = False
    return a_list
