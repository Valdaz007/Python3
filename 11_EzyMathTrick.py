# Ezy Math Trick is an Exercise
# The Program will let you think of a number
# and lets you do some Math Calculation on
# your number to give you the final answer.

# Not so much of a math trick hey...

import random

print("Welcome To Ezekiel's Brain Thinking Game!\n")
input("\nPress Enter To Continue... ")

print("\nThink Of A Number Less Than 20")
input("Press Enter To Continue... ")

print("\nAdd This Number With Itself")
input("Press Enter To Continue... ")

numberToAdd = random.randrange(0, 100, 2)               # Generates a Random Even Number between 0 and 100

print("\nAdd {} To Your Answer".format(numberToAdd))

input("Press Enter To Continue... ")

print("\nDivide Your Answer By 2")

input("Press Enter To Continue... ")

print("\nMinus Your Answer By The Number You Have Chosen")

input("Press Enter To Continue... ")

numberToAdd /= 2

print("\nYour Answer Is: {}".format(numberToAdd))

print()
