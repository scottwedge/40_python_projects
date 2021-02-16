#!/usr/bin/env python3

# Welcome user
# Get number of coin flip attempts to do
# Ask if want to see results of each flip, or not
# Display when number of heads = number of tails
# Display summary of all results for each side: count and percentage

# Imports
import random

# Functions
def header():
    print("Welcome to the Coin Toss App")
    print() # blank line

def get_number():
    print("I will flip a coin a set number of times.")
    num = input("How many times would you like me to flip the coin: ")
    num = int(num) # Convert input string type to integer type
    return num

def get_see_result():
    see_result = input("Would you like to see the result of each flip (y/n): ")
    see_result = see_result.lower() # convert to lower case (handle Y/N)
    return see_result

def flip():
    # random value either 0 or 1, if 1 then "HEADS"
    random.seed()
    result = random.randint(0,1)
    if result == 1:
        return True # result of HEADS
    else:
        return False # result of TAILS

def summary_results(num, head_count, tail_count):
    print() # blank line
    print("Results of Flipping a Coin {} Times".format(num))
    print() # blank line
    print("Side \t\t Count \t\t Percentage")
    print("Heads \t\t {}/{} \t {:.1f}".format(head_count, num, head_count/num * 100))
    print("Tails \t\t {}/{} \t {:.1f}".format(tail_count, num, tail_count/num * 100))

def main():
    header()
    
    num = get_number()
    
    see_result = get_see_result()
    
    # Initialize counters
    head_count = 0
    tail_count = 0 
    
    print("Flipping...")
    for j in range (num):
       res = flip()
       if res == True:
           head_count = head_count + 1
           if see_result == "y": print("HEAD")
       else:
           tail_count = tail_count + 1
           if see_result == "y": print("TAILS")
       if head_count == tail_count and see_result == "y":
           print("At {} flips, the number of heads and tails were equal at {},{} each.".format(head_count + tail_count, head_count, tail_count))
    
    # Print summary of all coin tosses
    summary_results(num, head_count, tail_count)

if __name__ == "__main__":
    main()
