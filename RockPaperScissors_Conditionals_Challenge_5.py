#!/usr/bin/env python3

# Rock Paper Scissors challenge


# Welcome user
# Ask how many rounds are to be played
# State current 
# State round number, current score
# Then select pick and show results
# If tie then no change in score
# If invalid choice then computer wins

# Functions

def welcome():
    print("Welcome to a game of Rock, Paper, Scissors")
    print() # blank line

def get_num():
    num = input("How many rounds would you like to play: ")
    num = int(num)
    return num



welcome()
get_num()

