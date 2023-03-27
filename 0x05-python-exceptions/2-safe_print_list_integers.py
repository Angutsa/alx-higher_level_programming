#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""

    count = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            count = count + 1
        except TypeError:
            continue
        except ValueError:
            continue

    print("")
    return (count)
