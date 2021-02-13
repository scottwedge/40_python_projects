#!/usr/bin/env python3

# Welcome user to program
# Prompt for name for each basketball position
# Display aligned column lists for position and player name
# Announce one player is injured
# Prompt for replacement for that position
# Display count and aligned list of position and names of final team

# Imports
import random

def header():
    print("Welcome to the Basketball Roster program.")
    print() # blank line

def main():
    # Welcome user
    header()
    
    # List roster positions
    position = ["point guard", "shooting guard","small forward","power forward","center"]
    
    # Initialize roster as a dictionary
    roster = {}
    
    # Prompt for each position (point guard, shooting guard, small forward
    # power forward, center)
    
    for j in position:
        player = input("Who is your {}: ".format(j))
        roster[j] = player.title()  # convert name to title format
    
    # Display roster
    title = "Your starting 5 for the upcoming basketball season"
    print() # blank line
    print("{:^80}".format(title))
    
    for k in position:
        print("          {:20s} {:20s}".format(k.title(), roster[k]))
    
    # Simulate random injury
    inj_pos = random.randint(0,4)

    print() # blank line
    print("Oh no, {} is injured.".format(roster[position[inj_pos]]))
    print("Your roster only has 4 players.")
    player = input("Who will take {}'s spot: ".format(roster[position[inj_pos]]))
    roster[position[inj_pos]] = player.title()  # convert to title format
    
    # Display roster again
    print() # blank line
    print("Your starting 5 for the upcoming basketball season")
    
    for k in position:
        print("          {:20s} {:20s}".format(k.title(), roster[k]))
    
    # Wish new player best
    print() # blank line
    print("Good luck {} you will do great!".format(roster[position[0]]))
    print("Your roster now has 5 players.")
    
if __name__ == "__main__":
    main()
