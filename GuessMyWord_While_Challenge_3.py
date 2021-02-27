#!/usr/bin/env python3

# Word Guessing Game

# Welcome user
# Provide a Category
# Present a string of dashes - one per letter in the word
# After each incorrect guess, reveal one random letter in the word
# If guess correct, state how many guesses user took
# Then offer option to play again

# Imports
import random

# Functions

def welcome():
    return "Welcome to the Guess My Word App"

def guess_dict():
    d = {"sports":["football", "hockey","soccer", "volleyball", "basketball"],
         "Beatles":["John", "George", "Paul", "Ringo"],
         "Single Digits": ["one","two","three","four","five","six","seven"]}
    return(d)

def get_category(d):
    category_list = [] # init blank list
    for j in d.keys():
        category_list.append(j)
    return category_list 


# Main code
print(welcome())
d = guess_dict()
list_of_categories = get_category(d)
print(list_of_categories)
