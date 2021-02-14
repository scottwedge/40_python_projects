#!/usr/bin/env python3

# Project 2 converts user-input miles per hour speed to km per hour
# input value can be integer or float
# output value should be accurate to two decimal places
# Starts with a welcome banner before prompt for user input.

# Tests
def test_convert_mph_to_mps():
    assert convert_mph_to_mps(100) == 160

# Functions
def header():
    print("Welcome to the Miles Per Hour to Meters Per Second Conversion App.")

def convert_mph_to_mps(speed_mph):
    speed_mps = speed_mph * 1.6
    return speed_mps

def main():
    # Welcome message
    header()
    
    # Prompt for user input
    user_speed = input("What is your speed in miles per hour? ")
    
    # Convert input to float type
    speed_mph = float(user_speed)
    
    # Convert from miles per hour to meter per second then round to two decimal places
    speed_mps = convert_mph_to_mps(speed_mph)
    
    # Print output
    print("Your speed in meters per second is {:.2f} .".format(speed_mps))
    
if __name__ == "__main__":
    main()
