#!/usr/bin/python3
"""Square class initialization"""


class Square:
    """initializing the Square

    Args: self-initializing size-int

    """
    def __init__(self, size=0):
        self.size = size

    @Property
    def size(self):
        self.size

    @Setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """returns current square area"""
    def area(self):
        return (self.__size ** 2)
