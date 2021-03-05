#!/usr/bin/env python3 

# Tic Tac Toe game

# Display board with positions numbered
# above board with taken (X or O) and free ('_') positions
# Alternate between users
# Three in a row wins


# Functions
def draw_board(g):
    print() # blank line
    print("\t   Tic-Tac-Toe")
    print("\t-----------------")
    print("\t|| {} || {} || {} ||".format(g[0], g[1], g[2]))
    print("\t-----------------")
    print("\t|| {} || {} || {} ||".format(g[3], g[4], g[5]))
    print("\t-----------------")
    print("\t|| {} || {} || {} ||".format(g[6], g[7], g[8]))
    print("\t-----------------")

def position_board():
    draw_board("123456789")

def init_guesses():
    guesses = []
    for j in range(9):
        guesses.append("_") 
    return guesses
    
def game_board(guesses):
    draw_board(guesses)

def get_side(previous_side):
    return not previous_side

def side(side_X):
    if side_X:
        return "X"
    else:
        return "O"

def place_piece(side_X, guesses):
    position = input("{}: Where would you like to place your piece (1-9): ".format(side(side_X)))
    position = int(position)     # convert input string type to integer type
    # check if position was taken already
    if guesses[position - 1] == "_": 
        guesses[position - 1] = side(side_X)
    return guesses

# Main code
# Init variables
guesses = init_guesses()
side_X = True
run_forever = True  # while loop boolean

while run_forever:
    position_board()
    game_board(guesses)
    guesses = place_piece(side_X, guesses)
