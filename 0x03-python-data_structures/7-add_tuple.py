#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
    sum1 = int(tuple_a[0]) + int(tuple_b[0])
    sum2 = int(tuple_a[1]) + int(tuple_b[1])

    return ("{} {}" .format(sum1, sum2))

