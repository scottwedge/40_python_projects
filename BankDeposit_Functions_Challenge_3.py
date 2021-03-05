#!/usr/bin/env python3

# Bank Deposit App

# Welcome user
# set name
# Setup balance in Savings Account
# Setup balance in Chequing Account
# Allowed to deposit
# Allowed to withdraw if not get negative balance
# Update account in successful
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
    trans = input("What type of transaction would you like to make (Deposit or Withdrawal): ")
    trans = trans.lower()
    trans = trans.rstrip()
    return trans

def get_amount():
    amount = float(input("How much money: "))
    amount = float(amount) # convert from string type to float type
    return amount

def balance(account, savings, checking):
    print(account)
    if account == "Savings":
        return savings
    else:
        return checking

def update_account(account, trans, savings, checking):
    # where account = "Savings" or "Checking"
    # trans = "Deposit" or "Withdrawl"
    # savings = balance of savings account
    # checking = balance of checking account
    if trans == "deposit":
        print() # blank line
        print("Deposited ${} into {}'s {} account.".format(amount, name.title(), account))
        if account == "Savings":
            savings = savings + amount
        else:
            checking = checking + amount
    elif trans == "withdrawal":
        if amount <= balance(account, savings, checking):
            print() # blank line
            print("Withdrew ${} from {}'s {} account.".format(amount, name.title(), account))
            if account == "Savings":
                savings = savings - amount
            else:
                checking = checking - amount
        else:
            print("Sorry, by withdrawing {} you will have a negative balance.".format(amount))
    else:
        print("ERROR. Neither Deposit nor Withdrawal selected")
    
    return (savings, checking)

def another_transaction():
    reply = input("Would you like to make another transaction (y/n): ")
    if reply == "y" or reply == "yes":
        return True
    else:
        return False

# Main code
welcome()
name = get_name()
savings = get_savings_balance()
checking = get_checking_balance()

loop_forever = True
while loop_forever:
    current_info(name, savings, checking)
    
    # Perform transaction
    account = get_account()
    trans = get_trans()
    amount = get_amount()
    
    (savings, checking) = update_account(account, trans, savings, checking)
    
    loop_forever = another_transaction()
