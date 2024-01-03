#!/usr/bin/python3
"""This module contains a function that multiplies 2 matrices by using the module NumPy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """This is a function that multiplies 2 matrices by using the module NumPy
    Arguments:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Returns:
        a new matrix which is the multiplication of m_a and m_b.
    """

    return (np.matmul(m_a, m_b))
