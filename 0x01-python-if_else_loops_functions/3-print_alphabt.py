#!/usr/bin/python3

a = ord('a')
while a <= ord('z'):
    if a != ord('e') and a != ord('q'):
        print("{}" .format(chr(a)), end = '')
    a += 1
