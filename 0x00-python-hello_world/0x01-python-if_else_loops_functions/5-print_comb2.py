#!/usr/bin/python3
numb = 0
while numb <= 99:
    if numb == 99:
        print("{:02}" .format(numb), end = '\n')
    else:
        sep = ', ' if numb <= 98 else '\n'
        print("{:02}" .format(numb), end = sep)
    numb += 1
