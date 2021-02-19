#!/usr/bin/env python3

# Database Administrator simulator program
# Simulate logging into database and prompt user to change password
# All usernames and passwords will be stored in a dictionary
# After enter correct credentials, program will prompt user for a new password
# New password must be at least 8 characters long
# Accept new password if valid, else reject it
# If logged in user is an Admin, all the usernames and passwords will be displayed


# Functions
def welcome():
    print("Welcome to the Database Admin Program")
    print() # blank line

def get_username():
    name = input("Enter your username: ")
    return name

def get_password():
    password = input("Enter your password: ")
    return password



welcome()
name = get_username()
password = get_password()
