#!/usr/bin/python3
"""function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    test: must be a string
        TypeError: text must be a string
    NO space at beginning or end of each printed line
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = ""
    for char in text:
        new_line += char
        if char in ".?:":
            new_line += "\n\n"

    print(new_line)
