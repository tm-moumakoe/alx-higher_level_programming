#!/usr/bin/python3
def r_sub(n_list):
    n_sub = 0
    m_list = max(n_list)
    for n in n_list:
        if m_list > n:
            n_sub += n
    return (m_list - n_sub)

def roman_to_int(roman_string):
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    num = 0
    r_last = 0
    n_list = [0]

    for ch in roman_string:
        for r_num in r_dict:
            if r_num == ch:
                if r_dict.get(ch) <= r_last:
                    num += r_sub(n_list)
                    n_list = [r_dict.get(ch)]
                else:
                    n_list.append(r_dict.get(ch))
                r_last = r_dict.get(ch)
    num += r_sub(n_list)
    return num
