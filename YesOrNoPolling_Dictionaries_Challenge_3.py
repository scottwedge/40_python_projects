#!/usr/bin/env python3

# Yes or No Polling Issue

# Conduct a poll on a yes or no issue
# Prompt user for an issue
# The number of voters
# And a password to view the poll results
# Then conduct the poll
# Ask for voters name
# If not yet voted, then display the issue and record the vote
# Polls close when all have voted
# Display summary of results
# If correct password is used, each voter's name and vote are displayed


# Functions
def welcome():
    print("Welcome to the Yes or No Issue Polling App")
    print() # blank line

def get_issue():
    issue = input("What is the yes or no issue you will be voting on today: ")
    return issue

def get_num():
    num = input("What is the number of voters you will allow on the issue: ")
    num = int(num) # convert from string type to integer type
    return num

def get_password():
    password = input("Enter a password for polling results: ")
    return password

def get_name():
    name = input("Enter your full name: ")
    return name

def show_issue(issue):
    print("Here is our issue: {}".format(issue))

def get_vote():
    vote = input("What do you think...yes or no: ")
    return vote
    
# Initialize variables
voting_db = {}


welcome()
issue = get_issue()
num = get_num()
password = get_password()

for j in range(num):
    print() # blank line
    name = get_name()
    print(name)
    show_issue(issue)
    vote = get_vote()
    voting_db[name] = vote # add vote to db
