#!/usr/bin/env python3

# Rock Paper Scissors challenge


# Welcome user
# Ask how many rounds are to be played
# State current 
# State round number, current score
# Then select pick and show results
# If tie then no change in score
# If invalid choice then computer wins
# Print which object wins over other object
# Print whether computer or player wins
# Print game summary

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
    random.seed()
    r = random.randint(0,2) # random index into list of choices
    choice = list_of_choices[r]
    return choice

def get_user_choice():
    choice = input("Time to pick...rock, paper, scissors: ")
    choice = choice.lower() # convert to lower case
    return choice

def main():    
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
                print("\tIt is a tie, how boring!\n\tThis round was a tie")
            else:
                if computer_choice == "rock":
                    if player_choice == "paper":       # Player wins
                        print("\tPaper covers rock!")
                        player_score = player_score + 1
                        print("\tYou win round {}.".format(j+1))
                    else:                              # Computer wins
                        print("Scissors block rock!")
                        computer_score = computer_score + 1
                        print("Computer wins round {}.".format(j+1))
                if computer_choice == "paper":
                    if player_choice == "scissors":       # Player wins
                        print("\tScissors cut paper!")
                        player_score = player_score + 1
                        print("\tYou win round {}.".format(j+1))
                    else:                              # Computer wins
                        print("\tPaper covers rock!")
                        computer_score = computer_score + 1
                        print("\tComputer wins round {}.".format(j+1))
                    if player_choice == "scissors": player_wins(player_score)
                if computer_choice == "scissors":
                    if player_choice == "rock":       # Player wins
                        print("\tRock blocks scissors!")
                        player_score = player_score + 1
                        print("\tYou win round {}.".format(j+1))
                    else:                              # Computer wins
                        print("\tScissors cut paper!")
                        computer_score = computer_score + 1
                        print("\tComputer wins round {}.".format(j+1))

# Game summary
    print() # blank line
    print("Final Game Results")
    print("\tRounds Played: {}".format(num))
    print("\tPlayer Score: {}".format(player_score))
    print("\tComputer Score: {}".format(computer_score))

# determine last line of game summary
    if player_score == computer_score:
        print("\tThis is a tie!")
    elif player_score > computer_score: # player wins
        print("\tWinner: Player :-)")
    else: # computer wins
        print("\tWinner: Computer :-(")
                
if __name__ == "__main__":
    main()
