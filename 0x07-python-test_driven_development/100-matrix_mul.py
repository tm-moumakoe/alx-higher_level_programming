#!/usr/bin/python3
"""Defines a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (matrix): first matrix.
        m_b (matrix): second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If one element of those list of lists is not an integer
        or a float.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b is not a rectangle (all ‘rows’ should be,
        of the same size).
        ValueError: If m_a and m_b can’t be multiplied.

    Returns:
        matrrix: Product of the two matrices.
    """
    lerr = "{} must be a list of lists"
    eerr = "{} can't be empty"
    terr = "{} should contain only integers or floats"
    serr = "each row of {} must be of the same size"
    verr = "{} and {} can't be multiplied"

    if (type(m_a) is not list) or (type(m_b) is not list):
        string = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError("{} must be a list".format(string))

    for element in m_a:
        if type(element) is not list:
            raise TypeError(lerr.format('m_a'))

    for element in m_b:
        if type(element) is not list:
            raise TypeError(lerr.format('m_b'))

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError(eerr.format('m_a'))

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError(eerr.format('m_b'))

    for element in m_a:
        for item in element:
            if not type(item) in (int, float):
                raise TypeError(terr.format('m_a'))

    for element in m_b:
        for item in element:
            if not type(item) in (int, float):
                raise TypeError(terr.format('m_b'))

    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])

    for element in m_a:
        if len_m_a != len(element):
            raise TypeError(serr.format('m_a'))

    for element in m_b:
        if len_m_b != len(element):
            raise TypeError(serr.format('m_b'))

    if len_m_a != len(m_b):
        raise ValueError(verr.format('m_a', 'm_b'))

    new_matrix = [[0 for a in m_b[0]] for x in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
