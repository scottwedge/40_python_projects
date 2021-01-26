#!/usr/bin/env python3

# Get four grades, sort them, drop lowest two grades and list them, then display remaining list

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

def sort_grades(grades_list):
    grades_list.sort() # sort grades from lowest to highest
    grades_list.reverse() # sort grades from highest to lowest
    print() # blank line
    print("Your grades from highest to lowest are: ", grades_list)
    
def pop_lowest_grade(grades_list, num):
    for count in range (1, 1+num, 1):
        lowest = grades_list.pop()
        print("Removed grade: ", lowest)
    return grades_list

# Tests
def test_sort_grades():
    order = [5,1,2,3]
    sort_grades(order)
    assert order == [5, 3, 2, 1]

def test_pop_lowest_grade():
    assert [9,8,7] == pop_lowest_grade([9,8,7,6], 1)

# main function
def main():
    # Print welcome message
    print("Welcome to the grade sorter application")
    print() # blank line

    
    # Get grades from users
    grades_list = get_grades()
    
    # List the four grades
    print() # blank line
    print("Your grades are: ", grades_list)
    
    # Display the grades sorted from highest to lowest
    sort_grades(grades_list)

    # State and list the two lowest grades will be removed
    print()  # blank line
    print("The lowest two grades will now be dropped")
    
    remaining_grades = pop_lowest_grade(grades_list, 2)  
    
    # Display the remaining grades
    print()  # blank line
    print("Your remaining grades are: ", remaining_grades)
    
    # Comment on the highest grade
    highest = remaining_grades[0]
    print() # blank line
    print("Nice work! Your highest grade is a {}.".format(highest))

if __name__ == "__main__":
    main()
