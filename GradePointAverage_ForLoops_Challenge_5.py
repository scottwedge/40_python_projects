#!/usr/bin/env python3

# Ask for user name
# Ask for how many grades are to be entered
# Enter grades
# Sort grades from highest to lowest
# Calculate average grade
# Display grades summary
# Ask for what average is desired
# Calculate what grade is needed to obtain that as overall average
# Change one grade and see how it changes the average
# Display new summary of grades


# Welcome header
print("Welcome to the Average Calculator App.")
print() # blank line

name = input("What is your name: ")
name = name.title() # convert to title format
num = input("How many grades would you like to enter: ")
num = int(num) # convert input string type to integer type

# Get grades
grade_list = [] # initialize list
for j in range(num):
    grade = input("Enter grade: ")
    grade = float(grade) # convert input from string type to float type
    grade_list.append(grade) # add input to list
