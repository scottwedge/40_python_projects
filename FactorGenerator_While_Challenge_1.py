#!/usr/bin/env python3

# Factor Generator App

# Welcome user
# Get number to be factored
# Show all factors
# Ask if user wants to factor another number

# Constants

# Variables
main_loop = True # main while loop
factor_loop = True # loop that lists factors
factor_list = []


# Imports

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
    
def summary():
    pass

# Main code
print(welcome())

while main_loop:
    num = get_number()
    factor_list = list_factors(num)
    summary()
