#!/usr/bin/python3
"""write a python function"""


def write_file(filename="", text=""):
    """a functions that writes text to a  file

    Args:
        filename: name of the file
        text: text to be writen to the fiel
    """

    with open(filename, "w", encoding="utf-8") as myFile:
        written = myFile.write(text)
        return written
