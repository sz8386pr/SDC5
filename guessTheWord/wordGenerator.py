# Created by Scott Kim
# This file is intended for generating words to guess for the game.
# 1. It reads from the dictionary file and create a word wordList
# 2. It randomly selects one from the list
# 3. It counts the number of characters on each words (used for "GUI")
# 4. It creates the Words class objects

import random
# import words

# Reads from the dictionary file (dictionary.txt by default) and stores & returns the value into a list. (Referenced try/except from ITEC1150 class lab 7 work )
def readDictionary():
    fileName = "dictionary.txt"
    dictionaryFile = open(fileName, "r")
    wordList = []

    try:
        words = dictionaryFile.readline().upper()
        while words != "":
            wordList.append(words.rstrip("\n"))
            words = dictionaryFile.readline().upper()
    # If an error found while reading from the file
    except IOError:
        print("Error found while reading the wordlist.txt file")
    # If wrong value type has been found
    except ValueError:
        print("Invalid value found in the file")
    # Close the file
    else:
        dictionaryFile.close()

    return wordList

# Simple method, but I still modularized it incase we want to implement a different method of picking a word from the dictionary
def pickAWord(wordList):
    randomWord = str(wordList[random.randint(0, len(wordList)-1)])
    return randomWord

# No longer utilized
    # # Counts the number of characters within words and store the value as a list (ie.:"Rotten Apple" will return [6,5])
    # def countWords(randomWord):
    #     randomWord = randomWord.split(" ")
    #     wordCount = []
    #
    #     for x in range(len(randomWord)):
    #         wordCount.append(len(randomWord[x]))
    #
    #     return wordCount

# Generate the words to be guessed for the game
def generateWords():
    wordList = readDictionary() # Create a dictionary list by reading from the txt file
    guessWords = pickAWord(wordList) # Randomly pick a word within the list (ie.: "Python Program")
    # No longer utilized
        # wordCount = countWords(word) # Count the characters of the words picked (ie.: [6, 7])
        #
        # guessWords = words.Words(word, wordCount) # Create a WordLists class object

    return(guessWords)
