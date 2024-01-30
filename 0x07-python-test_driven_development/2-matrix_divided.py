#!/usr/bin/python3
"""
Module 2-matrix_divided
A matrix divider function

"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    mtype = "matrix must be a matrix (list of lists) of integers/floats"
    msize = "Each row of the matrix must have the same size"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix) is not list or matrix == []:
        raise TypeError(mtype)
    else:
        for row in matrix:
            if len(row) == len(matrix[0]):
                pass
            else:
                raise TypeError(msize)
        for row in matrix:
            for elem in row:
                if type(elem) is not int and type(elem) is not float:
                    raise TypeError(mtype)
        mat = matrix
        return\
            list(map(lambda i: list(map(lambda x: round(x/div, 2), i)), mat))
