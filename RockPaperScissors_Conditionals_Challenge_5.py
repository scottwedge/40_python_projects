#!/usr/bin/env python3

# Rock Paper Scissors challenge


# Welcome user
# Ask how many rounds are to be played
# State current 
# State round number, current score
# Then select pick and show results
# If tie then no change in score
# If invalid choice then computer wins

# Imports
import random

# Functions


def welcome():
    print("Welcome to a game of Rock, Paper, Scissors")
    print() # blank line

def get_num():
    num = input("How many rounds would you like to play: ")
    num = int(num)
    return num

def choice(list_of_choices):
    r = random.randint(0,2) # random index into list of choices
    choice = list_of_choices[r]
    return choice

def get_user_choice():
    choice = input("Time to pick...rock, paper, scissors: ")
    choice = choice.lower() # convert to lower case

    
# Setup
list_of_choices = ["rock", "paper", "scissors"]
computer_wins = 0
player_wins = 0

welcome()
num = get_num()

for j in range(num):
    computer_choice = choice(list_of_choices)
    print() # blank line
    print("Round {}".format(j+1))  # Round number
    print("Player: {}\tComputer: {}".format(player_wins, computer_wins)) # Current score
    player_choice = get_user_choice()

    print("\tComputer: {}".format(computer_choice))
    print("\tPlayer: {}".format(player_choice))
