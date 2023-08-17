#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_list = list(a_dictionary.keys())
    for v_dict in k_list:
        if value == a_dictionary.get(v_dict):
            del a_dictionary[v_dict]
    return a_dictionary
