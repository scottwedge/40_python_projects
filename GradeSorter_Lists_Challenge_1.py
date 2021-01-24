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
print() # blank line
print("Your grades are: ", grades_list)

# Display the grades sorted from highest to lowest
grades_list.sort() # sort grades from lowest to highest
grades_list.reverse() # sort grades from highest to lowest
print() # blank line
print("Your grades from highest to lowest are: ", grades_list)

# State and list the two lowest grades will be removed
print("The lowest two grades will now be dropped")

for count in range (1, 3, 1):
    lowest = grades_list.pop()
    print("Removed grade: ", lowest)


# Display the remaining grades

# Comment on the highest grade
