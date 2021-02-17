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
    print() # blank line

def join_party():
    party = input("What party would you like to join: ")
    print() # blank line
    return party.title() # convert any case to title case

def party_status(party):
    if party == ("Republican" or "Democratic"):
        print("That is a major party!")
    else:
        print("That is not a major party.")

def congrats(name, party):
    print("Congratulations {}!  You have joined the {} party!".format(name, party))


def main():
    header()
    name = get_name()
    age = get_age()
    
    # check if age is allowed to vote
    
    if age < MIN_AGE:
        print("You are not old enough to register to vote")
    else:
        list_parties()
        party = join_party()
        congrats(name, party)
        party_status(party)


if __name__ == "__main__":
    main()
