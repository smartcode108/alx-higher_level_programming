#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number > 0:
    lastDigit = number % 10
elif number < 0:
    lastDigit = (-1 * number) % 10
print(f"Last digit of {number} is", end=" ")
if lastDigit > 5:
    print(f"{lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(f"{lastDigit} and is 0")
elif lastDigit < 6 and lastDigit != 0:
    print(f"{lastDigit} and is less than 6 and not 0")
