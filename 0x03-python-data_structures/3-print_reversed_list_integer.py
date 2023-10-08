#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """The function ptints a list in reverse order
    """
    my_list.reverse()

    for i in my_list:
        print("{}" .format(i))
