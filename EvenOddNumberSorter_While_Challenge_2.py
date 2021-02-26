#!/usr/bin/env python3

# Welcome user
# get list of numbers separated by commas
# List each number and state if odd or even
# Then list all even numbers
# Then list all odd numbers
# Then ask if user wants to do this again
# If no, thank user

# Functions
def welcome():
    return "Welcome to the Even Odd Number Sorter App"

def get_numbers():
    print() # blank line
    num_string = input("Enter in a string of numbers separated by a comma (,) : ")
    return num_string

def extract_num(num_string):
    num_list = num_string.split(sep = ",") # convert string into list of characters
    numbers = []
    for j in num_list:
        numbers.append(int(j))    # convert numbers from string type to integer type
    return numbers 

def even_odd(n):
    if n % 2 == 0:
        return "even"
    elif n % 2 == 1: 
        return "odd"
    else:
        return "ERROR"

def summary(numbers):
    print() # blank line
    print("------ Result Summary ------")
    for j in numbers:
        print("\t{} is {}!".format(j, even_odd(j)))

def make_even_odd_lists(numbers):
    even_list = []
    odd_list = []
    for j in numbers:
        if j % 2 == 0:
            even_list.append(j)
        else:
            odd_list.append(j)
    return (even_list, odd_list)

def print_even_list(even_list):
    print() # blank line
    print("The following {} numbers are even:".format(len(even_list)))
    even_list.sort() # put in ascending order
    for j in even_list: 
        print("\t{}".format(j))

def print_odd_list(odd_list):
    print() # blank line
    print("The following {} numbers are odd:".format(len(odd_list)))
    odd_list.sort() # put in ascending order
    for j in odd_list: 
        print("\t{}".format(j))

def run_again():
    print() # blank line
    result = input("Would you like to run the program again? (y/n): ")
    result = result.lower() # convert to lower case
    result = result.rstrip() # remove any trailing whitespace
    if result == "n" or result == "no":
        return False
    elif result == "y" or result == "yes":
        return True
    else:
        print("ERROR")
        return False

def goodbye():
    print("Thank you for using the program.  Goodbye.")

# Main program
def main():
    run_again_bool = True
    
    print(welcome())
    
    while run_again_bool:
        num_string = get_numbers()
        
        numbers = extract_num(num_string)
        
        summary(numbers)
        
        (even_list, odd_list) = make_even_odd_lists(numbers)
        
        print_even_list(even_list)
        print_odd_list(odd_list)
        
        run_again_bool = run_again()
    
    goodbye()


if __name__ == "__main__":
    main()
