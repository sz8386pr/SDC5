# SDC-Project-1
Guess the words game

This game is pretty much like a hangman, except there are no turn limits. (Maybe I should/can turn into Hangman instead?)
Game retrieves the words to guess from the dictionary file, selects one randomly and the player would have to guess
  the words to win the game.

<Files>
characters.py - Characters class contains the guessedCharacters list, defaultCharacters list, and the number of blanks int value


dictionary.txt - Default dictionary file for the game

gameLogic.py - Most of the game process goes through here. Displays the game board, checks the characters
                and displays previously guessed words

guessTheWords.py - The main program to run. Mostly for the UI. Moved program logic parts to gameLogic.py
(previous: While it is functional as intended, I think I could tidy up a bit more and move some of the codes/functions to gameLogic.py)

wordGenerator.py - Generates the words to be guessed for the game. More details in the file comments.

words.py - No longer used.
(previous: Words class object file. holds the str(word) and int[character count], but charCount[] is no longer utilized due to the change of direction/logic as I was writing the program. Not sure if I should just get rid of it.)


Overall, I'm mostly happy with the progress with this project. I think it was a good refresher for the Python(though,
  I feel like that there still are much to learn/relearn)

TO DO: turn into Hangman?
