#!/usr/bin/python3
__author__ = 'syurskyi'

# input is a string unless converted
x = int(input("Give me a number "))

if (x < 1):
    print("Too little")
elif (x >= 1 and x <= 10):
    print("Just about right")
else:
    print("Too high")

