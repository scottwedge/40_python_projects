#!/usr/bin/env python3

# Black Jack application

# Welcome user
# State miniumum bet
# Ask how much money to play with
# State current balance
# Ask what the bet is (minimum of $20)
# State current money and current bet
# Show dealer card
# Show player's two card hand and total
# Ask if want to hit
# If no, state how many cards dealer has
# Press enter to show dealer cards
# List dealers total and who won

# Imports
import random


# Functions
def welcome():
    print("Welcome to the Blackjack App.")
    print("The minimum bet at this table is #20.")

def get_starting_balance():
    balance = input("How much money are you willing to play with today: ")
    balance = int(balance)
    return balance

def get_bet():
    bet = input("What would you like to bet (minimum bet of 20): ")
    bet = int(bet)
    if bet < 20:
        bet = 20
    return bet

def init_deck():  # create deck of cards
    deck = []
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card = ["2", "3", "4","5","6","7","8","9","J", "Q","K", "A"]
    for j in card:
        for k in suit:
            deck.append((j, k)) # append tuple
    return deck

def get_card(deck):
    index = random.randint(1,len(deck))
    card = deck.pop(index)
    return(card, deck)

def current_money(balance, bet):
    print() # blank line
    print("Current Money: ${}\t\tCurrent Bet: ${}".format(balance, bet))

def dealer_showing(dealer_cards):
    (card, suit) = dealer_cards[0]
    print("The dealer is showing a {} of {}.".format(card, suit))

    

# Main code
welcome()
balance = get_starting_balance()
bet = get_bet()
deck = init_deck()
dealer_cards = []
player_cards = []
(card, deck) = get_card(deck)
dealer_cards.append(card)  # first card for dealer
current_money(balance, bet)
dealer_showing(dealer_cards)

print("Player's Hand:")
(card, deck) = get_card(deck)
player_cards.append(card)     # first player card
(card, deck) = get_card(deck)
player_cards.append(card)     # second player card
for j in range(len(player_cards)):
    (value, suit) = player_cards[j]
    print("{} of {}".format(value, suit))

# Print value of player's hand
sum = 0
for j in range(len(player_cards)):
    (card, suit) = player_cards[j]
    if card in ["J", "Q", "K"]:
        sum = sum + 10
    elif card in "A":
        sum = sum + 11   # Need to handle case of Ace = 1 
    else:
        sum = sum + int(card)   # convert string type 2..9 to integer type
print("Total value: {}".format(sum))
print() # blank line
hit = input("Would you like to hit (y/n): ")
print() # blank line


