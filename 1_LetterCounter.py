#!/usr/bin/env python3

# Project 1: 
# - prompts for user name and capitalizes it if needed
# - prompts for a line of text to be entered
# - prompts for which letter count is desired.
# - prints letter and count for that letter

# Instructions are that both upper case and lower case are counted for the same letter.

# Variables:
# name: entered name of user
# name_capitalized: capitalize name (as per example)
# line: text string to be evaluated
# line_lower: line in all lower case to simplify counting
# letter: letter to be counted in line
# letter_lower: letter in lower case to simplify counting
# count: number of occurrences of letter in line
# j: loop through line

# Functions
def count_letters(user_line, user_letter):
    num = 0
    for j in user_line:
        if j == user_letter:
            num = num + 1
    return num

# Testing
def test_fail():
    assert False

def test_pass():
    assert True





# Prompt for user name; all lower case name in example gets capitalized 
name = input("What is your name? ")
name_capitalized = name.capitalize()
print("Welcome {}.".format(name_capitalized))

# Prompt for line of text
line = input("Please enter the line of text to be evaluated: ")
print("Thank you for entering:", line)

# Prompt for letter to be counted
letter = input("What letter should be counted? ")

# Convert letter to lower case to simplify counting
letter_lower=letter.lower()

# Convert line to all lower case to simplify count
line_lower = line.lower()

# Count how many times the (upper or lower case) letter occurs in the line
count = count_letters(line_lower, letter_lower)

# Output results
print("{}, there are {} occurrences of {}.".format(name_capitalized, count, letter_lower))
