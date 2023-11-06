#!/usr/bin/python3

"""A class MyList that inherits from list"""
class MyList(list):
    """Create first instance of MyList"""
    def __init__(self):
        """Args:
            self: instance of the class
        """
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        my_list = sorted(self)
        print(my_list)
