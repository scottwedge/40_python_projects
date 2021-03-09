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
    print("The minimum bet at this table is $20.")

def get_starting_balance():
    print() # blank line
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
    card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K", "A"]
    for j in card:
        for k in suit:
            deck.append((j, k)) # append tuple
    return deck

def get_card(deck):
    index = random.randint(0,len(deck) - 1)
    card = deck.pop(index)
    return(card, deck)

def current_money(balance, bet):
    print() # blank line
    print("Current Money: ${}\t\tCurrent Bet: ${}".format(balance, bet))

def dealer_showing(dealer_cards):
    (card, suit) = dealer_cards[0]
    print("The dealer is showing a {} of {}.".format(card, suit))

def sort_cards(cards): # put Ace at end of list of cards
    if "A" in cards:
        cards.remove("A")
        cards.append("A")
    return cards

def card_sum(cards):
    cards = sort_cards(cards)
    sum = 0
    for j in cards:
        (card, suit) = j
        if card in ["J", "Q", "K"]:
            sum = sum + 10
        elif card in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            sum = sum + int(card)   # convert to integer type
        else:   # card is Ace
            if sum <= 10:
                sum = sum + 11 # treat Ace as 11
            else:
                sum = sum + 1 # treat Ace as 1 
    return sum
    
def get_dealer_cards(deck):    
    DEALER_MAX = 17
    dealer_sum = 0
    dealer_cards = []
    while dealer_sum <= DEALER_MAX:
        (card, deck) = get_card(deck)
        dealer_cards.append(card)  # card for dealer
        dealer_sum = card_sum(dealer_cards)
    return (dealer_cards, dealer_sum, deck)

# Main code
DEALER_MAX = 17
dealer_sum = 0
player_sum = 0
welcome()
balance = get_starting_balance()
bet = get_bet()
deck = init_deck()
dealer_cards = []
player_cards = []

# Determine dealer's hand but only show first card
(dealer_cards, dealer_sum, deck) = get_dealer_cards(deck)
print("DEBUG..  DEALER CARDS are: ",dealer_cards) # DEBUG
current_money(balance, bet)
dealer_showing(dealer_cards)

print() # blank line
print("Player's Hand:")
(card, deck) = get_card(deck)
player_cards.append(card)     # first player card
(card, deck) = get_card(deck)
player_cards.append(card)     # second player card
for j in player_cards:
    (value, suit) = j
    print("{} of {}".format(value, suit))

continue_player_hand = True
while continue_player_hand:
    # Print value of player's hand
    player_sum = 0
    for j in player_cards:
        (card, suit) = j
        if card in ["J", "Q", "K"]:
            player_sum = player_sum + 10
        elif card in ["A"]:
            player_sum = player_sum + 11   # Need to handle case of Ace = 1 
        else:
            player_sum = player_sum + int(card)   # convert string type 2..9 to integer type
    
    print("Total value: {}".format(player_sum))
    if player_sum > 21:
        continue_player_hand = False
    else:
        hit = input("Would you like to hit (y/n): ")
        print() # blank line
    
        if hit == "y" or hit == "yes":
            (card, deck) = get_card(deck)
            player_cards.append(card) 
            continue_player_hand = True
        else:
            continue_player_hand = False

print("Dealer is set with a total of {} cards.".format(len(dealer_cards)))
print() # blank line
result = input("Press enter to reveal the dealer's hand.")
for j in dealer_cards:
    (card, suit) = j
    print("{} of {}".format(card, suit))
if dealer_sum > 21:
    print("Dealer sum of {} - Dealer went over 21. You win!".format(dealer_sum))
else:
    print("Dealer total of {}".format(dealer_sum))

