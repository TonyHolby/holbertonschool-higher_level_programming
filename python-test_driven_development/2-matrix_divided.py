#!/usr/bin/python3
"""
    Divides all elements of the matrix by div.
    
    Parameters:
        matrice (list of list of int/float): The matrix to be divided.
        div (int/float): The divisor.
    
    Returns:
        list of list of float: A new matrix with all elements divided by div
        and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
"""


def matrix_divided(matrix, div):
    """ Returns a new matrix. """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
