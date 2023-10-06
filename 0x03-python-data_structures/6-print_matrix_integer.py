#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        row = ""
        for num in elem:
            row += "{} " .format(num)
        print("{}" .format(row))
