#!/usr/bin/env python3

# Print welcome message
print("Welcome to the grade sorter application")
print() # blank line

# initialize empty list of grades
grades_list = []

# Prompt for a grade four times
for j in ["first", "second", "third", "fourth"]:
    grade = input("What is your {} grade (0-100): ".format(j))
    grade = int(grade)  # convert string input to integer to match demo example
    grades_list.append(grade)

# List the four grades
print("Your grades are: ", grades_list)

# Display the grades sorted from highest to lowest

# State and list the two lowest grades will be removed

# Display the remaining grades

# Comment on the highest grade
