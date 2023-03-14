#!/usr/bin/python3

def islower(c):
    char = ord(c)
    if (char >= 97 and char <= 122):
        return (True)
    elif (char >= 65 and char <= 90):
        return (False)
