#!/usr/bin/env python3

# A Register To Vote application

# Get user name
# Get user age
# Check user age 
# Give list of parties that one can join
# Get party (case insensitive) to join from user
# State user has been registered to that party
# State whether it is a major party or not


def header():
    print("Welcome to the Voter Registration App.")
    print() # blank line

def get_name():
    name = input("Please enter your name: ")
    return name


header()
name = get_name()
