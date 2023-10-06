#!/usr/bin/python3

def no_c(my_string):
    res = ""
    for char in my_string:
        if char not in ('C', 'c'):
            res += char
    return res
