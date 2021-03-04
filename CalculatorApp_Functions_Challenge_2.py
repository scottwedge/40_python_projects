#!/usr/bin/env python3

# Calculator App

# Welcome user
# Ask for two numbers
# Ask for operation - accept either first letter or full word
# Print lexical (?) of operation
# Ask if want to repeat

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


# Main code
welcome()
first = get_number()
second = get_number()
op = get_operation()

if op == "addition" or op == "a":
    print("The sum of {} and {} is {}.".format(first, second, first + second))
elif op == "subtraction" or op == "s":
    print("The result of {} minus {} is {}.".format(first, second, first - second))
elif op == "multiplication" or op == "m":
    print("The product of {} and {} is {}.".format(first, second, first * second))
elif op == "division" or op == "d":
    print("The result of {} divied by {} is {}.".format(first, second, first / second))
elif op == "exponentiation" or op == "e":
    print("The result of {} to power of {} is {}.".format(first, second, first ** second))
else:
    print("ERROR")
