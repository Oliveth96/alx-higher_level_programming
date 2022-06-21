#!/usr/bin/python3
def safe_print_integer(my_list=[], x=0):
    '''print at most x items from a list'''
    try:
        for i in range(x):
            print(my_list[i], end='')
        return x
    except IndexError:
        return i
    finally:
        print()
