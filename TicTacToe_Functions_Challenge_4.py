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

def switch_sides(side_X):
    return not side_X

def all_spots_taken(guesses):
    if "_" not in guesses:
        print("All spots taken")
        return True
    else:
        return False
        
def place_piece(side_X, guesses):
    loop_again = True
    while loop_again:
        position = input("{}: Where would you like to place your piece (1-9): ".format(side(side_X)))
        position = int(position)     # convert input string type to integer type
        # check if position was taken already
        if guesses[position - 1] == "_": 
            guesses[position - 1] = side(side_X)
            loop_again = False
        else:
            print("Position already taken - guess again!")
            loop_again = True
    return guesses

def three_in_a_row(g):  # determine if anyone has three in a row (and wins)
    if g[0] == g[1] == g[2] == "O" or \
    g[3] == g[4] == g[5] == "O" or \
    g[6] == g[7] == g[8] == "O" or \
    g[0] == g[3] == g[6] == "O" or \
    g[1] == g[4] == g[7] == "O" or \
    g[2] == g[5] == g[8] == "O" or \
    g[0] == g[4] == g[8] == "O" or \
    g[6] == g[4] == g[2] == "O":
        return (True, "O")
    elif g[0] == g[1] == g[2] == "X" or \
    g[3] == g[4] == g[5] == "X" or \
    g[6] == g[7] == g[8] == "X" or \
    g[0] == g[3] == g[6] == "X" or \
    g[1] == g[4] == g[7] == "X" or \
    g[2] == g[5] == g[8] == "X" or \
    g[0] == g[4] == g[8] == "X" or \
    g[6] == g[4] == g[2] == "X":
        return (True, "X")
    else:
        return (False, "F")

# Main code
# Init variables
guesses = init_guesses()
side_X = True
run_forever = True  # while loop boolean
game_over = False  # set to True when all spots taken 
winner = False # set to True when player wins with three in a row

while run_forever:
    position_board()
    game_board(guesses)
    if all_spots_taken(guesses):
        break
    (winner, who_wins) = three_in_a_row(guesses)
    if winner:
        print(who_wins,"WINS!!")
        break    
    side_X = switch_sides(side_X)
    guesses = place_piece(side_X, guesses)
