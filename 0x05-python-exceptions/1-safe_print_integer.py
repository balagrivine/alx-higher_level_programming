#!/usr/bin/python3

def safe_print_integer(value):

    try:
        formatted = "{:d}".format(int(value))
        print(formatted)
        return True
    except (ValueError, TypeError):
        return False

