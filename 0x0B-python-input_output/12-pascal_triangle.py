#!/usr/bin/python3
"""A Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n."""
    if n <= 0:
        return []

    ret = [[1]]
    while len(ret) != n:
        t_li = ret[-1]
        tmp = [1]
        for i in range(len(t_li) - 1):
            tmp.append(t_li[i] + t_li[i + 1])
        tmp.append(1)
        ret.append(tmp)
    return ret
