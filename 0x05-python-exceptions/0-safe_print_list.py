#!/usr/bin/python3
from operator import index


def safe_print_integer(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
        return x
    except IndexError:
        return i
    finally:
        print()
