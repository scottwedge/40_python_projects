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



# Main code
welcome()
name = get_name()
savings = get_savings_balance()
checking = get_checking_balance()
