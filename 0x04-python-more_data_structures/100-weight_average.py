#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0
    for t in my_list:
        numerator += t[0] * t[1]
        denominator += t[1]
    return numerator/denominator
