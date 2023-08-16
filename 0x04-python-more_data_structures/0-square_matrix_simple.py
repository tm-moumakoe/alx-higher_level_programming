#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = matrix.copy()
    for idx in range(len(matrix)):
        matrix1[idx] = list(map(lambda n: n**2, matrix[idx]))
    return matrix1
