#!/usr/bin/env python3

# Welcome user to program
# Prompt for name for each basketball position
# Display aligned column lists for position and player name
# Announce one player is injured
# Prompt for replacement for that position
# Display count and aligned list of position and names of final team


# Welcome user
print("Welcome to the Basketball Roster program.")
print() # blank line

# List roster positions
position = ["point guard", "shooting guard","small forward","power forward","center"]

# Initialize roster as a dictionary
roster = {}

# Prompt for each position (point guard, shooting guard, small forward
# power forward, center)

for j in position:
    player = input("Who is your {}:".format(j))
    roster[j] = player

# Display roster
print("Your starting 5 for the upcoming basketball season")

for k in position:
    print("           {}           {}".format(k, roster[k]))

