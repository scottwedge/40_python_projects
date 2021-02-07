#!/usr/bin/env python3

# Print welcome header.
# Calculate the first n terms of the Fibonacci sequence.
# Then calculate the ratio of consecutive Fibonacci numbers.
# Which should approach 1.618

print("Welcome to the Fibonacci Calculator App.")
print() # blank line

num = input("How many digits of the Fibonacci Sequence would you likke to compute: ")
num = int(num) # convert input string to integer
print() # blank line

print("The first {} numbers of the Fibonacci sequence are: ".format(num))
