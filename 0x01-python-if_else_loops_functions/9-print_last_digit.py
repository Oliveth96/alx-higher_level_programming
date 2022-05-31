#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_integer = number % 10
    elif number < 0:
        last_integer (number * -1) % 10

    print(last_integer, end='')
    return last_integer
