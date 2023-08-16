#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    sum_u = 0
    for n in set1:
        sum_u += n
    return sum_u
