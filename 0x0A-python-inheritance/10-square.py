#!/usr/bin/python3
"""class that gets the area of a square"""

Rectangle = __import__('9-rectangle').Rectangle

"""
rectangle module for inheritance
"""

class Square(Rectangle):
    """square class defining a square

    Args:
        Rectangle: parent class
    """

    def __init__(self, size):
        """python instantiation

        Args:
            size: size of the squuarw
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area of the square

        Returns:
            calculated area
        """

        return self.__size ** 2
