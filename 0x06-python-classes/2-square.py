#!/usr/bin/python3
"""creating a class square"""


class Square:
    """form the square"""

    def __init__(self, size=0):
        """check if size is not integer
        args: taking size as input and should be an ionteger

        """

       if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
