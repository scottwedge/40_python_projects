#!/usr/bin/env python3

# Prime Number App

# Welcome user
# Print option #1 to determine if a number is prime
# Print option #2 to determine all prime numbers within a set range
# Prompt user to enter choice
# Check validity of choice; warn user if invalid and prompt again for input
# Enter input
# Record how long it took to determine results
# Display results
# Ask user if want to repeat program

# Imports
import time

# Functions
def welcome():
    print("Welcome to the Prime Number App")

def give_options():
    print() # blank line
    print("Enter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")

def get_option():
    option = input("Enter your choice 1 or 2: ")
    return option

def check_if_prime(user_num):
    is_prime = True # initialize result
    for j in range(2, user_num):
        if user_num % j == 0: # check if number is divisible
            is_prime = False
            break
    return is_prime

def test_check_if_prime_true():
    assert check_if_prime(11) == True

def test_check_if_prime_false():
    assert check_if_prime(100) == False

def run_again():
    res = input("Would you like to run the program again? (y/n): ")
    res = res.lower()
    res = res.rstrip()
    if res == "y" or res == "yes":
        return True
    else:
        return False

def get_bounds():
    print() # blank line
    lower_bound = input("Enter the lower bound of your range: ")
    lower_bound = int(lower_bound) # convert input string type to integer type
    upper_bound = input("Enter the lower bound of your range: ")
    upper_bound = int(upper_bound) # convert input string type to integer type
    return (lower_bound, upper_bound)

def calculate_duration(lower_bound, upper_bound):
    start = time.time() # start of time to calculate primes
    list_of_primes = [] #initialize blank list
    for j in range(lower_bound, upper_bound +1):
        if check_if_prime(j):
            list_of_primes.append(j)
    end = time.time() # end of time to calculate primes
    duration = end - start
    return (list_of_primes, duration)

def calculate_primes():
    (lower_bound, upper_bound) = get_bounds()
    (list_of_primes, duration) = calculate_duration(lower_bound, upper_bound)
    print() # blank line
    print("Calculations took a total of {:.3f} seconds.".format(duration))
    print("The following numbers between {} and {} are prime:".format(lower_bound, upper_bound))
    return list_of_primes

def test_calculate_primes(mocker):
    mocker.patch("PrimeNumber_While_Challenge_3.get_bounds", return_value = (11,21))
    assert calculate_primes() == [11,13,17,19]


def main():
    welcome()
    main_loop_boolean = True
    
    while main_loop_boolean:
        give_options()
        option = get_option()
        
        if option == "1":
            print() # blank line
            user_num = input("Enter a number to determine if it is prime or not: ")
            user_num = int(user_num)
            is_prime = check_if_prime(user_num)
        
            if is_prime:
                print("{} is prime!".format(user_num))
            else:
                print("{} is not prime!".format(user_num))
        elif option == "2":
            list_of_primes = calculate_primes()
            res = input("Press enter to continue and show {} primes.".format(len(list_of_primes)))
            for j in list_of_primes:
                print(j)
        else:
            print() # blank line
            print("That is not a valid option.")
        
        main_loop_boolean = run_again()

# Main code
if __name__ == "__main__":
    main()
