#!/usr/bin/python3
def fizzbuzz():
    num = 1
    while num <= 100:
        sep = ' ' if num <= 99 else '\n'
        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz", end = sep)
        elif num % 3 == 0:
            print("Fizz", end = sep)
        elif num % 5 == 0:
            print("Buzz", end = sep)
        else:
            print("{}" .format(num), end = sep)
        num += 1
