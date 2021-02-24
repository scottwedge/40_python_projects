#!/usr/bin/env python3

# Factor Generator App

# Welcome user
# Get number to be factored
# Show all factors
# Ask if user wants to factor another number

# Imports
import math

# Constants

# Variables
main_loop = True # main while loop
factor_loop = True # loop that lists factors
factor_list = []


# Functions
def welcome():
    return ("Welcome to the Factor Generator App")

def get_number():
    print() # blank line
    num = input("Enter a number to determine all factors of that number: ")
    num = int(num) # convert from string type to integer type
    return num

def list_factors(num):
    print() # blank line
    print("Factors of {} are:".format(num))
    for j in range(1, num+1):
        if num % j == 0:
            print(j)
            factor_list.append(j)
    return factor_list
    
def summary(factor_list):
    print() # blank line
    print("In summary:")
    for j in factor_list:
        if j <= math.sqrt(num): # Not repeat factor in demo example
            print("{} * {} = {}".format(j, int(num/j), num))

def run_again():
    print() # blank line
    y_n = input("Run again (y/n): ")
    y_n = y_n.lower() # convert from upper case 
    y_n = y_n.rstrip() # remove trailing white space
    if y_n == "y" or y_n == "yes":
        return True
    elif y_n == "n" or y_n == "no":
        print() # blank line
        print("Thank you for using the program. Have a great day.")
        return False
    else:
        print("That is not a valid response ... exiting")
        return False

# Main code
print(welcome())

while main_loop:
    factor_list = [] # initialize list for each number
    num = get_number()
    factor_list = list_factors(num)
    summary(factor_list)
    main_loop = run_again()
