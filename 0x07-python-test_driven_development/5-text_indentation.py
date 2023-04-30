#!/usr/bin/python3

"""Module contains a function that adds a new line in text"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' or ':'

    Args:
        text (str): text to be parsed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = ""
    for letter in text:
        if letter in [".", "?", ":"]:
            new_text = new_text + "{}\n\n".format(letter)
        else:
            new_text = new_text + letter

    if new_text[-2:] == "\n ":
        new_text = new_text[0:-2]

    new_text = new_text.replace("\n\n ", "\n\n")

    print(new_text, end="")
