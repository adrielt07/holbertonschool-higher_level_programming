#!/usr/bin/python3
"""
matrix_divided - divides all elements in a matrix.
def(s):
1) matrix_divided
"""

def matrix_divided(matrix, div):
    """
    Divides elems in the matrix by div and returns a new list

    args:
    matrix - takes a matrix (list of lists)
    Requirements:
    1) Elements in the matrix should be a list
    2) Elements in the list  should be int or floats
    2) Lists in the matrix should have the same length

    div - number to multiply by (can't be zero)
    Requirements:
    1) Must be a number
    2) Can't be zero

    Failure to meet the requirements will raise an exception error

    Return:
    new matrix with quotient (rounded in two decimal places max)
    """
    new_list = []
    ex_list = []

    if div is 0:
        raise ZeroDivisionError("division by zero")
    elif isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    for idx in range(len(matrix)):
        if idx > 0:
            if len(matrix[idx]) != len(matrix[idx-1]):
                raise TypeError("Each row of the matrix"
                                " must have the same size")
        elif isinstance(matrix[idx], list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")
    for elem in matrix:
        ex_list = []
        for elm in elem:
            if isinstance(elm, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
            ex_list.append(round(elm / div, 2))
        new_list.append(ex_list)

    return new_list
