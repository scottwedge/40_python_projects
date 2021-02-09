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

# Functions
def get_grades(num): # get grades from user
    grade_list = [] # initialize list
    for j in range(num):
        grade = input("Enter grade: ")
        grade = float(grade) # convert input from string type to float type
        grade_list.append(grade) # add input to list
    return grade_list

def sort_grades(grade_list): # Sort grades highest to lowest
    grade_list.sort()
    grade_list.reverse()

def show_grades(grade_list):
    print() # blank line
    print("Grades highest to lowest: ")
    for j in range(num):
        print("\t{}".format(grade_list[j]))
    
    print() # blank line
    # Display grade summary
    print("{}'s grade summary:".format(name))
    print("\tTotal number of grades: {}".format(len(grade_list)))
    print("\tHighest grade: {}".format(grade_list[0]))   # first number in list is highest grade
    print("\tLowest grade: {}".format(grade_list[-1])) # last number in list is lowest grade
    print("\tAverage grade: {}".format(average_grade(grade_list)))

def get_sort_show_grades():
    grade_list = get_grades(num)
    sort_grades(grade_list)
    show_grades(grade_list)
    return grade_list

def average_grade(list):
    sum = 0 # initialize sum
    num = len(list) 
    for j in range(num):
        sum = sum + list[j]
    return sum/num

def sum_list(list):
    sum = 0
    for j in (len(list)):
        sum = sum + list[j]
    return sum

def calc_req(desire, grade_list):
    total = desire * (len(grade_list) + 1)
    need = total - sum(grade_list)
    return need

# Welcome header
print("Welcome to the Average Calculator App.")
print() # blank line

name = input("What is your name: ")
name = name.title() # convert input of any format to title format
num = input("How many grades would you like to enter: ")
num = int(num) # convert input string type to integer type

# Get grades then sort them then display them
grade_list = get_sort_show_grades()

# get desired average
print() # blank line
desire = input("What is your desired average: ")
desire = float(desire) # convert input string type to float type

req_grade = calc_req(desire, grade_list)
# wish user good luck and state what next grade must be to get that average.
print() # blank line
print("Good luck {}!".format(name))
print("You will need to get a {} on your next assignment to earn a {} average.".format(req_grade, desire))

# Change one grade and see how that affects overall average
print() # blank line
print("Let's see what your average could have been if you did better/worse on an assignment.")
grade_to_change = input("What grade would you like to change: ")
grade_to_change = float(grade_to_change) # convert input string type to float type

# prompt for new grade
print() # blank line
new_grade = input("What grade would you like to change {} to: ".format(grade_to_change))

