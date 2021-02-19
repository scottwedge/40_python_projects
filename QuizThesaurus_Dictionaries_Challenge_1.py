#!/usr/bin/env python3

# Welcome user
# Print purpose statement
# List all words in thesaurus app
# Have user select which word for a synonym
# Then list all synonyms for all words in app

# Imports 
import random

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
    word = word.lower() # conver to lower case format
    return word

def get_synonym(word):
    syn = thesaurus[word]
    return syn

def view_all():
    print() # blank line
    result = input("Would you like to see the whole thesaurus (yes/no): ")
    result = result.lower()
    if result == "yes":
        return True
    else:
        return False
    
def print_thesaurus(thesaurus):
    for k,v in thesaurus.items():
        print(thesaurus[k])

# Initialize variables
thesaurus = {"happy":["merry", "joyful"], "sad":["unhappy", "morose"]}
list_of_words = ["hot", "cold", "happy", "sad"]

# Main program
welcome()
possible_words(list_of_words)
word = get_word()

# Check that word is valid thesaurus entry
if word not in list_of_words:
    print("The word {} is not a valid choice!".format(word))
else:
    syn = get_synonym(word)
    print("A synonym for {} is {}.".format(word, syn))

    res = view_all()

    if res: print_thesaurus(thesaurus)
