#!/usr/bin/python3
import random
number = random.randint(-10, 10)
res = ""
if number > 0:
    res = "{} is positive" .format(number)
elif number < 0:
    res = "{} is negative" .format(number)
else:
    res = "{} is zero" .format(number)
print(res)
