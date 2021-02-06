#!/usr/bin/env python3

# print Welcome header
# Prompt for factorial number
# Display how that factorial is calculated
# Show result from math library
# Show result from own algorithm.
# Verify that both results are the same.

# Import modules
import math

# Functions
def fact(n):
    product = 1
    for j in range(1, n+1):
        product = product * j
    return product


print("Welcome to the Factorial Calculator App.")
print() # blank line

fact_str = input("What number would you like to compute the factorial of? ")
fact_num = int(fact_str) # convert input string type to integer type

# Create factorial string then print it
f_string = ""
for j in range(1, fact_num): 
    f_string = f_string + str(j) + "*"  # create string of 1*2*3*...* 
f_string = f_string + str(fact_num)   # add final value of fact_num to string
print("{}! = {}".format(fact_str, f_string))

# Use math library to calculate factorial
print() # blank line
print("Here is the result from the math library:")
print("The factorial of {} is {}!".format(fact_str, math.factorial(10)))

# Calculate using own function and display result
print() # blank line
print("Here is the result from my own algorithm:")
print("The factorial of {} is {}!".format(fact_str, fact(fact_num)))
