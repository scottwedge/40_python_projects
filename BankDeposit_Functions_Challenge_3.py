#!/usr/bin/env python3

# Bank Deposit App

# Welcome user
# set name
# Setup balance in Savings Account
# Setup balance in Chequing Account
# Allowed to deposit
# Allowed to withdraw if not get negative balance
# Display current account info after every event
# Offer to perform another transaction

# Functions
def welcome():
    print("Welcome to the Python First National Bank.")

def get_name():
    print() # blank line
    name = input("Hello, what is your name: ")
    name = name.title()
    return name

def get_savings_balance():
    savings = input("How much money would you like to set up your savings account: ")
    savings = float(savings) # convert from string type to float type
    return savings

def get_checking_balance():
    checking = input("How much money would you like to set up your checking account: ")
    checking = float(checking) # convert from string to float type
    return checking

def current_info(name, savings, checking):
    print() # blank line
    print("Current Account Information")
    print("Name: {}".format(name.title()))
    print("Savings: ${}".format(savings))
    print("Checking: ${}".format(checking))

def get_account():
    print() # blank line
    account = input("What account would you like to access (Savings or Checking): ")
    return account

def get_trans():
    trans = input("What type of transaction would you like to make (Deposit or Withdrawl): ")
    trans = trans.lower()
    trans = trans.rstrip()
    return trans

def get_amount():
    amount = float(input("How much money: "))
    amount = float(amount) # convert from string type to float type
    return amount

# Main code
welcome()
name = get_name()
savings = get_savings_balance()
checking = get_checking_balance()
current_info(name, savings, checking)

# Perform transaction
account = get_account()
trans = get_trans()
amount = get_amount()

if trans == "deposit":
    print() # blank line
    print("Deposited ${} into {}'s {} account.".format(amount, name.title(), trans))
elif:
    trans == "withdrawl":
    print() # blank line
    print("Withdrew ${} from {}'s {} account.".format(amount, name.title(), trans))


