"""Pulls words from a file called 'dictionary.txt' and writes
them into a .json file."""

import json

with open('dictionary.txt', 'r') as f:
    text = f.read()

text = text.split()
print(len(text))

for word in text[:]:
    # We only want words that are 4 characters or more.
    if len(word) < 4:
        text.remove(word)

print(text)
with open('dictionary.json', 'w') as f:
    json.dump(text, f)