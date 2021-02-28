#!/usr/bin/env python3

# Word Guessing Game

# Welcome user
# Provide a Category
# Present a string of dashes - one per letter in the word
# After each incorrect guess, reveal one random letter in the word
# If guess correct, state how many guesses user took
# Then offer option to play again

# Imports
import random

# Functions

def welcome():
    return "Welcome to the Guess My Word App"

def guess_dict():
    d = {"sports":["football", "hockey","soccer", "volleyball", "basketball"],
         "Beatles":["John", "George", "Paul", "Ringo"],
         "Single Digits": ["one","two","three","four","five","six","seven"]}
    return(d)

def get_categories(d):
    category_list = [] # init blank list
    for j in d.keys():
        category_list.append(j)
    category_list.sort()	# sort alphabetically to simplify testing
    return category_list 

def test_get_categories():
    assert get_categories({"a1":["b1","c1"],"a2":["b2", "c2"]}) == ["a1", "a2"]

def get_random_category(list_of_categories):
    random.seed()
    random_index = random.randint(0, len(list_of_categories) - 1)
    random_category = list_of_categories[random_index]
    return random_category

def test_get_random_category(mocker):
    mocker.patch("random.randint",return_value = 1)
    assert get_random_category(["a1", "a2", "a3"]) == "a2"

def get_random_word(d, category):
    list_of_words = []              # initialize list
    for j in d[category]:
        list_of_words.append(j)    # create list
    random_index = random.randint(0,len(list_of_words) - 1)
    word = list_of_words[random_index]
    return word

def test_get_random_word(mocker):
    mocker.patch("random.randint", return_value = 1)
    assert get_random_word({"a1":["b1","c1"],"a2":["b2", "c2"]}, "a2") == "c2"

def init_clue(word):
    clue_list = []                    # initialize list
    for j in range(len(word)):   # all "-"
        clue_list.append("-")
    clue = list_to_string(clue_list)
    return clue

def test_init_clue():
    assert init_clue("Saturday") == "--------"

def display_category(length, category):
    print() # blank line
    print("Guess a {} letter word from the following category: {}.".format(length, category))

def list_to_string(l):    	# convert list 'l' to string 's' and return string
    s = ""
    s = s.join(l)
    return s

def update_clue(word, clue):
    clue_list = list(clue)   # convert string to list
    just_dashes_list = []   # initialize list of remaining dash indexes in clue list
    for j in range(len(clue_list)):
        if clue_list[j] == "-":
            just_dashes_list.append(j)

    random_index = random.randint(0, len(just_dashes_list) -1) # create random index
    index = just_dashes_list[random_index]   # get index into word
    word_list = list(word)
    clue_list = list(clue)
    clue_list[index] = word_list[index]    # switch another "-" to correct character
    clue = list_to_string(clue_list)
    return clue

def get_guess():
    print() # blank line
    g = input("Enter your guess: ")
    return g

def play_again():
    print() # blank line
    y_n = input("Would you like to play again (y/n): ")
    y_n = y_n.lower()   # convert to lower case
    y_n = y_n.rstrip()  # strip trailing white space
    if y_n == "y" or y_n == "yes":
        return True	# try game again
    else: 
        return False 	# exit program

def main():
    print(welcome())
    
    # initialize variables
    d = guess_dict()
    list_of_categories = get_categories(d)
    
    main_loop_boolean = True
    
    while main_loop_boolean:
    
        # start game
        category = get_random_category(list_of_categories)
        word = get_random_word(d, category)
        guess_count = 0  	# initialize counter
        clue = init_clue(word) # Initial word will be correct length but all dashes
        guess = ""
        display_category(len(word), category)
        print(clue)
    
        while guess != word and clue != word: 	# loop until guess word or clue reveals word
            guess = get_guess()    		# get guess from user
            guess_count = guess_count + 1
        
            if guess == word:
                print("Correct! You guessed the word in {} guesses".format(guess_count))
            else:
                print("That is not correct. Let us reveal a letter to help you!")
                clue = update_clue(word, clue)               
                print(clue)
        
        main_loop_boolean = play_again()
    
    print() # blank line
    print("Thank you for playing. Goodbye.")


# Main code
if __name__ == "__main__":
    main()
