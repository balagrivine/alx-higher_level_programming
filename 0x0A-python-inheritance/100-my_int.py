#!/usr/bin/python3
"""python class that inverts == and !=
"""


class MyInt(int):
    """inherits from int

    Args:
        int: python object
    """
    def __eq__(self, value):
        """equal to command

        Args:
        value: value to be compared
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """not-equal method

        Args:
            value: value to be compared

        """
        return super().__eq__(value)
