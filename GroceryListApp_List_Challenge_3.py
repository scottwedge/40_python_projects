#!/usr/bin/env python3

# Script will use datetime module to display current time when shopping occurs.
# Script that starts with two items in shopping list.
# Then will prompt for three more items so there are five items total.
# Sort list alphabetically and display the list.
# Then remove three items (spelled in any case) from list when prompted
# When two items remain, say requested purchase not available
# Remove it from list and add another item

# Imports
import datetime

# Get current time
now = datetime.datetime.now()

# Initialize list with two items
glist = ["Milk", "Apples"]

print("Welcome to the Grocery List App")
print("Current Date and Time:  {}/{}    {}:{}".format(now.month, now.day, now.hour, now.minute))

# Display current (two item) list
print("You currently have {} and {} in your list.".format(glist[0], glist[1]))

