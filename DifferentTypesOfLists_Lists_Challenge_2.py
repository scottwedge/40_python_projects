#!/usr/bin/env python3

# Highlight similarities and differences of four types of lists 
# Lists of strings, integers, floats and lists.
# For each list, compare its data type, the elements of the list, and the type of the first element.

# Then sort each list numerically and alphabetically

# Setup each of the four lists to match contents in the demo example
num_strings = ["15", "100", "55", "43"]
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857] 
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_list_names = ["num_strings", "num_ints", "num_floats", "num_lists"]
list_of_list_contents = [num_strings, num_ints, num_floats, num_lists]


# Print welcome message of "Summary Table", centred on line
title = "Summary Table"
centred_title = title.center(80)
print(centred_title)
print() # blank line

# Cycle through each list
for num in range(len(list_of_list_names)):
    print("The variable {} is a {}.".format(list_of_list_names[num], type(list_of_list_contents[num])))
    print("It contains the elements: {}".format(list_of_list_contents[num]))
    print("The first element {} is a {}.".format(list_of_list_contents[num][0], type(list_of_list_contents[num][0])))
    print() # blank line

# Now sort and print list of strings and list of integers and display results
print("Now sorting num_strings and num_ints...")
num_strings.sort()
num_ints.sort()
print("Sorted num_strings: {}".format(num_strings))
print("Sorted num_ints: {}".format(num_ints)) 
