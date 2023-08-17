#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dict = dict(sorted(a_dictionary.items()))
    for i in s_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
