#!/usr/bin/env python3

import sys


letters = {}
for line in sys.stdin:
    try:
        letter, count = line.split('\t')
    except:
        continue
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters.update({letter: int(count)})

for letter in letters:
    print(letter, '\t', letters[letter])