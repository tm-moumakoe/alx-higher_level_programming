#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        ret = add(a, b)
        for i in range(4, 6):
            ret = add(ret, i)
            return ret
        else:
            return sub(a, b)
