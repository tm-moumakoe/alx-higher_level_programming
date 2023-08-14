#!/usr/bin/env python3
def no_c(my_string):
    cp = [c for c in my_string if c not in 'cC']
    return ''.join(cp)
