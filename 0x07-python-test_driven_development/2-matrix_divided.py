#!/usr/bin/python3

"""Contains a divide matrix function

"""


def matrix_divided(matrix, div):
    # Validate input
    not_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(not_matrix)

    if len(matrix) < 2:
        raise TypeError(not_matrix)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(not_matrix)

        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(not_matrix)

    row_length = len(matrix[0])
    for row in matrix:
        if (len(row)) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if div != float('inf') and div == div:
        div = round(div, 2)

    # Actual Division
    matrix_div = []
    index = 0
    for row in matrix:
        matrix_div.append([])
        for item in row:
            quotient = item / div
            if div == div and item == item and float('inf') not in [div, item]:
                quotient = int(quotient)

            matrix_div[index].append(quotient)
        index += 1

    return matrix_div
