#!/usr/bin/python3
"""Defines a function that divides a matrix by a specified value."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): divisor

    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if rows are not the same size
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0

    Returns:
        matrix: A result of the division.
    """
    row_size = None
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or (type(matrix) is not list):
        raise TypeError(message)

    for row in matrix:
        if not row or (type(row) is not list):
            raise TypeError(message)

        for i in row:
            if (type(i) is not int) and (type(i) is not float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]

    return new_matrix
