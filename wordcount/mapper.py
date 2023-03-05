#!/usr/bin/env python3

import sys
# file = open('short_story.txt', 'r', encoding="utf8")
# text = file.read()

stripped = []

for line in sys.stdin:
    line = line.lower()
    words = line.split()

    # Czyszczenie wyrazów
    for word in words:
        if word == ' ' or word == '' or (len(word) == 1 and not word.isalpha()):
            continue
        try:
            while not word[0].isalpha():
                word = word[1:]
            while not word[-1].isalpha():
                word = word[:-1]
        except:
            continue
        if word == 'i':
            word = 'I'
        stripped.append(word)

for word in stripped:
    print(f'{word}\t{1}')

