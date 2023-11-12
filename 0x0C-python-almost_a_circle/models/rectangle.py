#!/usr/bin/python3
"""class rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class rectangle that inherits foem parent class Base"""
    def __init__(self,width, height, x=0, y=0, id=None):
        """python instantiation method"""
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns the current value of the variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """updates the value of the variable widht to th value of value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the current value of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the width to a new width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the current value of the variable x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the current value of the variable x to x"""
        if not isinstance(value, int):
            raise TypeError("x must be an intager")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets and returns current value of the variable x"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the current value of the variable y to y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the retangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle with the character #"""
        rect = []
        for row in range(self.__height):
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overrides the current __str__ method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        arg=["id", "width", "height", "x", "y"]
        for i, j in enumerate(args):
            setattr(self, arg[i], j)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns th rectangle attributes in dictionarry format"""
        Dict = {"x":self.__x,
                "y":self.__y,
                "id":self.id,
                "height":self.__height,
                "width":self.__width}
        return Dict

    def to_csv_row(self):
        """Rectangle method that returns an instance csv data
        Returns: 
            an instance csv data
        """

        return [self.__width, self.__height, self.__x, self.__y, self.id]
