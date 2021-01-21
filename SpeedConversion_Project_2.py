#!/usr/bin/env python3

# Project 2 converts user-input miles per hour speed to km per hour
# input value can be integer or float
# output value should be accurate to two decimal places
# Starts with a welcome banner before prompt for user input.

# Welcome message
print("Welcome to the Miles Per Hour to Meters Per Second Conversion App.")

# Prompt for user input
speed_mph = input("What is your speed in miles per hour? ")

# Convert from miles per hour to meter per second then round to two decimal places
speed_mps = speed_mph * 1.6

# Print output
print("Your speed in meters per second is: ", speed_mps)


