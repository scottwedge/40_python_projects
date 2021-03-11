#!/usr/bin/env python3

# Pykemon game

# Lots of Pokemon terms and assumed knowledge

# Steps:
# Welcome user
# Display settings for three potential choices
# Show Name, Element Type, Health, Speed  and Moves for each pykemon
# List three pykemon by name
# Choose one pykemon

# Imports
import random

# Functions
def welcome():
    print("Welcome to Pykemon!")
    print("Can you become the world's greatest Pykemon Trainer???")
    print()   # blank line
    print("Don't worry! Prof Eramo is here to help you on your quest.")
    print("He would like to gift you your first Pykemon!")
    print("Here are three potential Pykemon partners")

def get_enter():
    result = input("Press Enter to choose your Pykemon!")

def create_pykemon():
    tuple_of_settings = random.randint(1,10)
    return  tuple_of_settings
    
def choose_pykemon(list_of_pykemon):
    print("Profressor Eramo presents you with the three Pykemon:")
    for j in list_of_pykemon:
        print("({}) - {}".format(j, list_of_pykemon[j][name]))

# Main code
welcome()
get_enter()

list_of_pykemon = []
for j in range(3):
    new_pykemon = create_pykemon()
    list_of_pykemon.append(new_pykemon)

