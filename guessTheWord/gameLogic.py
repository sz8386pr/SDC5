# Created by Scott Kim
# Most of the game logic/background process is done here
import time
import wordGenerator
import characters

# Used for creating Characters class object
def createCharacterInformation():
    defaultCharacters = [" ", "-", "\'", "\"", "!", ".", ","] # Add special characters as needed to be revealed by default
    guessedCharacters = [] # User-guessed characters will append onto the list
    blanks = 1
    charInfo = characters.Characters(guessedCharacters, defaultCharacters, blanks)

    return charInfo

# Main display for the game
def gameDisplay(guessWords, charInfo, turn):

    board, blanks, userInputMatch = drawBoard(guessWords, charInfo)

    # Checks if the player's previous guess was a match or not
    if turn != 1: # No need to check for the first turn
        if userInputMatch:
            print("\nYou guessed correctly!")
            time.sleep(1)
        else:
            print("\nThat was not a correct guess")
            time.sleep(1)

    # Check if there are any blanks left. If all the characters have been
    #   guessed correctly, player wins!
    if blanks == 0:
        print("\n<< "+ board + " >>")
        print("Congratulations! You have won the game in " + str(turn-1) + " turns!!!")
        quit()

    # Diaplay the turn #, the game board, and previously guessed characters
    print("\n[ Turn " + str(turn) + " ]")
    print(board)
    displayGuessedCharacter(charInfo)

    userInput(charInfo)

# draws the game board with the guessed words and blanks "_"
def drawBoard(guessWords, charInfo):

    checkCharacters =  charInfo.get_defaultCharacters() + charInfo.get_guessedCharacters()
    board = "" # Initial board to display

    blanks = 0
    userInputMatch = False

    # Compares the guessedCharacters list to the words to guess.
    #   If they match, board should display that character.
    #   otherwise, display the character space holder "_" instead
    for char in guessWords:
        matched = False

        for cC in checkCharacters:
            if cC in char:
                board+=cC
                matched = True
                # user input is appended onto the last of the list
                #   If there is a match
                if checkCharacters[-1] in char:
                    userInputMatch = True

        if matched == False:
            board+="_"
            blanks +=1

    return board, blanks, userInputMatch

# Displays sorted list of guessed characters
def displayGuessedCharacter(charInfo):
    guessedCharacters = charInfo.get_guessedCharacters()
    guessedCharacters.sort()
    gC = ""
    for ch in guessedCharacters:
        gC += ch + " "

    if gC == "":
        print("There are no guesses yet")
    else:
        print("Guessed: " + gC)


# User input. Checks if the input is
#   1. is alphanumeric
#   2. is one character only
#   3. is NOT in the guessedCharacters list
#   Otherwise, append to the guessedCharacters list
def userInput(charInfo):

    while True:
        guess = input("Guess a character: ").upper()
        if not guess.isalnum():
            print("Enter a number or a letter only please")
        elif len(guess) != 1:
            print("Enter one character only please")
        elif guess in charInfo.get_guessedCharacters():
            print("You already have guessed " + guess)
        else:
            charInfo.append_guessedCharacters(guess)
            break
