"""Pulls words from 7 hangman art .txt files and writes
each string to 7 .json files."""

import json

def build_hangman(allowed_failures):
    """Builds ASCII art of a hangman based on remaining allowed failures."""
    filename = 'ascii_art/man' + str(allowed_failures) + '.txt'
    try:
        with open(filename, 'r') as f:
            hangman = f.read()
    except FileNotFoundError:
        pass
    else:
        print(hangman)
        filename2 = 'ascii_art/man' + str(allowed_failures) + '.json'
        with open(filename2, 'w') as f:
            json.dump(hangman, f)

i = 6
for num in range(7):
    build_hangman(i)
    i -= 1

build_hangman('_goodbye')