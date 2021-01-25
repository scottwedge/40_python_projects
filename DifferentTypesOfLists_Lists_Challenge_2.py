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
list_of_lists = [num_strings, num_ints, num_floats, num_lists]


# Print welcome message of "Summary Table", centred on line
title = "Summary Table"
centred_title = title.center(80)
print(centred_title)

# Cycle through each list
for j in list_of_lists:
    print(j)
#    print("The variable {} is a {}.".format(j, type(j))
#    print("It contains the elements: {}".format(list_of_lists[j]))
#    print("The first element {} is a {}.".format(list_of_lists[j].[0], type(list_of_lists[j].[0]))
