import characters, gameLogic, guessTheWords, wordGenerator
from unittest import TestCase, mock
from unittest.mock import patch

# 7 Tests
class test_characters(TestCase):

    def test_create_Characters_Object(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)
        self.assertEqual(guessedCharacters, testCharacterObject.guessedCharacters)
        self.assertCountEqual(defaultCharacters, testCharacterObject.defaultCharacters)
        self.assertEqual(blanks, testCharacterObject.blanks)

    def test_get_guessedCharacters(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)
        self.assertEqual(guessedCharacters, testCharacterObject.get_guessedCharacters())

    def test_get_defaultCharacters(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)
        self.assertEqual(defaultCharacters, testCharacterObject.get_defaultCharacters())

    def test_get_blanks(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)
        self.assertEqual(blanks, testCharacterObject.get_blanks())

    def test_append_guessedCharacters(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)

        guess = 'Q'
        testCharacterObject.append_guessedCharacters(guess)
        self.assertEqual(['Q'], testCharacterObject.get_guessedCharacters())

    def test_set_blanks(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)
        self.assertEqual(1, testCharacterObject.get_blanks())

        testCharacterObject.set_blanks(5)
        self.assertEqual(5, testCharacterObject.get_blanks())

    def test_str(self):
        guessedCharacters, defaultCharacters, blanks = [], [" ", "-", "\'", "\"", "!", ".", ","], 1
        testCharacterObject = characters.Characters(guessedCharacters, defaultCharacters, blanks)
        testCharacterObject.append_guessedCharacters('A')
        testCharacterObject.append_guessedCharacters('B')
        testCharacterObject.append_guessedCharacters('C')
        abc = 'A, B, C'

        self.assertEqual(abc, testCharacterObject.__str__())


class test_gameLogic(TestCase):
    
