#!/usr/bin/python3

def multiple_returns(sentence):
    if (len(sentence) == 0):
        char1 = None
    else:
        char1 = sentence[0]
    return (len(sentence), char1)
