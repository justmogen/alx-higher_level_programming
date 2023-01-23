#!/usr/bin/python3
"""creating a class square"""


class Square:
    """initialize the square"""
    def __init__(self, size=0):
        """check if size is not integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0)
        self._size = size
