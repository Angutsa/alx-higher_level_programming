#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    a1, a2 = 0, 0
    b1, b2 = 0, 0

    if (len_a == 1):
        a1 = tuple_a[0]
    elif (len_a != 0):
        a1, a2 = tuple_a

    if (len_b == 1):
        b1 = tuple_b[0]
    elif (len_b != 0):
        b1, b2 = tuple_b

    return (a1+b1, a2+b2)
