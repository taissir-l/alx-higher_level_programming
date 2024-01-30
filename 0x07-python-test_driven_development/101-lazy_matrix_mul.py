#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
function using NumPy to multply matrixes.

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function to return multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    """

    return (np.matmul(m_a, m_b))
