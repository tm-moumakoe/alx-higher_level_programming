#!/usr/bin/python3
def no_c(my_string):
    cp = [i for i in my_string if i not in 'cC']
    return "".join(cp)
