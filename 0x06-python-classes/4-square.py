#!/usr/bin/python3
"""Square class initialization"""



class Square:
    """creating the class"""

    def __init__(self, size=0):
        """initializing new square and set
        private size object
        size-int

        """
        self.__size = size

    @Property
    """Get and set the size of square"""
    def size(self):
        return self.__size

    #setter checks for errors and modify
    @Setter.of.size
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """returns current square area"""
    def area(self):
        return (self.__size ** 2)
