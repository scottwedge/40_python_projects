#!/usr/bin/env python3

# PowerBall simulator

# Print title
# Prompt user how many white balls to choose (normally 69)
# Prompt user how many red balls to choose (normally 26)
# Calculate odds
# Ask user how many tickets to purchase each interval
# Start game and welcome user
# Print winning numbers
# Press enter to start purchasing tickets
# Print tickets
# Must ensure tickets are unique

# Imports
from math import factorial as fact

# Functions
def intro():
    return "------------------- Power-Ball Simulator -----------------"

def get_white_ball_count():
    white_bc = input("How many white-balls to draw from for the 5 winning numbers (Normally 69): ")
    white_bc = int(white_bc)  # convert input string type to integer type
    return white_bc 

def get_red_ball_count():
    red_bc = input("How many red-balls to draw from for the 1 winning numbers (Normally 26): ")
    red_bc = int(red_bc)  # convert input string type to integer type
    return red_bc 

def calculate_odds(white_bc, red_bc):
    product = red_bc * fact(white_bc) / fact(white_bc - 5) / fact(5)
    return product

def get_ticket_purchase_interval():
    interval = int(input("Purchase tickets in what interval: "))
    return interval

def main():
    print(intro())
    white_bc = get_white_ball_count()
    red_bc = get_red_ball_count()
    odds = calculate_odds(white_bc, red_bc)
    print("You have a one in {} chance of winning this lottery.".format(odds))
    interval = get_ticket_purchase_interval()



# Main code
if __name__ == "__main__":
    main()
