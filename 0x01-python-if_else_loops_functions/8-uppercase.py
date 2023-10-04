#!/usr/bin/python
def uppercase(str):
    for char in str:
        sep = '\n' if char == '\0' else ''
        if 'a' <= char <= 'z':
            up_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}" .format(up_char), end=sep)
        else:
            print("{}" .format(char), end=sep)
