#!/usr/bin/env python3

# Analyze the letter distribution of a given text
# Take any text, 
# Remove any non-alpha characters,
# Count the frequency of each letter in the text
# Calculate the percentage of occurrence of each letter
# Create a list of letters ordered from highest occurrence to lowest occurrence
# For two different bodies of text

# Imports
import string

# Constants
NUM_LOOP = 2 # number of phrases to enter 

# Functions
def welcome():
    print("Welcome to the Frequency Analysis App")

def get_text():
    print() # blank line
    text = input("Enter a word or phrase to count the occurrences of each letter: ")
    return text

def print_results(round, alpha_count_db):
        print() # blank line
        print("Here is the frequency analysis from key phrase {}:".format(round + 1))
        print() # blank line
        print("\t{:<15} {:<15} {:<15}".format("Letter", "Occurrence", "Percentage"))
        
        # Determine sum of letters for percentage calculation
        sum = 0
        for value in alpha_count_db.values():
            sum = sum + value
        
        for key in alpha_count_db.keys():
            print("\t{:<15} {:<15} {:.2f}%".format(key, alpha_count_db[key], 100 * alpha_count_db[key]/sum))
        
        # To sort k,v dict in descending numerical order of v: 
        # create list of v,k tuples,
        # then sort list numerically to get ascending order, 
        # Then reverse sort list to get descending numerical order
        
        alpha_list = []
        for k,v in alpha_count_db.items():
            alpha_list.append((v,k))
        
        alpha_list.sort() # sort in ascending numerical order
        
        alpha_list.reverse() # sort in descending numerical order
        
        most_to_least = ""
        for j in range(len(alpha_list)):
            (v,k) = alpha_list[j]
            most_to_least = most_to_least + k
        
        print() # blank line
        print("Letters ordered from highest occurrence to lowest:")
        print(most_to_least)

def missing_letters(alpha_count_db): # determine what letters are missing from text string
    missing_char = ""
    a_to_z_string = string.ascii_lowercase  # create a through z string
    a_to_z_list = list(a_to_z_string)
    for j in range(len(a_to_z_list)):
        if a_to_z_list[j] not in alpha_count_db.keys():
            missing_char += a_to_z_list[j]
    return missing_char 


def main():
    welcome()
    
    for round in range(NUM_LOOP):
        
        text = get_text()
        
        # Analyze text
        alpha_count_db = {} # initialize blank alphabet dictionary
        text = text.lower() # convert to all lower case
        text_list = list(text) # convert text string to list of characters
        
        for j in range(len(text_list)):
            if text_list[j].isalpha():  # if alphanumeric
                if text_list[j] in alpha_count_db.keys(): # check if key already exists
                    alpha_count_db[text_list[j]] = alpha_count_db[text_list[j]] + 1 # increment counter
                else:
                    alpha_count_db[text_list[j]] = 1 # initialize counter
        
        # print results
        print_results(round, alpha_count_db) 

        missed = missing_letters(alpha_count_db)
        print() # blank line
        print("The following letters are not listed: {}".format(missed))

if __name__ == "__main__":
    main()
