#!/usr/bin/env python3

# Functions
def get_grades():
    # initialize empty list of grades
    grades_list = []

    # Prompt for a grade four times
    for j in ["first", "second", "third", "fourth"]:
        grade = input("What is your {} grade (0-100): ".format(j))
        grade = int(grade)  # convert string input to integer to match demo example
        grades_list.append(grade)
    return grades_list


# Print welcome message
print("Welcome to the grade sorter application")
print() # blank line

# Get grades from users
grades_list = get_grades()

# List the four grades
print() # blank line
print("Your grades are: ", grades_list)

# Display the grades sorted from highest to lowest
grades_list.sort() # sort grades from lowest to highest
grades_list.reverse() # sort grades from highest to lowest
print() # blank line
print("Your grades from highest to lowest are: ", grades_list)

# State and list the two lowest grades will be removed
print()  # blank line
print("The lowest two grades will now be dropped")

for count in range (1, 3, 1):
    lowest = grades_list.pop()
    print("Removed grade: ", lowest)

# Display the remaining grades
print()  # blank line
print("Your remaining grades are: ", grades_list)

# Comment on the highest grade
highest = grades_list[0]
print() # blank line
print("Nice work! Your highest grade is a {}.".format(highest))
