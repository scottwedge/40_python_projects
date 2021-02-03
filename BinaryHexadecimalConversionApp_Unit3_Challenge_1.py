#!/usr/bin/env python3

# Print welcome header
# Prompt for decimal number
# Generate lists
# Using slices, show a portion of each list
# Prompt for decimal value to start at
# Prompt for decimal number to stop at
# List decimal values in that portion
# List binary values in that portion
# List hexadecimal values in that portion
# Prompt for user to press enter to display all values
# using format of decimal number then binary then hexadecimal on same line separated by "----"


# print welcome banner
print("Welcome to the Binary/Hexadecimal Converter app")

# get value
val = input("Compute binary and hexidecimal values up to the following decimal number: ")
val = int(val) # convert string to integer
print("Generating lists .... complete!")

# Get range of slice to display
print("Using slices, we will now show a portion of each list.")
min = input("What decimal number would you like to start at: ")
min = int(min) # convert string to integer
max = input("What decimal number would you like to stop at: ")
max = int(max) # convert string to integer

print() # blank line
print("Decimal values from {} to {}:".format(min, max))
for j in range(min, max+1):
    print(j)

print() # blank line
print("Binary values from {} to {}:".format(min, max))
for j in range(min, max+1):
    print(bin(j))

print() # blank line
print("Hexadecimal values from {} to {}:".format(min, max))
for j in range(min, max+1):
    print(hex(j))

