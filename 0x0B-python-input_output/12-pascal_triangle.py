#!/usr/bin/python3

"""Contains a function to return Pascal's triangle
"""


def pascal_triangle(n):
    """returns a representation of Pascal’s triangle of n

    Args:
        n (int): levels of Pascal's triangle to return
    """

    triangle = []
    last_level = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
            last_level = [1]
        else:
            new_list = []
            prev_num = 0
            next_num = 0
            j = 0

            for j in range(len(last_level)):
                if j == 0:
                    prev_num = 0
                    next_num = last_level[j]
                else:
                    prev_num = last_level[j - 1]
                    next_num = last_level[j]

                new_list.append(next_num + prev_num)

            new_list.append(last_level[-1])
            triangle.append(new_list)
            last_level = new_list

    return triangle
