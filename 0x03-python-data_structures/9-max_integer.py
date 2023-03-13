#!/usr/bin/python3

def max_integer(my_list=[]):
    a = my_list[0]

    for x in my_list[1:]:
        if (x > a):
            a = x
    return (a)
