#!/usr/bin/env python3

# Welcome user
# Get number of coin flip attempts to do
# Ask if want to see results of each flip, or not
# Display when number of heads = number of tails
# Display summary of all results for each side: count and percentage

# Functions
def header():
    print("Welcome to the Coin Toss App")
    print() # blank line

def get_number():
    print("I will flip a coin a set number of times.")
    num = input("How many times would you like me to flip the coin: ")
    num = int(num) # Convert input string type to integer type
    return num


header()
