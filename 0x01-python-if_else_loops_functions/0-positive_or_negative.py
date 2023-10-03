#!/usr/bin/python3
import random
number = random.randint(-10, 10)
res = ""
if number > 0:
    res = "{} is positive\n" .format(number)
elif number < 0:
    res = "{} is negative\n" .format(number)
else:
    res = "{} is zero\n" .format(number)
print("{}" .format(res))
