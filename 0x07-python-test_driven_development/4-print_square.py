#!/usr/bin/python3
"""this function will print a square with character #"""


def print_square(size):
    """
    size: size must be an integer, otherwise raise a
        TypeError exception with the message size must be an integer

    If size < 0:
        ValueError: size must be >= 0
    If size is a float and is less than 0, raise a
        TypeError exception with the message size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
