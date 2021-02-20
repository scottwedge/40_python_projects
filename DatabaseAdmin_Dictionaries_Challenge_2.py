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

def login(name):
    print() # blank line
    print("Hello {}! You are logged in!".format(name))

def change_password():
    change = input("Would you like to change your password (yes/no): ")
    change = change.lower() # convert to lower case
    if change == ("yes" or "y"):
        return True # boolean
    else:
        return False

def check_password(new_password):
    if len(new_password) < 8:  # check password is at least 8 characters long
        print("{} not the minimum eight characters.".format(new_password))
        return False
    else:
        return True

def print_database():
    print() # blank line
    print("Here is the current user database:")
    for key in database.keys():
        print("Username: {} \t\tPassword: {}".format(key, database[key]))

# setup database
database = {
	"user1" : "password1",
	"user2" : "password2",
	"admin00" : "admin1234"
        }

welcome()
name = get_username()

if name not in database.keys():
    print("Username not in database, goodbye.")
else:
    password = get_password()
    login(name)
    if name == "admin00":
        print_database()
    else:
        if change_password():
            new_password = input("What would you like your new password to be: ")
            if check_password(new_password):
                database[name] = new_password             
                print() # blank line
    
        print() # blank line
        print("{} your password is {}".format(name, database[name])) # print password whether changed or not
    
