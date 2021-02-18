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
    return choice

def computer_wins(computer_score):
    print("\tComputer wins!")
    
def player_winds(player_score):
    print("\tPlayer wins!")

    
# Setup
list_of_choices = ["rock", "paper", "scissors"]
computer_score = 0
player_score = 0

welcome()
num = get_num()

for j in range(num):
    computer_choice = choice(list_of_choices)
    print() # blank line
    print("Round {}".format(j+1))  # Round number
    print("Player: {}\tComputer: {}".format(player_score, computer_score)) # Current score
    player_choice = get_user_choice()

    print("\tComputer: {}".format(computer_choice))
    print("\tPlayer: {}".format(player_choice))

    if player_choice not in list_of_choices:
        print("That is not a valid game option!\nComputer gets the point!")
        computer_score = computer_score + 1
    else: # user input is valid
        if computer_choice == player_choice: # tie scenario
            print("tIt is a tie, how boring!\n\tThis round was a tie")
        if computer_choice == "rock":
            if player_choice == "paper": player_wins(player_score)
            else: computer_wins(computer_score)
        if computer_choice == "paper":
            if player_choice == "scissors": player_wins(player_score)
            else: computer_wins(computer_score)
        if computer_choice == "scissors":
            if player_choice == "rock": player_wins(player_score)
            else: computer_wins(computer_score)
        
