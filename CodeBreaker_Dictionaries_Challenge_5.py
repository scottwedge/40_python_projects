#!/usr/bin/env python3

# Code Breaker app

# Create program that will encode or decode a secret message 
# based off a letter distribution (see previous Challenge 4 Letter Frequency Distribution program) of a pre-determined key text
# Determine the frequency analysis of two texts 
# And use the letter distributions to create a cypher
# to either encode or decode a text string entered by user
# 
# No longer asked to enter key phrase, instead use pre-determined key phrase
# 
# Analyze both phrases
# Decide if encoding or decoding
# Enter phrase
# Show encoded message and copy it
# Then rerun program and select decode and decode that message
# Verify that it matches original message


# Import
import FrequencyAnalysis_Dictinaries_Challenge_4 as fa
import ipsum_text_1 as TEXT1
import sherlock_holmes_2 as TEXT2


# Constants
NUM = 2 #number of phrases to analyze


# Functions
def welcome():
    return "Welcome to the Code Breakers App"

def get_encode_or_decode_input():
    code_input = input("Would you like to encode or decode a message: ")
    return code_input
    
def encode_or_decode(code_input):
    print() # blank line
    code_input = code_input.lower()
    code_input = code_input.rstrip()
    return code_input

def test_encode_or_decode1():
    assert encode_or_decode("ENcode  ") == "encode"

def test_encode_or_decode2():
    assert encode_or_decode("deCODE ") == "decode"


def get_phrase():
    print() # blank line
    phrase = input("What is the phrase: ")
    # Convert to all lower case and only alphabetic
    phrase = phrase.lower() # convert to lowercase
    phrase_list = list(phrase)
    alpha_string = ""
    for j in phrase_list:
        if j.isalpha():
            alpha_string += j
    return alpha_string

def make_cypher(descend_0, descend_1):
    # Assuming all 26 letters exist in both texts
    # In descending order, map letter from first db to letter from second db
    cypher = {}
    l = len(descend_0)
    for j in range(l):
        a = (list(descend_0))[j] 
        b = (list(descend_1))[j]
        cypher[a] = b
    return cypher

def test_make_cypher():
    assert make_cypher("abcd", "efgh") == {"a":"e", "b":"f", "c":"g", "d":"h"}

def encode(secret_string, encode_cypher):
    encoded_string = "" # initialize blank string
    secret_list = list(secret_string) # convert string to list
    for j in range(len(secret_list)):
        encoded_string += encode_cypher[secret_list[j]]
    return encoded_string

def test_encode():
    assert encode("abcddcba", {"a":"e", "b":"f", "c":"g", "d":"h"}) == "efghhgfe"

def decode(encoded_string, encode_cypher):
    decoded_string = "" # initialize blank string
    encoded_list = list(encoded_string) # convert string to list

    # must swap k,v encode to v,k to decode
    decode_cypher = {}
    for k,v in encode_cypher.items():
        decode_cypher[v] = k
    for j in range(len(encoded_list)):
        decoded_string += decode_cypher[encoded_list[j]]
    return decoded_string

def test_decode():
    assert decode("efghhgfe", {"a":"e", "b":"f", "c":"g", "d":"h"}) == "abcddcba"



# Main program
def main():
    print(welcome())
    
    db = [] # initialize list of db dictionaries
    missing = [] # init list of missing characters
    descending_string = [] # init list of descending strings
    text_string = [TEXT1.IPSUM_TEXT_1, TEXT2.SHERLOCK_HOLMES_2] # init text strings
    
    for j in range(NUM):
        # analyze the text of phrase 
        db.append(fa.make_db(text_string[j]))
        
        # display occurrences of each letter
        print() # blank line
        print("Here is the frequency analysis of string #{}: ".format(j+1))
        fa.show_occurrence(db[j])
        
        # List missing characters missing from analyzed text
        missing.append(fa.missing_letters(db[j]))
        print() # blank line
        print("The following letters are missing: {}".format(missing[j]))
        
        # List characters in descending order of occurrence
        descending_string.append(fa.descending_order(db[j]))
        print() # blank line
        print("Characters in descending order are: {}".format(descending_string[j]))
        
    # Determine if user wants to code or decode
    code_input = get_encode_or_decode_input()
    code = encode_or_decode(code_input)
    
    # Get phrase to encode or decode
    phrase = get_phrase()
    print("Entered phrase is: {}".format(phrase))
    print("String with only alphabetic characters is: {}". format(phrase))
     
    # Create cypher
    cypher = make_cypher(descending_string[0], descending_string[1])
    print("Cypher is: {}". format(cypher))
    
    if code == "encode":
        encoded_string = encode(phrase, cypher)
        print("Encoded string is: {}".format(encoded_string))
    elif code == "decode":
        decoded_string = decode(phrase, cypher)
        print("Decoded string is: {}".format(decoded_string))
    else:
        print("ERROR OCCURRED")

if __name__ == "__main__":
    main()
