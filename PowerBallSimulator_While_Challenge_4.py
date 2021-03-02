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
import random

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

def test_calculate_odds_10_1():
    assert calculate_odds(10, 1) == 252

def test_calculate_odds_69_26():
    assert calculate_odds(69, 26) == 292201338 

def get_ticket_purchase_interval():
    interval = int(input("Purchase tickets in what interval: "))
    return interval

def generate_available_wb_list(count):
    available_wb = []
    for j in range(1, count+1):
        available_wb.append(j)
    return available_wb
    
def pick_winning_white(white_bc):
    winner_white = []
    available_wb = generate_available_wb_list(white_bc)
    for j in range(5):
        random.seed()
        l = len(available_wb)
        list_index = random.randint(0,l-1)  
        chosen_ball = available_wb[list_index]
        available_wb.remove(chosen_ball)   # remove selected ball from available list
        winner_white.append(chosen_ball) # add selected ball to winner list
    winner_white.sort()  # sort white balls into numerical order
    return winner_white

def pick_winning_red(red_bc):
    random.seed()
    winner_red = random.randint(1,red_bc)
    return winner_red

def pick_winning_white_and_red_combo(white_bc, red_bc):
    winner = pick_winning_white(white_bc)
    winner_red = pick_winning_red(red_bc)
    winner.append(winner_red)  # combine white and red winners
    return l_to_s(winner)  # convert to string

def l_to_s(l): # convert list of integers to string with separator of " "
    s = ""
    for j in range(len(l) - 1):
        s = s + str(l[j]) + " "
    s = s + str(l[-1])  # add last digit in list
    return s

def buy_tickets(white_bc, red_bc, interval, winner, chosen_tickets):
    game_over_boolean = False
    while interval > 0:
        ticket = pick_winning_white_and_red_combo(white_bc, red_bc)
        if ticket == winner:
            l = len(chosen_tickets)
            game_over_boolean = True
            print() # blank line
            print("Congrats on picking winning ticket",ticket)
            print("Purchased a total of {} tickets.".format(l))
            chosen_tickets.append(ticket)
            break
        elif ticket not in chosen_tickets:
            print(ticket)
            chosen_tickets.append(ticket)
            interval = interval - 1 
        else:
            print(ticket, "Losing ticket generated; disregard...") # skip this repeat
    return (chosen_tickets, game_over_boolean)

def play_again(chosen_tickets, winner): 
    if winner not in chosen_tickets:
        print("{} tickets purchased so far with no winners...".format(len(chosen_tickets)))
        print() # blank line
        reply = input("Keep purchasing tickets (y/n): ")
        reply = reply.lower()  # convert to lower case
        reply = reply.rstrip() # remove all trailing white space
        if reply == "y" or reply == "yes":
            return True
        else:
            goodbye(chosen_tickets)
            return False
    else:
        pass

def goodbye(chosen_tickets):
    print() # blank line
    print("You bought {} tickets and still lost!".format(len(chosen_tickets)))
    print("Better luck next time!")
    

def main():
    print(intro())
    white_bc = get_white_ball_count()
    red_bc = get_red_ball_count()
    odds = calculate_odds(white_bc, red_bc)
    print("You have a one in {} chance of winning this lottery.".format(odds))
    interval = get_ticket_purchase_interval()

    # Generate winning combination (and sort numerically)
    winner = pick_winning_white_and_red_combo(white_bc, red_bc)
    print() # blank line
    print("Tonight's winning numbers are:",winner)

    # Start buying unique tickets
    start = input("Press 'Enter' to begin purchasing tickets!!!")
    chosen_tickets = [] # initialize list of chosen tickets
    game_over_boolean = False
    keep_playing = True
    while not game_over_boolean and keep_playing:
        (chosen_tickets, game_over_boolean) = buy_tickets(white_bc, red_bc, interval, winner, chosen_tickets)
        keep_playing = play_again(chosen_tickets, winner)


# Main code
if __name__ == "__main__":
    main()
