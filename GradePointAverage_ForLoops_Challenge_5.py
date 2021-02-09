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

# Get grades
grade_list = [] # initialize list
for j in range(num):
    grade = input("Enter grade: ")
    grade = float(grade) # convert input from string type to float type
    grade_list.append(grade) # add input to list

print() # blank line
# Sort grades highest to lowest
grade_list.sort()
grade_list.reverse()
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

print() # blank line

# get desired average
desire = input("What is your desired average: ")
desire = float(desire) # convert input string type to float type

req_grade = calc_req(desire, grade_list)
# wish user good luck and state what next grade must be to get that average.
print() # blank line
print("Good luck {}!".format(name))
print("You will need to get a {} on your next assignment to earn a {} average.".format(req_grade, desire))
