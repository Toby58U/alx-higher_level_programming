#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element ** 2)
        result_matrix.append(squared_row)
    return result_matrix
