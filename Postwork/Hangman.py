# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    i = 0
    for i in range (len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True
        
    
##print isWordGuessed('apple',['e', 'i', 'k', 'p', 'r', 's'])
##print isWordGuessed('apple',['a','p','l','e'])
##print isWordGuessed('banana', ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a'])
##print isWordGuessed('grapefruit', [])#False
##print isWordGuessed('durian', ['h', 'a', 'c', 'd',\
##                               'i', 'm', 'n', 'r', 't', 'u'])#True
##print isWordGuessed('grapefruit', [])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    i = 0
    guessedWord = ''
    for i in range (len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guessedWord = guessedWord + secretWord[i] + ' '
        else:
            guessedWord = guessedWord + '_ '
            
    return guessedWord

#secretWord = 'durian' 
#lettersGuessed = ['h', 'a', 'c', 'd','i', 'm', 'n', 'r', 't', 'u']
#print (getGuessedWord('durian', ['h', 'a', 'c', 'd','i', 'm', 'n', 'r', 't']))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in availableLetters:
            availableLetters = availableLetters.replace(lettersGuessed[i], '')
    return(availableLetters)

##print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
#print (getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])) # abcdfghjlmnoqtuvwxyz

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

#secretWord: The word to guess.
#lettersGuessed: The letters that have been guessed so far.
#mistakesMade: The number of incorrect guesses made so far.
#availableLetters: The letters that may still be guessed. 
#Every time a player guesses a letter, the guessed letter must be removed from 
# availableLetters (and if they guess a letter that is not in availableLetters
#you should print a message telling them they've already guessed that 
#- so try again!).
    
    lettersGuessed = ''
    mistakesMade = 0

    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is', len(secretWord),'letters long')
    while not isWordGuessed(secretWord, lettersGuessed) and mistakesMade < 8:
      print ('------------')
      print ('You have', 8 - mistakesMade,'guesses left')
      print ('Available Letters:',getAvailableLetters(lettersGuessed))
      guess = input ('Please guess a letter:')
      if guess not in getAvailableLetters(lettersGuessed):
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
      elif guess not in secretWord:
        print ("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        lettersGuessed = lettersGuessed + guess
        mistakesMade = mistakesMade + 1
      else:
        lettersGuessed = lettersGuessed + guess
        print ("Good guess:", getGuessedWord(secretWord, lettersGuessed))
    if mistakesMade == 8:
        print ('------------')  
        print ("Sorry, you ran out of guesses. The word was ", secretWord, ".")
    else:
        print ('------------')
        print ("Congratulations, you won!")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
