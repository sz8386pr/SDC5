# Created by Scott Kim
# The main Program

import time
import gameLogic
import wordGenerator

# Intial setup phase and welcome screen
def setup():
    guessWords = wordGenerator.generateWords() # Generate Words class object guessWords
    charInfo = gameLogic.createCharacterInformation()
    print("Welcome to Guess The Words game!!!")
    try:
        input("Press enter to play!")
    except SyntaxError:
        pass
    # unnecessaryCounter() # May remove it

    return guessWords, charInfo

# (Totally unnecessary)Start counter because WHY NOT?
def unnecessaryCounter():
    time.sleep(1)
    print("10000")
    time.sleep(2)
    print("9999")
    time.sleep(2)
    print("9998")
    time.sleep(1)
    print("OMG")
    time.sleep(1)
    print("1")
    time.sleep(0.5)
    print("0")
    time.sleep(0.5)
    print("LETS GO!")
    time.sleep(1)


# Actual game play
def gamePlay(guessWords, charInfo):

    turn = 0 # Number of turns to win the game

    while True:

        turn += 1
        gameLogic.gameDisplay(guessWords, charInfo, turn)

        time.sleep(1)

def main():

    guessWords, charInfo = setup()
    gamePlay(guessWords, charInfo)

if __name__ == '__main__':
    main()
