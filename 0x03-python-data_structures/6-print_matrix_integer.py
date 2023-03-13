#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints an integer matrix
    matrix: matrix to print
    """

    for row in matrix:
        for x in row:
            if (x == (row[len(row) - 1])):
                print("{}".format(x), end="")
            else:
                print("{}".format(x), end=" ")
        print("")
