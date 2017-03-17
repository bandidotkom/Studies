# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import binascii

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 12

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "C:/Users/Lenovo/Desktop/fu/mit/intro_cs_programming/words.txt"

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    scores = 0
    for i in word:
        scores += SCRABBLE_LETTER_VALUES[i.lower()]
    if len(word) == n:
        scores += 50
    return scores

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print (letter,)             # print all on the same line
    print                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)+1
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newhand = {}
    for letter in hand.keys():
        if letter in word:
            ctr = 0
            for i in range (len(word)):
                if word[i]==letter:
                    ctr+=1
            newFreq = hand[letter]-ctr
            if newFreq>0:
                newhand[letter]=newFreq
        else:
            newhand[letter]=hand[letter]
    return newhand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    inList=True
    if word not in word_list:
        inList=False
    inHand=True
    need = get_frequency_dict(word)
    for letter in need.keys():
        if letter not in hand.keys():
            inHand=False
        elif need[letter]>hand[letter]:
            inHand=False
    return inHand and inList
    

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    scores = 0
    end = False
    while end == False:
        print("Current hand: "), display_hand(hand)
        word = str(input("enter word or a . to indicate that you are finished: "))
        if word=='.':
            end = True
        elif is_valid_word(word, hand, word_list):
           currScores = get_word_score(word, HAND_SIZE)
           scores += currScores
           print(word, "earned", currScores, "points. Total: ", scores, "points")
           hand = update_hand(hand, word)
           if len(hand) == 0: end=True
        elif not is_valid_word(word, hand, word_list):
            print("your word is not valid")
    print("Final score:", scores, "points")
        
#
# Problem #5: Playing a game
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
     
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
from ps5a import *

#
# Test code
#
##def test_deal_hand():
##    """
##    Unit test for deal_hand.
##    """
##    
##    # (A)
##    # Basic test, see if the right kind of dictionary is
##    # being returned.
##    hand = deal_hand(HAND_SIZE)
##    if not type(hand) is dict:
##        print ("FAILURE: test_deal_hand()")
##        print ("\tUnexpected return type:", type(hand))
##        
##        return # exit function
##
##    num = 0
##    for k in hand.keys():
##        if (not type(k) is str) or (not type(hand[k]) is int):
##            print ("FAILURE: test_deal_hand()")
##            print ("\tUnexpected type of dictionary: string -> int expected, but was", type(k), "->", type(hand[k]))
##
##            return # exit function
##        elif not k in "abcdefghijklmnopqrstuvwxyz":
##            print ("FAILURE: test_deal_hand()")
##            print ("\tDictionary keys are not lowercase letters.")
##
##            return # exit function
##        else:
##            num += hand[k]
##            
##    if num != HAND_SIZE:
##            print ("FAILURE: test_deal_hand()")
##            print ("\tdeal_hand() returned more letters than it was asked to.")
##            print ("\tAsked for a hand of size", HAND_SIZE, "but it returned a hand of size", num)
##
##            return # exit function
##        
##    # (B)
##    # Tests randomness..
##    repeats=0
##    hand1 = deal_hand(HAND_SIZE)
##    for i in range(20):                
##        hand2 = deal_hand(HAND_SIZE)
##        if hand1 == hand2:
##            repeats += 1
##        hand1 = hand2
##        
##    if repeats > 10:
##        print ("FAILURE: test_deal_hand()")
##        print ("\tSame hand returned", repeats, "times by deal_hand(). This is HIGHLY unlikely.")
##        print ("\tIs the deal_hand implementation really using random numbers?")
##
##        return # exit function
##    
##    print ("SUCCESS: test_deal_hand()")
##
##def test_get_word_score():
##    """
##    Unit test for get_word_score
##    """
##    failure=False
##    # dictionary of words and scores
##    words = {("", 7):0, ("it", 7):2, ("was", 7):6, ("scored", 7):9, ("waybill", 7):65, ("outgnaw", 7):61, ("outgnawn", 8):62}
##    for (word, n) in words.keys():
##        score = get_word_score(word, n)
##        if score != words[(word, n)]:
##            print ("FAILURE: test_get_word_score()")
##            print ("\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
##            failure=True
##    if not failure:
##        print ("SUCCESS: test_get_word_score()")
##
##def test_update_hand():
##    """
##    Unit test for update_hand
##    """
##    # test 1
##    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
##    word = "quail"
##
##    hand2 = update_hand(hand.copy(), word)
##    expected_hand1 = {'l':1, 'm':1}
##    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
##    if hand2 != expected_hand1 and hand2 != expected_hand2:
##        print ("FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")")
##        print ("\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)
##
##        return # exit function
##        
##    # test 2
##    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
##    word = "evil"
##
##    hand2 = update_hand(hand.copy(), word)
##    expected_hand1 = {'v':1, 'n':1, 'l':1}
##    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
##    if hand2 != expected_hand1 and hand2 != expected_hand2:
##        print ("FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")")
##        print ("\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)
##
##        return # exit function
##
##    # test 3
##    hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
##    word = "hello"
##
##    hand2 = update_hand(hand.copy(), word)
##    expected_hand1 = {}
##    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
##    if hand2 != expected_hand1 and hand2 != expected_hand2:
##        print ("FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")"                )
##        print ("\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)
##        
##        return # exit function
##
##    print ("SUCCESS: test_update_hand()")
##
##def test_is_valid_word(word_list):
##    """
##    Unit test for is_valid_word
##    """
##    failure=False
##    # test 1
##    word = "hello"
##    hand = get_frequency_dict(word)
##
##    if not is_valid_word(word, hand, word_list):
##        print ("FAILURE: test_is_valid_word()")
##        print ("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
##
##        failure = True
##
##    # test 2
##    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
##    word = "rapture"
##
##    if  is_valid_word(word, hand, word_list):
##        print ("FAILURE: test_is_valid_word()")
##        print ("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
##
##        failure = True        
##
##    # test 3
##    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
##    word = "honey"
##
##    if  not is_valid_word(word, hand, word_list):
##        print ("FAILURE: test_is_valid_word()")
##        print ("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)
##
##        failure = True                        
##
##    # test 4
##    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
##    word = "honey"
##
##    if  is_valid_word(word, hand, word_list):
##        print ("FAILURE: test_is_valid_word()")
##        print ("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
##        
##        failure = True
##
##    # test 5
##    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
##    word = "evil"
##    
##    if  not is_valid_word(word, hand, word_list):
##        print ("FAILURE: test_is_valid_word()")
##        print ("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
##        
##        failure = True
##        
##    # test 6
##    word = "even"
##
##    if  is_valid_word(word, hand, word_list):
##        print ("FAILURE: test_is_valid_word()")
##        print ("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
##        print ("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")
##        
##        failure = True        
##
##    if not failure:
##        print ("SUCCESS: test_is_valid_word()")
##
##
##word_list = load_words()
##print ("----------------------------------------------------------------------")
##print ("Testing get_word_score...")
##test_get_word_score()
##print ("----------------------------------------------------------------------")
##print ("Testing update_hand...")
##test_update_hand()
##print ("----------------------------------------------------------------------")
##print ("Testing is_valid_word...")
##test_is_valid_word(word_list)
##print ("----------------------------------------------------------------------")
##print ("All done!")
