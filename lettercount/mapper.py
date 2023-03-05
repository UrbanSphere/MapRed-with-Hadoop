#!/usr/bin/env python3

import sys


letters = []

for line in sys.stdin:

    line = line.lower()
    words = line.split()

    for word in words:
        for letter in word:
            letters.append(letter)

for letter in letters:
    print(f'{letter}\t{1}')
