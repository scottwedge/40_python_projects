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
    print("Well {}, I am thinking of a number between 1 and 20.".format(name))
    print() # blank line
    return name

def generate_random():
    random.seed()
    r = random.randint(1,20)
    return r

def take_guess():
    guess = input("Take a guess: ")
    guess = int(guess) # convert input string type to integer type
    return guess


welcome()
name = get_name()
r = generate_random()

for j in range(5):
    guess = take_guess()  # prompt for user input
    if guess == r:
        print() # blank line
        print("Good job {}! You guessed my number in {} guesses!".format(name, j+1))
        break # stop loop
    elif guess < r:
        print("Your guess is too low.")
        print() # blank line
    else:
        print("Your guess is too high.")
        print() # blank line
