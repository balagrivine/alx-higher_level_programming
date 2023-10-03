#!/usr/bin/python3

a = ord('a')
while a <= ord('z'):
    if a != ord('e') and a != ord('q'):
        print(chr(a), end = ' ')
    a += 1
