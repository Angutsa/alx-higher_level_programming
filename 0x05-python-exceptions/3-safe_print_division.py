#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result"""

    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return (quotient)
