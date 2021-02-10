#!/usr/bin/env python3

# Prompt for user name
# If user in system user list, Welcome user
# If user not in system, say "sorry you do not have an account and Goodbye"
# List current shipping prices
# Prompt for how many items to ship
# State how much the shipping cost will be
# Prompt if the order should be places
# If yes, state shipping the items

# Functions
def header():
    print("Welcome to the Shipping Accounts Program")
    print() # blank line

def user_list():
    users = ["me", "you", "us", "them"]
    return users

def qty_to_cost(min, max, cost):
    print("Shipping orders {} to {}:\t\t${} each".format(min, max, cost))

def qty_over_cost(min, cost):
    print("Shipping orders over {}:\t\t${} each".format(min, cost))

def current_shipping_prices():
    print("Current shipping prices are as follows:")
    print() # blank line
    qty_to_cost(0, 100, "5.10")
    qty_to_cost(100, 500, "5.00")
    qty_to_cost(500, 1000, "4.95")
    qty_over_cost(1000, "4.80")




header()

name = input("Hello, what is your username: ")
print() # blank line

if name not in user_list():
    print("You do not have an account. Goodbye.") # not a valid user - program stops here
else:
    print("Hello {}. Welcome back to your account.".format(name))

    current_shipping_prices()
