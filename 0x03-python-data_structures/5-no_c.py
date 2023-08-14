#!/usr/bin/python3
def no_c(my_string):
    cp = [c for c in my_string if c != 'c' or c!= 'C']
    return ("".join(cp))
