#!/usr/bin/python3
def magic_calculation(a, b):
    product = 0
    for i in range(2, 4):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                product += (a ** b) / i
        except:
            product = b + a
            break
    return product
