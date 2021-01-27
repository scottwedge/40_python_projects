#!/usr/bin/env python3

# Script to print both multiplication and exponentiation table
# From range of 1 to 9 inclusive.

# Imports
import string # to access capwords method in string module

# Functions
def input_name():
    # Print welcome message 
    print("Welcome to the Multiplication/Exponentiation application.")
    
    # Prompt for user name
    user_name = input("What is your name: ")
    return user_name
    
def input_number():
    # Prompt for number to work with
    user_number = input("What number do you want to work with: ")
    
    # Convert input to float number (from character string)
    num = float(user_number)
    return num

def create_multiplication_table(num):
    print() # blank line
    print("Multiplication table for", num)
    
    for n in range(1,10,1):
        float_n = float(n)
        print("{:>10} * {} = {}".format(float_n, num, float_n * num))

def create_exponentiation_table(num):
    print()  # blank line
    print("Exponent table for", num)
    for n in  range(1, 10, 1):
        print("{:>10} ** {} = {:.4f}".format(num, n, num ** n))
    
        
def main ():
    # Print welcome message and get user name
    user_name = input_name()

    # Print welcome message and get user number
    num = input_number()
    
    # Display multiplication table for 1 through 9
    create_multiplication_table(num)
        
    # Display exponentiation table for 1 through 9
    create_exponentiation_table(num)
    
    # Print math is cool four times
    phrase = "math is cool!"
    print()  # add blank line
    print(user_name.capitalize(), phrase.capitalize())
    print("    ", user_name.lower(), phrase.lower())
    print("        ", user_name.capitalize(), string.capwords(phrase))
    print("            ", user_name.upper(), phrase.upper())

if __name__ == "__main__":
    main()
