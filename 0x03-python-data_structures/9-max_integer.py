#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest_int = 0
    for index in my_list:
        if index > biggest_int:
            biggest_int = index
    return biggest_int
