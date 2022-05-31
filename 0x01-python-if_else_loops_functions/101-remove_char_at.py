#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    for i, c in enumerate(str):
        if i != n:
            newstring += c
    return newstring
