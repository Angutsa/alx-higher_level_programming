#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""

    count = 0
    try:
        for item in range(x):
            print(f"{my_list[item]}", end="")
            count = count + 1

    except Exception:
        return

    finally:
        print("")
        return (count)
