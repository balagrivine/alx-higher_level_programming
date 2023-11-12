#!/usr/bin/python3
"""import python module Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square that inherits from the class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instance of the class sruare

            Args:
                size: size of the square

        """
        super().__init__(self, self, x=0, y=0, id=None)
        self.size = size

    def area(self):
        """Method that calculates area of a square"""
        return self.size ** 2

    def __str__(self):
        """returns a class in a string format
        """
        return "[square] ({}) {}/{} - {}" .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """returns the current size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """updates the value of width and height to value
            Args:
                value: value for the size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attr = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attr[i], value)

        if kwargs:
            for i, value in kwargs.items():
                if i == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)

                else:
                    setattr(self, i, value)

        def to_dictionary(self):
            """returns the dictionary representation of the square"""
            Dict = {"id":self.id,
                    "x":self.x,
                    "size":self.size,
                    "y":self.y}
            return Dict
