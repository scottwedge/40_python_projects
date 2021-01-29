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

# Functions
def capitalize_food(food):
    # Convert to lower case
    food = food.lower()
    # Capitalize first letter
    cap_lower_food = food.capitalize()
    return cap_lower_food

# Get current time
now = datetime.datetime.now()

# Initialize list with two items
glist = ["Milk", "Apples"]

print("Welcome to the Grocery List App")
print("Current Date and Time:  {}/{}    {}:{}".format(now.month, now.day, now.hour, now.minute))

# Display current (two item) list
print("You currently have {} and {} in your list.".format(glist[0], glist[1]))
print() # blank line

# Prompt for three more food types
for j in range(1,4,1):
    newfood = input("Type of food to add to the grocery list: ")
    cap_lower_food = capitalize_food(newfood)

    # Convert to lower case
    newfood = newfood.lower()
    # Capitalize new food
    cap_lower_newfood = newfood.capitalize()
    # Add to list
    glist.append(cap_lower_newfood)

# Display sorted list
print("Here is your grocery list: ", glist)

# Sort list alphabetically
sorted_glist = glist
sorted_glist.sort()

# Display sorted list
print("Here is your grocery list sorted: ", sorted_glist)

print("Simulating grocery shopping...")
print() # blank line

# Prompt three times to remove item from the list
for j in range(1,4,1):
    # Print current list
    print("Current grocery list: {} items.".format(len(sorted_glist)))
    print(sorted_glist)
    purchase = input("What food did you just buy: ")
    cap_purchase = capitalize_food(purchase)
    print("Removing {} from the list...".format(cap_purchase))
    sorted_glist.remove(cap_purchase)
    print() # blank line


