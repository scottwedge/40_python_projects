#!/usr/bin/env python3

# Black Jack application

# Welcome user
# State minimum bet
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
# Then automatically play again
# If balance < bet then quit game

# Imports
import random


# Functions
def welcome(MIN_BET):
    print("Welcome to the Blackjack App.")
    print("The minimum bet at this table is ${}.".format(MIN_BET))

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

def init_deck(card, suit):  # create deck of cards
    deck = []
    for j in card:
        for k in suit:
            deck.append((j, k)) # append tuple
    return deck

def get_card(deck):
    random.seed()
    index = random.randint(0,len(deck) - 1)
    card = deck.pop(index)
    return(card, deck)

def current_balance(balance):
    print() # blank line
    print("Current Money: ${}".format(balance))

def current_money_bet(balance, bet):
    print() # blank line
    print("Current Money: ${}\t\tCurrent Bet: ${}".format(balance, bet))

def dealer_showing(dealer_cards):
    (card, suit) = dealer_cards[0]
    print("The dealer is showing a {} of {}.".format(card, suit))

def sort_cards(suit_list, cards): # put Ace at end of list of cards
    for j in suit_list:
        if (("A", j)) in cards:
            cards.remove(("A", j))
            cards.append(("A", j))
        return cards

def card_sum(suit_list, cards):
    cards = sort_cards(suit_list, cards)
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
    
def get_dealer_cards(deck, DEALER_MAX):    
    dealer_sum = 0
    dealer_cards = []
    while dealer_sum <= DEALER_MAX:
        (card, deck) = get_card(deck)
        dealer_cards.append(card)  # card for dealer
        dealer_cards = sort_cards(suit_list, dealer_cards)
        dealer_sum = card_sum(suit_list, dealer_cards)
    return (dealer_cards, dealer_sum, deck)

def dealer_wins(balance, bet):
    balance = balance - bet
#    print("New balance is", balance)
    return balance

def player_wins(balance, bet):
    balance = balance + bet
#    print("New balance is", balance)
    return balance

def determine_winner(balance, player_sum, dealer_sum, HAND_MAX):
    if player_sum > HAND_MAX:
        print("Player went over {}...you lose!".format(HAND_MAX))
        balance = dealer_wins(balance, bet)
    elif dealer_sum > HAND_MAX:
        print("Dealer went over {}...you win!".format(HAND_MAX))
        balance = player_wins(balance, bet)
    elif player_sum > dealer_sum:
        print("Player wins with {} points. Dealer had {}.".format(player_sum, dealer_sum))
        balance = player_wins(balance, bet)
    else:
        print("Dealer wins with {} points. Player had {}.".format(dealer_sum, player_sum))
        balance = dealer_wins(balance, bet)
    return balance

# Main code
card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K", "A"]
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
DEALER_MAX = 17
HAND_MAX = 21
MIN_BET = 20
welcome(MIN_BET)
balance = get_starting_balance()
run_forever = True

while run_forever:
    dealer_sum = 0
    player_sum = 0
    current_balance(balance)
    bet = get_bet()
    deck = init_deck(card_list, suit_list)
    dealer_cards = []
    player_cards = []
    
    # Determine dealer's hand but only show first card
    (dealer_cards, dealer_sum, deck) = get_dealer_cards(deck, DEALER_MAX)
    current_money_bet(balance, bet)
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
        player_sum = card_sum(suit_list, player_cards)
        
        print("Total value: {}".format(player_sum))
        if player_sum > HAND_MAX:
            continue_player_hand = False
        else:
            hit = input("Would you like to hit (y/n): ")
            print() # blank line
        
            if hit == "y" or hit == "yes":
                (card, deck) = get_card(deck)
                player_cards.append(card) 
                player_cards = sort_cards(suit_list, player_cards)
                continue_player_hand = True
            else:
                continue_player_hand = False
    
    print("Dealer is set with a total of {} cards.".format(len(dealer_cards)))
    print() # blank line
    result = input("Press enter to reveal the dealer's hand.")
    for j in dealer_cards:
        (card, suit) = j
        print("{} of {}".format(card, suit))
    if dealer_sum > HAND_MAX:
        print("Dealer sum of {} - Dealer went over 21. You win!".format(dealer_sum))
    else:
        print("Dealer total of {}".format(dealer_sum))
    
    # Determine winner
    balance = determine_winner(balance, player_sum, dealer_sum, HAND_MAX)
    if balance < MIN_BET:
        print("Sorry, you ran out of money. Please play again.")
        run_forever = False
