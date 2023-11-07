#!/usr/bin/python3
"""write a python function"""


def read_file(filename=""):
    """a funciton that reds a text file
    Args:
        name of the file to be read from
    """
    with open(filename, encoding="utf-8") as file:

        for line in file:
            print("{}" .format(line), end="")
