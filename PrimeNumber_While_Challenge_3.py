#!/usr/bin/env python3

# Prime Number App

# Welcome user
# Print option #1 to determine if a number is prime
# Print option #2 to determine all prime numbers within a set range
# Prompt user to enter choice
# Check validity of choice; warn user if invalid and prompt again for input
# Enter input
# Record how long it took to determine results
# Display results
# Ask user if want to repeat program

# Imports
import time

# Functions
def welcome():
    print("Welcome to the Prime Number App")

def give_options():
    print() # blank line
    print("Enter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")

def get_option():
    option = input("Enter your choice 1 or 2: ")
    return option

def check_if_prime(user_num):
    is_prime = True # initialize result
    for j in range(2, user_num):
        if user_num % j == 0: # check if number is divisible
            is_prime = False
    return is_prime

def run_again():
    res = input("Would you like to run the program again? (y/n): ")
    res = res.lower()
    res = res.rstrip()
    if res == "y" or res == "yes":
        return True
    else:
        return False

# Main code
welcome()
main_loop_boolean = True

while main_loop_boolean:
    give_options()
    option = get_option()
    
    if option == "1":
        print() # blank line
        user_num = input("Enter a number to determine if it is prime or not: ")
        user_num = int(user_num)
        is_prime = check_if_prime(user_num)
    
        if is_prime:
            print("{} is prime!".format(user_num))
        else:
            print("{} is not prime!".format(user_num))
    elif option == "2":
        pass

    else:
        print() # blank line
        print("That is not a valid option.")
    
    main_loop_boolean = run_again()
