# Created by Scott Kim
# Characters class contains the guessedCharacters list, defaultCharacters list, and the number of blanks int value

class Characters:

    def __init__(self, guessedCharacters ,defaultCharacters, blanks):
        self.guessedCharacters = guessedCharacters
        self.defaultCharacters = defaultCharacters
        self.blanks = blanks

    def get_guessedCharacters(self):
        return self.guessedCharacters

    def get_defaultCharacters(self):
        return self.defaultCharacters

    def get_blanks(self):
        return self.blanks

    def append_guessedCharacters(self, guessedCharacters):
        self.guessedCharacters.append(guessedCharacters)

    def set_blanks(self, blanks):
        self.blanks = blanks

    def __str__(self):
        return ', '.join(self.guessedCharacters)
