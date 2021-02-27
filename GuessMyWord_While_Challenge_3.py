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

def get_random_category(list_of_categories):
    random_index = random.randint(0, len(list_of_categories) - 1)
    random_category = list_of_categories[random_index]
    return random_category

def get_random_word(d, category):
    list_of_words = []              # initialize list
    for j in d[category]:
        list_of_words.append(j)    # create list
    random_index = random.randint(0,len(list_of_words) - 1)
    word = list_of_words[random_index]
    return word

def init_clue(word):
    clue = []                    # initialize list
    for j in range(len(word)):   # all "-"
        clue.append("-")
    print("DEBUG clue is ",clue) #DEBUG
    return clue

def display_current_clue(clue):
    print() # blank line
    print("Guess a {} letter word from the following category: {}.".format(len(word), category))
    print(clue)

def update_clue(clue):
    clue_list = list(clue)   # convert string to list
    just_dashes_list = []   # initialize list of remaining dash indexes in clue list
    for j in range(len(clue_list)):
        if clue_list[j] == "-":
            just_dashes_list.append(j)

    random_index = random.randint(0, len(just_dashes_list) -1) # choose random index


def take_guess(word, clue, guess_count):
    print() # blank line
    guess_count += 1
    g = input("Enter your guess: ")
    if g == word:
        print("CORRECT guess in {} tries".format(guess_count))
    else:
        print("That is not correct. Let us reveal a letter to help you!")
        clue = update_clue(clue)               
        print(clue)
    return (clue, guess_count)

# Main code
print(welcome())
d = guess_dict()
list_of_categories = get_category(d)

category = get_random_category(list_of_categories)
print(category)   	#DEBUG

word = get_random_word(d, category)
print(word)     	#DEBUG 

guess_count = 0  	# initialize counter

clue = init_clue(word) # Initial word will be correct length but all dashes
display_current_clue(clue)

(clue, guess_count) = take_guess(word, clue, guess_count)
