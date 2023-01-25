#!/usr/bin/python3
"""creating a Square class"""


class Square:
    def __init__(self, size=0):
        """initialization

        Args: size-int
        """
       self.__size = size

    #Retriever
    @Property
    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(size):
        """returns the current square area **2 """
        return (self.__size ** 2)

    def my_print(self):
        size = self.__size

        if size == 0:
            print()

        for x in range(size):
            print('#' * size)
