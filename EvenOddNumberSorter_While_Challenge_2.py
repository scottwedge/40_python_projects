#!/usr/bin/env python3

# Welcome user
# get list of numbers separated by commas
# List each number and state if odd or even
# Then list all even numbers
# Then list all odd numbers
# Then ask if user wants to do this again
# If no, thank user

# Functions
def welcome():
    return "Welcome to the Even Odd Number Sorter App"

def get_numbers():
    print() # blank line
    num_string = input("Enter in a string of numbers separated by a comma (,) : ")
    return num_string

def extract_num(num_string):
    num_list = num_string.split(sep = ",") # convert string into list of characters
    numbers = []
    for j in num_list:
        numbers.append(int(j))    # convert numbers from string type to integer type
    return numbers 

def even_odd(n):
    if n % 2 == 0:
        return "even"
    elif n % 2 == 1: 
        return "odd"
    else:
        return "ERROR"

def summary(numbers):
    print() # blank line
    print("------ Result Summary ------")
    for j in numbers:
        print("\t{} is {}!".format(j, even_odd(j)))

# Main program
print(welcome())

num_string = get_numbers()

numbers = extract_num(num_string)

summary(numbers)

