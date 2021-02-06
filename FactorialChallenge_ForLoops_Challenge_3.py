#!/usr/bin/env python3

# print Welcome header
# Prompt for factorial number
# Display how that factorial is calculated
# Show result from math library
# Show result from own algorithm.
# Verify that both results are the same.

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

