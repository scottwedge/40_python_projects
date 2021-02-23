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


# Constants
NUM = 2 #number of phrases to analyze

IPSUM_TEXT_1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fermentum orci venenatis est faucibus venenatis. Mauris euismod quam quis neque rutrum cursus. Vivamus at diam massa. Nullam sit amet accumsan purus. Nullam metus turpis, aliquet id pharetra suscipit, fringilla in ex. Aliquam condimentum non lectus non aliquet. Nunc est tellus, vestibulum et ipsum non, mattis varius velit. Integer lobortis turpis in eros ornare lacinia.

Sed mollis, nibh non pellentesque porttitor, dui felis ornare magna, ac elementum erat sapien vitae ante. Ut quis magna mi. Integer quis bibendum sem. Morbi ac purus lorem. Morbi a sem rhoncus, varius metus in, consequat neque. Nulla nisi turpis, bibendum a ante vitae, ornare dictum quam. Integer quis nulla mi. Vivamus varius cursus est, a auctor mi aliquam quis.

Sed augue quam, aliquam at nunc at, sodales sagittis nunc. Sed vel arcu ac mauris mollis blandit non convallis leo. Mauris euismod nulla at eleifend fringilla. Praesent tempus lorem leo, sed consectetur quam varius at. Mauris bibendum ut neque eleifend cursus. Suspendisse pharetra, ante ac tempus consequat, lacus neque hendrerit orci, aliquam pellentesque lectus sapien imperdiet tortor. Cras at urna ac purus rhoncus elementum. Nam condimentum risus ac mattis blandit. In aliquam at lorem vel blandit. Ut maximus orci sapien, consectetur fermentum ex elementum sed. Vestibulum nec tempor dui. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Maecenas non ipsum id nunc sollicitudin ullamcorper. Nam vehicula lacinia turpis in fringilla. Nullam vel nisl sed eros pharetra ultrices ut sit amet nunc. Quisque vestibulum elementum nulla nec vulputate. Maecenas quam leo, posuere vel congue sed, dictum et lacus. Donec non aliquam lorem. Nam tempus lacinia nisi nec elementum. Donec sit amet tortor vitae augue pulvinar consectetur vitae non ante. Curabitur condimentum convallis lectus, id pharetra ex ultricies sed. Integer vitae aliquam lacus. In ultrices nisi ac ipsum imperdiet, vel mattis dui hendrerit.
jkwyz
"""

SHERLOCK_HOLMES_2 = """
1. “You have a grand gift for silence, Watson. It makes you quite invaluable as a companion.” — Arthur Conan Doyle, The Man with the Twisted Lip

2. “Oh, hell! What does that matter?! So we go around the sun! If we went around the moon or round and round the garden like a teddy bear, it wouldn’t make any difference! All that matters to me is the work! Without that, my brain rots. Put that in your blog — or better still, stop inflicting your opinions on the world!” — Sherlock BBC series (spoken by Benedict Cumberbatch)

3. “You see, but you do not observe.” — Arthur Conan Doyle, A Scandal in Bohemia 

4.“It is a capital mistake to theorize before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.” — Arthur Conan Doyle, A Scandal in Bohemia

5.  “When you have eliminated the impossible, whatever remains, however improbable, must be the truth?” — Arthur Conan Doyle, The Sign of Four

6. “Watson. Come at once if convenient. If inconvenient, come all the same.” — Arthur Conan Doyle, The Adventure of the Creeping Man

7. “Dear God. What is it like in your funny little brains? It must be so boring.” —Sherlock BBC Series (spoken by Benedict Cumberbatch)

8. “To a great mind, nothing is little.” — Arthur Conan Doyle, A Study in Scarlet

9. “Crime is common. Logic is rare.” — Arthur Conan Doyle, The Adventure of the Copper Beeches

10. “The devil’s due a soul, I’d say.” — Sherlock Holmes 2009 Film Adaptation (spoken by Robert Downey Jr.)

11. “My name is Sherlock Holmes. It is my business to know what other people do not know.” — Arthur Conan Doyle, The Adventure of the Blue Carbuncle

12. “Ive always assumed that love is a dangerous disadvantage. Thank you for the final proof.” — Sherlock BBC Series (spoken by Benedict Cumberbatch)

13. “I abhor the dull routine of existence. I crave for mental exaltation. That is why I have chosen my own particular profession, or rather created it, for I am the only one in the world.” — Arthur Conan Doyle, The Sign of the Four

14. “A good detective knows that every task, every interaction, no matter how seemingly banal, has the potential to contain multitudes.” — Elementary CBS Series (spoken by Jonny Lee Miller)

15. “The game is afoot.” — Arthur Conan Doyle, The Adventure of the Abbey Grange
"""


# Functions
def welcome():
    return "Welcome to the Code Breakers App"

def encode_or_decode():
    print() # blank line
    code = input("Would you like to encode or decode a message: ")
    code = code.lower()
    code = code.rstrip()
    return code

def get_phrase():
    print() # blank line
    phrase = input("What is the phrase: ")
    return phrase

def make_cypher(db_0, db_1):
    # Assume all 26 letters exist in both texts
    cypher = 1
    return cypher

# Main program
print(welcome())

db = [] # initialize list of db dictionaries
missing = [] # init list of missing characters
descending_string = [] # init list of descending strings
text_string = [IPSUM_TEXT_1, SHERLOCK_HOLMES_2] # init text strings
print(text_string)

for j in range(NUM):
    print("Index is : ",j)
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
code = encode_or_decode()

# Get phrase to encode or decode
phrase = get_phrase()
 
# Create cypher
cypher = make_cypher(db[0], db[1])
