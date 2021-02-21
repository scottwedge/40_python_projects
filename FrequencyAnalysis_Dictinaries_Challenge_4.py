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

# Analyze text
alpha_count_db = {} # initialize blank alphabet dictionary
text = text.lower() # convert to all lower case
text_list = list(text) # convert text string to list of characters
print(text_list)

for j in range(len(text_list)):
    if text_list[j].isalpha():  # if alphanumeric
        if text_list[j] in alpha_count_db.keys(): # check if key already exists
            alpha_count_db[text_list[j]] = alpha_count_db[text_list[j]] + 1 # increment counter
        else:
            alpha_count_db[text_list[j]] = 1 # initialize counter

