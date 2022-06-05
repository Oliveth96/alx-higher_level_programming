#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    index_count = 0
    for index in new_list:
        if index == 'c' and index == 'C':
            new_list[index_count] = ""
        index_count += 1
    return "".join(new_list)
