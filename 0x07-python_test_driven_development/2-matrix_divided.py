#!/usr/bin/python3
"""divides all elemnts of a matrix"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    
    Args:
        matrix: list if ints ar floats
        div: number to be used for division

    Raises:
        TypeError: if a non-int or non-float is encountered
        TypeError: ech row of a matrix must have the same size
        TypeError: if div is not a number(float or int)

    Return:
        a new matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integer or floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of a matrix must have the same size")

        for x in row:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
