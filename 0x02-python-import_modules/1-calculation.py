#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5


def calc():
    """ Performs in built calculations

        Prints the result of the inbuilt calculations
    """

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if (__name__ == '__main__'):
    calc()
