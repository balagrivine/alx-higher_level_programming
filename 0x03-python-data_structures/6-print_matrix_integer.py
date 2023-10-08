#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for num in elem:
            print("{:d}" .format(num), end="  " if num != elem[-1] else "")
        print()
