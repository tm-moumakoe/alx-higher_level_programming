#!/usr/bin/python3
"""Defines a function that multiplies two matrices by with the NumPy module."""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy

    Args:
        m_a (matrix): first matrix
        m_b (matrix): second matrix

    Returns:
        matrix: the product of the two matrices.
    """
    return np.matmul(m_a, m_b)
