#!/usr/bin/python3
"""write function"""


def append_write(filename="", text=""):
    """function that appends text to a file
    Args:
        filename: name of the file
        text: text to be appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        written = file.write(text)
        return written
