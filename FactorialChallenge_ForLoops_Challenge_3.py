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
def calc_my_fact(n):
    product = 1
    for j in range(1, n+1):
        product = product * j
    return product

def test_calc_my_fact():
    assert calc_my_fact(5) == 120

def calc_math_fact(fact_num):
    return math.factorial(fact_num)

def test_calc_math_fact():
    assert calc_math_fact(6) == 720

def make_f_string(fact_num):
    f_string = "1"
    for j in range(2, fact_num + 1): 
        f_string = f_string + "*" + str(j)   # create string of 1*2*3*...* 
    return f_string

def test_make_f_string():
    assert make_f_string(10) == "1*2*3*4*5*6*7*8*9*10"

def main():
    print("Welcome to the Factorial Calculator App.")
    print() # blank line
    
    fact_str = input("What number would you like to compute the factorial of? ")
    fact_num = int(fact_str) # convert input string type to integer type
    
    # Create factorial string then print it
    f_string = make_f_string(fact_num)
    print("{}! = {}".format(fact_str, f_string))
    
    # Use math library to calculate factorial
    print() # blank line
    print("Here is the result from the math library:")
    print("The factorial of {} is {}!".format(fact_str, calc_math_fact(fact_num)))
    
    # Calculate using own function and display result
    print() # blank line
    print("Here is the result from my own algorithm:")
    print("The factorial of {} is {}!".format(fact_str, calc_my_fact(fact_num)))
    print() # blank line
    
    # Compare math and own algorithm values
    if math.factorial(fact_num) == calc_my_fact(fact_num):
        print("It is shown twice that {}! = {} (with excitement)".format(fact_num, calc_my_fact(fact_num)))
    else:
        print("The values differ with math module result of {} different than own \
    calculation of {}".format(math.factorial(fact_num), fact(fact_num)))

if __name__ == "__main__":
    main()
