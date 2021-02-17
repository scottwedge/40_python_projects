#!/usr/bin/env python3

# Welcome user
# Get user name
# Generate random number between 1 and 20
# Start taking number guesses from user
# Reply if guess is correct, too high or too low.
# If not correct after five guesses, state value and end game.


# Functions
def welcome():
    print("Welcome to the Guess My Number app.")
    print() # blank line

def get_name():
    name = input("What is your name: ")
    name = name.title() # convert name to title format


welcome()

name = get_name()
