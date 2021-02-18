#!/usr/bin/env python3

# Welcome user
# Print purpose statement
# List all words in thesaurus app
# Have user select which word for a synonym
# Then list all synonyms for all words in app

# Functions
def welcome():
    print("Welcome to the Thesaurus App!")
    print() # blank line
    print("Choose a word from the thesaurus and I will give you a synonym.")
    print() # blank line

def possible_words(list_of_words):
    print("Here are the words in the thesaurus:")
    for j in list_of_words:
        print("\t-{}".format(j))
    print() # blank line

def get_word():
    word = input("What word would you like a synonym for: ")
    return word

# Initialize variables
list_of_words = ["hot", "cold", "happy", "sad"]

# Main program
welcome()
possible_words(list_of_words)
word = get_word()
