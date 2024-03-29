#!/usr/bin/python3
"""Define the class"""


class Square:
    """Thee Square class

    Args: size of the square

    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of square"""
        return (self.__size * self.__size)
