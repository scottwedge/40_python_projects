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
        grade = int(grade) # convert input from string type to int type
        grade_list.append(grade) # add input to list
    return grade_list

def sort_grades(grade_list): # Sort grades highest to lowest
    grade_list.sort()
    grade_list.reverse()

def show_grades(grade_list):
    for j in range(len(grade_list)):
        print("\t{}".format(grade_list[j]))
    
def show_summary(grade_list):
    # Display grade summary
    print() # blank line
    print("\tTotal Number of Grades: {}".format(len(grade_list)))
    print("\tHighest Grade: {}".format(grade_list[0]))   # first number in list is highest grade
    print("\tLowest Grade: {}".format(grade_list[-1])) # last number in list is lowest grade
    print("\tAverage: {}".format(average_grade(grade_list)))


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


def main():
    # Welcome header
    print("Welcome to the Average Calculator App.")
    print() # blank line
    
    name = input("What is your name: ")
    name = name.title() # convert input of any format to title format
    num = input("How many grades would you like to enter: ")
    num = int(num) # convert input string type to integer type
    
    # Get grades then sort them then display them
    grade_list = get_grades(num)
    sort_grades(grade_list)
    
    print("Grades Highest to Lowest: ")
    show_grades(grade_list)
    
    # Display grades summary
    print() # blank line
    print("{}'s Grade Summary:".format(name))
    show_summary(grade_list)
    
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
    grade_to_change = int(grade_to_change) # convert input string type to int type
    
    # prompt for new grade
    print() # blank line
    new_grade = input("What grade would you like to change {} to: ".format(grade_to_change))
    new_grade = int(new_grade) # convert input string type to int type
    
    # copy grade list, remove old grade, add new grade, resort list and display list
    fantasy_grade_list = grade_list.copy()
    fantasy_grade_list.remove(grade_to_change) # remove old grade
    fantasy_grade_list.append(new_grade)
    sort_grades(fantasy_grade_list)
    print() # blank line
    print("New Grades Highest to Lowest: ")
    show_grades(fantasy_grade_list)
    
    # Display grades summary
    print() # blank line
    print("{}'s New Grade Summary:".format(name))
    show_summary(fantasy_grade_list)
    
    print() # blank line
    old_av = average_grade(grade_list) 
    fantasy_av = average_grade(fantasy_grade_list)
    print("Your new average would be a {} compared to your real average of {}!".format(fantasy_av, old_av))
    print("That is a change of {} points".format(fantasy_av - old_av))
    print() # blank line
    
    # print "too bad" and list old list of grades
    print("Too bad your original grades are still the same!")
    print(grade_list)
    print("You should go ask for extra credit!")


if __name__ == "__main__":
    main()
