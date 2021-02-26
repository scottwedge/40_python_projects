#!/usr/bin/env python3

# Prime Number App

# Welcome user
# Print option #1 to determine if a number is prime
# Print option #2 to determine all prime numbers within a set range
# Prompt user to enter choice
# Check validity of choice; warn user if invalid and prompt again for input
# Enter input
# Display results
# Ask user if want to repeat program

# Imports
import time

# Functions
def welcome():
    return "Welcome to the Prime Number App"

def give_options():
    print() # blank line
    print("Enter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")

def get_option():
    option = input("Enter your choice 1 or 2: ")
    return option

# Main code
welcome()
give_options()
option = get_option()

