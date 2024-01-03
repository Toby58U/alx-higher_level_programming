#!/usr/bin/python3
"""This is a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """This divides all elements of a matrix.
    Arguments:
        matrix (list):  must be a list of lists of integers or floats.
        div: must be a number (integer or float).
    Raises:
        TypeError: if matrix contains nonnumbers,  with the message: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: if matrix contains rows of different sizes, with the message: Each row of the matrix must have the same size.
        TypeError: if div is not an integer or a float, with the mesage: div must be a number.
        ZeroDivisionError: if div is equal to zero, with the message: division by zero.
    Returns:
        A new matrix representing the result of the division rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix) or not all((isinstance(ele, int) or isinstance(ele, float)) for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)

    return (result_matrix)
