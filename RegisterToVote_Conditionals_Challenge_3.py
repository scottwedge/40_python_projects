#!/usr/bin/env python3

# A Register To Vote application that simulates a user registering to vote

# Get user name
# Get user age
# Check user age 
# Give list of parties that one can join
# Get party (case insensitive) to join from user
# State user has been registered to that party
# State whether it is a major party or not

# Constants
MIN_AGE = 18

# Functions
def header():
    print("Welcome to the Voter Registration App.")
    print() # blank line

def get_name():
    name = input("Please enter your name: ")
    return name

def get_age():
    age = input("What is your age: ")
    age = int(age) # convert input string type to integer type
    return age

def congrats(name):
    print("Congratulations {}! You are old enough to register to vote.".format(name))
    print() # blank line

def list_parties():
    print("Here is a list of political parties to join.")
    party_list = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]
    for j in party_list:
        print("\t- {}".format(j))


header()
name = get_name()
age = get_age()

# check if age is allowed to vote

if age < MIN_AGE:
    print("You are not old enough to register to vote")
else:
    congrats(name)
    list_parties()
    
