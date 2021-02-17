#!/usr/bin/env python3

# Welcome user
# Get user name
# Generate random number between 1 and 20
# Start taking number guesses from user
# Reply if guess is correct, too high or too low.
# If not correct after five guesses, state value and end game.

# Imports
import random

# Functions
def welcome():
    print("Welcome to the Guess My Number app.")
    print() # blank line

def get_name():
    name = input("Hello! What is your name: ")
    name = name.title() # convert name to title format
    return name

def generate_random():
    random.seed()
    r = random.randomint(1,20)
    return r


welcome()

name = get_name()

r = generate_random()
