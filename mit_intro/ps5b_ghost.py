# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 1)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()
def ghost():
    currWord = ''
    playerNr = 0
    ctr = 1
    valid = False
    #initializing game
    print('Welcome to Ghost!')
    print('Player 1 goes first.')
    currWord = ''
    print('Current word fragment: ', currWord)
    while not valid:
        currCh = input('Player 1 says letter: ')
        valid = isValid(currCh)
        if not valid: print('Please enter a valid character')
    currWord = currWord + str(currCh).lower()
    #continue game
    
    while True:
        print('Current word fragment: ', currWord)
        if ((len(currWord)>3) and (currWord in wordlist)):
            print('Player ', playerNr, 'loses because', currWord ,'is a word!')
            print('Player ',playerNr%2+1, 'wins!')
            break
        elif isIllegal(currWord):
            print('Player ', playerNr, 'loses because no word begins with', currWord)
            print('Player ', (playerNr+1)%2, 'wins!') 
            break
        elif ctr%2==0: #it's player 1's turn
            playerNr=1
        else: #it's player 2's turn
            playerNr=2
        print('Player ', playerNr, '\'s turn.')
        valid=False
        while not valid:
            currCh = input('Player ' + str(playerNr) + ' says letter: ')
            valid = isValid(currCh)
            print(valid)
            if not valid: print('Please enter a valid character')
        currWord = currWord + str(currCh).lower()
        ctr += 1
    
def isValid(ch):
    """
    Returns True if the input character is alphabetic, accepting both
    lowercase and uppercase letters

    ch: char
    return: Boolean
    """
    isValid = False
    if ch in string.ascii_letters: isValid=True
    return isValid
def isIllegal(word):
    """
    Returns True if the input character is alphabetic, accepting both
    lowercase and uppercase letters

    word: string
    return: Boolean
    """
    isIllegal = True
    for voc in wordlist:
        if voc.startswith(word): isIllegal=False
    return isIllegal
ghost()
