#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_integer = number % -10
else:
    last_integer = number % -10
print("Last digit of", number, "is", last_integer, end=" ")
if last_integer > 5:
    print("and is greater than 5")
elif last_integer == 0:
    print('and is 0')
else:
    print("and is less than 6 nd not 0")
