#!/usr/bin/env python3

# Analyze the letter distribution of a given text
# Take any text, 
# Remove any non-alpha characters,
# Count the frequency of each letter in the text
# Calculate the percentage of occurrence of each letter
# Create a list of letters ordered from highest occurrence to lowest occurrence
# For two different bodies of text

# Functions

def welcome():
    print("Welcome to the Frequency Analysis App")
    print() # blank line

def get_text():
    text = input("Enter a word or phrase to count the occurrences of each letter: ")
    return text


welcome()
text = get_text()
