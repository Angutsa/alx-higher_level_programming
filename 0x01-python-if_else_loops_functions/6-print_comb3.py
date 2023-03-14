#!/usr/bin/python3

for x in range(10):
    for y in range(10):
        if (y == x or y < x):
            continue

        print("{}{}".format(x, y), end="")
        if (x == 8 and y == 9):
            print("")
        else:
            print(", ", end="")
