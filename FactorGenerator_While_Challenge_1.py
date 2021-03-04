#!/usr/bin/env python3

# Factor Generator App

# Welcome user
# Get number to be factored
# Speed up calculation by only searching for factors up to the square root of the number
# Show all factors
# Ask if user wants to factor another number

# Imports
import math
import time

# Constants

# Functions
def welcome():
    return ("Welcome to the Factor Generator App")

def get_number():
    print() # blank line
    num = input("Enter a number to determine all factors of that number: ")
    num = int(num) # convert from string type to integer type
    return num

def slow_list_factors(num):
    factor_list = []
    print() # blank line
    print("Factors of {} are:".format(num))
    for j in range(1, num+1):
        if num % j == 0:
#            print(j)
            factor_list.append(j)
    print(factor_list)
    return factor_list


def fast_list_factors(num):
    factor_list = []
    print() # blank line
    print("Factors of {} are:".format(num))
    # only do factors up to the square root of the number
    for j in range(1, math.floor(math.sqrt(num)) + 1):
        if num % j == 0:
#            print(j)
            factor_list.append(j)
#    print(factor_list) #DEBUG
    # Then divide num by all values in list to determine missing factors
    missing_factors = []
    for j in factor_list:
        factor = num / j
        missing_factors.append(factor)
#    print(missing_factors)
    # Combine lists, sort and remove duplicates
    factor_list = factor_list + missing_factors
    factor_list.sort() # sort 
    unique_list = []
    for j in factor_list:
        if j not in unique_list:
            unique_list.append(j)
    print(unique_list)
    return unique_list

def test_list_factors():
    assert list_factors(100) == [1,2,4,5,10,20,25,50,100]
    
def summary(factor_list, num):
    print() # blank line
    print("In summary:")
    for j in factor_list:
        if j <= math.sqrt(num): # Not repeat factor in demo example
             pass
#            print("{} * {} = {}".format(j, int(num/j), num))

def duration(start_time, end_time):
    print("Program duration of ...:", end_time - start_time, "seconds")

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
def main():
    main_loop = True 
    factor_loop = True 
    factor_list = []

    print(welcome())
    
    while main_loop:
        factor_list = [] # initialize list for each number
        num = get_number()
        start_time = time.time()
        factor_list = slow_list_factors(num)  # slow calculation method
        summary(factor_list, num)
        end_time = time.time()
        duration(start_time, end_time)
        print("---------------------------")
        start_time = time.time()
        factor_list = fast_list_factors(num)  # slow calculation method
        summary(factor_list, num)
        end_time = time.time()
        duration(start_time, end_time)
        main_loop = run_again()

if __name__ == "__main__":
    main()
