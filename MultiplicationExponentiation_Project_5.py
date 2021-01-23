#!/usr/bin/env python3

# Script to print both multiplication and exponentiation table
# From range of 1 to 9 inclusive.

# Print welcome message 
print("Welcome to the Multiplication/Exponentiation application.")

# Prompt for user name
user_name = input("What is your name: ")

# Prompt for number to work with
user_number = input("What number do you want to work with: ")

# Convert input to float number (from character string)
num = float(user_number)


# Display multiplication table for 1 through 9
print() # blank line
print("Multiplication table for", user_number)

for n in range(9):
    print(n," *", num, "=", num * n)
    

# Display exponentiation table for 1 through 9
print()  # blank line
print("Exponentiation table for", user_number)

# Print math is cool four times
phrase = "math is cool"
print(user_name, phrase)
