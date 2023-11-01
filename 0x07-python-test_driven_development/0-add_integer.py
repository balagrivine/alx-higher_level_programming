#!/usr/bin/python3
"""defines an integer addition function"""

def add_integer(a, b=98):
    """
        add_integer: adds two integers

        Floats are type casted into ints

        Raises:
            TypeError: if either a bor b is non int or non-float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
