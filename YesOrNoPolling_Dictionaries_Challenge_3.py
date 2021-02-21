#!/usr/bin/env python3

# Yes or No Polling Issue

# Conduct a poll on a yes or no issue
# Prompt user for an issue
# The number of voters
# And a password to view the poll results
# Then conduct the poll
# Ask for voters name
# If not yet voted, then display the issue and record the vote
# If already voted then warn that that name has already voted.
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
    num = num.rstrip() # strip trailing white space
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
    vote = vote.lower() # convert to lower case
    vote = vote.rstrip() # strip trailing white space
    return vote

def print_who_voted(voting_db):
    print("The following {} people voted:".format(len(voting_db.keys())))
    for key in voting_db.keys():
        print(key)

def print_winner(issue, voting_db):
    print() # blank line
    print("On the following issue: {}".format(issue))
    yes_count = 0
    no_count = 0
    other_count = 0
    for j in voting_db.values():
        if j == "no":
            no_count = no_count + 1
        elif j == "yes":
            yes_count = yes_count + 1
        else:
            other_count = other_count + 1 # for something other that 'yes' or 'no'

    if yes_count == no_count:
        print("A tie! {} votes to {}.".format(yes_count, no_count))
    elif yes_count > no_count:
        print("Yes wins! {} votes to {}.".format(yes_count, no_count))
    else:
        print("No wins! {} votes to {}.".format(no_count, yes_count))

def print_vote_results(password, voting_db):
    print() # blank line
    passwd = input("To see the voting results enter the admin password: ")
    if passwd == password:
        for key in voting_db.keys():
            print("Voter: {:<40}  Vote: {}".format(key, voting_db[key]))



# Initialize variables
voting_db = {}


welcome()
issue = get_issue()
num = get_num()
password = get_password()

for j in range(num):
    print() # blank line
    name = get_name()
    if name in voting_db.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        show_issue(issue)
        vote = get_vote()
        voting_db[name] = vote # add vote to db
        print("Thank you {}! Your vote of {} has been recorded.".format(name, vote))

print_who_voted(voting_db)

print_winner(issue, voting_db)

print_vote_results(password, voting_db)
