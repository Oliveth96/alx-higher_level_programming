#!/usr/bin/python3
from turtle import home


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return home
    return my_list[idx]
