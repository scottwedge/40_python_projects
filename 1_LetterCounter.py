#!/usr/bin/env python3

# Project 1: 
# - prompts for user name and capitalizes it if needed
# - prompts for a line of text to be entered
# - prompts for which letter count is desired.
# - prints letter and count for that letter

# Instructions are that both upper case and lower case are counted for the same letter.

# Variables:
# name: entered name of user
# line: text string to be evaluated
# letter: letter to be counted in line
# count: number of occurrences of letter in line

# Prompt for user name, capitalize to be safe
name = input("What is your name? ")
name = name.capitalize()

print("Welcome", name)
line = input("Please enter the line of text to be evaluated: ")

print("Thank you for entering:", line)

