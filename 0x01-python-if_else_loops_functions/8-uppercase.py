#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            up_char = chr(ord(char) - 32)
            print("{}" .format(up_char), end="")
    print("")
