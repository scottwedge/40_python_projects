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

# Tests
def test_upper_capitalize_food():
    assert capitalize_food("FISH") == "Fish"

def test_lower_capitalize_food():
    assert capitalize_food("beef") == "Beef"

def main():
    # get current time
    now = datetime.datetime.now()
    
    # initialize list with two items
    glist = ["Milk", "Apples"]
    
    print("Welcome to the Grocery List App")
    print("Current Date and Time:  {}/{}    {}:{}".format(now.month, now.day, now.hour, now.minute))
    
    # display current (two item) list
    print("You currently have {} and {} in your list.".format(glist[0], glist[1]))
    print() # blank line
    
    # prompt for three more food types
    for j in range(1,4,1):
        newfood = input("Type of food to add to the grocery list: ")
        cap_lower_food = capitalize_food(newfood)
    
        # Add to list
        glist.append(cap_lower_newfood)
    
    # display sorted list
    print("Here is your grocery list: ", glist)
    
    # sort list alphabetically
    sorted_glist = glist
    sorted_glist.sort()
    
    # display sorted list
    print("Here is your grocery list sorted: ", sorted_glist)
    
    print("Simulating grocery shopping...")
    print() # blank line
    
    # prompt three times to remove item from the list
    for j in range(1,4,1):
        # Print current list
        print("Current grocery list: {} items.".format(len(sorted_glist)))
        print(sorted_glist)
        purchase = input("What food did you just buy: ")
        cap_purchase = capitalize_food(purchase)
        print("Removing {} from the list...".format(cap_purchase))
        sorted_glist.remove(cap_purchase)
        print() # blank line
    
    # randomly choose one remaining item and say it is not available 
    # then prompt for a replacement
    out_of_stock = sorted_glist[0]
    print("Sorry the store is out of {}.".format(out_of_stock))
    replacement = input("What food would you like instead: ")
    capitalized_replacement = capitalize_food(replacement)
    sorted_glist.append(capitalized_replacement)
    
    print()
    print("Here is what remains on your grocery list: ")
    print(sorted_glist)

if __name__ == "__main__":
    main()
