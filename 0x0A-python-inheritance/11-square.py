#!/usr/bin/python3
"""
class that returns a formatted string
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
rectangle module for inheriatnce
"""


class Square(Rectangle):
    """define a square class
    args:
        Rectangle: parent class
    """
    def __init__(self, size):
        """instantiation method

        Args:
            size: size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

        def area(self):
            """calculates the area of the square

            Returns:
                calcuated area of the square
            """
            return self.__size ** 2
        def __str__(self):
            """returns class instance in string fmt
            """
            return "[square] {}/{}" .format(self.__size, self.__size)
