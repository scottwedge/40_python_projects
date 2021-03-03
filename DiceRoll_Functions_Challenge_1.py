#!/usr/bin/env python3

# Dice Roll App

# Welcome user
# Get user input for number of sides of each dice
# Get user input for number of dice
# State number of dice and number of sides of dice
# List results for each dice
# Sum the results of all dice
# Ask if want to roll again (and start at beginning again)

# Imports
import random

# Functions
def welcome():
    print("Welcome to the Python Dice App")
    print() # blank line

def get_dice_sides():
    print() # blank line
    num_sides = int(input("How many sides would you like on your dice: "))
    return num_sides

def get_number_of_dice():
    num_dice = int(input("How many dice would you like to roll: "))
    return num_dice

def roll_dice(num_sides, num_dice):
    results = []		# initialize results list
    for j in range(num_dice):
        k = random.randint(1, num_sides)
        results.append(k)
    print() # blank line
    print("You rolled {} {} sided dice.".format(num_dice, num_sides))
    return results

def display_results(results):
    print() # blank line
    print("----- Results are as follows -----")
    for j in results:
        print("\t{}".format(j))

def sum_results(results):
    sum = 0
    for j in results:
        sum = sum + j
    print("The total value of your roll is {}.".format(sum))

def roll_again():
    print() # blank line
    answer = input("Would you like to roll again (y/n): ")
    answer = answer.lower()
    answer = answer.rstrip()
    if answer == "y" or answer == "yes":
        return True
    else:
        return False

def thankyou():
    print("Thank you for using the Python Dice App.")

# Main code
welcome()
loop_forever = True

while loop_forever:
    num_sides = get_dice_sides()
    num_dice = get_number_of_dice()
    results = roll_dice(num_sides, num_dice)
    display_results(results)
    sum_results(results)
    loop_forever = roll_again()
thankyou()
