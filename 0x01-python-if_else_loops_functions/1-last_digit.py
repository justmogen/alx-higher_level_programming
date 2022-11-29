#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = abs(number) % 10  # absolute value of num mod 10 -> gives last digit

if number < 0:
    lastD = -lastD   # digit changes to negative
print("Last digit of {} is {} and is ".format(number, lastD), end="")

if lastD > 5:
    print("greater than 5")
elif lastD == 0:
    print("0")
else:
    print("less than 6 and not 0")
