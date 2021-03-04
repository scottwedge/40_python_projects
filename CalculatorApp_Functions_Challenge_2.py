#!/usr/bin/env python3

# Calculator App

# Welcome user
# Ask for two numbers
# Ask for operation - accept either first letter or full word
# Print lexical (?) of operation
# Ask if want to repeat
# If not, list all calculations

# Functions
def welcome():
    print("Welcome to the Python Applicator App")
    print("Enter two numbers and the desired operation")

def get_number():
    num = input("Enter a number: ")
    num = float(num)  # convert from string type to float type
    return num

def get_operation():
    op = input("Enter an operation (addition, subtraction, multiplication, division or exponentiation): ")
    op = op.lower()
    op = op.rstrip()
    return op

def play_again():
    reply = input("Would you like to run the program again (y/n): ")
    if reply == "y" or reply == "yes":
        return True
    else:
        return False

def summary(op_list):
    print() # blank line
    print("Calculation Summary:")
    for j in op_list:
        print(j)

# Main code
welcome()
op_list = []
main_loop_boolean = True

while main_loop_boolean:
    print() # blank line
    first = get_number()
    second = get_number()
    op = get_operation()
    
    if op == "addition" or op == "a":
        print("The sum of {} and {} is {}.".format(first, second, first + second))
        op_list.append("{} + {} = {}".format(first, second, first + second))
    elif op == "subtraction" or op == "s":
        print("The result of {} minus {} is {}.".format(first, second, first - second))
        op_list.append("{} - {} = {}".format(first, second, first - second))
    elif op == "multiplication" or op == "m":
        print("The product of {} and {} is {}.".format(first, second, first * second))
        op_list.append("{} * {} = {}".format(first, second, first * second))
    elif op == "division" or op == "d":
        print("The result of {} divided by {} is {}.".format(first, second, first / second))
        op_list.append("{} / {} = {}".format(first, second, first / second))
    elif op == "exponentiation" or op == "e":
        print("The result of {} raised to the power of {} is {}.".format(first, second, first ** second))
        op_list.append("{} ** {} = {}".format(first, second, first ** second))
    else:
        print("ERROR")
        op_list.append("ERROR")
    
    main_loop_boolean = play_again()

summary(op_list)
