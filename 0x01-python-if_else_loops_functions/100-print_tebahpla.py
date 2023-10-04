#!/usr/bin/python3

a = 0
for i in range(ord('z'), ord('A') - 1, -1):
    print("{}" .format(chr(i)), end='')
    a = 32 if a == 0 else 0
