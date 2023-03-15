#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Squares all elements in a matrix"""
    new_matrix = []
    for row in matrix:
        p = []
        for x in row:
            p.append(x ** 2)
        new_matrix.append(p)
    return (new_matrix)
