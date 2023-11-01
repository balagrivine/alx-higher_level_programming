#!/usr/bin/python3

"""Module for text indentation"""

def text_indentation(text):
    """Method for adding 2 new lines

    Args:
        text: the str text

    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raises TypeError("text must be a string")

    for delim in ".?:":
        # prin(delim, text.split(delim))
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ = "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
